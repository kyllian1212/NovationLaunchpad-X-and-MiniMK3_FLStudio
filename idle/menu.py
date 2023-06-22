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
    state = lp.state["static"] if not pv.buttonPressed[pc.SHIFT_PAD] else lp.state["pulsing"]
    lp.lightPad(pc.FLTRANSPORT_MENUPAD, lp.color["dark_gray"], state)