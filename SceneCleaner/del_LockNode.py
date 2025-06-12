import maya.cmds as cmds

sel = cmds.ls(' TurtleDefaultBakeLayer')

lock =cmds.lockNode(sel , l =0)




cmds.delete(sel)