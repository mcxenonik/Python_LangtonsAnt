# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UiMainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(361, 476)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(361, 476))
        MainWindow.setMaximumSize(QSize(361, 476))
        icon = QIcon()
        icon.addFile(u"ant_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 361, 471))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.probabilitySB = QDoubleSpinBox(self.groupBox)
        self.probabilitySB.setObjectName(u"probabilitySB")
        self.probabilitySB.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.probabilitySB.sizePolicy().hasHeightForWidth())
        self.probabilitySB.setSizePolicy(sizePolicy2)
        self.probabilitySB.setAlignment(Qt.AlignCenter)
        self.probabilitySB.setDecimals(3)
        self.probabilitySB.setMaximum(1.000000000000000)
        self.probabilitySB.setSingleStep(0.100000000000000)
        self.probabilitySB.setValue(0.100000000000000)

        self.gridLayout.addWidget(self.probabilitySB, 3, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.heightLabel = QLabel(self.groupBox)
        self.heightLabel.setObjectName(u"heightLabel")
        sizePolicy1.setHeightForWidth(self.heightLabel.sizePolicy().hasHeightForWidth())
        self.heightLabel.setSizePolicy(sizePolicy1)
        self.heightLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.heightLabel, 0, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.widthLabel = QLabel(self.groupBox)
        self.widthLabel.setObjectName(u"widthLabel")
        sizePolicy1.setHeightForWidth(self.widthLabel.sizePolicy().hasHeightForWidth())
        self.widthLabel.setSizePolicy(sizePolicy1)
        self.widthLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.widthLabel, 0, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.imageFromFileRB = QRadioButton(self.groupBox)
        self.imageFromFileRB.setObjectName(u"imageFromFileRB")
        sizePolicy2.setHeightForWidth(self.imageFromFileRB.sizePolicy().hasHeightForWidth())
        self.imageFromFileRB.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.imageFromFileRB, 5, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.widthSB = QSpinBox(self.groupBox)
        self.widthSB.setObjectName(u"widthSB")
        sizePolicy2.setHeightForWidth(self.widthSB.sizePolicy().hasHeightForWidth())
        self.widthSB.setSizePolicy(sizePolicy2)
        self.widthSB.setLayoutDirection(Qt.LeftToRight)
        self.widthSB.setFrame(True)
        self.widthSB.setAlignment(Qt.AlignCenter)
        self.widthSB.setProperty("showGroupSeparator", False)
        self.widthSB.setMinimum(2)
        self.widthSB.setMaximum(1000)
        self.widthSB.setSingleStep(100)
        self.widthSB.setValue(100)

        self.gridLayout.addWidget(self.widthSB, 1, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.randomImageRB = QRadioButton(self.groupBox)
        self.randomImageRB.setObjectName(u"randomImageRB")
        sizePolicy2.setHeightForWidth(self.randomImageRB.sizePolicy().hasHeightForWidth())
        self.randomImageRB.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.randomImageRB, 3, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.pathImageLabel = QLabel(self.groupBox)
        self.pathImageLabel.setObjectName(u"pathImageLabel")
        self.pathImageLabel.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.pathImageLabel.sizePolicy().hasHeightForWidth())
        self.pathImageLabel.setSizePolicy(sizePolicy1)
        self.pathImageLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.pathImageLabel, 4, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.whiteImageRB = QRadioButton(self.groupBox)
        self.whiteImageRB.setObjectName(u"whiteImageRB")
        sizePolicy2.setHeightForWidth(self.whiteImageRB.sizePolicy().hasHeightForWidth())
        self.whiteImageRB.setSizePolicy(sizePolicy2)
        self.whiteImageRB.setChecked(True)

        self.gridLayout.addWidget(self.whiteImageRB, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.heightSB = QSpinBox(self.groupBox)
        self.heightSB.setObjectName(u"heightSB")
        sizePolicy2.setHeightForWidth(self.heightSB.sizePolicy().hasHeightForWidth())
        self.heightSB.setSizePolicy(sizePolicy2)
        self.heightSB.setAlignment(Qt.AlignCenter)
        self.heightSB.setMinimum(2)
        self.heightSB.setMaximum(1000)
        self.heightSB.setSingleStep(100)
        self.heightSB.setValue(100)

        self.gridLayout.addWidget(self.heightSB, 1, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pathLE = QLineEdit(self.groupBox)
        self.pathLE.setObjectName(u"pathLE")
        self.pathLE.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.pathLE.sizePolicy().hasHeightForWidth())
        self.pathLE.setSizePolicy(sizePolicy1)
        self.pathLE.setReadOnly(True)

        self.gridLayout.addWidget(self.pathLE, 5, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.probabilityLabel = QLabel(self.groupBox)
        self.probabilityLabel.setObjectName(u"probabilityLabel")
        self.probabilityLabel.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.probabilityLabel.sizePolicy().hasHeightForWidth())
        self.probabilityLabel.setSizePolicy(sizePolicy1)
        self.probabilityLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.probabilityLabel, 2, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.selectFilePB = QPushButton(self.groupBox)
        self.selectFilePB.setObjectName(u"selectFilePB")
        self.selectFilePB.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.selectFilePB.sizePolicy().hasHeightForWidth())
        self.selectFilePB.setSizePolicy(sizePolicy1)
        self.selectFilePB.setCheckable(False)

        self.gridLayout.addWidget(self.selectFilePB, 5, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.generateImagePB = QPushButton(self.groupBox)
        self.generateImagePB.setObjectName(u"generateImagePB")
        sizePolicy1.setHeightForWidth(self.generateImagePB.sizePolicy().hasHeightForWidth())
        self.generateImagePB.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.generateImagePB, 3, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(3)
        self.gridLayout_2.setVerticalSpacing(0)
        self.allIterationsRB = QRadioButton(self.groupBox_2)
        self.allIterationsRB.setObjectName(u"allIterationsRB")
        self.allIterationsRB.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.allIterationsRB.sizePolicy().hasHeightForWidth())
        self.allIterationsRB.setSizePolicy(sizePolicy3)
        self.allIterationsRB.setChecked(True)

        self.gridLayout_2.addWidget(self.allIterationsRB, 1, 0, 1, 1, Qt.AlignRight|Qt.AlignVCenter)

        self.saveImageToFileCB = QCheckBox(self.groupBox_2)
        self.saveImageToFileCB.setObjectName(u"saveImageToFileCB")
        sizePolicy3.setHeightForWidth(self.saveImageToFileCB.sizePolicy().hasHeightForWidth())
        self.saveImageToFileCB.setSizePolicy(sizePolicy3)
        self.saveImageToFileCB.setChecked(False)

        self.gridLayout_2.addWidget(self.saveImageToFileCB, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.everyNIterationsLabel = QLabel(self.groupBox_2)
        self.everyNIterationsLabel.setObjectName(u"everyNIterationsLabel")
        self.everyNIterationsLabel.setEnabled(False)

        self.gridLayout_2.addWidget(self.everyNIterationsLabel, 2, 2, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.saveItersSB = QSpinBox(self.groupBox_2)
        self.saveItersSB.setObjectName(u"saveItersSB")
        self.saveItersSB.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.saveItersSB.sizePolicy().hasHeightForWidth())
        self.saveItersSB.setSizePolicy(sizePolicy4)
        self.saveItersSB.setAlignment(Qt.AlignCenter)
        self.saveItersSB.setMinimum(1)
        self.saveItersSB.setMaximum(1000000)
        self.saveItersSB.setSingleStep(10000)
        self.saveItersSB.setValue(100)

        self.gridLayout_2.addWidget(self.saveItersSB, 2, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.everyNIterationsRB = QRadioButton(self.groupBox_2)
        self.everyNIterationsRB.setObjectName(u"everyNIterationsRB")
        self.everyNIterationsRB.setEnabled(False)

        self.gridLayout_2.addWidget(self.everyNIterationsRB, 2, 0, 1, 1, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(3)
        self.gridLayout_3.setVerticalSpacing(0)
        self.defaultSavePathCB = QCheckBox(self.groupBox_2)
        self.defaultSavePathCB.setObjectName(u"defaultSavePathCB")
        self.defaultSavePathCB.setEnabled(False)
        self.defaultSavePathCB.setChecked(True)

        self.gridLayout_3.addWidget(self.defaultSavePathCB, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.saveFilePathLE = QLineEdit(self.groupBox_2)
        self.saveFilePathLE.setObjectName(u"saveFilePathLE")
        self.saveFilePathLE.setEnabled(False)
        self.saveFilePathLE.setReadOnly(True)

        self.gridLayout_3.addWidget(self.saveFilePathLE, 1, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.saveFileNameLE = QLineEdit(self.groupBox_2)
        self.saveFileNameLE.setObjectName(u"saveFileNameLE")
        self.saveFileNameLE.setEnabled(False)

        self.gridLayout_3.addWidget(self.saveFileNameLE, 0, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.defaultFileNameCB = QCheckBox(self.groupBox_2)
        self.defaultFileNameCB.setObjectName(u"defaultFileNameCB")
        self.defaultFileNameCB.setEnabled(False)
        self.defaultFileNameCB.setChecked(True)

        self.gridLayout_3.addWidget(self.defaultFileNameCB, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.selectSaveFolderPB = QPushButton(self.groupBox_2)
        self.selectSaveFolderPB.setObjectName(u"selectSaveFolderPB")
        self.selectSaveFolderPB.setEnabled(False)

        self.gridLayout_3.addWidget(self.selectSaveFolderPB, 1, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_4.addLayout(self.gridLayout_3)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.numOfItersLabel = QLabel(self.groupBox_3)
        self.numOfItersLabel.setObjectName(u"numOfItersLabel")
        sizePolicy1.setHeightForWidth(self.numOfItersLabel.sizePolicy().hasHeightForWidth())
        self.numOfItersLabel.setSizePolicy(sizePolicy1)
        self.numOfItersLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.numOfItersLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.numOfItersSB = QSpinBox(self.groupBox_3)
        self.numOfItersSB.setObjectName(u"numOfItersSB")
        sizePolicy1.setHeightForWidth(self.numOfItersSB.sizePolicy().hasHeightForWidth())
        self.numOfItersSB.setSizePolicy(sizePolicy1)
        self.numOfItersSB.setAlignment(Qt.AlignCenter)
        self.numOfItersSB.setMinimum(1)
        self.numOfItersSB.setMaximum(10000000)
        self.numOfItersSB.setSingleStep(10000)
        self.numOfItersSB.setValue(11000)

        self.verticalLayout_2.addWidget(self.numOfItersSB, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.resetPB = QPushButton(self.groupBox_3)
        self.resetPB.setObjectName(u"resetPB")
        self.resetPB.setEnabled(False)

        self.horizontalLayout.addWidget(self.resetPB, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.runPB = QPushButton(self.groupBox_3)
        self.runPB.setObjectName(u"runPB")
        self.runPB.setEnabled(False)

        self.horizontalLayout.addWidget(self.runPB, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.groupBox_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Langton's Ant", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Image", None))
        self.heightLabel.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.widthLabel.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.imageFromFileRB.setText(QCoreApplication.translate("MainWindow", u"Image from file", None))
        self.randomImageRB.setText(QCoreApplication.translate("MainWindow", u"Random image", None))
        self.pathImageLabel.setText(QCoreApplication.translate("MainWindow", u"Path to image", None))
        self.whiteImageRB.setText(QCoreApplication.translate("MainWindow", u"White image", None))
        self.probabilityLabel.setText(QCoreApplication.translate("MainWindow", u"Probability of black pixels", None))
        self.selectFilePB.setText(QCoreApplication.translate("MainWindow", u"Select file", None))
        self.generateImagePB.setText(QCoreApplication.translate("MainWindow", u"Generate image", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Output", None))
        self.allIterationsRB.setText(QCoreApplication.translate("MainWindow", u"All iterations", None))
        self.saveImageToFileCB.setText(QCoreApplication.translate("MainWindow", u"Save images to files", None))
        self.everyNIterationsLabel.setText(QCoreApplication.translate("MainWindow", u"iterations", None))
        self.everyNIterationsRB.setText(QCoreApplication.translate("MainWindow", u"Every          ", None))
        self.defaultSavePathCB.setText(QCoreApplication.translate("MainWindow", u"Default save path", None))
        self.saveFilePathLE.setText(QCoreApplication.translate("MainWindow", u"out", None))
        self.saveFileNameLE.setInputMask(QCoreApplication.translate("MainWindow", u"NNNNNNNNNN", None))
        self.saveFileNameLE.setText(QCoreApplication.translate("MainWindow", u"outImage", None))
        self.defaultFileNameCB.setText(QCoreApplication.translate("MainWindow", u"Default file name", None))
        self.selectSaveFolderPB.setText(QCoreApplication.translate("MainWindow", u"Select folder", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Algorithm", None))
        self.numOfItersLabel.setText(QCoreApplication.translate("MainWindow", u"Number of iterations", None))
        self.resetPB.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.runPB.setText(QCoreApplication.translate("MainWindow", u"RUN", None))
    # retranslateUi

