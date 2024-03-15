from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QComboBox, QPushButton
import sqlite3


class EditDialog(QDialog):

    def __init__(self, selected_data):
        super().__init__()
        self.setWindowTitle("Edit Student Data")
        self.setFixedSize(300, 300)
        self.selected_data = selected_data
        layout = QVBoxLayout()

        self.student_name_input = QLineEdit(self.selected_data[1])
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
        current_index = self.course_dropdown.findText(self.selected_data[2])
        if current_index != -1:
            self.course_dropdown.setCurrentIndex(current_index)
        layout.addWidget(self.course_dropdown)

        self.mobile_input = QLineEdit(self.selected_data[3])
        self.mobile_input.setPlaceholderText("Enter mobile number")
        layout.addWidget(self.mobile_input)

        self.submit_button = QPushButton("Update")
        self.submit_button.clicked.connect(self.update_student)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def update_student(self):
        try:
            student_name = self.student_name_input.text()
            course = self.course_dropdown.currentText()
            mobile_number = self.mobile_input.text()
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            sql_query = "UPDATE students SET name=?, course=?, mobile=? WHERE name=? AND course=? AND mobile=?"
            cursor.execute(sql_query, (student_name, course, mobile_number,
                           self.selected_data[1], self.selected_data[2], self.selected_data[3]))
            connection.commit()
        except ValueError as e:
            print("ValueError updating student:", e)
        except AttributeError as e:
            print("AttributeError updating student:", e)
        except TypeError as e:
            print("TypeError updating student:", e)
        except Exception as e:
            print("Error updating student:", e)
        finally:
            cursor.close()
            connection.close()
            self.accept()
