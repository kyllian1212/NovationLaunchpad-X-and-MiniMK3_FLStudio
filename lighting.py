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

import launchpad as lp

def LightPad(xy: int, color: dict[str, lp.Color], state: dict[str, lp.State], revertToPrev: bool = True):
    if "9" in str(xy):
        device.midiOutMsg(state.ccValue, 0, xy, color.value)
    else:
        device.midiOutMsg(state.noteValue, 0, xy, color.value)
    
    if revertToPrev:
        lp.grid[f"pad{str(xy)}"].prevColor = lp.grid[f"pad{str(xy)}"].color
        lp.grid[f"pad{str(xy)}"].prevState = lp.grid[f"pad{str(xy)}"].state
        
    lp.grid[f"pad{str(xy)}"].color = color
    lp.grid[f"pad{str(xy)}"].state = state

def RevertPad(xy: int):
    prevState = lp.grid[f"pad{str(xy)}"].prevState
    prevColor = lp.grid[f"pad{str(xy)}"].prevColor

    if "9" in str(xy):
        device.midiOutMsg(prevState.ccValue, 0, xy, prevColor.value)
    else:
        device.midiOutMsg(prevState.noteValue, 0, xy, prevColor.value)
    
    lp.grid[f"pad{str(xy)}"].color = prevColor
    lp.grid[f"pad{str(xy)}"].state = prevState

def ResetLighting(main: bool = True, cc: bool = False):
    for padkey, padvalues in lp.grid:
        device.midiOutMsg(lp.state["static"].noteValue, 0, padvalues.xy, lp.color["black"].value)
        device.midiOutMsg(lp.state["static"].ccValue, 0, padvalues.xy, lp.color["black"].value)
