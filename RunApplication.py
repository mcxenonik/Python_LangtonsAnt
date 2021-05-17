from PySide2.QtWidgets import QApplication
import sys

from MainWindow import MainWindow


def runApp(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    runApp(sys.argv)