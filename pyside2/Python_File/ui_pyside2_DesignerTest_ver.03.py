# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pyside2_DesignerTest_verXYIDDz.ui'
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
        Dialog.resize(448, 262)
        Dialog.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 50, 431, 31))
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 80, 431, 31))
        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 110, 431, 31))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(15, 152, 421, 20))
        self.label_2.setToolTipDuration(-1)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 220, 121, 31))
        self.pushButton_8 = QPushButton(Dialog)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(380, 220, 61, 31))
        self.pushButton_8.setAcceptDrops(False)
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(100, 220, 271, 31))
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 431, 41))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.radioButton = QRadioButton(self.widget)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.widget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.widget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout.addWidget(self.radioButton_3)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setAcceptDrops(False)

        self.horizontalLayout.addWidget(self.pushButton)

        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(10, 170, 431, 41))
        self.splitter.setOrientation(Qt.Horizontal)
        self.pushButton_5 = QPushButton(self.splitter)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.splitter.addWidget(self.pushButton_5)
        self.pushButton_6 = QPushButton(self.splitter)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.splitter.addWidget(self.pushButton_6)
        self.pushButton_7 = QPushButton(self.splitter)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.splitter.addWidget(self.pushButton_7)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.pushButton)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Paint Skin Weights Tool", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Hand Joint Clean", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Delete History And Freeze", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"one Click Match/blend", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Finding Node :", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"Enter", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Create  :", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"Loctor", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"Cluster", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Joint", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Enter", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Loc->Jnt", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"Ctrl->Jnt", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"Dummy->Geo", None))
    # retranslateUi

