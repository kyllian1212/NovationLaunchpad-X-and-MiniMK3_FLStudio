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

def browser():
    lp.lightPad(pc.UP_PAD, pc.COLOR_DARK_GRAY if not pv.buttonPressed[pc.UP_PAD] else pc.COLOR_WHITE, pc.STATE_STATIC)
    lp.lightPad(pc.DOWN_PAD, pc.COLOR_DARK_GRAY if not pv.buttonPressed[pc.DOWN_PAD] else pc.COLOR_WHITE, pc.STATE_STATIC)
    lp.lightPad(pc.LEFT_PAD, pc.COLOR_DARK_GRAY if not pv.buttonPressed[pc.LEFT_PAD] else pc.COLOR_WHITE, pc.STATE_STATIC)
    lp.lightPad(pc.RIGHT_PAD, pc.COLOR_DARK_GRAY if not pv.buttonPressed[pc.RIGHT_PAD] else pc.COLOR_WHITE, pc.STATE_STATIC)