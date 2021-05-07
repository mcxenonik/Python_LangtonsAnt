from PySide2.QtWidgets import QApplication, QMainWindow
import sys
import cv2

from ui_app_gui import Ui_MainWindow
import langton


class LangtonsAntWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._image = []
        self._mainApplication()

    def _mainApplication(self):
        self.ui.whiteImageRB.clicked.connect(self._whiteImageClick)
        self.ui.imageFromFileRB.clicked.connect(self._imageFromFileClick)
        self.ui.randomImageRB.clicked.connect(self._randomImageClick)

        self.ui.saveImageToFileCB.clicked.connect(self._saveImageToFileClick)
        self.ui.allIterationsRB.clicked.connect(self._allIterationsClick)
        self.ui.everyNIterationsRB.clicked.connect(self._everyNIterationsClick)

        self.ui.showImagePB.clicked.connect(self._showImageClick)
        self.ui.runPB.clicked.connect(self._runClick)

    def _whiteImageClick(self):
        self._setImageGroupEnabled((True, True, False, False))

    def _imageFromFileClick(self):
        self._setImageGroupEnabled((False, False, True, False))

    def _randomImageClick(self):
        self._setImageGroupEnabled((True, True, False, True))

    def _setImageGroupEnabled(self, isEnabled):
        self.ui.widthLE.setEnabled(isEnabled[0])
        self.ui.heightLE.setEnabled(isEnabled[1])
        self.ui.pathLE.setEnabled(isEnabled[2])
        self.ui.probabilityLE.setEnabled(isEnabled[3])

    def _saveImageToFileClick(self):
        if(self.ui.saveImageToFileCB.isChecked() is True):
            self._setOutputGroupEnabled(True)
            if(self.ui.everyNIterationsRB.isChecked() is True):
                self.ui.saveIterationsLE.setEnabled(True)
        else:
            self._setOutputGroupEnabled(False)
            self.ui.saveIterationsLE.setEnabled(False)

    def _setOutputGroupEnabled(self, isEnabled):
        self.ui.allIterationsRB.setEnabled(isEnabled)
        self.ui.everyNIterationsRB.setEnabled(isEnabled)

    def _allIterationsClick(self):
        self.ui.saveIterationsLE.setEnabled(False)

    def _everyNIterationsClick(self):
        self.ui.saveIterationsLE.setEnabled(True)

    def _showImageClick(self):
        self.ui.runPB.setEnabled(True)
        if(self.ui.whiteImageRB.isChecked() is True):
            height = int(self.ui.heightLE.text())
            width = int(self.ui.widthLE.text())
            self._image = langton.generate_white_image(height, width)
            cv2.imshow('Image', self._image)
            cv2.waitKey(0)
        elif(self.ui.imageFromFileRB.isChecked() is True):
            path = str(self.ui.pathLE.text())
            self._image = langton.read_image_from_file(path)
            cv2.imshow('Image', self._image)
            cv2.waitKey(0)
        elif(self.ui.randomImageRB.isChecked() is True):
            height = int(self.ui.heightLE.text())
            width = int(self.ui.widthLE.text())
            proba = float(self.ui.probabilityLE.text())
            self._image = langton.generate_random_image(height, width, proba)
            cv2.imshow('Image', self._image)
            cv2.waitKey(0)

    def _runClick(self):
        iterations = int(self.ui.numberOfIterationsLE.text())
        langton.ant_algorithm(self._image, iterations)


def guiMain(args):
    app = QApplication(args)
    window = LangtonsAntWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
