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

def mainSidebar(event):
    if e.buttonPressedCheck(pc.PATTERN_PAD, event):
        transport.setLoopMode()
    
    if e.buttonPressedCheck(pc.PLAYPAUSE_PAD, event):
        transport.start()

    if e.buttonPressedCheck(pc.STOP_PAD, event):
        transport.stop()

    if e.buttonPressedCheck(pc.RECORD_PAD, event):
        transport.record()

    if e.buttonPressedCheck(pc.RETURN_PAD, event) and pv.mode != pc.MENU_MODE:
        lp.modeChange(pc.MENU_MODE)