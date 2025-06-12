
import maya.mel as mel
import maya.OpenMayaUI as omui
import getpass
import maya.cmds as cmds
import maya.cmds as mc
import os


from PySide2.QtUiTools import *
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtUiTools
from PySide2 import QtGui
from shiboken2 import wrapInstance
from functools import partial
#모듈 임포트




User= getpass.getuser()
version = cmds.about(version=True)
Path= "C:/Users/{}/Documents/maya/{}/scripts/GimHa/new".format(User,version)
#폴더 경로설정


def Gim_window():
    Gim_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(Gim_window_ptr), QtWidgets.QWidget)
    #Ui윈도우 생성


class DesignerUI(QtWidgets.QDialog):
    def __init__(self, parent=Gim_window()):
        super(DesignerUI, self).__init__(parent)
        #Ui클래스 생성 (https://doc.qt.io/qtforpython-5/PySide2/QtUiTools/QUiLoader.html#more)


        self.setWindowTitle("KHN_UI")
        self.resize(464, 512)
        self.init_ui()
        self.create_connection()
        #Ui 메서드 정의


    def init_ui(self):


        f = QtCore.QFile(Path + "/Kim_Ui_Re_Pyside_07.ui")
        #pyside파일 경로설정
        
        f.open(QtCore.QFile.ReadOnly)


        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(f, parentWidget=self)


        f.close()
        #열었다가 닫는 이유는 무한루프를 끊기 위함. (https://onlytojay.medium.com/pyside2-1-%EA%B8%B0%EB%B3%B8%EB%8F%99%EC%9E%91%EC%9B%90%EB%A6%AC-72ea6572a65b)
#---------------------------------------------------------


    def create_connection(self):
        self.ui.objectMirror_bt.clicked.connect(self.Blsh_ObjMirror)
        self.ui.JointClean_bt.clicked.connect(self.Joint_Cleaner)
        self.ui.create_Enter_bt.clicked.connect(lambda: self.executeCreation())
        #라디오 버튼 (https://pbj0812.tistory.com/339)
        

        self.ui.Z0_bt.clicked.connect(self.Z0_Out)
        self.ui.skinAllClear_bt.clicked.connect(self.VtxSkinCopy)
        self.ui.ctrlConnect_bt.clicked.connect(self.ConnenctCtrl)
        #2025.03.04 추가 =Dn
        self.ui.rename_bt.clicked.connect(self.Function_ReName)
        #2025.03.04 추가 =rename
        #텍스트 필드는 함수로 연결해줘야 함. 인수는 self(다른 글자 넣어도 됨. 근데 헷갈리니까 그냥 셀프로)

        self.ui.sub_lock_bt.clicked.connect(lambda: self.Sub_lock())
        self.ui.sub_unlock_bt.clicked.connect(self.Sub_unlock)
        self.ui.keydelete_bt.clicked.connect(self.key_Delete)
        self.ui.turtledelete_bt.clicked.connect(self.TurtleTurnOff)

        self.ui.copyskin_bt.clicked.connect(self.cpSkin)
        self.ui.polcf_loc_bt.clicked.connect(self.CrvPOCIF)
        self.ui.foli_bt.clicked.connect(lambda : self.Function_JntFoli())
        self.ui.min_find_bt.clicked.connect(self.create_MinFind)
        self.ui.min_delete_bt.clicked.connect(self.create_MinDel)
        
        #버튼과 함수들을 연결
