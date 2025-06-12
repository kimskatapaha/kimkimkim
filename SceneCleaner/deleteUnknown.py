import maya.cmds as cmds


def deleteUnknown():
    lst = []

    sel01 = cmds.ls('vray*')
    sel02 = cmds.ls(type="unknown")
    sel03 = cmds.ls( ' TurtleDefaultBakeLayer')

    lst.extend(sel01)
    lst.extend(sel02)
    lst.extend(sel03)

    lst_unlock = [ cmds.lockNode(x, l =0) for x in lst]

    cmds.delete(lst)



deleteUnknown()