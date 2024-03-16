from PyQt6.QtWidgets import QLineEdit, QPushButton, QDialog, QVBoxLayout, QComboBox
import sqlite3


class InsertDialog(QDialog):
    def __init__(self):
        """
        Initialize the Add Student Data window with input fields for student name, course selection, and mobile number. Also includes a submit button to register the student.
        """
        super().__init__()
        self.setWindowTitle("Add Student Data")
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()

        self.student_name_input = QLineEdit()
        self.student_name_input.setPlaceholderText("Enter student name")
        layout.addWidget(self.student_name_input)

        self.course_dropdown = QComboBox()
        courses = [
            "Computer Science", "Electronics and Communication Engineering",
            "Mechanical Engineering", "Civil Engineering", "Information Technology",
            "Biology", "Mathematics", "Astronomy", "Physics", "Chemistry",
            "Physical Education", "Business Administration", "English", "History",
            "Geography", "Hindi"
        ]
        self.course_dropdown.addItems(courses)
        layout.addWidget(self.course_dropdown)

        self.mobile_input = QLineEdit()
        self.mobile_input.setPlaceholderText("Enter mobile number")
        layout.addWidget(self.mobile_input)

        self.submit_button = QPushButton("Register")
        self.submit_button.clicked.connect(self.add_student)

        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def add_student(self):
        """
        A function that adds a student to the database with the provided name, course, and mobile number.
        """
        try:
            name = self.student_name_input.text()
            course = self.course_dropdown.currentText()
            mobile = self.mobile_input.text()
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            sql_query = "INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)"
            cursor.execute(sql_query, (name, course, mobile))
            connection.commit()
        except ValueError as e:
            print("ValueError adding student:", e)
        except AttributeError as e:
            print("AttributeError adding student:", e)
        except TypeError as e:
            print("TypeError adding student:", e)
        except Exception as e:
            print("Error adding student:", e)
        finally:
            cursor.close()
            connection.close()
            self.accept()
