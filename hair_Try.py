import maya.cmds as cmds




class Hair_build():
    def __init__(self):
        self.Create_Base()
        self.connect_Outliner()
        self.Loc_hierarchy()
        self.d_LocOnCv()
        self.add_out_of_necessity()
        

#-----------------------------------------

    def Create_Base(self):
        cmds.select('HairA01_Cv')
        selObj= cmds.ls(sl=True)

        #커브cv에 맞춰서 클러스터 빌드
        for A in selObj:
            cv_list= cmds.ls(A + '.cv[*]', flatten=True)
            for B in cv_list:
                cmds.cluster(B , n=A + '_clu1')

        #클러스터 위치에 ik용 컨트롤러 빌드
        On_Ctrl= cmds.curve(degree=1, 
                            point=[(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,-1),(1,-1,-1),
                                   (1,-1,1),(1,1,1),(1,1,-1),
                                   (1,1,1),(-1,1,1),(-1,1,-1),(-1,-1,-1),(-1,-1,1),
                                   (-1,1,1),(-1,-1,1),(1,-1,1)], n='HairA01_ik_Ctrl1')
        Tw_Ctrl= cmds.duplicate(On_Ctrl)
        Th_Ctrl= cmds.duplicate(On_Ctrl)
        Fo_Ctrl= cmds.duplicate(On_Ctrl)
        Fi_Ctrl= cmds.duplicate(On_Ctrl)
        cmds.matchTransform(On_Ctrl, 'HairA01_Cv_clu1Handle')
        cmds.matchTransform(Tw_Ctrl, 'HairA01_Cv_clu3Handle')
        cmds.matchTransform(Th_Ctrl, 'HairA01_Cv_clu4Handle')
        cmds.matchTransform(Fo_Ctrl, 'HairA01_Cv_clu5Handle')
        cmds.matchTransform(Fi_Ctrl, 'HairA01_Cv_clu7Handle')
        cmds.select(cl=1)

        #클러스터 위치를 참고로 조인트 빌드
        new_Jnt1= cmds.joint(n = 'HairA01_Sp_Jnt1')
        cmds.matchTransform(new_Jnt1, 'HairA01_ik_Ctrl1')
        new_Jnt2= cmds.joint(n = 'HairA01_Sp_Jnt2')
        cmds.matchTransform(new_Jnt2, 'HairA01_ik_Ctrl2')
        new_Jnt3= cmds.joint(n = 'HairA01_Sp_Jnt3')
        cmds.matchTransform(new_Jnt3, 'HairA01_ik_Ctrl3')
        new_Jnt4= cmds.joint(n = 'HairA01_Sp_Jnt4')
        cmds.matchTransform(new_Jnt4, 'HairA01_ik_Ctrl4')
        new_Jnt5= cmds.joint(n = 'HairA01_Sp_Jnt5')
        cmds.matchTransform(new_Jnt5, 'HairA01_ik_Ctrl5')

        #스플라인용 조인트 셋과 바인드용 조인트 셋을 분리, 바인드용 조인트 셋은 컨트롤러들 밑으로 집어넣기
        HairA01sp_Jnt_Grp= cmds.ls('HairA01_Sp_Jnt*', type= 'joint')
        HairA01_Jnt_Grp= cmds.duplicate(HairA01sp_Jnt_Grp, n= 'HairA01_Jnt1')
        HairA01_Ctrl_Grp= cmds.ls('HairA01_Ctrl*')

        for HairA01_Ctrl_Grp, HairA01_Jnt_Grp in zip(HairA01_Ctrl_Grp, HairA01_Jnt_Grp):
            cmds.parent(HairA01_Jnt_Grp, HairA01_Ctrl_Grp)

        #스플라인용 조인트 셋에 스플라인 핸들 빌드
        cmds.ikHandle(n= 'HairA01_Ikhandle', startJoint= 'HairA01_Sp_Jnt1', 
                        endEffector= 'HairA01_Sp_Jnt5', solver= 'ikSplineSolver', curve= 'HairA01_Cv',
                        createCurve= False, freezeJoints= True)

        #fk용 서클 컨트롤러 생성
        On_circle= cmds.circle(normal= (0,1,0), n= 'HairA01_fk_Ctrl1')
        cmds.matchTransform(On_circle, 'HairA01_ik_Ctrl1')
        Tw_On_circle= cmds.duplicate(On_circle)
        cmds.matchTransform(Tw_On_circle, 'HairA01_ik_Ctrl2')
        Th_On_circle= cmds.duplicate(On_circle)
        cmds.matchTransform(Th_On_circle, 'HairA01_ik_Ctrl3')
        Fo_On_circle= cmds.duplicate(On_circle)
        cmds.matchTransform(Fo_On_circle, 'HairA01_ik_Ctrl4')
        Fi_On_circle= cmds.duplicate(On_circle)
        cmds.matchTransform(Fi_On_circle, 'HairA01_ik_Ctrl5')

        #클러스터 컨스트레인용 무브 컨트롤러 생성
        bOn_Ctrl= cmds.curve(degree= 1, 
                            point=[(1.5,-1.5,-1.5),(1.5,1.5,-1.5),(-1.5,1.5,-1.5),
                                   (-1.5,-1.5,-1.5),(1.5,-1.5,-1.5),
                                   (1.5,-1.5,1.5),(1.5,1.5,1.5),(1.5,1.5,-1.5),
                                   (1.5,1.5,1.5),(-1.5,1.5,1.5),(-1.5,1.5,-1.5),
                                   (-1.5,-1.5,-1.5),(-1.5,-1.5,1.5),
                                   (-1.5,1.5,1.5),(-1.5,-1.5,1.5),(1.5,-1.5,1.5)], n='HairA01_move_Ctrl1')
        cmds.matchTransform(bOn_Ctrl, 'HairA01_ik_Ctrl1')
        bTw_Ctrl= cmds.duplicate(bOn_Ctrl)
        cmds.matchTransform(bTw_Ctrl, 'HairA01_ik_Ctrl2')
        bTh_Ctrl= cmds.duplicate(bOn_Ctrl)
        cmds.matchTransform(bTh_Ctrl, 'HairA01_ik_Ctrl3')
        bFo_Ctrl= cmds.duplicate(bOn_Ctrl)
        cmds.matchTransform(bFo_Ctrl, 'HairA01_ik_Ctrl4')
        bFi_Ctrl= cmds.duplicate(bOn_Ctrl)
        cmds.matchTransform(bFi_Ctrl, 'HairA01_ik_Ctrl5')



    def connect_Outliner(self):
        HairA01_ik_Ctrl= cmds.ls('HairA01_ik_Ctrl*')
        HairA01_Cv_clu= cmds.ls('HairA01_Cv_clu*Handle')
        
        #Z0맞추기
        for int, D in enumerate(HairA01_ik_Ctrl):
            Name= "HairA01_ik_Ctrl{}".format
            Number= int+1
            cmds.group(empty= True, n= Name(Number) + '_G')

        cmds.matchTransform('HairA01_ik_Ctrl1_G', 'HairA01_ik_Ctrl1')
        cmds.matchTransform('HairA01_ik_Ctrl2_G', 'HairA01_ik_Ctrl2')
        cmds.matchTransform('HairA01_ik_Ctrl3_G', 'HairA01_ik_Ctrl3')
        cmds.matchTransform('HairA01_ik_Ctrl4_G', 'HairA01_ik_Ctrl4')
        cmds.matchTransform('HairA01_ik_Ctrl5_G', 'HairA01_ik_Ctrl5')

        cmds.duplicate('HairA01_ik_Ctrl1_G', n= 'HairA01_fk_Ctrl1_G')
        cmds.duplicate('HairA01_ik_Ctrl2_G', n= 'HairA01_fk_Ctrl2_G')
        cmds.duplicate('HairA01_ik_Ctrl3_G', n= 'HairA01_fk_Ctrl3_G')
        cmds.duplicate('HairA01_ik_Ctrl4_G', n= 'HairA01_fk_Ctrl4_G')
        cmds.duplicate('HairA01_ik_Ctrl5_G', n= 'HairA01_fk_Ctrl5_G')

        cmds.duplicate('HairA01_ik_Ctrl1_G', n= 'HairA01_move_Ctrl1_G')
        cmds.duplicate('HairA01_ik_Ctrl2_G', n= 'HairA01_move_Ctrl2_G')
        cmds.duplicate('HairA01_ik_Ctrl3_G', n= 'HairA01_move_Ctrl3_G')
        cmds.duplicate('HairA01_ik_Ctrl4_G', n= 'HairA01_move_Ctrl4_G')
        cmds.duplicate('HairA01_ik_Ctrl5_G', n= 'HairA01_move_Ctrl5_G')

        cmds.parent('HairA01_ik_Ctrl1', 'HairA01_ik_Ctrl1_G')
        cmds.parent('HairA01_ik_Ctrl2', 'HairA01_ik_Ctrl2_G')
        cmds.parent('HairA01_ik_Ctrl3', 'HairA01_ik_Ctrl3_G')
        cmds.parent('HairA01_ik_Ctrl4', 'HairA01_ik_Ctrl4_G')
        cmds.parent('HairA01_ik_Ctrl5', 'HairA01_ik_Ctrl5_G')

        cmds.parent('HairA01_fk_Ctrl1', 'HairA01_fk_Ctrl1_G')
        cmds.parent('HairA01_fk_Ctrl2', 'HairA01_fk_Ctrl2_G')
        cmds.parent('HairA01_fk_Ctrl3', 'HairA01_fk_Ctrl3_G')
        cmds.parent('HairA01_fk_Ctrl4', 'HairA01_fk_Ctrl4_G')
        cmds.parent('HairA01_fk_Ctrl5', 'HairA01_fk_Ctrl5_G')

        cmds.parent('HairA01_move_Ctrl1', 'HairA01_move_Ctrl1_G')
        cmds.parent('HairA01_move_Ctrl2', 'HairA01_move_Ctrl2_G')
        cmds.parent('HairA01_move_Ctrl3', 'HairA01_move_Ctrl3_G')
        cmds.parent('HairA01_move_Ctrl4', 'HairA01_move_Ctrl4_G')
        cmds.parent('HairA01_move_Ctrl5', 'HairA01_move_Ctrl5_G')

        HairA01_move_Ctrl= cmds.ls('HairA01_move_Ctrl*_G')
        cmds.group(HairA01_move_Ctrl, n= 'HairA01_move_Ctrl_Grp')
        
        #fk 계층구조 맞추기
        cmds.parent('HairA01_fk_Ctrl5_G', 'HairA01_fk_Ctrl4')
        cmds.parent('HairA01_fk_Ctrl4_G', 'HairA01_fk_Ctrl3')
        cmds.parent('HairA01_fk_Ctrl3_G', 'HairA01_fk_Ctrl2')
        cmds.parent('HairA01_fk_Ctrl2_G', 'HairA01_fk_Ctrl1')

        cmds.parent('HairA01_ik_Ctrl5_G', 'HairA01_fk_Ctrl5')
        cmds.parent('HairA01_ik_Ctrl4_G', 'HairA01_fk_Ctrl4')
        cmds.parent('HairA01_ik_Ctrl3_G', 'HairA01_fk_Ctrl3')
        cmds.parent('HairA01_ik_Ctrl2_G', 'HairA01_fk_Ctrl2')
        cmds.parent('HairA01_ik_Ctrl1_G', 'HairA01_fk_Ctrl1')

        #조인트들 집어넣기
        cmds.parent('HairA01_Jnt5', 'HairA01_ik_Ctrl5')
        cmds.parent('HairA01_Jnt4', 'HairA01_ik_Ctrl4')
        cmds.parent('HairA01_Jnt3', 'HairA01_ik_Ctrl3')
        cmds.parent('HairA01_Jnt2', 'HairA01_ik_Ctrl2')
        cmds.parent('HairA01_Jnt1', 'HairA01_ik_Ctrl1')

        #move컨트롤러들 클러스터 컨스트레인 하기 
        cmds.parentConstraint('HairA01_move_Ctrl1', 'HairA01_Cv_clu1Handle')
        cmds.parentConstraint('HairA01_move_Ctrl2', 'HairA01_Cv_clu3Handle')
        cmds.parentConstraint('HairA01_move_Ctrl3', 'HairA01_Cv_clu4Handle')
        cmds.parentConstraint('HairA01_move_Ctrl4', 'HairA01_Cv_clu5Handle')
        cmds.parentConstraint('HairA01_move_Ctrl5', 'HairA01_Cv_clu7Handle')
        cmds.group(HairA01_Cv_clu, n= 'HairA01_Cv_clu_Grp')

        #아웃라이너 정리 
        cmds.group('HairA01_Cv','HairA01_Sp_Jnt1','HairA01_Ikhandle','HairA01_Cv_clu_Grp', 
                   n= 'HairA01_hair_Sys')
        cmds.group('HairA01_fk_Ctrl1_G','HairA01_move_Ctrl_Grp',
                   n= 'HairA01_ctrl_Grp')
        cmds.group('HairA01_hair_Sys','HairA01_ctrl_Grp', 
                   n= 'HairA01_hair_RigGrp')
        
        #---fk로케이터 생성---
        TargetCrv= 'HairA01_Cv'
        Name= 'HairA01_Cv'
        CV= cmds.ls(TargetCrv + '.cv[*]', fl=1)
        Spans= len(CV)
        DuCrv= cmds.duplicate(TargetCrv, n= Name + '_Fix')[0]

        for x in range(Spans):
            cv_position= cmds.pointPosition(CV[x], w= True)
            fkLoc= cmds.spaceLocator(n= Name + '_fk{}_loc'.format(str(x + 1)))[0]
            cmds.move(cv_position[0], cv_position[1], cv_position[2], fkLoc, absolute=True)

        cmds.delete(DuCrv)



    def Loc_hierarchy(self):
        fk_Loc= cmds.ls('HairA01_Cv_fk*_loc', type='transform')
        print(fk_Loc)

        for int, D in enumerate(fk_Loc):
            Name= "HairA01_Cv_fk_loc{}".format
            Number= int+1
            fk_loc_G= cmds.group(empty= True, n= Name(Number)+'_G')
            cmds.matchTransform(fk_loc_G, D)

        #---fk로케이터 계층구조---
        cmds.parent('HairA01_Cv_fk7_loc', 'HairA01_Cv_fk_loc7_G')
        cmds.parent('HairA01_Cv_fk6_loc', 'HairA01_Cv_fk_loc6_G')
        cmds.parent('HairA01_Cv_fk5_loc', 'HairA01_Cv_fk_loc5_G')
        cmds.parent('HairA01_Cv_fk4_loc', 'HairA01_Cv_fk_loc4_G')
        cmds.parent('HairA01_Cv_fk3_loc', 'HairA01_Cv_fk_loc3_G')
        cmds.parent('HairA01_Cv_fk2_loc', 'HairA01_Cv_fk_loc2_G')
        cmds.parent('HairA01_Cv_fk1_loc', 'HairA01_Cv_fk_loc1_G')

        cmds.parent('HairA01_Cv_fk_loc7_G', 'HairA01_Cv_fk6_loc')
        cmds.parent('HairA01_Cv_fk_loc6_G', 'HairA01_Cv_fk5_loc')
        cmds.parent('HairA01_Cv_fk_loc5_G', 'HairA01_Cv_fk4_loc')
        cmds.parent('HairA01_Cv_fk_loc4_G', 'HairA01_Cv_fk3_loc')
        cmds.parent('HairA01_Cv_fk_loc3_G', 'HairA01_Cv_fk2_loc')
        cmds.parent('HairA01_Cv_fk_loc2_G', 'HairA01_Cv_fk1_loc')



    def d_LocOnCv(self):
        TargetCrv= 'HairA01_Cv'
        Name= 'HairA01_Cv'

        # 타겟 커브의 CV를 가져오기
        CV= cmds.ls(TargetCrv + '.cv[*]', fl=1)
        Spans= len(CV)

        # 타겟 커브를 복제하고 rebuild
        DuCrv= cmds.duplicate(TargetCrv, n= Name + '_Fix')[0]

        # 각 CV에 대해 로케이터 생성
        lst= []
        for x in range(Spans):
            # 각 CV의 위치를 가져오기
            cv_position= cmds.pointPosition(CV[x], w=True)

            # 로케이터+조인트 생성 및 위치 설정
            cmds.joint(n= Name + '_fk_Jnt{}'.format(str(x + 1)))[0]
            Loc= cmds.spaceLocator(n= Name + '_{}_POICF_loc'.format(str(x + 1)))[0]
            cmds.move(cv_position[0], cv_position[1], cv_position[2], Loc, absolute= True)



    def add_out_of_necessity (self):
            
        #---ik로케이터 Z0---
        for int, E in enumerate(Loc):
            ik_Name= "HairA01_Cv_6_POICF_loc{}".format
            ik_Number= int+1
            ik_loc_G= cmds.group(empty= True, n= ik_Name(ik_Number) + '_G')
            cmds.matchTransform(ik_loc_G, E)
            

        #---fk로케이터 밑으로 ikloc집어넣기---
        cmds.parent('HairA01_Cv_1_POICF_loc_G', 'HairA01_Cv_fk1_loc')
        cmds.parent('HairA01_Cv_2_POICF_loc_G', 'HairA01_Cv_fk2_loc')
        cmds.parent('HairA01_Cv_3_POICF_loc_G', 'HairA01_Cv_fk3_loc')
        cmds.parent('HairA01_Cv_4_POICF_loc_G', 'HairA01_Cv_fk4_loc')
        cmds.parent('HairA01_Cv_5_POICF_loc_G', 'HairA01_Cv_fk5_loc')
        cmds.parent('HairA01_Cv_6_POICF_loc_G', 'HairA01_Cv_fk6_loc')
        cmds.parent('HairA01_Cv_7_POICF_loc_G', 'HairA01_Cv_fk7_loc')
    
        #---fk조인트 컨트롤러에 집어넣기---
        cmds.matchTransform('HairA01_Cv_fk_Jnt1', 'HairA01_Cv_fk1_loc')
        cmds.parent('HairA01_Cv_fk_Jnt1', 'HairA01_fk_Ctrl1')
        cmds.matchTransform('HairA01_Cv_fk_Jnt3', 'HairA01_Cv_fk3_loc')
        cmds.parent('HairA01_Cv_fk_Jnt3', 'HairA01_fk_Ctrl2')
        cmds.matchTransform('HairA01_Cv_fk_Jnt4', 'HairA01_Cv_fk4_loc')
        cmds.parent('HairA01_Cv_fk_Jnt4', 'HairA01_fk_Ctrl3')
        cmds.matchTransform('HairA01_Cv_fk_Jnt5', 'HairA01_Cv_fk5_loc')
        cmds.parent('HairA01_Cv_fk_Jnt5', 'HairA01_fk_Ctrl4')
        cmds.matchTransform('HairA01_Cv_fk_Jnt7', 'HairA01_Cv_fk7_loc')
        cmds.parent('HairA01_Cv_fk_Jnt7', 'HairA01_fk_Ctrl5')

        cmds.delete('HairA01_Cv_fk_Jnt2', 'HairA01_Cv_fk_Jnt6')


        #커브 부드럽게하기
        cmds.rebuildCurve("HairA01_Cv", 
                        ch=1, rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, s=6, d=3, tol=0.01)
        # DuCrv 삭제
        cmds.delete(DuCrv)

        return lst


Hair_build()
