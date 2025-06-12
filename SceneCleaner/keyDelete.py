import maya.cmds as cmds


def Delete_animCurveAni(Delete_Bool = True):
    
    
    All =[]
    
    lst_PO = cmds.ls(type = 'animCurveTL')
    lst_RO = cmds.ls(type = 'animCurveTA')
    lst_ETF = cmds.ls(type = 'animCurveTU')
    
    
    All.extend(lst_PO)
    All.extend(lst_RO)
    All.extend(lst_ETF)
    if Delete_Bool == True:
        cmds.delete(All)
    else:
        pass
    
Delete_animCurveAni()