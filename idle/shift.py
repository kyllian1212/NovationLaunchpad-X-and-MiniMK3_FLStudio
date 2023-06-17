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
    if not pv.shiftPressed:
        lp.lightPad(pc.SHIFT_PAD, lp.color["dark_gray"], lp.state["static"])
    elif pv.shiftPressed:
        lp.lightPad(pc.SHIFT_PAD, lp.color["white"], lp.state["static"])
