from PySide2.QtWidgets import QMainWindow, QFileDialog
from cv2 import imwrite, imshow, waitKey
from os import path, makedirs

from Application.LangtonAlgorithm import LangtonAlgorithm
from Application.UiMainWindow import Ui_MainWindow
from Application.Const import SUPPORTED_FILE_TYPES
from Application.Const import DEFAULT_FILE_NAME
from Application.Const import DEFAULT_SAVE_PATH


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._antAlgorithm = LangtonAlgorithm()

        self._connectWithGUI()

    def _connectWithGUI(self):
        self.ui.whiteImageRB.clicked.connect(self._whiteImageClick)
        self.ui.randomImageRB.clicked.connect(self._randomImageClick)
        self.ui.imageFromFileRB.clicked.connect(self._imageFromFileClick)

        self.ui.saveImageToFileCB.clicked.connect(self._saveImageToFileClick)
        self.ui.allIterationsRB.clicked.connect(self._allIterationsClick)
        self.ui.everyNIterationsRB.clicked.connect(self._everyNIterationsClick)
        self.ui.defaultFileNameCB.clicked.connect(self._defaultFileNameClick)
        self.ui.defaultSavePathCB.clicked.connect(self._defaultSavePathClick)

        self.ui.selectSaveFolderPB.clicked.connect(self._selectSaveFolderClick)
        self.ui.selectFilePB.clicked.connect(self._selectFileClick)
        self.ui.generateImagePB.clicked.connect(self._generateImageClick)
        self.ui.resetPB.clicked.connect(self._resetClick)
        self.ui.runPB.clicked.connect(self._runClick)

    def _whiteImageClick(self):
        self._setImageGroupEnabled((True, True, True, True, False,
                                    False, False, False, False, True))
        self._checkIfRunAndResetButtonCanBeEnabled()

    def _randomImageClick(self):
        self._setImageGroupEnabled((True, True, True, True, True,
                                    True, False, False, False, True))
        self._checkIfRunAndResetButtonCanBeEnabled()

    def _imageFromFileClick(self):
        self._setImageGroupEnabled((False, False, False, False, False,
                                    False, True, True, True, False))
        self._checkIfGeneratImageButtonCanBeEnabled()
        self._checkIfRunAndResetButtonCanBeEnabled()

    def _saveImageToFileClick(self):
        if(self.ui.saveImageToFileCB.isChecked()):
            self._setOutputGroupEnabled((True, True, False, False,
                                         True, True, False, False,
                                         False))

            self._everyNIterationsClick()
            self._defaultFileNameClick()
            self._defaultSavePathClick()
        else:
            self._setOutputGroupEnabled((False, False, False, False,
                                         False, False, False, False,
                                         False))

    def _allIterationsClick(self):
        self.ui.saveItersSB.setEnabled(False)
        self.ui.everyNIterationsLabel.setEnabled(False)

    def _everyNIterationsClick(self):
        if(self.ui.everyNIterationsRB.isChecked()):
            self.ui.saveItersSB.setEnabled(True)
            self.ui.everyNIterationsLabel.setEnabled(True)

    def _defaultFileNameClick(self):
        if(self.ui.defaultFileNameCB.isChecked()):
            self.ui.saveFileNameLE.setEnabled(False)
            self.ui.saveFileNameLE.setText(DEFAULT_FILE_NAME)
        else:
            self.ui.saveFileNameLE.setEnabled(True)

    def _defaultSavePathClick(self):
        if(self.ui.defaultSavePathCB.isChecked()):
            self.ui.saveFilePathLE.setEnabled(False)
            self.ui.selectSaveFolderPB.setEnabled(False)
            self.ui.saveFilePathLE.setText(DEFAULT_SAVE_PATH)
        else:
            self.ui.saveFilePathLE.setEnabled(True)
            self.ui.selectSaveFolderPB.setEnabled(True)

    def _selectSaveFolderClick(self):
        dialog = QFileDialog(self)
        dirPath = dialog.getExistingDirectory(caption="Select Directory",
                                              options=dialog.ShowDirsOnly)
        if(dirPath != ''):
            self.ui.saveFilePathLE.setText(dirPath)

    def _selectFileClick(self):
        dialog = QFileDialog(self)
        filePath = dialog.getOpenFileName(caption="Select Image",
                                          filter=SUPPORTED_FILE_TYPES)[0]
        if(filePath != ''):
            self.ui.pathLE.setText(filePath)

        self._checkIfGeneratImageButtonCanBeEnabled()

    def _generateImageClick(self):
        # print('Image generated')

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
            proba = self.ui.probabilitySB.value()

            self._antAlgorithm.generate_random_image(height, width, proba)

        self._checkIfRunAndResetButtonCanBeEnabled()

        self._antAlgorithm.copy_image_to_reset()

        self._showImage()

    def _resetClick(self):
        # print('RESET')

        self._antAlgorithm.copy_image_from_reset()

        self._showImage()

    def _runClick(self):
        # print('RUN')

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

    def _setImageGroupEnabled(self, isEnabled):
        self.ui.widthSB.setEnabled(isEnabled[0])
        self.ui.heightSB.setEnabled(isEnabled[1])
        self.ui.widthLabel.setEnabled(isEnabled[2])
        self.ui.heightLabel.setEnabled(isEnabled[3])

        self.ui.probabilitySB.setEnabled(isEnabled[4])
        self.ui.probabilityLabel.setEnabled(isEnabled[5])

        self.ui.pathLE.setEnabled(isEnabled[6])
        self.ui.selectFilePB.setEnabled(isEnabled[7])
        self.ui.pathImageLabel.setEnabled(isEnabled[8])

        self.ui.generateImagePB.setEnabled(isEnabled[9])

    def _setOutputGroupEnabled(self, isEnabled):
        self.ui.allIterationsRB.setEnabled(isEnabled[0])
        self.ui.everyNIterationsRB.setEnabled(isEnabled[1])
        self.ui.saveItersSB.setEnabled(isEnabled[2])
        self.ui.everyNIterationsLabel.setEnabled(isEnabled[3])

        self.ui.defaultFileNameCB.setEnabled(isEnabled[4])
        self.ui.defaultSavePathCB.setEnabled(isEnabled[5])
        self.ui.saveFileNameLE.setEnabled(isEnabled[6])
        self.ui.saveFilePathLE.setEnabled(isEnabled[7])
        self.ui.selectSaveFolderPB.setEnabled(isEnabled[8])

    def _checkIfGeneratImageButtonCanBeEnabled(self):
        if(self.ui.pathLE.text() == ''):
            self.ui.generateImagePB.setEnabled(False)
        else:
            self.ui.generateImagePB.setEnabled(True)

    def _checkIfRunAndResetButtonCanBeEnabled(self):
        if(self._antAlgorithm.is_image_genarated()):
            self.ui.resetPB.setEnabled(True)
            self.ui.runPB.setEnabled(True)
        else:
            self.ui.resetPB.setEnabled(False)
            self.ui.runPB.setEnabled(False)

    def _showImage(self):
        image = self._antAlgorithm.get_image()
        imshow('Image', image)
        waitKey(0)

    def _saveImageToFile(self, image, numOfIter):
        savePath = self.ui.saveFilePathLE.text()
        fileName = self.ui.saveFileNameLE.text() + f'_{numOfIter}.png'

        if(not(path.exists(savePath))):
            makedirs(savePath)

        fullSavePath = path.join(savePath, fileName)
        imwrite(fullSavePath, image)

    def _runAlgorithm(self, numOfIters, isSave=False, saveIters=1):
        self._antAlgorithm.create_ant()

        for i in range(1, numOfIters + 1):
            image = self._antAlgorithm.step_algorithm()

            if(isSave and (i % saveIters == 0 or i in [1, numOfIters])):
                self._saveImageToFile(image, i)
