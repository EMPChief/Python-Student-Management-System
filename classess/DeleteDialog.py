from PyQt6.QtWidgets import QLabel, QPushButton, QDialog, \
    QVBoxLayout, QMessageBox
import sqlite3
from .DatabaseConnection import DatabaseConnection


class DeleteDialog(QDialog):

    def __init__(self, selected_data):
        """
        Initialize the Delete Student window with the selected student's data.
        
        Parameters:
            selected_data (tuple): A tuple containing the student's ID, name, course, and number.
        
        Returns:
            None
        """
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
        """
        A method to delete a student record from the database based on the provided data.
        """
        try:
            student_data = self.selected_data
            connection = DatabaseConnection().connect()
            cursor = connection.cursor()
            sql_query = "DELETE FROM students WHERE id=%s AND name=%s AND course=%s AND mobile=%s"
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
            print("TypeError deleting student:", e)
        except Exception as e:
            print("Error deleting student:", e)
        finally:
            cursor.close()
            connection.close()
            self.accept()

    def close(self):
        """
        Closes the current operation by rejecting it.
        """
        self.reject()
