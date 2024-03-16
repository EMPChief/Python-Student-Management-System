from PyQt6.QtWidgets import QLineEdit, QPushButton, QVBoxLayout, QDialog, QTableWidget
import sqlite3
from .DatabaseConnection import DatabaseConnection


class SearchDialog(QDialog):
    def __init__(self, main_window):
        """
        Initializes the SearchStudentDialog with the given main_window.

        Parameters:
            main_window (object): The main window object.

        Returns:
            None
        """
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
        """
        A function to search for a student in the database based on the provided name.
        It retrieves student information associated with the provided name and highlights the matching row in the GUI table.
        """
        try:
            name = self.student_name.text().strip()
            connection = DatabaseConnection().connect()
            cursor = connection.cursor()

            sql_query = "SELECT * FROM students WHERE name LIKE %s"
            cursor.execute(sql_query, (f'{name}',))

            self.found_items.clear()
            self.main_window.student_table.clearSelection()

            for row_num in range(self.main_window.student_table.rowCount()):
                item = self.main_window.student_table.item(row_num, 1)
                if item is not None and item.text() == name:
                    self.found_items.append(item)

            if not self.found_items:
                print("No matching rows found.")
                self.reset_search()
                return

            # Reset last found row if it exceeds found_items length
            self.last_found_row %= len(self.found_items)
            current_item = self.found_items[self.last_found_row]

            current_item.setSelected(True)
            self.main_window.student_table.scrollToItem(
                current_item, QTableWidget.ScrollHint.EnsureVisible)
            cursor.close()
            connection.close()
        except ValueError as e:
            print("ValueError searching student:", e)
        except AttributeError as e:
            print("AttributeError searching student:", e)
        except TypeError as e:
            print("TypeError searching student:", e)
        except Exception as e:
            print("Function error searching student:", e)

    def reset_search(self):
        """
        Reset the search functionality by clearing the last found row, student names, and table selection.
        """
        try:
            self.last_found_row = -1
            self.student_name.clear()
            self.main_window.student_table.clearSelection()
        except ValueError as e:
            print("ValueError resetting search:", e)
        except AttributeError as e:
            print("AttributeError resetting search:", e)
        except TypeError as e:
            print("TypeError resetting search:", e)
        except Exception as e:
            print("Error resetting search:", e)
