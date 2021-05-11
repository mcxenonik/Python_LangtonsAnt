from PySide2.QtWidgets import QApplication, QFileDialog, QMainWindow
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
        self._image_reset = []

        self._connectWithGUI()

    def _connectWithGUI(self):
        self.ui.whiteImageRB.clicked.connect(self._whiteImageClick)
        self.ui.imageFromFileRB.clicked.connect(self._imageFromFileClick)
        self.ui.randomImageRB.clicked.connect(self._randomImageClick)

        self.ui.saveImageToFileCB.clicked.connect(self._saveImageToFileClick)
        self.ui.allIterationsRB.clicked.connect(self._allIterationsClick)
        self.ui.everyNIterationsRB.clicked.connect(self._everyNIterationsClick)

        self.ui.selectFilePB.clicked.connect(self._selectFileClick)
        self.ui.generateImagePB.clicked.connect(self._generateImageClick)
        self.ui.resetPB.clicked.connect(self._resetClick)
        self.ui.runPB.clicked.connect(self._runClick)

    def _whiteImageClick(self):
        self._setImageGroupEnabled((True, True, False, False, False, True))
        self._checkIfRunButtonCanBeEnabled()

    def _imageFromFileClick(self):
        self._setImageGroupEnabled((False, False, True, False, True, False))
        self._checkIfPathisEmpty()

    def _randomImageClick(self):
        self._setImageGroupEnabled((True, True, False, True, False, True))
        self._checkIfRunButtonCanBeEnabled()
 
    def _saveImageToFileClick(self):
        if(self.ui.saveImageToFileCB.isChecked()):
            self._setOutputGroupEnabled(True)
            if(self.ui.everyNIterationsRB.isChecked()):
                self.ui.saveItersSB.setEnabled(True)
        else:
            self._setOutputGroupEnabled(False)
            self.ui.saveItersSB.setEnabled(False)

    def _allIterationsClick(self):
        self.ui.saveItersSB.setEnabled(False)

    def _everyNIterationsClick(self):
        self.ui.saveItersSB.setEnabled(True)

    def _selectFileClick(self):
        self.ui.pathLE.setText(QFileDialog.getOpenFileName()[0])
        self._checkIfPathisEmpty()

    def _generateImageClick(self):
        print('Image generated')

        if(self.ui.whiteImageRB.isChecked()):
            height = self.ui.heightSB.value()
            width = self.ui.widthSB.value()

            self._image = langton.generate_white_image(height, width)

        elif(self.ui.imageFromFileRB.isChecked()):
            path = self.ui.pathLE.text()

            self._image = langton.read_image_from_file(path)

        elif(self.ui.randomImageRB.isChecked()):
            height = self.ui.heightSB.value()
            width = self.ui.widthSB.value()
            pro = self.ui.probabilitySB.value()

            self._image = langton.generate_random_image(height, width, pro)

        self._setPushButtonsEnabled()

        self._image_reset = self._image.copy()

        cv2.imshow('Image', self._image)
        cv2.waitKey(0)

    def _resetClick(self):
        print('RESET')

        self._image = self._image_reset.copy()

        cv2.imshow('Image', self._image)
        cv2.waitKey(0)

    def _runClick(self):
        print('RUN')

        isSave = self.ui.saveImageToFileCB.isChecked()
        allIters = self.ui.allIterationsRB.isChecked()
        everyNIters = self.ui.everyNIterationsRB.isChecked()

        iterations = self.ui.numOfItersSB.value()

        if(isSave and allIters):
            langton.ant_algorithm(self._image, iterations, isSave)
        elif(isSave and everyNIters):
            saveIters = self.ui.saveItersSB.value()
            langton.ant_algorithm(self._image, iterations, isSave, saveIters)
        else:
            langton.ant_algorithm(self._image, iterations)

    def _setPushButtonsEnabled(self):
        self.ui.resetPB.setEnabled(True)
        self.ui.runPB.setEnabled(True)

    def _setImageGroupEnabled(self, isEnabled):
        self.ui.widthSB.setEnabled(isEnabled[0])
        self.ui.heightSB.setEnabled(isEnabled[1])
        self.ui.pathLE.setEnabled(isEnabled[2])
        self.ui.probabilitySB.setEnabled(isEnabled[3])
        self.ui.selectFilePB.setEnabled(isEnabled[4])
        self.ui.generateImagePB.setEnabled(isEnabled[5])

    def _setOutputGroupEnabled(self, isEnabled):
        self.ui.allIterationsRB.setEnabled(isEnabled)
        self.ui.everyNIterationsRB.setEnabled(isEnabled)

    def _checkIfPathisEmpty(self):
        if(self.ui.pathLE.text() == ''):
            self.ui.runPB.setEnabled(False)
            self.ui.generateImagePB.setEnabled(False)
        else:
            self.ui.generateImagePB.setEnabled(True)

    def _checkIfRunButtonCanBeEnabled(self):
        if(len(self._image) != 0):
            self.ui.runPB.setEnabled(True)
        else:
            self.ui.runPB.setEnabled(False)


def guiMain(args):
    app = QApplication(args)
    window = LangtonsAntWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
