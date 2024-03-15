from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, \
    QVBoxLayout, QComboBox, QToolBar, QStatusBar, QMessageBox
from PyQt6.QtGui import QAction, QIcon
import sys
import sqlite3


class DeleteDialog(QDialog):

    def __init__(self, selected_data):
        super().__init__()
        self.setWindowTitle("Delete Student")
        self.selected_data = selected_data

        layout = QVBoxLayout()

        confirmation = QLabel(
            f"Are you sure you want to delete the following student?")
        layout.addWidget(confirmation)

        student_info = QLabel(f"ID: {self.selected_data[0]}\n"
                              f"Name: {self.selected_data[1]}\n"
                              f"Course: {self.selected_data[2]}\n"
                              f"Number: {self.selected_data[3]}\n")
        layout.addWidget(student_info)

        yes_button = QPushButton("Yes")
        layout.addWidget(yes_button)
        no_button = QPushButton("No")
        layout.addWidget(no_button)

        self.setLayout(layout)
        yes_button.clicked.connect(self.delete_student)
        no_button.clicked.connect(self.close)

    def delete_student(self):
        try:
            student_data = self.selected_data
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            sql_query = "DELETE FROM students WHERE id=? AND name=? AND course=? AND mobile=?"
            cursor.execute(sql_query, student_data)
            connection.commit()
            confirmation_widget = QMessageBox()
            confirmation_widget.setWindowTitle("Success")
            confirmation_widget.setText("Student record deleted successfully.")
            confirmation_widget.exec()
        except ValueError as e:
            print("ValueError deleting student:", e)
        except AttributeError as e:
            print("AttributeError deleting student:", e)
        except TypeError as e:
            print("AttributeError deleting student:", e)
        except Exception as e:
            print("Error deleting student:", e)
        finally:
            cursor.close()
            connection.close()
            self.accept()

    def close(self):
        self.reject()
