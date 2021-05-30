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
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 361, 521))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.gridLayoutWidget = QWidget(self.groupBox_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 341, 161))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.whiteImageRB = QRadioButton(self.gridLayoutWidget)
        self.whiteImageRB.setObjectName(u"whiteImageRB")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.whiteImageRB.sizePolicy().hasHeightForWidth())
        self.whiteImageRB.setSizePolicy(sizePolicy2)
        self.whiteImageRB.setChecked(True)

        self.gridLayout.addWidget(self.whiteImageRB, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.heightSB = QSpinBox(self.gridLayoutWidget)
        self.heightSB.setObjectName(u"heightSB")
        sizePolicy2.setHeightForWidth(self.heightSB.sizePolicy().hasHeightForWidth())
        self.heightSB.setSizePolicy(sizePolicy2)
        self.heightSB.setAlignment(Qt.AlignCenter)
        self.heightSB.setMinimum(2)
        self.heightSB.setMaximum(1000)
        self.heightSB.setSingleStep(100)
        self.heightSB.setValue(100)

        self.gridLayout.addWidget(self.heightSB, 1, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.imageFromFileRB = QRadioButton(self.gridLayoutWidget)
        self.imageFromFileRB.setObjectName(u"imageFromFileRB")
        sizePolicy2.setHeightForWidth(self.imageFromFileRB.sizePolicy().hasHeightForWidth())
        self.imageFromFileRB.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.imageFromFileRB, 3, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.randomImageRB = QRadioButton(self.gridLayoutWidget)
        self.randomImageRB.setObjectName(u"randomImageRB")
        sizePolicy2.setHeightForWidth(self.randomImageRB.sizePolicy().hasHeightForWidth())
        self.randomImageRB.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.randomImageRB, 5, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.probabilitySB = QDoubleSpinBox(self.gridLayoutWidget)
        self.probabilitySB.setObjectName(u"probabilitySB")
        self.probabilitySB.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.probabilitySB.sizePolicy().hasHeightForWidth())
        self.probabilitySB.setSizePolicy(sizePolicy2)
        self.probabilitySB.setAlignment(Qt.AlignCenter)
        self.probabilitySB.setDecimals(3)
        self.probabilitySB.setMaximum(1.000000000000000)
        self.probabilitySB.setSingleStep(0.100000000000000)
        self.probabilitySB.setValue(0.100000000000000)

        self.gridLayout.addWidget(self.probabilitySB, 5, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pathLE = QLineEdit(self.gridLayoutWidget)
        self.pathLE.setObjectName(u"pathLE")
        self.pathLE.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.pathLE.sizePolicy().hasHeightForWidth())
        self.pathLE.setSizePolicy(sizePolicy1)
        self.pathLE.setReadOnly(True)

        self.gridLayout.addWidget(self.pathLE, 3, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.generateImagePB = QPushButton(self.gridLayoutWidget)
        self.generateImagePB.setObjectName(u"generateImagePB")
        sizePolicy1.setHeightForWidth(self.generateImagePB.sizePolicy().hasHeightForWidth())
        self.generateImagePB.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.generateImagePB, 5, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.widthSB = QSpinBox(self.gridLayoutWidget)
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

        self.selectFilePB = QPushButton(self.gridLayoutWidget)
        self.selectFilePB.setObjectName(u"selectFilePB")
        self.selectFilePB.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.selectFilePB.sizePolicy().hasHeightForWidth())
        self.selectFilePB.setSizePolicy(sizePolicy1)
        self.selectFilePB.setCheckable(False)

        self.gridLayout.addWidget(self.selectFilePB, 3, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.gridLayoutWidget_2 = QWidget(self.groupBox)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 20, 240, 61))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(3)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.allIterationsRB = QRadioButton(self.gridLayoutWidget_2)
        self.allIterationsRB.setObjectName(u"allIterationsRB")
        self.allIterationsRB.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.allIterationsRB.sizePolicy().hasHeightForWidth())
        self.allIterationsRB.setSizePolicy(sizePolicy3)
        self.allIterationsRB.setChecked(True)

        self.gridLayout_2.addWidget(self.allIterationsRB, 1, 0, 1, 1, Qt.AlignRight|Qt.AlignVCenter)

        self.saveImageToFileCB = QCheckBox(self.gridLayoutWidget_2)
        self.saveImageToFileCB.setObjectName(u"saveImageToFileCB")
        sizePolicy3.setHeightForWidth(self.saveImageToFileCB.sizePolicy().hasHeightForWidth())
        self.saveImageToFileCB.setSizePolicy(sizePolicy3)
        self.saveImageToFileCB.setChecked(False)

        self.gridLayout_2.addWidget(self.saveImageToFileCB, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_5 = QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(False)

        self.gridLayout_2.addWidget(self.label_5, 2, 2, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.saveItersSB = QSpinBox(self.gridLayoutWidget_2)
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

        self.gridLayout_2.addWidget(self.saveItersSB, 2, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.everyNIterationsRB = QRadioButton(self.gridLayoutWidget_2)
        self.everyNIterationsRB.setObjectName(u"everyNIterationsRB")
        self.everyNIterationsRB.setEnabled(False)

        self.gridLayout_2.addWidget(self.everyNIterationsRB, 2, 0, 1, 1, Qt.AlignRight|Qt.AlignVCenter)

        self.gridLayoutWidget_3 = QWidget(self.groupBox)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(30, 90, 321, 51))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(3)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.defaultSavePathCB = QCheckBox(self.gridLayoutWidget_3)
        self.defaultSavePathCB.setObjectName(u"defaultSavePathCB")
        self.defaultSavePathCB.setEnabled(False)
        self.defaultSavePathCB.setChecked(True)

        self.gridLayout_3.addWidget(self.defaultSavePathCB, 1, 0, 1, 1)

        self.saveFilePathLE = QLineEdit(self.gridLayoutWidget_3)
        self.saveFilePathLE.setObjectName(u"saveFilePathLE")
        self.saveFilePathLE.setEnabled(False)
        self.saveFilePathLE.setReadOnly(True)

        self.gridLayout_3.addWidget(self.saveFilePathLE, 1, 1, 1, 1)

        self.saveFileNameLE = QLineEdit(self.gridLayoutWidget_3)
        self.saveFileNameLE.setObjectName(u"saveFileNameLE")
        self.saveFileNameLE.setEnabled(False)

        self.gridLayout_3.addWidget(self.saveFileNameLE, 0, 1, 1, 1)

        self.defaultFileNameCB = QCheckBox(self.gridLayoutWidget_3)
        self.defaultFileNameCB.setObjectName(u"defaultFileNameCB")
        self.defaultFileNameCB.setEnabled(False)
        self.defaultFileNameCB.setChecked(True)

        self.gridLayout_3.addWidget(self.defaultFileNameCB, 0, 0, 1, 1)

        self.selectSaveFolderPB = QPushButton(self.gridLayoutWidget_3)
        self.selectSaveFolderPB.setObjectName(u"selectSaveFolderPB")
        self.selectSaveFolderPB.setEnabled(False)

        self.gridLayout_3.addWidget(self.selectSaveFolderPB, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayoutWidget_2 = QWidget(self.groupBox_3)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 20, 100, 51))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.numOfItersSB = QSpinBox(self.verticalLayoutWidget_2)
        self.numOfItersSB.setObjectName(u"numOfItersSB")
        sizePolicy1.setHeightForWidth(self.numOfItersSB.sizePolicy().hasHeightForWidth())
        self.numOfItersSB.setSizePolicy(sizePolicy1)
        self.numOfItersSB.setAlignment(Qt.AlignCenter)
        self.numOfItersSB.setMinimum(1)
        self.numOfItersSB.setMaximum(10000000)
        self.numOfItersSB.setSingleStep(10000)
        self.numOfItersSB.setValue(11000)

        self.verticalLayout_2.addWidget(self.numOfItersSB)

        self.horizontalLayoutWidget = QWidget(self.groupBox_3)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 80, 161, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.resetPB = QPushButton(self.horizontalLayoutWidget)
        self.resetPB.setObjectName(u"resetPB")
        self.resetPB.setEnabled(False)

        self.horizontalLayout.addWidget(self.resetPB)

        self.runPB = QPushButton(self.horizontalLayoutWidget)
        self.runPB.setObjectName(u"runPB")
        self.runPB.setEnabled(False)

        self.horizontalLayout.addWidget(self.runPB)


        self.verticalLayout.addWidget(self.groupBox_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Langton's Ant", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Image", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.whiteImageRB.setText(QCoreApplication.translate("MainWindow", u"White image", None))
        self.imageFromFileRB.setText(QCoreApplication.translate("MainWindow", u"Image from file", None))
        self.randomImageRB.setText(QCoreApplication.translate("MainWindow", u"Random image", None))
        self.generateImagePB.setText(QCoreApplication.translate("MainWindow", u"Generate image", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Path to image", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.selectFilePB.setText(QCoreApplication.translate("MainWindow", u"Select file", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Probability of black pixels", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Output", None))
        self.allIterationsRB.setText(QCoreApplication.translate("MainWindow", u"All iterations", None))
        self.saveImageToFileCB.setText(QCoreApplication.translate("MainWindow", u"Save images to files", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"iterations", None))
        self.everyNIterationsRB.setText(QCoreApplication.translate("MainWindow", u"Every          ", None))
        self.defaultSavePathCB.setText(QCoreApplication.translate("MainWindow", u"Default save path", None))
        self.saveFilePathLE.setText(QCoreApplication.translate("MainWindow", u"out/", None))
        self.saveFileNameLE.setInputMask(QCoreApplication.translate("MainWindow", u"NNNNNNNNNN", None))
        self.saveFileNameLE.setText(QCoreApplication.translate("MainWindow", u"outImage", None))
        self.defaultFileNameCB.setText(QCoreApplication.translate("MainWindow", u"Default file name", None))
        self.selectSaveFolderPB.setText(QCoreApplication.translate("MainWindow", u"Select folder", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Algorithm", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Number of iterations", None))
        self.resetPB.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.runPB.setText(QCoreApplication.translate("MainWindow", u"RUN", None))
    # retranslateUi