#---------------------------------------------------------




    #함수시작
    def Joint_Cleaner(*args):
        Joint_sel = cmds.ls(selection=True, type='joint')
            
        
        if Joint_sel:
            for IntheJoint in Joint_sel:
                cmds.setAttr(IntheJoint + ".jointOrientX", 0)
                cmds.setAttr(IntheJoint + ".jointOrientY", 0)
                cmds.setAttr(IntheJoint + ".jointOrientZ", 0)
    
            for IntheJoint in Joint_sel:
                cmds.setAttr(IntheJoint + ".rotateX", 0)
                cmds.setAttr(IntheJoint + ".rotateY", 0)
                cmds.setAttr(IntheJoint + ".rotateZ", 0)




    import maya.cmds as cmds

    def Blsh_ObjMirror(*args):
        selected = cmds.ls(selection=True)

        for ctrl in selected:
            # 원래의 위치 및 회전 값을 가져오기
            origin_translation = cmds.xform(ctrl, q=True, translation=True, worldSpace=True)
            origin_rotation = cmds.xform(ctrl, q=True, rotation=True, worldSpace=True)

            # X 위치 및 Y, Z 회전값 반전
            mirrored_translation = [-origin_translation[0], origin_translation[1], origin_translation[2]]
            mirrored_rotation = [origin_rotation[0], -origin_rotation[1], -origin_rotation[2]]

            # 새로운 값 적용
            cmds.xform(ctrl, translation=mirrored_translation, worldSpace=True)
            cmds.xform(ctrl, rotation=mirrored_rotation, worldSpace=True)




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


    #2025.03.04 추가 함수
    def Function_Pre_ReName(self,*args):
        self.SufFix = self.ui.Suffix_rename_TP.toPlainText()
        self.PreFix = self.ui.Prefix_rename_TP.toPlainText()
        self.Name = self.ui.Name_rename_TP.toPlainText()  

        sel = cmds.ls(sl=1)

        if self.Prefix_rename_TP == '':
                PreFix = ''
        else:
            PreFix = self.Prefix_rename_TP

        if self.Suffix_rename_TP == '':
                SufFix = ''
        else:
            SufFix = self.Name_rename_TP

        self.Namelist = []
        if len(sel) == 0:
            Range = 1
        else:
            Range = len(sel)

        for x in range(0, Range):
            if self.Name_rename_TP == '':
                if len(sel) == 0:
                    Name = 'NoName'
                else:
                    Name = sel[x]
            else:
                Name = self.Name_rename_TP

            Num = int(self.ui.SB_rename_StartNum.value()) + x

            if self.Name_rename_TP == '':
                NameSet = str(PreFix) + str(Name) + str(SufFix)
            else:
                NameSet = str(PreFix) + str(Name) + str(Num) + str(SufFix)

            self.Namelist.append(NameSet)

        if self.Namelist == '':
            self.Namelist = ['nonName']

    
    def Function_ReName(self,*args):
        self.NameSetting = self.Function_Pre_ReName()
        self.sel = cmds.ls(sl=1)

        for x in range(0, len(sel)):
            try:
                cmds.rename(sel[x], self.Namelist[x])
            except:
                pass



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



    def Sub_lock(Check,self):
        pre_lst = cmds.ls(type='RedshiftMeshParameters')
        lst = [x for x in pre_lst if '_sub' in x]


        if Check:
            lock = True
        else:
            lock = False


        for obj in lst:
            cmds.lockNode(obj, lock=lock)



    def Sub_unlock(self):
        pre_lst = cmds.ls(type='RedshiftMeshParameters')
        lst = [x for x in pre_lst if '_sub' in x]
        lock = False


        lst_lock = [cmds.lockNode(x, l=lock) for x in lst]


        
    def key_Delete(self = True):
        All =[]
        lst_PO = cmds.ls(type = 'animCurveTL')
        lst_RO = cmds.ls(type = 'animCurveTA')
        lst_ETF = cmds.ls(type = 'animCurveTU')
        
        All.extend(lst_PO)
        All.extend(lst_RO)
        All.extend(lst_ETF)


        cmds.delete(All)


    #2025.03.04 추가 함수
    def TurtleTurnOff(*args):
        Turtle_plugin_path = r"C:\Program Files\Autodesk\Maya2020\bin\plug-ins\Turtle.mll"
        
        if os.path.exists(Turtle_plugin_path):
            if cmds.pluginInfo('Turtle.mll', query=True, loaded=True):
                cmds.unloadPlugin('Turtle.mll',force=True)
            cmds.pluginInfo('Turtle.mll', edit=True, autoload=False)
            print("Turtle 꺼짐.")



    def cpSkin(*args):
        sel=mc.ls(sl=1);selFirst=sel[0];sel2nd=sel[1:];selRange=len(sel2nd);bindJsList=mc.skinCluster(sel[0],q=1,wi=1)


        for s in sel2nd:
            mc.select(bindJsList);mc.skinCluster(bindJsList,'%s'%s,tsb=1)
            mc.copySkinWeights(sel[0],'%s'%s,nm=1,sa='closestPoint',ia=('label','oneToOne'))



    def CrvPOCIF(*args):
        sel = cmds.ls(sl=1)
        total = 1.0
        value = 1.0 / (len(sel) - 1)
        list = []
        for x in sel:
            Pos = cmds.xform(x, q=1, t=1, ws=1)
            Tuple = tuple(Pos)


            list.append(Tuple)


        sel_Crv = cmds.curve(d=1, p=list)


        for x in range(0, len(sel)):
            result = x * value
            loc = cmds.spaceLocator(n='locPOICF_' + sel[x])
            node = cmds.createNode('pointOnCurveInfo', n=sel[x] +'_POCIF')
            Find = cmds.listRelatives(sel_Crv, s=1, type='shape')


            cmds.connectAttr(Find[0] + '.worldSpace[0]', node + '.inputCurve')
            cmds.connectAttr(node + '.position', loc[0] + '.translate')
            cmds.setAttr(node + '.turnOnPercentage', 1)
            cmds.setAttr(node + '.parameter', result)
            p = cmds.listRelatives(sel[x] , p =1 )[0]
            cmds.pointConstraint(loc[0],p, mo=1)



    def Function_JntFoli(self):
        sel = cmds.ls(sl=1 )


        self.foli_x_rbt = self.ui.foli_x_rbt.isChecked()
        self.foli_y_rbt = self.ui.foli_y_rbt.isChecked()
        self.foli_z_rbt = self.ui.foli_z_rbt.isChecked()
        self.foli_spin_rbt = self.ui.foli_spin_rbt.value()


        if self.foli_x_rbt == True:
            value = 'X'
        elif self.foli_y_rbt == True:
            value = 'Y'
        else:
            value = 'Z'
        A = c_JntFoli(sel ,value, self.foli_spin_rbt)

    #class인 함수는 따로 빼놓고 위 처럼 def의 변수로 처리해서 넣어버리기



    def create_MinFind(self):
        cmds.select(cl=1)
        selA = cmds.ls( '_Ctrl', '_Con', '*_C', type='transform' )
        resultA = []
        resultC = []
        resultE = []
        print ('\n\n    print -> Ctrl List\n\n')
    
        for x in range(len(selA)):
            #print selA[x]
            trs = [ 'translateX', 'translateY', 'translateZ', 'rotateX', 'rotateY', 'rotateZ', 'scaleX', 'scaleY', 'scaleZ' ]
            for y in range(len(trs)):
                ga = cmds.getAttr('%s.%s'%(selA[x],trs[y]))
                if(y<=5):
                    if(ga!=0.0):
                        #if(ga>=0.1):
                        print ('%s.%s    %s'%(selA[x],trs[y],ga))
                        resultA.append(selA[x])
                else:
                    if(ga!=1.0):
                        #if(ga>=1.1):
                        print ('%s.%s    %s'%(selA[x],trs[y],ga))
                        resultA.append(selA[x])
        if not selA:
            print("No relevant nodes found.")
            return
    
        for x in range(len(selA)):
            trs = [ 'rotatePivotX', 'rotatePivotY', 'rotatePivotZ', 'scalePivotX', 'scalePivotY', 'scalePivotZ' ]
            for y in range(len(trs)):
                try:
                    ga = cmds.getAttr('%s.%s'%(selA[x],trs[y]))
                    if (y <= 5):
                        if(ga!=0.0):
                            #if(ga>=0.1):
                            print ('%s.%s    %s'%(selA[x],trs[y],ga))
                            resultC.append(selA[x])
                    else:
                        if (ga != 1.0):
                            # if(ga>=1.1):
                            print ('%s.%s    %s' % (selA[x], trs[y], ga))
                            resultA.append(selA[x])
                except:
                    pass


            selA = cmds.ls( 'Mod_Grp' )
        if selA:
            selB = cmds.listRelatives( selA, ad=1, type='transform')
            for x in range(len(selB)):
            #print selB[x]
                trs = [ 'scaleX', 'scaleY', 'scaleZ' ]
               
                for y in range(len(trs)):
                    ga = cmds.getAttr('%s.%s'%(selB[x],trs[y]))
                    if(ga!=1.0):
                        print ('%s.%s    %s'%(selB[x],trs[y],ga))
                        resultE.append(selB[x])
        else:
            print ('\n\n    Check!    "Mod_Grp"\n\n')
        resultBB = set(resultA)
        resultDD = set(resultC)
        resultFF = set(resultE)
        resultB = list(resultBB)
        resultD = list(resultDD)
        resultF = list(resultFF)
        corName = 'correction_SET'
        pivName = 'pivot_SET'
        modName = 'modScale_SET'
        selCP = [ corName, pivName, modName ]
        selBD = [ resultB, resultD, resultF ]
        for x in range(len(selCP)):
            #print len(selBD[x])
            print (selBD[x])
            selE = cmds.ls( selCP[x] )
            if (len(selE)!=0):# type
                cmds.delete( selCP[x] )
            if(len(selBD[x])!=0):# list
                cmds.sets( selBD[x], n=selCP[x] )



    def create_MinDel(self):
        cmds.select(cl=1)
        selA = cmds.ls('_Ctrl', '_Con', '*_C', type='transform')
        resultA = []
        resultB = []
        resultC = []
        resultE = []


        for x in range(len(selA)):
            trs = ['translateX', 'translateY', 'translateZ', 'rotateX', 'rotateY', 'rotateZ']
            for y in range(len(trs)):
                if cmds.getAttr('%s.%s' % (selA[x], trs[y]), lock=1):
                    resultC.append(selA[x] + '.' + trs[y])
                    continue
                
                ga = cmds.getAttr('%s.%s' % (selA[x], trs[y]))
                if (y <= 5):
                    if (ga != 0.0):
                        if 'e' in str(ga):
                            cmds.setAttr('%s.%s' % (selA[x], trs[y]), 0)
                            resultA.append(selA[x])
                        else:
                            resultB.append(selA[x] + '.' + trs[y])
                            pass
                else:
                    if (ga != 1.0):
                        if 'e' in str(ga):
                            cmds.setAttr('%s.%s' % (selA[x], trs[y]), 0)
                            resultA.append(selA[x])
                        else:
                            resultB.append(selA[x] + '.' + trs[y])
                            pass
        
        print('---0 list---   ' + ', '.join(resultA))
        print('---0 or Move list---   ' + ', '.join(resultB))
        print('---lock list---   ' + ', '.join(resultC))





    #2025.03.04 추가 함수
    def Z0_Out(self):
        selA = cmds.ls(sl=1)
        for x in range(0, len(selA)):
            parentObj = cmds.listRelatives('%s'%selA[x], p=1)
            # parentObj 가 존재하지 않으면 실행 = if not
            if not parentObj:
                cmds.group( em=1, n='%s_G'%selA[x] )
                cmds.delete(cmds.parentConstraint( '%s'%selA[x], '%s_G'%selA[x], w=.1 ))
                cmds.delete(cmds.scaleConstraint( '%s'%selA[x], '%s_G'%selA[x], w=.1 ))
                cmds.parent( '%s'%selA[x], '%s_G'%selA[x] )
            else:
                cmds.group( em=1, n='%s_G'%selA[x] )
                cmds.delete(cmds.parentConstraint( '%s'%selA[x], '%s_G'%selA[x], w=.1 ))
                cmds.delete(cmds.scaleConstraint( '%s'%selA[x], '%s_G'%selA[x], w=.1 ))
                cmds.parent( '%s'%selA[x], '%s_G'%selA[x] )
                cmds.parent( '%s_G'%selA[x], parentObj[0] )


    #2025.03.04 추가 함수
    def VtxSkinCopy(self):
        sel = cmds.ls(sl = 1, fl =1)
        FirstVtx =sel[0]
        OtherVtxs =sel

        cmds.select(FirstVtx)
        mel.eval("CopyVertexWeights")
        cmds.select(OtherVtxs)
        mel.eval("PasteVertexWeights")
    


    #2025.03.04 추가 함수
    def ConnenctCtrl(self):
        selected = cmds.ls(selection=True)
        LocList = []
        ctrlList = []


        for obj in selected:
            if '_Ctrl' in obj:
                ctrlList.append(obj)


            if '_Loc' in obj:
                LocList.append(obj)


        for Loc in LocList:
            Loc_n_name = Loc.split('_')[-2]
            for ctrl in ctrlList:
                ctrl_n_name = ctrl.split('_')[-2]
                if ctrl_n_name.isdigit() and Loc_n_name.isdigit() and ctrl_n_name == Loc_n_name:
                    
                    L_T = Loc + '.translate'
                    L_R = Loc + '.rotate'
                    L_S = Loc + '.scale'


                    C_T = ctrl + '.translate'
                    C_R = ctrl + '.rotate'
                    C_S = ctrl + '.scale'


                    cmds.connectAttr(C_T, L_T)
                    cmds.connectAttr(C_R, L_R)
                    cmds.connectAttr(C_S, L_S)
                    break
        


