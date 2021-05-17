from PySide2.QtWidgets import QMainWindow, QFileDialog

from UiMainWindow import Ui_MainWindow
from LangtonAlgorithm import LangtonAlgorithm


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._ant_algorithm = LangtonAlgorithm()

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

            self._ant_algorithm.generate_white_image(height, width)

        elif(self.ui.imageFromFileRB.isChecked()):
            path = self.ui.pathLE.text()

            self._ant_algorithm.read_image_from_file(path)

        elif(self.ui.randomImageRB.isChecked()):
            height = self.ui.heightSB.value()
            width = self.ui.widthSB.value()
            pro = self.ui.probabilitySB.value()

            self._ant_algorithm.generate_random_image(height, width, pro)

        self._setPushButtonsEnabled()

        self._ant_algorithm.copy_image_to_reset()

        self._ant_algorithm.show_image()

    def _resetClick(self):
        print('RESET')

        self._ant_algorithm.copy_image_from_reset()

        self._ant_algorithm.show_image()

    def _runClick(self):
        print('RUN')

        isSave = self.ui.saveImageToFileCB.isChecked()
        allIters = self.ui.allIterationsRB.isChecked()
        everyNIters = self.ui.everyNIterationsRB.isChecked()

        iterations = self.ui.numOfItersSB.value()

        if(isSave and allIters):
            self._ant_algorithm.run_algorithm(iterations, isSave)
        elif(isSave and everyNIters):
            saveIters = self.ui.saveItersSB.value()
            self._ant_algorithm.run_algorithm(iterations, isSave, saveIters)
        else:
            self._ant_algorithm.run_algorithm(iterations)

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
        if(self._ant_algorithm.isImageGenarated()):
            self.ui.runPB.setEnabled(True)
        else:
            self.ui.runPB.setEnabled(False)
