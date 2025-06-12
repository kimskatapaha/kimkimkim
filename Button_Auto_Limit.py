import maya.cmds as cmds

def Button_Roll():
    selected = cmds.ls(selection=True)

    for x in selected:
        cmds.transformLimits( x, ty=(-0.05, 0.01), ety =(1,1) )

Button_Roll()