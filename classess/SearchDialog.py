
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QLabel,QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QDialog, \
    QVBoxLayout
import sqlite3


class SearchDialog(QDialog):
    search = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Search Student")
        self.setFixedSize(300, 300)
        self.search_label = QLabel("Search")
        self.search_text = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.search_label)
        layout.addWidget(self.search_text)

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.query_db)
        layout.addWidget(self.search_button)

        self.results_table = QTableWidget()  # Initialize the results table
        self.results_table.setColumnCount(4)
        header_labels = ("ID", "Name", "Course", "Number")
        self.results_table.setHorizontalHeaderLabels(header_labels)
        layout.addWidget(self.results_table)

        self.setLayout(layout)

    def query_db(self):
        query = self.search_text.text().strip()
        if not query:
            return

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        results = cursor.execute(
            "SELECT * FROM students WHERE name LIKE ? OR course LIKE ? OR mobile LIKE ?",
            (f"%{query}%", f"%{query}%", f"%{query}%")
        )
        self.results_table.setRowCount(0)

        for row_num, row_data in enumerate(results):
            self.results_table.insertRow(row_num)
            for col_num, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.results_table.setItem(row_num, col_num, item)

        cursor.close()
        connection.close()
