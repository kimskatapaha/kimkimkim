import maya.cmds as cmds
from functools import partial
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


#---external Function Set-----
def createJnt():
    cmds.joint()


def createLoc():
    cmds.spaceLocator()


def createClu():
    cmds.cluster()


def LfHand_Joint_Cleaner(*args):
    Index = cmds.listRelatives('LfIndexRoot_Jnt', ad=True, type='joint')
    Middle = cmds.listRelatives('LfMiddleRoot_Jnt', ad=True, type='joint')
    Ring = cmds.listRelatives('LfRingRoot_Jnt', ad=True, type='joint')
    Thumb = cmds.listRelatives('LfThumbRoot_Jnt', ad=True, type='joint')
    Pinky = cmds.listRelatives('LfPinkyRoot_Jnt', ad=True, type='joint')
    

    if Index:
        for IntheIndex in Index:
            cmds.setAttr(IntheIndex + ".jointOrientX", 0)
            cmds.setAttr(IntheIndex + ".jointOrientY", 0)
            cmds.setAttr(IntheIndex + ".jointOrientZ", 0)
    if Middle:
        for IntheMiddle in Middle:
            cmds.setAttr(IntheMiddle + ".jointOrientX", 0)
            cmds.setAttr(IntheMiddle + ".jointOrientY", 0)
            cmds.setAttr(IntheMiddle + ".jointOrientZ", 0)
    if Ring:
        for IntheRing in Ring:
            cmds.setAttr(IntheRing + ".jointOrientX", 0)
            cmds.setAttr(IntheRing + ".jointOrientY", 0)
            cmds.setAttr(IntheRing + ".jointOrientZ", 0)
    if Thumb:
        for IntheThumb in Thumb:
            cmds.setAttr(IntheThumb + ".jointOrientX", 0)
            cmds.setAttr(IntheThumb + ".jointOrientY", 0)
            cmds.setAttr(IntheThumb + ".jointOrientZ", 0)
    if Pinky:
        for InthePinky in Pinky:
            cmds.setAttr(InthePinky + ".jointOrientX", 0)
            cmds.setAttr(InthePinky + ".jointOrientY", 0)
            cmds.setAttr(InthePinky + ".jointOrientZ", 0)

            
    for IntheIndex in Index:
        cmds.setAttr(IntheIndex + ".rotateX", 0)
        cmds.setAttr(IntheIndex + ".rotateY", 0)
        cmds.setAttr(IntheIndex + ".rotateZ", 0)

    for IntheMiddle in Middle:
        cmds.setAttr(IntheMiddle + ".rotateX", 0)
        cmds.setAttr(IntheMiddle + ".rotateY", 0)
        cmds.setAttr(IntheMiddle + ".rotateZ", 0)


    for IntheRing in Ring:
        cmds.setAttr(IntheRing + ".rotateX", 0)
        cmds.setAttr(IntheRing + ".rotateY", 0)
        cmds.setAttr(IntheRing + ".rotateZ", 0)

    for IntheThumb in Thumb:
        cmds.setAttr(IntheThumb + ".rotateX", 0)
        cmds.setAttr(IntheThumb + ".rotateY", 0)
        cmds.setAttr(IntheThumb + ".rotateZ", 0)

    for InthePinky in Pinky:
        cmds.setAttr(InthePinky + ".rotateX", 0)
        cmds.setAttr(InthePinky + ".rotateY", 0)
        cmds.setAttr(InthePinky + ".rotateZ", 0)



def ArtPaintSkinWeightsTool():
    cmds.ArtPaintSkinWeightsTool()


def DeleteHisAndFreeze():
    cmds.select(cl=True)
    selA = cmds.ls('*_Geo', '*_geo', type='transform')
    for Geo in selA:
        cmds.delete(Geo, constructionHistory=True)
        cmds.makeIdentity(Geo, apply=True, t=1, r=1, s=1)


