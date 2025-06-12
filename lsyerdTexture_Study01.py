import maya.cmds as cmds

NodeName = "layeredTexture1"

#inputs추가
#1의 이유는 마지막 인덱스를 지정하기 위해 (두개까지 만들고 싶다->1, 다섯개 만들거야->4)
#isVisible은 조정하고 싶은 어트리
cmds.setAttr("{}.inputs[{}].{}".format(NodeName , 1 , "isVisible") ,0)


#inputs 리스트 찾기, 보기
sel = cmds.ls("{}.inputs[*]".format(NodeName))

for x in sel:
    print (x)