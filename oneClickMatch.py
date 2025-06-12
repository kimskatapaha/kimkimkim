import maya.cmds as cmds

def oneClickMatch():
    selected = cmds.ls(selection=True)
    geoList = []
    ctrlList = []

    for obj in selected:
        if '_Geo' in obj:
            geoList.append(obj)

        if '_Ctrl' in obj:
            ctrlList.append(obj)

    for ctrl in ctrlList:
        ctrl_n_name = ctrl.split('_')[-1]
        for geo in geoList:
            geo_n_name = geo.split('_')[-1]
            if geo_n_name.isdigit() and ctrl_n_name.isdigit() and geo_n_name == ctrl_n_name:
                cmds.matchTransform(ctrl, geo)
                break

oneClickMatch()