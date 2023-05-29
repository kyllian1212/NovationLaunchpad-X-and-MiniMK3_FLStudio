import arrangement
import channels
import device
import general
import launchMapPages
import midi
import mixer
import patterns
import playlist
import plugins
import transport
import ui
import utils

import math

class Color:
    def __init__(self, value: int, hexcode: str):
        self.value = value
        self.hexcode = hexcode

class State:
    def __init__(self, value: int, noteValue: int, ccValue: int):
        self.value = value
        self.noteValue = noteValue
        self.ccValue = ccValue

class PadType:
    def __init__(self, value: int):
        self.value = value

class Pad:
    def __init__(self, x: int, y: int, color: Color, prevColor: Color, state: State, prevState: State, type: PadType):
        self.x = x
        self.y = y
        self.color = color
        self.prevColor = prevColor
        self.state = state
        self.prevState = prevState
        self.type = type

#init colors
#besides off to white, everything is light > normal > dark > darker
color = {}

color["off"] = Color(0, "000000")
color["darker"] = Color(1, "b3b3b3")
color["dark"] = Color(2, "dddddd")
color["white"] = Color(3, "ffffff")

color["light_red"] = Color(4, "ffb3b3F")
color["red"] = Color(5, "ff6161")
color["dark_red"] = Color(6, "dd6161")
color["darker_red"] = Color(7, "b36161")

color["light_orange"] = Color(8, "fff3d5")
color["orange"] = Color(9, "ffb361")
color["dark_orange"] = Color(10, "dd8c61")
color["darker_orange"] = Color(11, "b37661") #also brown

color["light_yellow"] = Color(12, "ffeea1")
color["yellow"] = Color(13, "ffff61")
color["dark_yellow"] = Color(14, "dddd61")
color["darker_yellow"] = Color(15, "b3b361")

color["light_lime_green"] = Color(16, "ddffa1")
color["lime_green"] = Color(17, "c2ff61")
color["dark_lime_green"] = Color(18, "a1dd61")
color["darker_lime_green"] = Color(19, "81b361")

color["light_green"] = Color(20, "c2ffb3")
color["green"] = Color(21, "61ff61")
color["dark_green"] = Color(22, "61dd61")
color["darker_green"] = Color(23, "61b361")

color["light_blue_green"] = Color(24, "c2ffc2")
color["blue_green"] = Color(25, "61ff8c")
color["dark_blue_green"] = Color(26, "61dd76")
color["darker_blue_green"] = Color(27, "61b36b")

color["light_aqua"] = Color(28, "c2ffcc")
color["aqua"] = Color(29, "61ffcc")
color["dark_aqua"] = Color(30, "61dda1")
color["darker_aqua"] = Color(31, "61b381")

color["light_cyan"] = Color(32, "c2fff3")
color["cyan"] = Color(33, "61ffe9")
color["darkcyan"] = Color(34, "61ddc2")
color["darkercyan"] = Color(35, "61b396")

color["light_turquoise"] = Color(36, "c2f3ff")
color["turquoise"] = Color(37, "61eeff")
color["dark_turquoise"] = Color(38, "61c7dd")
color["darker_turquoise"] = Color(39, "61a1b3")

color["light_azure"] = Color(40, "c2ddff")
color["azure"] = Color(41, "61c7ff")
color["dark_azure"] = Color(42, "61a1dd")
color["darker_azure"] = Color(43, "6181b3")

color["light_blue"] = Color(44, "a18cff")
color["blue"] = Color(45, "6161ff")
color["dark_blue"] = Color(46, "6161dd")
color["darker_blue"] = Color(47, "6161b3")

color["light_cobalt"] = Color(48, "ccb3ff")
color["cobalt"] = Color(49, "a161ff")
color["dark_cobalt"] = Color(50, "8161dd")
color["darker_cobalt"] = Color(51, "7661b3")

color["light_purple"] = Color(52, "ffb3ff")
color["purple"] = Color(53, "ff61ff")
color["dark_purple"] = Color(54, "dd61dd")
color["darker_purple"] = Color(55, "b361b3")

color["light_pink"] = Color(56, "ffb3d5")
color["pink"] = Color(57, "ff61c2")
color["dark_pink"] = Color(58, "dd61a1")
color["darker_pink"] = Color(59, "b3618c")

