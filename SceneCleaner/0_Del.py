import maya.cmds as cmds
import maya.mel as mel
#khs
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
        
        print('---0 list---   ' + ', '.join(resultA))
        print('---0 or Move list---   ' + ', '.join(resultB))
        print('---lock list---   ' + ', '.join(resultC))


def show():
    SDPwin().create()

show()
