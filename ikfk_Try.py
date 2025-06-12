import maya.cmds as cmds


class Arm_build():
    def __init__(self):

        self.base_Ctrl()

        self.ik_BaseJnt()
        self.fk_BaseJnt()
        self.add_Ctrl()
        self.add_Ctrl_function()
        self.Switch_function()
        self.stretch_function()
        self.cleanUpTheCode()





#-----------------------------------------


    def base_Ctrl(self):
        DfRoot = cmds.ls('Df1_Jnt', type='joint') 

        for A in DfRoot:
            A = cmds.curve(degree=1, point=[(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,-1),(1,-1,-1),
                                        (1,-1,1),(1,1,1),(1,1,-1),
                                        (1,1,1),(-1,1,1),(-1,1,-1),(-1,-1,-1),(-1,-1,1),
                                        (-1,1,1),(-1,-1,1),(1,-1,1)])
            cmds.matchTransform(A, 'Df1_Jnt', position=True)
            cmds.rename(A, 'Root_Ctrl')
                
        Ctrl_Grp =cmds.group(empty=True, n='Root_Ctrl_G')
        cmds.matchTransform(Ctrl_Grp,'Root_Ctrl')
        cmds.parent('Root_Ctrl',Ctrl_Grp)
        cmds.addAttr(shortName= 'Switch', longName='Switch',attributeType="float",
                        hasMaxValue=True,maxValue=1,hasMinValue=True,minValue=0,keyable=True)
        cmds.addAttr(shortName= 'Stretch', longName='Stretch',attributeType="float",
                        hasMaxValue=True,maxValue=1,hasMinValue=True,minValue=0,keyable=True)


    def ik_BaseJnt(self):
        cmds.select(cl=1)
        Df_JntGrp= cmds.ls('Df*_Jnt', type='joint' )



        for int ,B in enumerate(Df_JntGrp):
            Name = "Arm{}IK_Jnt".format
            Number = int +1
            new_Jnt =cmds.joint(n = Name(Number))
            cmds.matchTransform(new_Jnt, B)


    def fk_BaseJnt(self):
        cmds.select(cl=1)
        Df_JntGrp= cmds.ls('Df*_Jnt', type='joint' )



        for int ,C in enumerate(Df_JntGrp):
            Name = "Arm{}FK_Jnt".format
            Number = int +1
            new_Jnt =cmds.joint(n = Name(Number))
            cmds.matchTransform(new_Jnt, C)

    #----------------------------------------------------
    def add_Ctrl(self):
        FkJntList= cmds.ls('Arm*FK_Jnt', type='joint')

        ik_Ctrl_1= cmds.circle(normal=(1,0,0), n = 'Arm1Ik_Ctrl')
        cmds.matchTransform(ik_Ctrl_1, 'Arm1IK_Jnt')
        IK_Ctrl_Grp1 =cmds.group(empty=True, n= 'Arm1Ik_Ctrl_G')
        cmds.matchTransform(IK_Ctrl_Grp1,ik_Ctrl_1)
        cmds.parent('Arm1Ik_Ctrl',IK_Ctrl_Grp1)

        ik_Ctrl_2= cmds.circle(normal=(1,0,0), n = 'Arm2Ik_Ctrl')
        cmds.matchTransform(ik_Ctrl_2, 'Arm3IK_Jnt')
        IK_Ctrl_Grp2 =cmds.group(empty=True, n= 'Arm2Ik_Ctrl_G')
        cmds.matchTransform(IK_Ctrl_Grp2, ik_Ctrl_2)
        cmds.parent('Arm2Ik_Ctrl',IK_Ctrl_Grp2)

        for int ,D in enumerate(FkJntList):
                Name = "Arm{}FK_Ctrl".format
                Number = int +1
                new_Fk_Ctrl =cmds.curve(degree=1, point=[(0,1,-1),(0,-1,-1),(0,-1,1),(0,1,1),(0,1,-1)], n = Name(Number))
                cmds.matchTransform(new_Fk_Ctrl, D)

            
                FK_Ctrl_Grp =cmds.group(empty=True, n= new_Fk_Ctrl+'_G')
                cmds.matchTransform(FK_Ctrl_Grp,new_Fk_Ctrl)
                cmds.parent(new_Fk_Ctrl,FK_Ctrl_Grp)


    def add_Ctrl_function(self):
        #ikConstraint
        cmds.ikHandle(n='Arm_Ikhandle', startJoint='Arm1IK_Jnt', endEffector='Arm3IK_Jnt', solver='ikRPsolver')
        cmds.parent('Arm_Ikhandle','Arm2Ik_Ctrl')
        cmds.parentConstraint('Arm1Ik_Ctrl','Arm1IK_Jnt')

        #fkConstraint
        cmds.parentConstraint('Arm1FK_Ctrl','Arm1FK_Jnt')
        cmds.parentConstraint('Arm2FK_Ctrl','Arm2FK_Jnt')
        cmds.parentConstraint('Arm3FK_Ctrl','Arm3FK_Jnt')

        #parentgroup
        cmds.parent('Arm2Ik_Ctrl_G','Arm1Ik_Ctrl')
        cmds.parent('Arm3FK_Ctrl_G','Arm2FK_Ctrl')
        cmds.parent('Arm2FK_Ctrl_G','Arm1FK_Ctrl')
        
        cmds.parent('Arm1FK_Ctrl_G','Arm1Ik_Ctrl_G','Root_Ctrl')


    def Switch_function(self):
        Df_JntGrp = cmds.ls('Df*_Jnt', type='joint')
        Fk_JntGrp = cmds.ls("Arm*FK_Jnt", type='joint')
        Ik_JntGrp = cmds.ls("Arm*IK_Jnt", type='joint')

        for Df_Jnt, Fk_Jnt in zip(Df_JntGrp, Fk_JntGrp):
            cmds.parentConstraint(Fk_Jnt, Df_Jnt)
        for Df_Jnt, Ik_Jnt in zip(Df_JntGrp,Ik_JntGrp):
            cmds.parentConstraint(Ik_Jnt, Df_Jnt)

        cmds.createNode('blendColors', n='ikfk_Switch_Bc')
        cmds.setAttr('ikfk_Switch_Bc.color1R', 0)
        cmds.setAttr('ikfk_Switch_Bc.color1G', 1)
        cmds.setAttr('ikfk_Switch_Bc.color2R', 1)
        cmds.setAttr('ikfk_Switch_Bc.color2B', 0)

        cmds.connectAttr('Root_Ctrl.Switch','ikfk_Switch_Bc.blender')
        cmds.connectAttr('ikfk_Switch_Bc.outputG', 'Df1_Jnt_parentConstraint1.Arm1FK_JntW0')
        cmds.connectAttr('ikfk_Switch_Bc.outputR', 'Df1_Jnt_parentConstraint1.Arm1IK_JntW1')
        cmds.connectAttr('ikfk_Switch_Bc.outputG', 'Df2_Jnt_parentConstraint1.Arm2FK_JntW0')
        cmds.connectAttr('ikfk_Switch_Bc.outputR', 'Df2_Jnt_parentConstraint1.Arm2IK_JntW1')
        cmds.connectAttr('ikfk_Switch_Bc.outputG', 'Df3_Jnt_parentConstraint1.Arm3FK_JntW0')
        cmds.connectAttr('ikfk_Switch_Bc.outputR', 'Df3_Jnt_parentConstraint1.Arm3IK_JntW1')

        cmds.connectAttr('ikfk_Switch_Bc.outputG', 'Arm1FK_Ctrl_G.visibility')
        cmds.connectAttr('ikfk_Switch_Bc.outputR', 'Arm1Ik_Ctrl_G.visibility')


    def stretch_function(self):
        StartObj= 'Df1_Jnt'
        EndObj= 'Df3_Jnt'

        E = cmds.spaceLocator(n='Stretch_start_Loc')
        F = cmds.spaceLocator(n='Stretch_end_Loc')
        cmds.matchTransform(E, 'Arm1Ik_Ctrl')
        cmds.matchTransform(F, 'Arm2Ik_Ctrl')
        cmds.parent(E,'Arm1Ik_Ctrl')
        cmds.parent(F,'Arm2Ik_Ctrl')

        cmds.createNode('distanceDimShape', n='Arm_DT')
        cmds.rename( 'distanceDimension1', 'ArmDT' )
        cmds.connectAttr('Stretch_start_LocShape.worldPosition','Arm_DT.startPoint')
        cmds.connectAttr('Stretch_end_LocShape.worldPosition','Arm_DT.endPoint')

        cmds.spaceLocator(n='ScaleDefault')

        S_Pos = cmds.xform(StartObj , q =1, t =1 ,ws =1)
        E_Pos = cmds.xform(EndObj, q=1, t=1, ws=1)
        Arm_distance = DT = ((S_Pos[0] - E_Pos[0])**2 + (S_Pos[1] - E_Pos[1])**2 + (S_Pos[2] - E_Pos[2])**2)**0.5

        cmds.createNode('multiplyDivide',n='ScDefault_Md')
        cmds.setAttr('ScDefault_Md.input1X', Arm_distance )
        cmds.setAttr('ScDefault_Md.input1Y', Arm_distance )
        cmds.connectAttr('ScaleDefault.scaleX','ScDefault_Md.input2X')

        cmds.createNode('multiplyDivide',n='Distance_Md')
        cmds.setAttr('Distance_Md.operation', 2)
        cmds.connectAttr('Arm_DT.distance', 'Distance_Md.input1X')
        cmds.connectAttr('ScDefault_Md.outputX', 'Distance_Md.input2X')

        cmds.createNode('blendColors', n='Stretch_Bc')
        cmds.setAttr('Stretch_Bc.color2R', 1)
        cmds.setAttr('Stretch_Bc.color2B', 0)

        cmds.connectAttr('Root_Ctrl.Stretch','Stretch_Bc.blender')
        cmds.connectAttr('Distance_Md.outputX','Stretch_Bc.color1R')

        cmds.createNode('condition',n='Stretch_Cd')
        cmds.setAttr('Stretch_Cd.operation', 3)
        cmds.connectAttr('Arm_DT.distance','Stretch_Cd.firstTerm')
        cmds.connectAttr('Distance_Md.outputX','Stretch_Cd.secondTerm')
        cmds.connectAttr('Stretch_Bc.outputR','Stretch_Cd.colorIfTrue.colorIfTrueR')

        cmds.connectAttr('Stretch_Cd.outColor.outColorR','Arm1IK_Jnt.scale.scaleX')
        cmds.connectAttr('Stretch_Cd.outColor.outColorR','Arm2IK_Jnt.scale.scaleX')


    def cleanUpTheCode(self):
        cmds.parentConstraint('Root_Ctrl','ScaleDefault')
        cmds.group(empty=True, n= 'Jnt_Grp')
        cmds.group(empty=True, n= 'Sys_Grp')

        Sys_Grp_Obj= ('ArmDT','ScaleDefault')
        Jnt_Grp_Obj= ('Arm1FK_Jnt','Arm1IK_Jnt','Df1_Jnt')

        cmds.parent(Jnt_Grp_Obj,'Jnt_Grp')
        cmds.parent(Sys_Grp_Obj,'Sys_Grp')

        cmds.parent('Jnt_Grp','Sys_Grp','Root_Ctrl_G')


Arm_build()