class c_JntFoli():
    def __init__(self, lst_Select, normal, size):
        self.lst_Select = lst_Select
        self.normal = normal
        self.size = size


        self.lst_Foli = []
        self.lst_PN = []


        if self.normal == 'X':
            nor_lst = [1, 0, 0]
        elif self.normal == 'Y':
            nor_lst = [0, 1, 0]
        else:
            nor_lst = [0, 0, 1]


        for x in lst_Select:
            PN = cmds.polyPlane(ax=nor_lst, n='PN_Foli_' + x, sx=1, sy=1, w=self.size, h=self.size)


            pos_t = cmds.xform(x, ws=1, t=1, q=1)
            pos_r = cmds.xform(x, ws=1, ro=1, q=1)


            cmds.xform(PN[0], ws=1, t=pos_t)
            cmds.xform(PN[0], ws=1, ro=pos_r)


            Foli = cmds.createNode('follicle', n='Foli_' + x + 'Shape')


            Tf = cmds.listRelatives(Foli, ap=1, type='transform')
            PN_shp = cmds.listRelatives(PN[0], s=1, type='mesh')


            cmds.connectAttr(Foli + '.outTranslate', Tf[0] + '.translate', f=1)
            cmds.connectAttr(Foli + '.outRotate', Tf[0] + '.rotate', f=1)


            cmds.connectAttr(PN_shp[0] + '.outMesh', Foli + '.inputMesh')
            cmds.connectAttr(PN_shp[0] + '.worldMatrix[0]', Foli + '.inputWorldMatrix')


            cmds.setAttr(Foli + '.parameterU', 0.5)
            cmds.setAttr(Foli + '.parameterV', 0.5)


            grp = cmds.listRelatives(x, p=1, type='transform')
            prime = cmds.listRelatives(grp, p=1, type='transform')


            try:
                cmds.parentConstraint(Tf[0], grp, mo=1)
            except:
                pass


            self.lst_PN.append(PN[0])
            self.lst_Foli.append(Tf[0])


        g_Foli = cmds.group(self.lst_Foli, n='grp_All_Foli_' + lst_Select[0])
        g_PN = cmds.group(self.lst_PN, n='grp_All_PN_' + lst_Select[0])
#함수 끝
#---------------------------------------------------------




if __name__ == "__main__":
    try:
        desinger_ui.close()
        desinger_ui.deleteLater()
    except:
        pass


    desinger_ui = DesignerUI()
    desinger_ui.show()
    #클래스를 변수화 하여 열기



