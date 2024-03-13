import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QGridLayout, QPushButton
from PyQt6.QtGui import QDoubleValidator

class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Average Speed Calculator')
        self.initUI()

    def initUI(self):
        layout = QGridLayout()

        # Input fields
        self.distanceInput = QLineEdit(placeholderText="Enter distance")
        self.distanceInput.setValidator(QDoubleValidator(0.0, float('inf'), 2))
        self.timeInput = QLineEdit(placeholderText="Enter time in hours")
        self.timeInput.setValidator(QDoubleValidator(0.0, float('inf'), 2))

        # Unit selection
        self.unitSelector = QComboBox()
        self.unitSelector.addItems(['Metric (km)', 'Imperial (miles)'])

        # Calculate button
        self.calculateButton = QPushButton('Calculate')
        self.calculateButton.clicked.connect(self.calculateSpeed)
        self.calculateButton.setEnabled(False)

        # Result display
        self.resultLabel = QLabel("")

        # Layout setup
        layout.addWidget(QLabel('Distance:'), 0, 0)
        layout.addWidget(self.distanceInput, 0, 1)
        layout.addWidget(self.unitSelector, 0, 2)
        layout.addWidget(QLabel('Time (hours):'), 1, 0)
        layout.addWidget(self.timeInput, 1, 1)
        layout.addWidget(self.calculateButton, 2, 1)
        layout.addWidget(self.resultLabel, 3, 0, 1, 2)

        self.setLayout(layout)

        # Enable calculate button when inputs are valid
        self.distanceInput.textChanged.connect(self.validateInputs)
        self.timeInput.textChanged.connect(self.validateInputs)

    def validateInputs(self):
        distance = self.distanceInput.text()
        time = self.timeInput.text()
        self.calculateButton.setEnabled(bool(distance and time))

    def calculateSpeed(self):
        distance = float(self.distanceInput.text())
        time = float(self.timeInput.text())

        speed, unit = self.calculate(distance, time)

        # Display the result
        self.resultLabel.setText(f"Average Speed: {speed} {unit}")

    def calculate(self, distance, time):
        speed = distance / time
        if self.unitSelector.currentText() == 'Metric (km)':
            return round(speed, 2), 'km/h'
        elif self.unitSelector.currentText() == 'Imperial (miles)':
            speed_mph = round(speed * 0.621371, 2)
            return speed_mph, 'mph'
        return None, None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = SpeedCalculator()
    calculator.show()
    sys.exit(app.exec())
