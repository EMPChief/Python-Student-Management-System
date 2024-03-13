from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
     QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, \
     QVBoxLayout, QComboBox
from PyQt6.QtGui import QAction
import sys
import sqlite3
from classess import InsertDialog, SearchDialog

class StudentManagementSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setFixedSize(800, 600)
        self._create_menu()
        self._create_table()
        self._load_data()
        self.search_dialog = SearchDialog()
        self.search_dialog.search.connect(self._load_data)

    def _create_menu(self):
        file_menu = self.menuBar().addMenu("&File")
        help_menu = self.menuBar().addMenu("&Help")
        search_menu = self.menuBar().addMenu("&Search")

        add_student_action = QAction("Add Student", self)
        add_student_action.triggered.connect(self.add_student)
        file_menu.addAction(add_student_action)

        about_action = QAction("About", self)
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)
        
        search_action = QAction("Search", self)
        search_action.triggered.connect(self.search)
        search_menu.addAction(search_action)
        
    def _create_table(self):
        self.student_table = QTableWidget()
        self.student_table.setColumnCount(4)
        header_labels = ("ID", "Name", "Course", "Number")
        self.student_table.setHorizontalHeaderLabels(header_labels)
        self.student_table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.student_table)

    def _load_data(self):
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

    def add_student(self):
        dialog = InsertDialog()
        dialog.student_added.connect(self._reload_data)
        dialog.exec()

    def _reload_data(self):
        self._load_data()

    def about(self):
        pass
    
    def search(self):
        self.search_dialog = SearchDialog()
        self.search_dialog.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentManagementSystem()
    window.show()
    sys.exit(app.exec())
