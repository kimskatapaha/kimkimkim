import maya.cmds as cmds

def oneClickMatch():
    selected = cmds.ls(selection=True)
    ctrlList = []
    jntList = []

    for obj in selected:
        if '_Jnt' in obj:
            jntList.append(obj)

        if '_Ctrl' in obj:
            ctrlList.append(obj)

    for ctrl in ctrlList:
        ctrl_n_name = ctrl.split('_')[-1]
        for jnt in jntList:
            jnt_n_name = jnt.split('_')[-1]
            if jnt_n_name.isdigit() and ctrl_n_name.isdigit() and jnt_n_name == ctrl_n_name:
                cmds.matchTransform(ctrl, jnt)
                break

oneClickMatch()