# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pyside2_DesignerTest_verNOVFgw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(462, 333)
        Dialog.setLayoutDirection(Qt.LeftToRight)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(330, 90, 81, 51))
        self.buttonBox.setTabletTracking(False)
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(330, 150, 75, 23))
        self.toolButton = QToolButton(Dialog)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(320, 190, 91, 71))
        self.toolButton.setCheckable(False)
        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(170, 50, 81, 61))
        self.radioButton = QRadioButton(Dialog)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(40, 70, 90, 16))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 210, 56, 12))
        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(90, 210, 181, 61))
        self.textBrowser.setOverwriteMode(False)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 120, 191, 20))
        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(350, 70, 76, 22))
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.textBrowser)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.checkBox, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.radioButton)
        QWidget.setTabOrder(self.radioButton, self.textBrowser)
        QWidget.setTabOrder(self.textBrowser, self.toolButton)
        QWidget.setTabOrder(self.toolButton, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.comboBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        Dialog.accepted.connect(self.comboBox.clear)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.toolButton.setText(QCoreApplication.translate("Dialog", u"what??", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"RadioButton", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Label1", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Gulim'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Test </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.lineEdit.setText(QCoreApplication.translate("Dialog", u"utyiyuyiu", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"d", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"dd", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"ddd", None))

    # retranslateUi

