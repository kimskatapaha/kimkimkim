import maya.cmds as cmds
from functools import partial


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
def Khn_Ui():
    if cmds.window('win', exists=True):
        cmds.deleteUI('win')

    cmds.window('win', title='Khn_Ui', widthHeight=(450, 100))
    cmds.columnLayout(adjustableColumn=True)


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

#---Button Set-----

    cmds.columnLayout(adjustableColumn=True)

    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1, 370), (2, 80)])
    createTypeRadio = cmds.radioButtonGrp(label='Create     : ', 
                                          labelArray3=['Locator', 'Cluster', 'Joint'], 
                                          numberOfRadioButtons=3,
                                          columnWidth=[(1, 75)],
                                          columnAlign=[(1, 'left')])
    cmds.button(label='Enter', command=executeCreation, backgroundColor=[0.0,0.7,1.0])
    cmds.setParent('..')

    cmds.button(label='Paint Skin Weights Tool', command='ArtPaintSkinWeightsTool()')
    cmds.button(label='Hand Joint Clean', command='LfHand_Joint_Cleaner()')
    cmds.button(label='Delete History And Freeze', command='DeleteHisAndFreeze()')


    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1, 150), (2, 150), (3, 150)])
    cmds.button(label='one Click Match: Loc->Jnt', command='oneClickMatchJ_L()', height=50, backgroundColor=[1.0,0.0,0.8])
    cmds.button(label='one Click Match: Ctrl->Jnt', command='oneClickMatchC_L()', height=50, backgroundColor=[0.0,1.0,1.0])
    cmds.button(label='one Click blend', command='oneClickblend()', height=50, backgroundColor=[1.0,1.0,0.0])
    cmds.setParent('..')


    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1, 100), (2, 270), (3, 80)])
    cmds.text(label='Finding Node   :')
    ConstraintTextset = cmds.textField(tx="Constraint")
    cmds.button(label='Enter', c=lambda x: FindSet(), backgroundColor=[1.0,0.3,0.0])
    cmds.setParent('..')
    cmds.showWindow()

Khn_Ui()
