import maya.cmds as cmds



def Fix_Leg_Stratch():
    L_Leg_St = cmds.group( 'L_Leg_IK_DTEnd_loc', 'L_Leg_IK_End_PVst_DTEnd_loc', n = 'L_Leg_IK_DTEnd_loc_Grp' )
    R_Leg_St = cmds.group( 'R_Leg_IK_DTEnd_loc', 'R_Leg_IK_End_PVst_DTEnd_loc', n = 'R_Leg_IK_DTEnd_loc_Grp' )

    cmds.parent (L_Leg_St , 'L_Ankle_IK_HD_Grp')
    cmds.parent (R_Leg_St , 'R_Ankle_IK_HD_Grp')


Fix_Leg_Stratch()