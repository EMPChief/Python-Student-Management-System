from classess import StudentManagementSystem
from PyQt6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = StudentManagementSystem()
    main_window.show()
    sys.exit(app.exec())
