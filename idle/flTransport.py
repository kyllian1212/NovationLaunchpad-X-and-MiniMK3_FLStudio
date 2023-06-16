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

def flTransport():
    if transport.getLoopMode() == 0:
        lp.lightPad(pc.PATTERN_PAD, lp.color["orange"], lp.state["static"])
    else:
        lp.lightPad(pc.PATTERN_PAD, lp.color["lime_green"], lp.state["static"])

    if transport.isPlaying():
        lp.lightPad(pc.PLAYPAUSE_PAD, lp.color["green"], lp.state["static"])
        lp.lightPad(pc.STOP_PAD, lp.color["red"], lp.state["static"])
    else:
        lp.lightPad(pc.PLAYPAUSE_PAD, lp.color["darker_green"], lp.state["static"])
        if pv.stopPressed == False:
            lp.lightPad(pc.STOP_PAD, lp.color["dark_gray"], lp.state["static"])
        else:
            lp.lightPad(pc.STOP_PAD, lp.color["red"], lp.state["static"])
        
    if transport.isRecording():
        lp.lightPad(pc.RECORD_PAD, lp.color["red"], lp.state["static"])
    else:
        lp.lightPad(pc.RECORD_PAD, lp.color["coral_tree"], lp.state["static"])
