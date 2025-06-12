import maya.cmds as cmds

def Ctrl_OneLimit():
    selected = cmds.ls(selection=True)  # 선택한 오브젝트 목록 가져오기

    for ctrl in selected:
        cmds.transformLimits(ctrl, ty=(-0.04, 0.01), ety=(1, 1))  # Translate Y 값 제한 설정

# 함수 실행
Ctrl_OneLimit()