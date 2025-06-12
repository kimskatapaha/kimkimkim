import maya.cmds as cmds
import random


def GeoMover( name , copyConut, transRange ):
    select = cmds.ls(sl=True)
    geoList = [obj for obj in select[:] if name in obj]

    value_copyConut = int(copyConut)
    value_transRange = int(transRange)

    for obj in geoList:
        num_copies = int(random.randint(1, value_copyConut))
        randomNumber = int(random.uniform(0, value_transRange)) 

        pos = cmds.xform(obj, q=True, t=True)
        for x in range(0, num_copies):
            copied_objects = cmds.duplicate(obj, name=obj + "_#", rc=True)[0]
            cmds.setAttr(copied_objects + ".translate", pos[0] + float(random.uniform(-randomNumber , randomNumber)), pos[1], pos[2]+ float(random.uniform(-randomNumber , randomNumber)))
            treeSacle = random.uniform(0.1 , 5)


            print (treeSacle)
            cmds.setAttr(copied_objects + ".scale", float(treeSacle), float(treeSacle), float(treeSacle))
            cmds.setAttr(copied_objects + ".rotateY", float(random.uniform(0, 360)))





GeoMover('_Geo' , 50 ,100)