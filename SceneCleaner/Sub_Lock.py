import maya.cmds as cmds


def Sub_lock(Check):
    pre_lst = cmds.ls(type='RedshiftMeshParameters')
    lst = [x for x in pre_lst if '_sub' in x]

    print(lst)
    if Check == True:
        lock = True
    else:
        lock = False
    lst_lock = [cmds.lockNode(x, l=lock) for x in lst]


Sub_lock(True)

def deleteUnknown():
    lst = []

    sel01 = cmds.ls('vray*')
    sel02 = cmds.ls(type="unknown")
    sel03 = cmds.ls( ' TurtleDefaultBakeLayer')

    lst.extend(sel01)
    lst.extend(sel02)
    lst.extend(sel03)

    lst_unlock = [ cmds.lockNode(x, l =0) for x in lst]

    cmds.delete(lst)

class SDPwin:
    def create(self):
        cmds.select(cl=1)
        selA = cmds.ls('_Ctrl', '_Con', '*_C', type='transform')
        resultA = []
        resultB = []
        resultC = []
        resultE = []

        for x in range(len(selA)):
            trs = ['translateX', 'translateY', 'translateZ', 'rotateX', 'rotateY', 'rotateZ']
            for y in range(len(trs)):
                try:
                    if cmds.getAttr('%s.%s' % (selA[x], trs[y]), lock=1):
                        resultC.append(selA[x] + '.' + trs[y])
                        continue

                    ga = cmds.getAttr('%s.%s' % (selA[x], trs[y]))
                    if (y <= 5):
                        if (ga != 0.0):
                            if 'e' in str(ga):
                                cmds.setAttr('%s.%s' % (selA[x], trs[y]), 0)
                                resultA.append(selA[x])
                            else:
                                resultB.append(selA[x] + '.' + trs[y])
                                pass
                    else:
                        if (ga != 1.0):
                            if 'e' in str(ga):
                                cmds.setAttr('%s.%s' % (selA[x], trs[y]), 0)
                                resultA.append(selA[x])
                            else:
                                resultB.append(selA[x] + '.' + trs[y])
                                pass
                except:
                    pass

        print('---0 list---   ' + ', '.join(resultA))
        print('---0 or Move list---   ' + ', '.join(resultB))
        print('---lock list---   ' + ', '.join(resultC))


def show():
    SDPwin().create()


show()
Sub_lock(True)
deleteUnknown()