import maya.cmds as cmds
import re

list = cmds.ls()
name = 'Index'
pattern = r'\S+_\S+_{}\d+'.format(name)

for x in list:
    match = re.search(pattern, x)
    if match:
        Find = match.group()
        print(Find)