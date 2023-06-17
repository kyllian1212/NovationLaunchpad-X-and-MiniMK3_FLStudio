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

def mainSideBar(event):
    if event.data1 == pc.PATTERN_PAD:
        if e.buttonPressed(event):
            transport.setLoopMode()
    
    if event.data1 == pc.PLAYPAUSE_PAD:
        if e.buttonPressed(event):
            transport.start()

    if event.data1 == pc.STOP_PAD:
        if e.buttonPressed(event):
            pv.stopPressed = True
        else:
            pv.stopPressed = False

        transport.stop()

    if event.data1 == pc.RECORD_PAD:
        if e.buttonPressed(event):
            transport.record()

    if event.data1 == pc.RETURN_PAD and pv.mode != pc.MENU_MODE:
        if e.buttonPressed(event):
            lp.modeChange(pc.MENU_MODE)