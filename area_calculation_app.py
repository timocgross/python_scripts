from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

def calculate_area():
    try:
        height = float(height_input.text())
        width = float(width_input.text())
        area = height * width
        area_label.setText(f"Area: {area}")
    except ValueError:
        area_label.setText("Invalid input. Please enter numbers.")

app = QApplication([])

window = QWidget()
window.setWindowTitle("Rectangle Area Calculator")

layout = QVBoxLayout()

height_input = QLineEdit()
height_input.setPlaceholderText("Enter height")
layout.addWidget(height_input)

width_input = QLineEdit()
width_input.setPlaceholderText("Enter width")
layout.addWidget(width_input)

calc_button = QPushButton("Calculate Area")
calc_button.clicked.connect(calculate_area)
layout.addWidget(calc_button)

area_label = QLabel("Area: ")
layout.addWidget(area_label)

window.setLayout(layout)
window.show()

app.exec()