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

import eventHandler as e

import sys
import time

def menu(event):
    if e.buttonPressedCheck(pc.FLTRANSPORT_MENUPAD, event):
        if not pv.buttonPressed[pc.SHIFT_PAD]:
            lp.modeChange(pc.FLTRANSPORT_MODE)
        else:
            lp.scrollText("FL Transport Mode", pc.COLOR_WHITE)