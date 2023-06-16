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

import progConst as pc
import progVars as pv
import launchpad as lp

import sys
import time

def bpm():
    bpm = list(str(mixer.getCurrentTempo(1)))
    
    if len(bpm) == 5:
        bpm.pop(4)
        bpm.pop(3)
        bpm[0] = "s" + bpm[0]
    else:
        bpm.pop(3)
        bpm.pop(2)
        bpm.insert(0, "s0")
    
    if mixer.getCurrentTempo(1) != pv.bpm:
        pv.bpm = mixer.getCurrentTempo(1)
        lp.resetLighting()

    lp.lightGroup(lp.character[bpm[0]], lp.color["onahau"], lp.state["static"], 40)
    lp.lightGroup(lp.character[bpm[1]], lp.color["white"], lp.state["static"], 42)
    lp.lightGroup(lp.character[bpm[2]], lp.color["onahau"], lp.state["static"], 45)

    