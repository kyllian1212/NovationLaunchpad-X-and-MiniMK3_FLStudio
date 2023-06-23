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

def shift():
    shiftColor = pc.COLOR_DARK_GRAY if not pv.buttonPressed[pc.SHIFT_PAD] else pc.COLOR_WHITE
    lp.lightPad(pc.SHIFT_PAD, shiftColor, pc.STATE_STATIC)
