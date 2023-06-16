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

class PadGroup:
    def __init__(self, xy: list[int]):
        self.xy = xy

#init colors
#besides off to white, everything is light > normal > dark > darker
color = {}

color["off"] = Color(0, "000000")
color["dark_gray"] = Color(1, "b3b3b3")
color["light_gray"] = Color(2, "dddddd")
color["white"] = Color(3, "ffffff")

color["light_red"] = Color(4, "ffb3b3F")
color["red"] = Color(5, "ff6161")
color["dark_red"] = Color(6, "dd6161")
color["darker_red"] = Color(7, "b36161")

color["light_orange"] = Color(8, "fff3d5")
color["orange"] = Color(9, "ffb361")
color["dark_orange"] = Color(10, "dd8c61")
color["darker_orange"] = Color(11, "b37661")

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

color["alt_darker_green"] = Color(64, "61b361")
color["silver_tree"] = Color(65, "61b38c")
color["danube"] = Color(66, "618cd5")
color["alt_blue"] = Color(67, "6161ff")

color["tradewind"] = Color(68, "61b3b3")
color["cornflower_blue"] = Color(69, "8c61f3")
color["lily"] = Color(70, "ccb3c2")
color["empress"] = Color(71, "8c7681")

color["alt_red"] = Color(72, "ff6161")
color["milan"] = Color(73, "f3ffa1")
color["canary"] = Color(74, "eefc61")
color["greener_canary"] = Color(75, "ccff61")

color["pastel_green"] = Color(76, "76dd61")
color["alt_aqua"] = Color(77, "61ffcc")
color["malibu"] = Color(78, "61e9ff")
color["bluer_malibu"] = Color(79, "61a1ff")

color["heliotrope"] = Color(80, "8c61ff")
color["lavender"] = Color(81, "cc61fc")
color["lavender_magenta"] = Color(82, "ee8cdd")
color["brown"] = Color(83, "a17661")

color["atomic_tangerine"] = Color(84, "ffa161")
color["light_canary"] = Color(85, "ddf961")
color["reef"] = Color(86, "d5ff8c")
color["alt_green"] = Color(87, "61ff61")

color["greener_reef"] = Color(88, "b3ffa1")
color["snowy_mint"] = Color(89, "ccfcd5")
color["aero_blue"] = Color(90, "b3fff6")
color["onahau"] = Color(91, "cce4ff")

color["perano"] = Color(92, "a1c2f6")
color["perfume"] = Color(93, "d5c2f9")
color["pink_heliotrope"] = Color(94, "f98cff")
color["hot_pink"] = Color(95, "ff61cc")

color["koromiko"] = Color(96, "ffc261")
color["portica"] = Color(97, "f3ee61")
color["lemon"] = Color(98, "e4ff61")
color["gold"] = Color(99, "ddcc61")

color["teak"] = Color(100, "b3a161")
color["fern"] = Color(101, "61ba76")
color["de_york"] = Color(102, "76c28c")
color["waterloo"] = Color(103, "8181a1")

color["polo_blue"] = Color(104, "818ccc")
color["tan"] = Color(105, "ccaa81")
color["alt_dark_red"] = Color(106, "dd6161")
color["rose_bud"] = Color(107, "f9b3a1")

color["rajah"] = Color(108, "f9ba76")
color["dolly"] = Color(109, "fff38c")
color["texas"] = Color(110, "e9f9a1")
color["sulu"] = Color(111, "d5ee76")

color["alt_waterloo"] = Color(112, "8181a1")
color["citrine_white"] = Color(113, "f9f9d5")
color["scandal"] = Color(114, "ddfce4")
color["titan_white"] = Color(115, "e9e9ff")

color["fog"] = Color(116, "e4d5ff")
color["alt_dark_gray"] = Color(117, "b3b3b3")
color["gray"] = Color(118, "d5d5d5")
color["near_white"] = Color(119, "f9ffff")

color["mandy"] = Color(120, "e96161")
color["coral_tree"] = Color(121, "aa6161")
color["screamin_green"] = Color(122, "81f661")
color["alt2_darker_green"] = Color(123, "61b361")

