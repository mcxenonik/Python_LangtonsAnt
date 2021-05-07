from PySide2.QtWidgets import QApplication, QMainWindow
# from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout
# from PySide2.QtWidgets importQWidget, QLineEdit, QPushButton

import sys

from ui_app_gui import Ui_MainWindow


class LangtonsAntWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._mainApplication()

    def _mainApplication(self):
        self.ui.whiteImageRB.clicked.connect(self._whiteImageClick)
        self.ui.imageFromFileRB.clicked.connect(self._imageFromFileClick)
        self.ui.randomImageRB.clicked.connect(self._randomImageClick)

    def _whiteImageClick(self):
        self.ui.widthLE.setEnabled(True)
        self.ui.heightLE.setEnabled(True)
        self.ui.pathLE.setEnabled(False)
        self.ui.probabilityLE.setEnabled(False)

    def _imageFromFileClick(self):
        self.ui.widthLE.setEnabled(False)
        self.ui.heightLE.setEnabled(False)
        self.ui.pathLE.setEnabled(True)
        self.ui.probabilityLE.setEnabled(False)

    def _randomImageClick(self):
        self.ui.widthLE.setEnabled(False)
        self.ui.heightLE.setEnabled(False)
        self.ui.pathLE.setEnabled(False)
        self.ui.probabilityLE.setEnabled(True)


def guiMain(args):
    app = QApplication(args)
    window = LangtonsAntWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
