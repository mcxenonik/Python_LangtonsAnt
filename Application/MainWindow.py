from PySide2.QtWidgets import QMainWindow, QFileDialog
from cv2 import imwrite, imshow, waitKey

from Application.UiMainWindow import Ui_MainWindow
from Application.LangtonAlgorithm import LangtonAlgorithm


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._antAlgorithm = LangtonAlgorithm()

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
        self._checkIfPathIsEmpty()

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
        path = QFileDialog.getOpenFileName(caption="Open Image",
                                           filter="Images (*.png *.jpg)")[0]
        if(path != ''):
            self.ui.pathLE.setText(path)

        self._checkIfPathIsEmpty()

    def _generateImageClick(self):
        print('Image generated')

        if(self.ui.whiteImageRB.isChecked()):
            height = self.ui.heightSB.value()
            width = self.ui.widthSB.value()

            self._antAlgorithm.generate_white_image(height, width)

        elif(self.ui.imageFromFileRB.isChecked()):
            path = self.ui.pathLE.text()

            self._antAlgorithm.read_image_from_file(path)

        elif(self.ui.randomImageRB.isChecked()):
            height = self.ui.heightSB.value()
            width = self.ui.widthSB.value()
            pro = self.ui.probabilitySB.value()

            self._antAlgorithm.generate_random_image(height, width, pro)

        self._setPushButtonsEnabled()

        self._antAlgorithm.copy_image_to_reset()

        self._showImage()

    def _resetClick(self):
        print('RESET')

        self._antAlgorithm.copy_image_from_reset()

        self._showImage()

    def _runClick(self):
        print('RUN')

        isSave = self.ui.saveImageToFileCB.isChecked()
        allIters = self.ui.allIterationsRB.isChecked()
        everyNIters = self.ui.everyNIterationsRB.isChecked()

        iterations = self.ui.numOfItersSB.value()

        if(isSave and allIters):
            self._runAlgorithm(iterations, isSave)

        elif(isSave and everyNIters):
            saveIters = self.ui.saveItersSB.value()
            self._runAlgorithm(iterations, isSave, saveIters)

        else:
            self._runAlgorithm(iterations)

        self._showImage()

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

    def _checkIfPathIsEmpty(self):
        if(self.ui.pathLE.text() == ''):
            self.ui.runPB.setEnabled(False)
            self.ui.generateImagePB.setEnabled(False)
        else:
            self.ui.generateImagePB.setEnabled(True)

    def _checkIfRunButtonCanBeEnabled(self):
        if(self._antAlgorithm.is_image_genarated()):
            self.ui.runPB.setEnabled(True)
        else:
            self.ui.runPB.setEnabled(False)

    def _showImage(self):
        image = self._antAlgorithm.get_image()
        imshow('Image', image)
        waitKey(0)

    def _saveImageToFile(self, image, iter):
        path = f'out/out_{iter}.png'
        imwrite(path, image)

    def _runAlgorithm(self, numOfIters, isSave=False, saveIters=1):
        self._antAlgorithm.create_ant()

        for i in range(1, numOfIters + 1):
            image = self._antAlgorithm.step_algorithm()
            
            if(isSave and (i % saveIters == 0 or i in [1, numOfIters])):
                self._saveImageToFile(image, i)
