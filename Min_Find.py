import maya.cmds as cmds
import maya.mel as mel

class SDPwin:
    def create( self ):
        cmds.select(cl=1)
        selA = cmds.ls( '_Ctrl', '_Con', '*_C', type='transform' )
        resultA = []
        resultC = []
        resultE = []
        print '\n\n    print -> Ctrl List\n\n'
        
        for x in range(len(selA)):
            #print selA[x]
            trs = [ 'translateX', 'translateY', 'translateZ', 'rotateX', 'rotateY', 'rotateZ', 'scaleX', 'scaleY', 'scaleZ' ]
            for y in range(len(trs)):
                ga = cmds.getAttr('%s.%s'%(selA[x],trs[y]))
                if(y<=5):
                    if(ga!=0.0):
                        #if(ga>=0.1):
                        print '%s.%s    %s'%(selA[x],trs[y],ga)
                        resultA.append(selA[x])
                else:
                    if(ga!=1.0):
                        #if(ga>=1.1):
                        print '%s.%s    %s'%(selA[x],trs[y],ga)
                        resultA.append(selA[x])
        
        for x in range(len(selA)):
            trs = [ 'rotatePivotX', 'rotatePivotY', 'rotatePivotZ', 'scalePivotX', 'scalePivotY', 'scalePivotZ' ]
            for y in range(len(trs)):
                ga = cmds.getAttr('%s.%s'%(selA[x],trs[y]))
                if(ga!=0.0):
                    #if(ga>=0.1):
                    print '%s.%s    %s'%(selA[x],trs[y],ga)
                    resultC.append(selA[x])
        
        selA = cmds.ls( 'Mod_Grp' )
        if selA:
            selB = cmds.listRelatives( selA, ad=1, type='transform')
            for x in range(len(selB)):
                #print selB[x]
                trs = [ 'scaleX', 'scaleY', 'scaleZ' ]
                for y in range(len(trs)):
                    ga = cmds.getAttr('%s.%s'%(selB[x],trs[y]))
                    if(ga!=1.0):
                        print '%s.%s    %s'%(selB[x],trs[y],ga)
                        resultE.append(selB[x])
        else:
            print '\n\n    Check!    "Mod_Grp"\n\n'
        resultBB = set(resultA)
        resultDD = set(resultC)
        resultFF = set(resultE)
        resultB = list(resultBB)
        resultD = list(resultDD)
        resultF = list(resultFF)
        corName = 'correction_SET'
        pivName = 'pivot_SET'
        modName = 'modScale_SET'
        selCP = [ corName, pivName, modName ]
        selBD = [ resultB, resultD, resultF ]
        for x in range(len(selCP)):
            #print len(selBD[x])
            print selBD[x]
            selE = cmds.ls( selCP[x] )
            if (len(selE)!=0):# type
                cmds.delete( selCP[x] )
            if(len(selBD[x])!=0):# list
                cmds.sets( selBD[x], n=selCP[x] )
        
def show():
    SDPwin().create()
show() 