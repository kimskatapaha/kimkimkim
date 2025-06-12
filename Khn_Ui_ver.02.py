import maya.cmds as cmds
from functools import partial


def createJnt(*args):
    cmds.joint()


def createLoc(*args):
    cmds.spaceLocator()


def createClu(*args):
    cmds.cluster()


def LfHand_Joint_Cleaner(*args):
    Index = cmds.listRelatives('LfIndexRoot_Jnt', ad=True, type='joint') 
    Middle = cmds.listRelatives('LfMiddleRoot_Jnt', ad=True, type='joint')  
    Ring = cmds.listRelatives('LfRingRoot_Jnt', ad=True, type='joint')
    Thumb = cmds.listRelatives('LfThumbRoot_Jnt', ad=True, type='joint')
    Pinky = cmds.listRelatives('LfPinkyRoot_Jnt', ad=True, type='joint')

    #jointOrient
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

    #freeze
    if Index:
        for IntheIndex in Index:
            cmds.makeIdentity(IntheIndex, apply=True, t=1, r=1, s=1)
    if Middle:
        for IntheMiddle in Middle:
            cmds.makeIdentity(IntheMiddle, apply=True, t=1, r=1, s=1)
    if Ring:
        for IntheRing in Ring:
            cmds.makeIdentity(IntheRing, apply=True, t=1, r=1, s=1)
    if Thumb:
        for IntheThumb in Thumb:
            cmds.makeIdentity(IntheThumb, apply=True, t=1, r=1, s=1)
    if Pinky:
        for InthePinky in Pinky:
            cmds.makeIdentity(InthePinky, apply=True, t=1, r=1, s=1)
            break 



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
                cmds.blendShape(Dum,Geo)



def Findnode(item):
    query = cmds.textField(item ,query=1, tx=1)


    all_objects = cmds.ls()
    variable_obj = []

    for obj in all_objects:
        if query in obj:
            variable_obj.append(obj)

    if variable_obj:
        cmds.select(variable_obj, replace=True)
    else:
        print("Not found")

     



def Khn_Ui():
    if cmds.window('win', q=1, ex=1):
        cmds.deleteUI('win', window=True)
        
#---Function-Set------------------------------------------------------------------------------------------------------

        if cmds.window('win', exists=True):
            cmds.deleteUI('win', window=True)
        

    cmds.window('win', title='Khn_Ui')
    cmds.columnLayout(adjustableColumn=True)

    cmds.window('win', edit=True, widthHeight=(300, 300))
    cmds.showWindow('win')

#---Window-Set------------------------------------------------------------------------------------------------------

    cmds.button(label='Locator', command=createLoc)
    cmds.button(label='Cluster', command=createClu)
    cmds.button(label='Joint', command=createJnt)
    cmds.button(label='Hand Joint Clean', command=LfHand_Joint_Cleaner)
    cmds.button(label='Paint Skin Weights Tool', command=ArtPaintSkinWeightsTool)    
    cmds.button(label='Delete History And Freeze', command=DeleteHisAndFreeze)  
    cmds.button(label='one Click Match: Loc->Jnt', command=oneClickMatchJ_L) 
    cmds.button(label='one Click Match: Ctrl->Jnt', command=oneClickMatchC_L) 
    cmds.button(label='one Click blend', command=oneClickblend)
    
    cmds.rowColumnLayout(numberOfColumns=3, columnAttach=[(1, 'right', 0), (2, 'left', 0), (3, 'left', 0)])
    cmds.text(label='Finding Node')

    ConstraintTextset = cmds.textField( tx="Constraint", width=180)
    cmds.button(label='Enter', c= 'Findnode({})' .format(ConstraintTextset), width=50)
    
    
#---Button-Set------------------------------------------------------------------------------------------------------

Khn_Ui()