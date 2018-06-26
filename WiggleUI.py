import maya.cmds as cmds
import random

mainWindow = None


def CreateWindow(windowName):
    if cmds.window(windowName, exists=True):
        cmds.deleteUI(windowName)

    global mainWindow
    mainWindow = cmds.window(windowName, title=windowName)

    cmds.showWindow(mainWindow)
    return mainWindow

def WiggleUI():

    editedWindow = CreateWindow("Wiggle")
    cmds.window(editedWindow, edit=True, title="Wiggle", widthHeight=(850, 200))
    intro = cmds.rowColumnLayout(nc=1, rs=[(1, 10), (2, 10)], rat=[(1, "top", 10), (2, "top", 10)], ro=[(1, "top", 20)],
                                 cal=[(1, "center")], columnWidth=[(1, 800)], cat=[(1, "both", 10)])
    cmds.text(label="Use the WIGGLE slider to move the selected object.")
    cmds.text(label="Type minimum and maximum value to set the RANGE of the wiggle movement.")
    floatSlider = cmds.floatSliderGrp(label="Wiggle", minValue=0, maxValue=1, dc=DoMove, value=0 )
    cmds.text(label="Value Range")
    cmds.floatFieldGrp('minValueRange', label="Min Value", value1=1 )
    cmds.floatFieldGrp('maxValueRange', label="Max Value", value1=1.1)


def GetSelection():

    selection = cmds.ls(selection=True, typ='transform')
    if len(selection) == 0 or len(selection) > 1:
        raise Exception("You must select one object")
    return selection[0]


def GetRange(*args):

    valueRange = []
    minValue = cmds.floatFieldGrp('minValueRange', query=True, v1=True)
    valueRange.append(minValue)
    maxValue = cmds.floatFieldGrp('maxValueRange', query=True, v1=True)
    valueRange.append(maxValue)
    return valueRange


def DoMove(*args):

    obj = GetSelection()
    valueRange = GetRange()
    minRangeValue = valueRange[0]
    maxRangeValue = valueRange[1]

    randX = random.uniform(minRangeValue, maxRangeValue)
    randY = random.uniform(minRangeValue, maxRangeValue)
    randZ = random.uniform(minRangeValue, maxRangeValue)
    cmds.move(randX, randY, randZ, obj, os=True, xyz=True)


WiggleUI()