color["pure_orange"] = Color(60, "ff7661")
color["yellow_orange"] = Color(61, "e9b361")
color["yellow_green"] = Color(62, "ddc261")
color["apple_green"] = Color(63, "a1a161")

#init states
state = {}

state["static"] = State(1, 144, 176)
state["flashing"] = State(2, 145, 177)
state["pulsing"] = State(3, 146, 178)

#init pad types
type = {}

type["main"] = PadType(1)
type["cc"] = PadType(2)

#init grid
grid = {}

for x in range(1, 10):
    for y in range(1, 10):
        if x == 9 or y == 9:
            grid[f"pad{x}{y}"] = Pad(x, y, color["off"], color["off"], state["static"], state["static"], type["cc"])
        else:
            grid[f"pad{x}{y}"] = Pad(x, y, color["off"], color["off"], state["static"], state["static"], type["main"])

#for padkey, padvalues in grid.items():
#    print(f"{padkey}: {padvalues.x} {padvalues.y} {padvalues.color} {padvalues.state} {padvalues.type}")

#color processing
def rgbColorToPaletteColor(rgb: int):
    r, g, b = utils.ColorToRGB(rgb)
    colorHexList = []

    for colorkey, colorvalue in color:
        rc, gc, bc = utils.ColorToRGB(rgb)
    


#launchpad functions
def enableDawMode():
    device.midiOutSysex(bytes([240, 0, 32, 41, 2, 13, 16, 1, 247])) #enable daw mode
    device.midiOutSysex(bytes([240, 0, 32, 41, 2, 13, 0, 0, 247])) #switch to session automatically

def disableDawMode():
    device.midiOutSysex(bytes([240, 0, 32, 41, 2, 13, 18, 1, 0, 1, 247])) #daw clear state
    device.midiOutSysex(bytes([240, 0, 32, 41, 2, 13, 16, 0, 247])) #disable daw mode

def lightAllPadsTest():
    colorVal = 0
    for xtest in range(8, 0, -1):
        for ytest in range(1, 9):
            device.midiOutMsg(state["static"].noteValue, 0, int(str(xtest) + str(ytest)), colorVal)
            colorVal += 1

def lightPad(xy: int, color: dict[str, Color], state: dict[str, State], revertToPrev: bool = True):
    if "9" in str(xy):
        device.midiOutMsg(state.ccValue, 0, xy, color.value)
    else:
        device.midiOutMsg(state.noteValue, 0, xy, color.value)
    
    if revertToPrev:
        grid[f"pad{str(xy)}"].prevColor = grid[f"pad{str(xy)}"].color
        grid[f"pad{str(xy)}"].prevState = grid[f"pad{str(xy)}"].state
        
    grid[f"pad{str(xy)}"].color = color
    grid[f"pad{str(xy)}"].state = state

def revertPad(xy: int):
    prevState = grid[f"pad{str(xy)}"].prevState
    prevColor = grid[f"pad{str(xy)}"].prevColor

    if "9" in str(xy):
        device.midiOutMsg(prevState.ccValue, 0, xy, prevColor.value)
    else:
        device.midiOutMsg(prevState.noteValue, 0, xy, prevColor.value)
    
    grid[f"pad{str(xy)}"].color = prevColor
    grid[f"pad{str(xy)}"].state = prevState

def resetLighting(main: bool = True, cc: bool = False):
    for padkey, padvalues in grid:
        device.midiOutMsg(state["static"].noteValue, 0, padvalues.xy, color["off"].value)
        device.midiOutMsg(state["static"].ccValue, 0, padvalues.xy, color["off"].value)

def scrollText(text: str, color: Color, speed: int = 8, looping: int = 0):
    """Scrolls text on the Launchpad.

    ## Args:
        * text (`str`): Text to scroll
        * color (`Color`): Text color
        * speed (`int`): speed in pads per seconds. 0 full stop (?), 1-63 forward, 64-127 backwards
        * looping (`int`): sets if the text is looping (until input). 0 doesn't loop, 1 does.
    """
    if speed < 0 or speed > 127:
        raise ValueError("speed must be between 0 and 127")
    
    message = []
    
    #put message start values, followed by looping, speed & color values to message
    message.extend([240, 0, 32, 41, 2, 13, 7, looping, speed, 0, color.value])
    
    #put text (in ascii) to message
    for char in text:
        message.append(ord(char))
    
    #put message end value
    message.append(247)
    
    #play on launchpad
    device.midiOutSysex(bytes(message))