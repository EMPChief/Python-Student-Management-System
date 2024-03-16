from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        """
        Initialize the About window with a specific parent.

        Parameters:
            parent: Optional parent widget (default is None)

        Return:
            None
        """
        super().__init__(parent)
        self.setWindowTitle("About")

        layout = QVBoxLayout(self)

        title = QLabel("Student Management System", self)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Arial", 20, QFont.Weight.Bold))

        content = QLabel("""
            Student Management System is a simple application designed to manage
            student data in a SQLite database. It provides a user interface for
            inserting, editing, searching and deleting students.
            """, self)
        content.setWordWrap(True)

        layout.addWidget(title)
        layout.addWidget(content)
        self.setLayout(layout)
