import maya.cmds as cmds

def ConnenctCtrl():
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

                cmds.connectAttr(L_T, C_T)
                cmds.connectAttr(L_R, C_R)
                cmds.connectAttr(L_S, C_S)
                break

ConnenctCtrl()