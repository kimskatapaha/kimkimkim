import maya.cmds as cmds

def Shape_Vis_Off():
    selectObj = cmds.ls(sl=True)

    print(selectObj)
    for obj in selectObj:
        selectShape = cmds.listRelatives(obj, shapes=True, fullPath=True)
        
        for shape in selectShape:
            selectShapeVisOP = shape + ".visibility"
            cmds.setAttr(selectShapeVisOP, 0)

Shape_Vis_Off()