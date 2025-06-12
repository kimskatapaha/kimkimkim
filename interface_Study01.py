import maya.cmds as cmds
from functools import partial

def gui():
    if cmds.window('win', q=1, ex=1):
        cmds.deleteUI('win', window=True)

    cmds.window('win', title='Generator')
    cmds.columnLayout(adjustableColumn=True)

    def generate_poly(cube_size, *arguments):
        cmds.polyCube(width=1.0, height=1.0, depth=1.0)[0]
        
    cmds.button(label='hello', command=partial(generate_poly, ))
    cmds.floatSliderGrp('test', label='Test_F', field=1, minValue=0.0, maxValue=10.0, fieldMinValue=0.0, value=10)
    cmds.showWindow('win')

gui()