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
    lp.lightPad(pc.FLTRANSPORT_MENUPAD, pc.COLOR_DARK_GRAY if not pv.buttonPressed[pc.FLTRANSPORT_MENUPAD] else pc.COLOR_WHITE, state)
    lp.lightPad(pc.MIXER_MENUPAD, pc.COLOR_DARK_GRAY if not pv.buttonPressed[pc.MIXER_MENUPAD] else pc.COLOR_WHITE, state)
    lp.lightPad(pc.CHANNELRACK_MENUPAD, pc.COLOR_DARK_GRAY if not pv.buttonPressed[pc.CHANNELRACK_MENUPAD] else pc.COLOR_WHITE, state)
    lp.lightPad(pc.PATTERNS_MENUPAD, pc.COLOR_DARK_GRAY if not pv.buttonPressed[pc.PATTERNS_MENUPAD] else pc.COLOR_WHITE, state)
    lp.lightPad(pc.BROWSER_MENUPAD, pc.COLOR_DARK_GRAY if not pv.buttonPressed[pc.BROWSER_MENUPAD] else pc.COLOR_WHITE, state)
    lp.lightPad(pc.VERSION_MENUPAD, pc.COLOR_AQUA, pc.STATE_STATIC)