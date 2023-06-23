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

def metronome():
    currentBeat = transport.getSongPos(4)

    beat1_steps = [1, 2]
    beat234_steps = [5, 6, 9, 10, 13, 14]
    
    if currentBeat in beat1_steps and transport.isPlaying():
        if transport.getSongLength(0) == 0 and transport.getLoopMode() == 1:
            lp.lightPad(pc.METRONOME_DISPLAYPAD, pc.COLOR_OFF, pc.STATE_STATIC)
        else:    
            lp.lightPad(pc.METRONOME_DISPLAYPAD, pc.COLOR_LIGHT_ORANGE, pc.STATE_STATIC)
    elif currentBeat in beat234_steps and transport.isPlaying():
        lp.lightPad(pc.METRONOME_DISPLAYPAD, pc.COLOR_DARKER_ORANGE, pc.STATE_STATIC)
    else:
        lp.lightPad(pc.METRONOME_DISPLAYPAD, pc.COLOR_OFF, pc.STATE_STATIC)