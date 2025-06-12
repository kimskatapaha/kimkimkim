import maya.cmds as cmds
from functools import partial
import maya.mel as mel


#_____0_Del Function add_____
#khs
class SDPwin_Del:
    def create_MinDel(self, Delete_Bool=True, *arguments):
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


#_____Min_Find Function add_____
class SDPwin_Find:
    def create_MinFind(self, Delete_Bool=True, *arguments):
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
        if not selA:
            print("No relevant nodes found.")
            return
    
        for x in range(len(selA)):
            trs = [ 'rotatePivotX', 'rotatePivotY', 'rotatePivotZ', 'scalePivotX', 'scalePivotY', 'scalePivotZ' ]
            for y in range(len(trs)):
                try:
                    ga = cmds.getAttr('%s.%s'%(selA[x],trs[y]))
                    if (y <= 5):
                        if(ga!=0.0):
                            #if(ga>=0.1):
                            print '%s.%s    %s'%(selA[x],trs[y],ga)
                            resultC.append(selA[x])
                    else:
                        if (ga != 1.0):
                            # if(ga>=1.1):
                            print '%s.%s    %s' % (selA[x], trs[y], ga)
                            resultA.append(selA[x])
                except:
                    pass

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

#_____create Gui_____
def Scene_Cleaner_Gui():
    if cmds.window('win', q=1, ex=1):
        cmds.deleteUI('win', window=True)

    cmds.window('win', title='Scene Cleaner')
    cmds.columnLayout(adjustableColumn=True)

#_____del_LockNode Function add_____
    def del_LockNode(Delete_Bool = True):

        sel = cmds.ls(' TurtleDefaultBakeLayer')

        lock =cmds.lockNode(sel , l =0)

        cmds.delete(sel)
        
#_____del_LockNode button add_____
    cmds.button(label='Turtle Delete', command=partial(del_LockNode, ))


#_____key_Delete Function add_____
    def key_Delete(Delete_Bool = True, *arguments):
    
    
        All =[]
    
        lst_PO = cmds.ls(type = 'animCurveTL')
        lst_RO = cmds.ls(type = 'animCurveTA')
        lst_ETF = cmds.ls(type = 'animCurveTU')
    
    
        All.extend(lst_PO)
        All.extend(lst_RO)
        All.extend(lst_ETF)
        if Delete_Bool == True:
            cmds.delete(All)
        else:
            pass

#_____key_Delete button add_____
    cmds.button(label='key Delete', command=partial(key_Delete, True))


#_____deleteUnknown Function add_____
    def deleteUnknown(Delete_Bool = True, *arguments):
        lst = []

        sel01 = cmds.ls('vray*')
        sel02 = cmds.ls(type="unknown")
        sel03 = cmds.ls( ' TurtleDefaultBakeLayer')

        lst.extend(sel01)
        lst.extend(sel02)
        lst.extend(sel03)

        lst_unlock = [ cmds.lockNode(x, l =0) for x in lst]

        cmds.delete(lst)

#_____deleteUnknown button add_____
    cmds.button(label='delete Unknown', command=partial(deleteUnknown, True))


#_____Sub_Lock Function add_____
    def Sub_lock(Check):
        pre_lst = cmds.ls(type='RedshiftMeshParameters')
        lst = [x for x in pre_lst if '_sub' in x]

        if Check:
            lock = True
        else:
            lock = False

        for obj in lst:
            cmds.lockNode(obj, lock=lock)

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

#_____Sub_Lock button add_____
    def button_callback(*args):
        if Sub_lock(True):
            SDPwin().create()

    cmds.columnLayout(adjustableColumn=True)
    cmds.button(label='Sub lock', command=button_callback)

#_____Min_Find button add_____
    cmds.button(label='Min Find', command=partial(SDPwin_Find().create_MinFind, True))

#_____Min Del button add_____
    cmds.button(label='Min Del', command=partial(SDPwin_Del().create_MinDel, True))

#_____design interface_____ 
    cmds.window('win', e=1, widthHeight=(280, 140))
        

#_____Display Window_____
    cmds.showWindow('win')


Scene_Cleaner_Gui()
