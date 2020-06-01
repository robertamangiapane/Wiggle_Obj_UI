import maya.cmds as cmds
import random

mainWindow = None


def create_window(windowName):
    if cmds.window(windowName, exists=True):
        cmds.deleteUI(windowName)

    global mainWindow
    mainWindow = cmds.window(windowName, title=windowName)

    cmds.showWindow(mainWindow)
    return mainWindow

def wiggle_window():

    editedWindow = create_window("Wiggle")
    cmds.window(editedWindow, edit=True, title="Wiggle", widthHeight=(850, 200))
    intro = cmds.rowColumnLayout(nc=1, rs=[(1, 10), (2, 10)], rat=[(1, "top", 10), (2, "top", 10)], ro=[(1, "top", 20)],
                                 cal=[(1, "center")], columnWidth=[(1, 800)], cat=[(1, "both", 10)])
    cmds.text(label="Use the WIGGLE slider to move the selected object.")
    cmds.text(label="Type minimum and maximum value to set the RANGE of the wiggle movement.")
    floatSlider = cmds.floatSliderGrp(label="Wiggle", minValue=0, maxValue=1, dc=do_move, value=0 )
    cmds.text(label="Value Range")
    cmds.floatFieldGrp('minValueRange', label="Min Value", value1=1 )
    cmds.floatFieldGrp('maxValueRange', label="Max Value", value1=1.1)


def get_obj_from_selection():

    selection = cmds.ls(selection=True, typ='transform')

    return get_obj(selection)


def get_obj(selection):
    if len(selection) == 0 or len(selection) > 1:
        raise Exception("You must select one object")
    else:
        return selection[0]


def get_range(*args):

    valueRange = []
    minValue = cmds.floatFieldGrp('minValueRange', query=True, v1=True)
    valueRange.append(minValue)
    maxValue = cmds.floatFieldGrp('maxValueRange', query=True, v1=True)
    valueRange.append(maxValue)
    return valueRange


def do_move(*args):

    obj = get_obj_from_selection()
    valueRange = get_range()
    minRangeValue = valueRange[0]
    maxRangeValue = valueRange[1]

    randX = random.uniform(minRangeValue, maxRangeValue)
    randY = random.uniform(minRangeValue, maxRangeValue)
    randZ = random.uniform(minRangeValue, maxRangeValue)
    cmds.move(randX, randY, randZ, obj, os=True, xyz=True)


wiggle_window()
