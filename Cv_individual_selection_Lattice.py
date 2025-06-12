import maya.cmds as cmds



def Cv_individual_selection():
    selObj = cmds.ls(sl=True)


    for A in selObj:
        cv_list = cmds.ls(A + ".pt[*]", flatten=True)
        print(cv_list)

        for B in cv_list:
                cmds.cluster(B,n=A + "_clu")


Cv_individual_selection()