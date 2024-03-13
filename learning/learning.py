from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QLineEdit, QPushButton, QGridLayout
)
import sys
from datetime import datetime


class AgeCalculator(QWidget):
    """
    A simple PyQt6 application for calculating a person's age
    based on their inputted date of birth.
    """

    def __init__(self):
        """
        Initializes the AgeCalculator widget.
        """
        super().__init__()
        grid = QGridLayout()
        # Creating Widgets
        name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()
        date_birth_label = QLabel("Date of birth (dd/mm/yyyy):")
        self.date_birth_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate Age")
        calculate_button.clicked.connect(self.calculate_age)

        self.output_label = QLabel("")

        # Adding Widgets to Layout
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_birth_label, 1, 0)
        grid.addWidget(self.date_birth_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)
        # Setting layout and window title
        self.setLayout(grid)
        self.setWindowTitle("Age Calculator")

    def calculate_age(self):
        """
        Calculates the age based on the entered date of birth.
        Displays the result in the output_label.
        checks if date is valid and calculate based on
        current date taking account of days, month and year!
        """
        try:
            birth_date = datetime.strptime(
                self.date_birth_line_edit.text(), "%d/%m/%Y")
            current_date = datetime.now()

            years = current_date.year - birth_date.year
            if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
                years -= 1

            if years == 0:
                months = current_date.month - birth_date.month
                if months == 0:
                    days = current_date.day - birth_date.day
                    self.output_label.setText(
                        f"{self.name_line_edit.text()} is {days} days old.")
                else:
                    self.output_label.setText(
                        f"{self.name_line_edit.text()} is {months} months old.")
            else:
                self.output_label.setText(
                    f"{self.name_line_edit.text()} is {years} years old.")
        except ValueError:
            self.output_label.setText(
                "Please enter a valid date (dd/mm/yyyy).")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    age_calc = AgeCalculator()
    age_calc.show()
    sys.exit(app.exec())
