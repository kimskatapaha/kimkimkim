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
#-Ui클래스 생성 (https://doc.qt.io/qtforpython-5/PySide2/QtUiTools/QUiLoader.html#more)

        self.setWindowTitle("KHN_UI_Test")
        self.resize(475,275)
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
        self.ui.create_Enter_bt.clicked.connect(lambda: self.executeCreation)
        
        self.ui.sub_lock_bt.clicked.connect(self.Sub_lock)
        self.ui.sub_unlock_bt.clicked.connect(self.Sub_Unlock)
        #-라디오 버튼 (https://pbj0812.tistory.com/339)
        self.ui.findingNodeEnter_bt.clicked.connect(lambda: self.FindSet(self))
        #-텍스트 필드는 함수로 연결해줘야 함. 인수는 self(다른 글자 넣어도 됨. 근데 헷갈리니까 그냥 셀프로)
        #-버튼과 함수들을 연결
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





    def FindSet(self,Query):
        Query = self.ui.findingnode_TextF_txf.toPlainText() 
                    #-필드에 쓰인 텍스트를 가져와야 하므로 toPlainText을 사용(https://wikidocs.net/35491)
        variable_obj = []
        
        for obj in cmds.ls(type='transform'):
            if Query in obj:
                variable_obj.append(obj)
        if variable_obj:
            cmds.select(variable_obj, replace=True)
        else:
            print("Not found")




    def executeCreation(self):
        self.create_Loc_rbt = self.ui.create_Loc_rbt.isChecked()
        self.create_Clu_rbt = self.ui.create_Clu_rbt.isChecked()
        self.create_Jnt_rbt = self.ui.create_Jnt_rbt.isChecked()
        if self.create_Loc_rbt == True:
            cmds.spaceLocator()
        elif self.create_Clu_rbt == True:
            cmds.cluster()
        else:
            cmds.joint()


    def Sub_lock(lock_Check):
        lock_pre_lst = cmds.ls(type='RedshiftMeshParameters')
        lock_lst = [lock_x for lock_x in lock_pre_lst if '_sub' in lock_x]

        print(lock_lst)
        if lock_Check == True:
            lock_lock = True
        else:
            lock_lock = False
        lock_lst_lock = [cmds.lockNode(lock_x, l=lock_lock) for lock_x in lock_lst]

    Sub_lock(True)


    def Sub_Unlock(Unlock_Check):
        Unlock_pre_lst = cmds.ls(type='RedshiftMeshParameters')
        Unlock_lst = [Unlock_x for Unlock_x in Unlock_pre_lst if '_sub' in Unlock_x]

        print(Unlock_lst)
        if Unlock_Check == True:
            Unlock_lock = True
        else:
            Unlock_lock = False
        Unlock_lst_lock = [cmds.lockNode(Unlock_x, l=Unlock_lock) for Unlock_x in Unlock_lst]

    Sub_Unlock(False)
        
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