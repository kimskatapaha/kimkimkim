import maya.cmds as cmds

sel  = cmds.ls("_Ctrl_Twist_MDL" , type ="multDoubleLinear" )

for x in sel:
    try:
        cmds.setAttr(x + ".input2"  ,1)
    except:
        pass