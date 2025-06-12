import maya.cmds as cmds
import os

def TurtleTurnOff():
    plugin_path = r"C:\Program Files\Autodesk\Maya2020\bin\plug-ins\Turtle.mll"
    
    if os.path.exists(plugin_path):
        if cmds.pluginInfo('Turtle.mll', query=True, loaded=True):
            cmds.unloadPlugin('Turtle.mll')
        cmds.pluginInfo('Turtle.mll', edit=True, autoload=False)
        print("Turtle 꺼짐.")

TurtleTurnOff()