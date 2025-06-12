import maya.cmds as cmds

def Blsh_ObjMirror():
    selected = cmds.ls(selection=True)

    for ctrl in selected:
        # 원래의 위치 및 회전 값을 가져오기
        origin_translation = cmds.xform(ctrl, q=True, translation=True, worldSpace=True)
        origin_rotation = cmds.xform(ctrl, q=True, rotation=True, worldSpace=True)

        # X 위치 및 Y, Z 회전값 반전
        mirrored_translation = [-origin_translation[0], origin_translation[1], origin_translation[2]]
        mirrored_rotation = [origin_rotation[0], -origin_rotation[1], -origin_rotation[2]]

        # 새로운 값 적용
        cmds.xform(ctrl, translation=mirrored_translation, worldSpace=True)
        cmds.xform(ctrl, rotation=mirrored_rotation, worldSpace=True)

Blsh_ObjMirror()