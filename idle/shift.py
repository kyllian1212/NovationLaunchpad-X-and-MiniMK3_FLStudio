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
    shiftColor = lp.color["dark_gray"] if not pv.buttonPressed[pc.SHIFT_PAD] else lp.color["white"]
    lp.lightPad(pc.SHIFT_PAD, shiftColor, lp.state["static"])
