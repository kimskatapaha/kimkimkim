import maya.cmds as cmds
import random 

selected = cmds.ls(selection=True)
sel_ = cmds.ls( selection=True )
for x in sel_[:10] :
    cmds.move( random.uniform( -10, 20 ), random.uniform( -10, 20 ), random.uniform( -10, 20 ), x, r=1 )