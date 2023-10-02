# Import QColor, QTableWidget and QTableWidgetItem to display dackground colors.
import sys
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QApplication, QTableWidget, QTableWidgetItem)

# Data model with list of names/hex codes for different colors:
colors = [('Red', '#FF0000'),
          ('Yellow', '#F9E56d'),
          ('Green', '#00FF00'),
          ('Electric Green', '#41CD52'),
          ('Blue', '#0000FF'),
          ('Dark Blue', '#222840'),
          ('Black', '#000000'),
          ('White', '#FFFFFF')]

# Function for translating the hex code into an RGB equivalent:
def get_rgb_from_hex(code):
    code_hex = code.replace('#', '')
    rgb = tuple(int(code_hex[i:i+2], 16) for i in (0, 2, 4))
    return QColor.fromRgb(rgb[0], rgb[1], rgb[2])

# Initialising of QApplication
app = QApplication()

# Configuration of QTableWidget.
# The reason of using + 1 is to include a new column where we can display the color:
table = QTableWidget
table.setRowCount(len(colors))
table.setColumnCount(len(colors[0]) + 1)
table.setHorizontalHeaderLAbels(['Name', 'Hex Code', 'Color'])

# Iterating the data structure, create the QTableWidgetItems instances and adding them using x, y:
for i, (name, code) in enumerate(colors):
    item_name = QTableWidgetItem(name)
    item_code = QTableWidgetItem(code)
    item_color = QTableWidgetItem()
    item_color.setBackground(get_rgb_from_hex(code))
    table.setItem(i, 0, item_name)
    table.setItem(i, 1, item_code)
    table.setItem(i, 2, item_color)

# Show the table and execute the QApplication:
table.show()
sys.exit(app.exec())
