# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imgeModeWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(875, 695)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(350, 20, 511, 411))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 481, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_ImagePreviewRaw = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_ImagePreviewRaw.setObjectName("radioButton_ImagePreviewRaw")
        self.horizontalLayout.addWidget(self.radioButton_ImagePreviewRaw)
        self.radioButton_ImagePreviewGray = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_ImagePreviewGray.setObjectName("radioButton_ImagePreviewGray")
        self.horizontalLayout.addWidget(self.radioButton_ImagePreviewGray)
        self.radioButton_ImagePreviewBW = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_ImagePreviewBW.setObjectName("radioButton_ImagePreviewBW")
        self.horizontalLayout.addWidget(self.radioButton_ImagePreviewBW)
        self.label_ImagePreview = QtWidgets.QLabel(self.groupBox)
        self.label_ImagePreview.setGeometry(QtCore.QRect(10, 80, 480, 320))
        self.label_ImagePreview.setFrameShape(QtWidgets.QFrame.Box)
        self.label_ImagePreview.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ImagePreview.setObjectName("label_ImagePreview")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 20, 301, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_OpenImage = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_OpenImage.setGeometry(QtCore.QRect(20, 30, 251, 61))
        self.pushButton_OpenImage.setObjectName("pushButton_OpenImage")
        self.textEdit_ShowImageName = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_ShowImageName.setGeometry(QtCore.QRect(20, 106, 251, 81))
        self.textEdit_ShowImageName.setObjectName("textEdit_ShowImageName")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 250, 301, 261))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_HistogramView = QtWidgets.QLabel(self.groupBox_3)
        self.label_HistogramView.setGeometry(QtCore.QRect(20, 30, 256, 128))
        self.label_HistogramView.setFrameShape(QtWidgets.QFrame.Box)
        self.label_HistogramView.setAlignment(QtCore.Qt.AlignCenter)
        self.label_HistogramView.setObjectName("label_HistogramView")
        self.horizontalSlider_HistogramThresholdValue = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSlider_HistogramThresholdValue.setGeometry(QtCore.QRect(14, 160, 270, 21))
        self.horizontalSlider_HistogramThresholdValue.setMinimum(1)
        self.horizontalSlider_HistogramThresholdValue.setMaximum(254)
        self.horizontalSlider_HistogramThresholdValue.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_HistogramThresholdValue.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider_HistogramThresholdValue.setObjectName("horizontalSlider_HistogramThresholdValue")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 190, 261, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.spinBox_HistogramThresholdValue = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.spinBox_HistogramThresholdValue.setWrapping(True)
        self.spinBox_HistogramThresholdValue.setSuffix("")
        self.spinBox_HistogramThresholdValue.setMinimum(1)
        self.spinBox_HistogramThresholdValue.setMaximum(254)
        self.spinBox_HistogramThresholdValue.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.spinBox_HistogramThresholdValue.setObjectName("spinBox_HistogramThresholdValue")
        self.horizontalLayout_2.addWidget(self.spinBox_HistogramThresholdValue)
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(350, 450, 511, 231))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_OutputImagePreview = QtWidgets.QLabel(self.groupBox_4)
        self.label_OutputImagePreview.setGeometry(QtCore.QRect(40, 50, 256, 128))
        self.label_OutputImagePreview.setFrameShape(QtWidgets.QFrame.Box)
        self.label_OutputImagePreview.setAlignment(QtCore.Qt.AlignCenter)
        self.label_OutputImagePreview.setObjectName("label_OutputImagePreview")
        self.checkBox_invertBW = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_invertBW.setGeometry(QtCore.QRect(320, 60, 101, 19))
        self.checkBox_invertBW.setObjectName("checkBox_invertBW")
        self.groupBox_5 = QtWidgets.QGroupBox(Form)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 530, 301, 151))
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton_OutputBWImageToCArray = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_OutputBWImageToCArray.setGeometry(QtCore.QRect(30, 30, 231, 91))
        self.pushButton_OutputBWImageToCArray.setObjectName("pushButton_OutputBWImageToCArray")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Image"))
        self.groupBox.setTitle(_translate("Form", "PreView Selection"))
        self.radioButton_ImagePreviewRaw.setText(_translate("Form", "Raw"))
        self.radioButton_ImagePreviewGray.setText(_translate("Form", "Gray"))
        self.radioButton_ImagePreviewBW.setText(_translate("Form", "BlackAndWhite"))
        self.label_ImagePreview.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Image PreView</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("Form", "File Import"))
        self.pushButton_OpenImage.setText(_translate("Form", "Open Image"))
        self.groupBox_3.setTitle(_translate("Form", "Gray Histogram and BW threshold"))
        self.label_HistogramView.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Histogram</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "Threshold Value"))
        self.groupBox_4.setTitle(_translate("Form", "Output Image"))
        self.label_OutputImagePreview.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Output Image</span></p></body></html>"))
        self.checkBox_invertBW.setText(_translate("Form", "Invert BW"))
        self.groupBox_5.setTitle(_translate("Form", "GroupBox"))
        self.pushButton_OutputBWImageToCArray.setText(_translate("Form", "Output BW image to C array"))
