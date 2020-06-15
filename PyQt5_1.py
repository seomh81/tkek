import sys

from PyQt5.QtWidgets import QMainWindow, QApplication


class ExWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Main Window')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExWindow()
    sys.exit(app.exec_())
