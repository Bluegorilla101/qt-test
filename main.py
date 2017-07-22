import sys
from PyQt5.QtWidgets import QApplication, QDialog
from test import Ui_Form


def main():
    ui.label.setText('Hello')
    ui.pushButton.clicked.connect(button_clicked)


def button_clicked():
    ui.label.setText('what')


app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Form()
ui.setupUi(window)
main()
window.show()
sys.exit(app.exec_())
