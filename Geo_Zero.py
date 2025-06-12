import maya.cmds as cmds

def Geo_Zero():
    not_0_Geo = []

    AllNodes = cmds.ls()

    for node in AllNodes:
        if cmds.nodeType(node) == 'mesh':
            parent_node = cmds.listRelatives(node, parent=True, fullPath=True)
            if parent_node:
                not_0_Geo.append(parent_node[0])

    if not_0_Geo:
        cmds.xform(not_0_Geo, centerPivots=True)
        cmds.delete(not_0_Geo, constructionHistory=True)
        cmds.makeIdentity(not_0_Geo, apply=True, translate=True, rotate=True, scale=True)
        
        for post_obj in not_0_Geo:
            lockwillneverdie = cmds.listAttr(post_obj, keyable=True)
            if lockwillneverdie:
                for lockwillneverdie in lockwillneverdie:
                    lockwillnever_name = post_obj + "." + lockwillneverdie
                    cmds.setAttr(lockwillnever_name, lock=True)

Geo_Zero()