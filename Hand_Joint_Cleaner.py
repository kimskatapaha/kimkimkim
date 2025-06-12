import maya.cmds as cmds

def LfHand_Joint_Cleaner():
    
    Index = cmds.listRelatives('LfIndexRoot_Jnt', ad=True, type='joint' ) 
    Middle = cmds.listRelatives('LfMiddleRoot_Jnt', ad=True, type='joint' )  
    Ring = cmds.listRelatives('LfRingRoot_Jnt', ad=True, type='joint' )
    Thumb = cmds.listRelatives('LfThumbRoot_Jnt', ad=True, type='joint' )
    Pinky = cmds.listRelatives('LfPinkyRoot_Jnt', ad=True, type='joint' )


    #jointOrient
    for IntheIndex in Index:
        cmds.setAttr(IntheIndex + ".jointOrientX", 0)
        cmds.setAttr(IntheIndex + ".jointOrientY", 0)
        cmds.setAttr(IntheIndex + ".jointOrientZ", 0)

    for IntheMiddle in Middle:
        cmds.setAttr(IntheMiddle + ".jointOrientX", 0)
        cmds.setAttr(IntheMiddle + ".jointOrientY", 0)
        cmds.setAttr(IntheMiddle + ".jointOrientZ", 0)

    for IntheRing in Ring:
        cmds.setAttr(IntheRing + ".jointOrientX", 0)
        cmds.setAttr(IntheRing + ".jointOrientY", 0)
        cmds.setAttr(IntheRing + ".jointOrientZ", 0)

    for IntheThumb in Thumb:
        cmds.setAttr(IntheThumb + ".jointOrientX", 0)
        cmds.setAttr(IntheThumb + ".jointOrientY", 0)
        cmds.setAttr(IntheThumb + ".jointOrientZ", 0)

    for InthePinky in Pinky:
        cmds.setAttr(InthePinky + ".jointOrientX", 0)
        cmds.setAttr(InthePinky + ".jointOrientY", 0)
        cmds.setAttr(InthePinky + ".jointOrientZ", 0)



    for IntheIndex in Index:
        cmds.setAttr(IntheIndex + ".rotateX", 0)
        cmds.setAttr(IntheIndex + ".rotateY", 0)
        cmds.setAttr(IntheIndex + ".rotateZ", 0)

    for IntheMiddle in Middle:
        cmds.setAttr(IntheMiddle + ".rotateX", 0)
        cmds.setAttr(IntheMiddle + ".rotateY", 0)
        cmds.setAttr(IntheMiddle + ".rotateZ", 0)


    for IntheRing in Ring:
        cmds.setAttr(IntheRing + ".rotateX", 0)
        cmds.setAttr(IntheRing + ".rotateY", 0)
        cmds.setAttr(IntheRing + ".rotateZ", 0)

    for IntheThumb in Thumb:
        cmds.setAttr(IntheThumb + ".rotateX", 0)
        cmds.setAttr(IntheThumb + ".rotateY", 0)
        cmds.setAttr(IntheThumb + ".rotateZ", 0)

    for InthePinky in Pinky:
        cmds.setAttr(InthePinky + ".rotateX", 0)
        cmds.setAttr(InthePinky + ".rotateY", 0)
        cmds.setAttr(InthePinky + ".rotateZ", 0)



LfHand_Joint_Cleaner()