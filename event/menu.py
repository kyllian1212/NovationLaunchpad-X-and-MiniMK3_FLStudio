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
    if e.oldButtonPressed(event) and e.buttonNumber(pc.FLTRANSPORT_MENUPAD, event):
        if not pv.shiftPressed:
            lp.modeChange(pc.FLTRANSPORT_MODE)
        else:
            lp.scrollText("FL Transport Mode", lp.color["white"])