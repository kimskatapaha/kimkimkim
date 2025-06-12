import maya.cmds as cmds

property1 = "jointOrientX"
property2 = "jointOrientY"
property3 = "jointOrientZ"

selected = cmds.ls(selection=True)

for obj in selected:
    cmds.setAttr(obj + "." + property1, 0)
    cmds.setAttr(obj + "." + property2, 0)
    cmds.setAttr(obj + "." + property3, 0)