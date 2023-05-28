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
color = {}

color["black"] = Color(0, "000000")
color["white"] = Color(3, "ffffff")

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
            grid[f"pad{x}{y}"] = Pad(x, y, color["black"], color["black"], state["static"], state["static"], type["cc"])
        else:
            grid[f"pad{x}{y}"] = Pad(x, y, color["black"], color["black"], state["static"], state["static"], type["main"])

#for padkey, padvalues in grid.items():
#    print(f"{padkey}: {padvalues.x} {padvalues.y} {padvalues.color} {padvalues.state} {padvalues.type}")

def enableDawMode():
    device.midiOutSysex(bytes([240, 0, 32, 41, 2, 13, 16, 1, 247])) #enable daw mode
    device.midiOutSysex(bytes([240, 0, 32, 41, 2, 13, 0, 0, 247])) #switch to session automatically

def disableDawMode():
    device.midiOutSysex(bytes([240, 0, 32, 41, 2, 13, 18, 1, 0, 1, 247])) #daw clear state
    device.midiOutSysex(bytes([240, 0, 32, 41, 2, 13, 16, 0, 247])) #disable daw mode