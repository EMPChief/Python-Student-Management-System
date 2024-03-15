from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, \
    QVBoxLayout, QComboBox, QToolBar, QStatusBar, QMessageBox
from PyQt6.QtGui import QAction, QIcon
import sys
import sqlite3
from .DeleteDialog import DeleteDialog
from .EditDialog import EditDialog
from .SearchDialog import SearchDialog
from .InsertStudent import InsertDialog


class StudentManagementSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setMinimumSize(800, 600)
        self._create_menu()
        self._create_table()
        self._load_data()
        self._toolbar()
        self._statusbar()
        self.search_dialog = SearchDialog(self)

    def _create_menu(self):
        file_menu = self.menuBar().addMenu("&File")
        help_menu = self.menuBar().addMenu("&Help")
        search_menu = self.menuBar().addMenu("&Search")

        self.add_student_action = QAction(
            QIcon("icons/add.png"), "Add Student", self)
        self.add_student_action.triggered.connect(self.add_student)
        file_menu.addAction(self.add_student_action)

        self.about_action = QAction("About", self)
        self.about_action.triggered.connect(self.about)
        help_menu.addAction(self.about_action)

        self.search_action = QAction(QIcon("icons/search.png"), "Search", self)
        self.search_action.triggered.connect(self.search)
        search_menu.addAction(self.search_action)

    def _create_table(self):
        self.student_table = QTableWidget()
        self.student_table.setColumnCount(4)
        header_labels = ("ID", "Name", "Course", "Number")
        self.student_table.setHorizontalHeaderLabels(header_labels)
        self.student_table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.student_table)

    def _toolbar(self):
        toolbar = QToolBar("Toolbar")
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(self.add_student_action)
        toolbar.addAction(self.search_action)

    def _statusbar(self):
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        labeling = QLabel("EMP")
        self.statusbar.addWidget(labeling)
        self.student_table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        selected_row = self.student_table.currentRow()
        selected_data = []
        for column in range(self.student_table.columnCount()):
            item = self.student_table.item(selected_row, column)
            if item is not None:
                selected_data.append(item.text())
            else:
                selected_data.append("")

        edit_button = QPushButton("Edit")
        edit_button.clicked.connect(lambda: self.edit_cell(selected_data))
        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(self.delete_cell)

        children = self.statusbar.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)

        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)

    def edit_cell(self, selected_data):
        dialog = EditDialog(selected_data)
        dialog.exec()
        self.clear_status_bar()
        self._load_data()

    def delete_cell(self):
        selected_row = self.student_table.currentRow()
        if selected_row >= 0:
            selected_data = []
            for column in range(self.student_table.columnCount()):
                item = self.student_table.item(selected_row, column)
                if item is not None:
                    selected_data.append(item.text())
                else:
                    selected_data.append("")
            dialog = DeleteDialog(selected_data)
            dialog.exec()
        self.clear_status_bar()
        self._load_data()

    def _load_data(self):
        try:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            result = cursor.execute("SELECT * FROM students")
            self.student_table.setRowCount(0)
            for row_num, row_data in enumerate(result):
                self.student_table.insertRow(row_num)
                for col_num, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    self.student_table.setItem(row_num, col_num, item)
            conn.close()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error",
                                 f"Database error: {str(e)}")

    def add_student(self):
        dialog = InsertDialog()
        dialog.exec()
        self._load_data()

    def clear_status_bar(self):
        children = self.statusbar.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)

    def about(self):
        pass

    def search(self):
        self.search_dialog.exec()