from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLineEdit, QPushButton, QVBoxLayout, QDialog, QTableWidgetItem, QTableWidget
import sqlite3

class SearchDialog(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.last_found_row = -1
        self.found_items = []

        self.setWindowTitle("Search Student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_student)
        layout.addWidget(self.search_button)

        self.setLayout(layout)

    def search_student(self):
        try:
            name = self.student_name.text().strip()
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            result = cursor.execute("SELECT * FROM students WHERE name LIKE ?", (name + '%',))
            rows = list(result)
            cursor.close()
            connection.close()

            if not rows:
                print("No student found with that name.")
                self.reset_search()
                return

            self.found_items.clear()
            self.main_window.student_table.clearSelection()

            for row in rows:
                for row_num in range(self.main_window.student_table.rowCount()):
                    item = self.main_window.student_table.item(row_num, 1)
                    if item is not None and item.text() == name:
                        self.found_items.append(item)

            if not self.found_items:
                print("No matching rows found.")
                self.reset_search()
                return

            self.last_found_row = (self.last_found_row + 1) % len(self.found_items)
            current_item = self.found_items[self.last_found_row]

            current_item.setSelected(True)
            self.main_window.student_table.scrollToItem(current_item, QTableWidget.ScrollHint.EnsureVisible)
        except ValueError as e:
            print("Error searching student:", e)

    def reset_search(self):
        try:
            self.last_found_row = -1
            self.student_name.clear()
            self.main_window.student_table.clearSelection()
        except ValueError as e:
            print("Error resetting search:", e)
        except AttributeError as e:
            print("Error resetting search:", e)
        except TypeError as e:
            print("Error resetting search:", e)
        except Exception as e:
            print("Error resetting search:", e)