color["alt_portica"] = Color(124, "f3ee61")
color["alt_teak"] = Color(125, "b3a161")
color["ronchi"] = Color(126, "eec261")
color["contessa"] = Color(127, "c27661")

#init states
state = {}

state["static"] = State(1, 144, 176)
state["flashing"] = State(2, 145, 177)
state["pulsing"] = State(3, 146, 178)

#init pad types
type = {}

type["main"] = PadType(1)
type["cc"] = PadType(2)

#init padgroup (characters)
character = {}

character["s0"] = PadGroup([41, 42, 11, 12])
character["s1"] = PadGroup([42, 32, 22, 12])
character["s2"] = PadGroup([41, 42, 32, 21, 11, 12])
character["s3"] = PadGroup([41, 42, 32, 21, 22, 11, 12])
character["s4"] = PadGroup([41, 31, 21, 22, 12])
character["s5"] = PadGroup([41, 42, 31, 22, 11, 12])
character["s6"] = PadGroup([41, 42, 31, 21, 22, 11, 12])
character["s7"] = PadGroup([41, 42, 32, 22, 12])
character["s8"] = PadGroup([41, 42, 31, 32, 21, 22, 11, 12])
character["s9"] = PadGroup([41, 42, 31, 32, 22, 11, 12])

character["0"] = PadGroup([41, 42, 43, 31, 33, 21, 23, 11, 12, 13])
character["1"] = PadGroup([43, 33, 23, 13])
character["2"] = PadGroup([41, 42, 43, 33, 21, 22, 11, 12, 13])
character["3"] = PadGroup([41, 42, 43, 33, 22, 23, 11, 12, 13])
character["4"] = PadGroup([41, 31, 33, 21, 22, 23, 13])
character["5"] = PadGroup([41, 42, 43, 31, 32, 23, 11, 12, 13])
character["6"] = PadGroup([41, 42, 43, 31, 21, 22, 23, 11, 12, 13])
character["7"] = PadGroup([42, 43, 33, 23, 13])
character["8"] = PadGroup([41, 42, 43, 31, 32, 33, 21, 23, 11, 12, 13])
character["9"] = PadGroup([41, 42, 43, 31, 32, 33, 23, 11, 12, 13])

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
def rgbColorToPaletteColor(rgb: int) -> Color:
    try:
        r, g, b = utils.ColorToRGB(rgb)
        colorDiffList = []

        for colorkey, colorvalue in color.items():
            rc, gc, bc = utils.ColorToRGB(int(colorvalue.hexcode, 16))
            colorDiff = math.sqrt((r-rc)**2+(g-gc)**2+(b-bc)**2)
            colorDiffList.append((colorDiff, utils.ColorToRGB(int(colorvalue.hexcode, 16))))

        result = min(colorDiffList)[1]

        rr = f'{result[0]:x}'
        gr = f'{result[1]:x}'
        br = f'{result[2]:x}'

        paletteHex = rr+gr+br

        for colorkey, colorvalue in color.items():
            if colorvalue.hexcode == paletteHex:
                return color[colorkey]
        
        return color["off"]
    except:
        print("issue finding color!")
        return color["off"]

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

def lightGroup(group: PadGroup, color: dict[str, Color], state: dict[str, State], offset: int = 0, revertToPrev: bool = True):
    for padXy in group.xy:
        finalXy = padXy+offset
        if "9" in str(finalXy):
            device.midiOutMsg(state.ccValue, 0, finalXy, color.value)
        else:
            device.midiOutMsg(state.noteValue, 0, finalXy, color.value)
        
        if revertToPrev:
            grid[f"pad{str(finalXy)}"].prevColor = grid[f"pad{str(finalXy)}"].color
            grid[f"pad{str(finalXy)}"].prevState = grid[f"pad{str(finalXy)}"].state
            
        grid[f"pad{str(finalXy)}"].color = color
        grid[f"pad{str(finalXy)}"].state = state

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
    for padkey, padvalues in grid.items():
        padXy = int(str(padvalues.x)+str(padvalues.y))
        if main and "9" not in str(padXy):
            lightPad(padXy, color["off"], state["static"])
        elif cc and "9" in str(padXy):
            lightPad(padXy, color["off"], state["static"])

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