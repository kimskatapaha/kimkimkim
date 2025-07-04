import maya.mel as mel
import maya.OpenMayaUI as omui
import getpass
import maya.cmds as cmds
from PySide2.QtUiTools import *
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtUiTools
from PySide2 import QtGui
from shiboken2 import wrapInstance
#-



User= getpass.getuser()
version = cmds.about(version=True)
Path= "C:/Users/{}/Documents/maya/{}/scripts/GimHa".format(User,version)
#-폴더 경로설정

def Gim_window():
    Gim_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(Gim_window_ptr), QtWidgets.QWidget)
#-Ui윈도우 생성

class DesignerUI(QtWidgets.QDialog):
    def __init__(self, parent=Gim_window()):
        super(DesignerUI, self).__init__(parent)
#-Ui클래스 생성

        self.setWindowTitle("KHN_UI_Test")
        self.resize(477,280)
        self.init_ui()
        self.create_connection()
#-Ui 메서드 정의

    def init_ui(self):

        f = QtCore.QFile(Path + "/pyside2_DesignerTest_ver.04.ui")
        #-pyside파일 경로설정
        
        f.open(QtCore.QFile.ReadOnly)

        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(f, parentWidget=self)

        f.close()
        #-열었다가 닫는 이유는 무한루프를 끊기 위함. (https://onlytojay.medium.com/pyside2-1-%EA%B8%B0%EB%B3%B8%EB%8F%99%EC%9E%91%EC%9B%90%EB%A6%AC-72ea6572a65b)
#---------------------------------------------------------

    def create_connection(self):
        self.ui.paintSkinWeightTool_bt.clicked.connect(self.ArtPaintSkinWeightsTool)
        self.ui.deleteHistoryAndFreeze_bt.clicked.connect(self.DeleteHisAndFreeze)
        self.ui.handJointClean_bt.clicked.connect(self.LfHand_Joint_Cleaner)
        self.ui.oneclick_L_J_bt.clicked.connect(self.oneClickMatchJ_L)
        self.ui.oneclick_C_J_bt.clicked.connect(self.oneClickMatchC_L)
        self.ui.oneclick_D_G_bt.clicked.connect(self.oneClickblend)
        #-버튼과 함수들을 연결
        self.ui.create_Enter_bt.clicked.connect(self.executeCreation)      
        self.ui.findingNodeEnter_bt.clicked.connect(self.FindSet)
        #-이 두개 오류남


#---------------------------------------------------------



    #-함수시작
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



    def ArtPaintSkinWeightsTool(*args):
        cmds.ArtPaintSkinWeightsTool()


    def DeleteHisAndFreeze(*args):
        cmds.select(cl=True)
        selA = cmds.ls('*_Geo', '*_geo', type='transform')
        for Geo in selA:
            cmds.delete(Geo, constructionHistory=True)
            cmds.makeIdentity(Geo, apply=True, t=1, r=1, s=1)


    def oneClickMatchJ_L(*args):
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


    def oneClickMatchC_L(*args):
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


    def oneClickblend(*args):
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





    def FindSet(*args):
        Query = cmds.textField(ConstraintTextset, q=1, tx=1)
        Findnode(Query)

        all_objects = cmds.ls()
        variable_obj = []
        for obj in all_objects:
            if self.Find_Search in obj:
                variable_obj.append(obj)
        if variable_obj:
            cmds.select(variable_obj, replace=True)
        else:
            print("Not found")



    def executeCreation(*args):
        selectedRadioButton = cmds.radioButtonGrp(createTypeRadio, q=True, select=True)

        if selectedRadioButton == 1:
            createLoc()
        elif selectedRadioButton == 2:
            createClu()
        elif selectedRadioButton == 3:
            createJnt()

        def createJnt():
            cmds.joint()
        def createLoc():
            cmds.spaceLocator()
        def createClu():
            cmds.cluster()
    #-함수 끝


#---------------------------------------------------------



if __name__ == "__main__":
    try:
        desinger_ui.close()
        desinger_ui.deleteLater()
    except:
        pass

    desinger_ui = DesignerUI()
    desinger_ui.show()
#-클래스를 변수화 하여 열기