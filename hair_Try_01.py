import maya.cmds as cmds


def connect_POICF_Loc():
    ikJnt_Grp= cmds.ls('HairA01_Jnt*', type='joint')
    fkCtrl_Grp= cmds.ls('HairA01_fk_Ctrl1','HairA01_fk_Ctrl2','HairA01_fk_Ctrl3',
                        'HairA01_fk_Ctrl4','HairA01_fk_Ctrl5', type='transform')
    fkJnt_Grp= cmds.ls('HairA01_fk_Jnt*',type='joint')

    #fk조인트 생성
    for int ,B in enumerate(ikJnt_Grp):
        cmds.select(cl=1)
        Name = "HairA01_fk_Jnt{}".format
        Number = int +1
        new_fkJnt =cmds.joint(n = Name(Number))
        cmds.matchTransform(new_fkJnt, B)    
    
    #새로 만든 fk조인트 집어넣기
    cmds.parent('HairA01_fk_Jnt1', 'HairA01_fk_Ctrl1')
    cmds.parent('HairA01_fk_Jnt2', 'HairA01_fk_Ctrl2')
    cmds.parent('HairA01_fk_Jnt3', 'HairA01_fk_Ctrl3')
    cmds.parent('HairA01_fk_Jnt4', 'HairA01_fk_Ctrl4')
    cmds.parent('HairA01_fk_Jnt5', 'HairA01_fk_Ctrl5')





connect_POICF_Loc()