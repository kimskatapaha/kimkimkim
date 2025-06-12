import maya.cmds as cmds

#클릭한 오브젝트의 cv를 개별로 선택해서 clu하는 스크립트 필요 (특히 래티스, 커브등등)
        #____선택해서 리스트로 만드는 함수
        #그 리스트에 로케이터 넣는 함수
        #그 리스트에 조인트 넣는 함수
        #그 리스트에 클러스터 넣는 함수


def Cv_individual_selection():
    selObj = cmds.ls(sl=True)


    for A in selObj:
        cv_list = cmds.ls(A + ".cv[*]", flatten=True)
        print(cv_list)

        for B in cv_list:
                cmds.cluster(B,n=A + "_clu")


Cv_individual_selection()