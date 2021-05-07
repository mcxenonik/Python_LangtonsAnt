from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton
from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout
from PySide2.QtWidgets import QMainWindow, QListWidgetItem
import sys

from ui_app_gui import Ui_MainWindow


class LangdonsAntWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def guiMain(args):
    app = QApplication(args)
    window = LangdonsAntWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