def oneClickMatchJ_L():
    selected = cmds.ls(selection=True)
    locList = []
    jntList = []
    for obj in selected:
        if '_Jnt' in obj:
            jntList.append(obj)
        if '_Loc' in obj:
            locList.append(obj)
    for loc in locList:
        loc_n_name = loc.split('_')[-2]
        for jnt in jntList:
            jnt_n_name = jnt.split('_')[-2]
            if jnt_n_name.isdigit() and loc_n_name.isdigit() and jnt_n_name == loc_n_name:
                cmds.matchTransform(loc, jnt)
                break


def oneClickMatchC_L():
    selected = cmds.ls(selection=True)
    ctrlList = []
    jntList = []
    for obj in selected:
        if '_Jnt' in obj:
            jntList.append(obj)
        if '_Ctrl' in obj:
            ctrlList.append(obj)
    for ctrl in ctrlList:
        ctrl_n_name = ctrl.split('_')[-2]
        for jnt in jntList:
            jnt_n_name = jnt.split('_')[-2]
            if jnt_n_name.isdigit() and ctrl_n_name.isdigit() and jnt_n_name == ctrl_n_name:
                cmds.matchTransform(ctrl, jnt)
                break


def oneClickblend():
    selected = cmds.ls(selection=True)
    before = []
    after = []
    for obj in selected:
        if '_Geo' in obj:
            before.append(obj)
        if '_Dummy' in obj:
            after.append(obj)
    for Geo in before:
        Geo_n_name = Geo.split('_')[-2]
        for Dum in after:
            Dum_n_name = Dum.split('_')[-2]
            if Geo_n_name.isdigit() and Dum_n_name.isdigit() and Geo_n_name == Dum_n_name:
                cmds.blendShape(Dum, Geo)


def Findnode(query):
    all_objects = cmds.ls()
    variable_obj = []
    for obj in all_objects:
        if query in obj:
            variable_obj.append(obj)
    if variable_obj:
        cmds.select(variable_obj, replace=True)
    else:
        print("Not found")




#---Window Set-----



#---Internal function-----
    def FindSet(*args):
        Query = cmds.textField(ConstraintTextset, q=1, tx=1)
        Findnode(Query)



    def executeCreation(*args):
        selectedRadioButton = cmds.radioButtonGrp(createTypeRadio, q=True, select=True)
        if selectedRadioButton == 1:
            createLoc()
        elif selectedRadioButton == 2:
            createClu()
        elif selectedRadioButton == 3:
            createJnt()


def Khn_Ui():
    if cmds.window('win', exists=True):
        cmds.deleteUI('win')

    app = QApplication.instance()
    if app is None:
        app = QApplication([])

    win = QDialog()
    ui = Khn_Ui_Dialog()
    ui.setupUi(win)
    win.show()

class Khn_Ui_Dialog(object):
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


        self.label.setBuddy(self.pushButton)
        #endif // QT_CONFIG(shortcut)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    
    def retranslateUi(self, Dialog):
        self.label.setText(QCoreApplication.translate("Dialog", u"Create  :", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"Loctor", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"Cluster", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Joint", None))

        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))

        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Paint Skin Weights Tool", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Hand Joint Clean", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Delete History And Freeze", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u"one Click Match/blend", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Loc->Jnt", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"Ctrl->Jnt", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"Dummy->Geo", None))

        self.label_3.setText(QCoreApplication.translate("Dialog", u"Finding Node :", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"Enter", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Enter", None))


if __name__ == '__main__':
    app = QApplication([])

    mainWindow = QDialog()
    ui = Khn_Ui_Dialog()
    ui.setupUi(mainWindow)
    ui.retranslateUi(mainWindow)

    layout = QVBoxLayout()
    layout.addWidget(mainWindow)
    mainWindow.setLayout(layout)
    mainWindow.setWindowTitle("khn_Ui")

    mainWindow.show()

