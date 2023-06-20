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
    if e.buttonNumber(pc.PATTERN_PAD, event):
        if e.buttonPressed(event):
            transport.setLoopMode()
    
    if e.buttonNumber(pc.PLAYPAUSE_PAD, event):
        if e.buttonPressed(event):
            transport.start()

    if e.buttonNumber(pc.STOP_PAD, event):
        if e.buttonPressed(event):
            pv.stopPressed = True
        else:
            pv.stopPressed = False

        transport.stop()

    if e.buttonNumber(pc.RECORD_PAD, event):
        if e.buttonPressed(event):
            transport.record()

    if e.buttonNumber(pc.RETURN_PAD, event) and pv.mode != pc.MENU_MODE:
        if e.buttonPressed(event):
            lp.modeChange(pc.MENU_MODE)