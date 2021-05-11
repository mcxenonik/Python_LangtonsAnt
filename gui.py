from PySide2.QtWidgets import QApplication, QMainWindow
import sys
import cv2

from ui_app_gui import Ui_MainWindow
import langton
import input_validator


class LangtonsAntWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._image = []
        self._valid_width = False
        self._valid_height = False
        self._valid_probability = False
        self._valid_numOfIter = False
        self._valid_saveIters = False

        self._connectWithGUI()

    def _connectWithGUI(self):
        self.ui.whiteImageRB.clicked.connect(self._whiteImageClick)
        self.ui.imageFromFileRB.clicked.connect(self._imageFromFileClick)
        self.ui.randomImageRB.clicked.connect(self._randomImageClick)

        self.ui.saveImageToFileCB.clicked.connect(self._saveImageToFileClick)
        self.ui.allIterationsRB.clicked.connect(self._allIterationsClick)
        self.ui.everyNIterationsRB.clicked.connect(self._everyNIterationsClick)

        self.ui.generateImagePB.clicked.connect(self._generateImageClik)
        self.ui.showImagePB.clicked.connect(self._showImageClick)
        self.ui.runPB.clicked.connect(self._runClick)

        self.ui.widthLE.editingFinished.connect(self._widthImageEdit)
        self.ui.heightLE.editingFinished.connect(self._heightImageEdit)
        self.ui.probabilityLE.editingFinished.connect(self._probabilityEdit)
        self.ui.saveIterationsLE.editingFinished.connect(self._saveItersEdit)

        self.ui.numOfIterLE.editingFinished.connect(self._numOfIterEdit)

    def _widthImageEdit(self):
        width = self.ui.widthLE.text()

        self._valid_width = input_validator.validate_image_width(width)

        if(self._valid_width is True):
            self._setLineEditBackground(self.ui.widthLE, 'white')
        else:
            self._setLineEditBackground(self.ui.widthLE, 'red')

    def _heightImageEdit(self):
        height = self.ui.heightLE.text()

        self._valid_height = input_validator.validate_image_height(height)

        if(self._valid_height is True):
            self._setLineEditBackground(self.ui.heightLE, 'white')
        else:
            self._setLineEditBackground(self.ui.heightLE, 'red')

    def _probabilityEdit(self):
        pro = self.ui.probabilityLE.text()

        self._valid_probability = input_validator.validate_probabilty(pro)

        if(self._valid_probability is True):
            self._setLineEditBackground(self.ui.probabilityLE, 'white')
        else:
            self._setLineEditBackground(self.ui.probabilityLE, 'red')

    def _saveItersEdit(self):
        saveIters = self.ui.saveIterationsLE.text()

        self._valid_saveIters = input_validator.validate_save_iterations(saveIters)

        if(self._valid_saveIters is True):
            self._setLineEditBackground(self.ui.saveIterationsLE, 'white')
        else:
            self._setLineEditBackground(self.ui.saveIterationsLE, 'red')

    def _numOfIterEdit(self):
        numOfIter = self.ui.numOfIterLE.text()

        self._valid_numOfIter = input_validator.validate_num_of_iter(numOfIter)

        if(self._valid_numOfIter is True):
            self._setLineEditBackground(self.ui.numOfIterLE, 'white')
        else:
            self._setLineEditBackground(self.ui.numOfIterLE, 'red')

    def _setLineEditBackground(self, lineEdit, color):
        setting = f'QLineEdit{{background : {color};}}'
        lineEdit.setStyleSheet(setting)

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

    def _generateImageClik(self):
        if(self.ui.whiteImageRB.isChecked() is True):
            if(self._valid_height is False or self._valid_width is False):
                print('Invalid input data')
            else:
                height = int(self.ui.heightLE.text())
                width = int(self.ui.widthLE.text())
                self._image = langton.generate_white_image(height, width)
                print('Image generated')

                self.ui.runPB.setEnabled(True)
                self.ui.showImagePB.setEnabled(True)

        elif(self.ui.imageFromFileRB.isChecked() is True):
            path = str(self.ui.pathLE.text())
            self._image = langton.read_image_from_file(path)

            self.ui.runPB.setEnabled(True)
            self.ui.showImagePB.setEnabled(True)

        elif(self.ui.randomImageRB.isChecked() is True):
            if(self._valid_height is False or self._valid_width is False
               or self._valid_probability is False):
                print('Invalid input data')
            else:
                height = int(self.ui.heightLE.text())
                width = int(self.ui.widthLE.text())
                pro = float(self.ui.probabilityLE.text())
                self._image = langton.generate_random_image(height, width, pro)
                print('Image generated')

                self.ui.runPB.setEnabled(True)
                self.ui.showImagePB.setEnabled(True)

    def _showImageClick(self):
        cv2.imshow('Image', self._image)
        print('Show image')
        cv2.waitKey(0)

    def _runClick(self):
        isSave = self.ui.saveImageToFileCB.isChecked()
        everyNIters = self.ui.everyNIterationsRB.isChecked()

        if(self._valid_numOfIter is False
           or (isSave and everyNIters and self._valid_saveIters is False)):
            print('Invalid input data')
        else:
            print('RUN')

            iterations = int(self.ui.numOfIterLE.text())

            allIters = self.ui.allIterationsRB.isChecked()

            if(isSave and allIters):
                langton.ant_algorithm(self._image, iterations, isSave)
            elif(isSave and everyNIters):
                saveIters = int(self.ui.saveIterationsLE.text())
                langton.ant_algorithm(self._image, iterations, isSave, saveIters)
            else:
                langton.ant_algorithm(self._image, iterations)


def guiMain(args):
    app = QApplication(args)
    window = LangtonsAntWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
