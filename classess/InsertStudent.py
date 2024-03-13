from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QLineEdit, QPushButton, QDialog, QVBoxLayout, QComboBox
import sqlite3

class InsertDialog(QDialog):
    student_added = pyqtSignal()
    def __init__(self):
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
        name = self.student_name_input.text()
        course = self.course_dropdown.currentText()
        mobile = self.mobile_input.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        sql_query = "INSERT OR IGNORE INTO students (name, course, mobile) SELECT ?, ?, ? WHERE NOT EXISTS (SELECT 1 FROM students WHERE name=? AND course=? AND mobile=?)"
        cursor.execute(sql_query, (name, course, mobile, name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
        self.student_added.emit()

        
