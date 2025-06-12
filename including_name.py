import maya.cmds as cmds

all_objects = cmds.ls()
variable_obj = []

for obj in all_objects:
    if "V" in obj:
        variable_obj.append(obj)

if variable_obj:
    cmds.select(variable_obj, replace=True)
else:
    print("Not found")