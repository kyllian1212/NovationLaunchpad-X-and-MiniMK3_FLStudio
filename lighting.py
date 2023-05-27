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

import gridSetup as g

def LightPad(xy: int, color: dict[str, g.Color], state: dict[str, g.State]):
    if "9" in str(xy):
        device.midiOutMsg(state.ccvalue, state.notevalue, xy, color.value)
    else:
        device.midiOutMsg(state.notevalue, state.ccvalue, xy, color.value)
    g.grid[f"pad{str(xy)}"].color = color
    g.grid[f"pad{str(xy)}"].state = state
    