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

def menu():
    state = pc.STATE_STATIC if not pv.buttonPressed[pc.SHIFT_PAD] else pc.STATE_PULSING
    lp.lightPad(pc.FLTRANSPORT_MENUPAD, pc.COLOR_DARK_GRAY, state)
    lp.lightPad(pc.MIXER_MENUPAD, pc.COLOR_DARK_GRAY, state)