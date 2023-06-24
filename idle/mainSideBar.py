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

def mainSidebar():
    if transport.getLoopMode() == 0:
        lp.lightPad(pc.PATTERN_PAD, pc.COLOR_ORANGE, pc.STATE_STATIC)
    else:
        lp.lightPad(pc.PATTERN_PAD, pc.COLOR_LIME_GREEN, pc.STATE_STATIC)

    if transport.isPlaying():
        lp.lightPad(pc.PLAYPAUSE_PAD, pc.COLOR_GREEN, pc.STATE_STATIC)
        lp.lightPad(pc.STOP_PAD, pc.COLOR_RED, pc.STATE_STATIC)
    else:
        lp.lightPad(pc.PLAYPAUSE_PAD, pc.COLOR_DARKER_GREEN, pc.STATE_STATIC)
        if not pv.buttonPressed[pc.STOP_PAD]:
            lp.lightPad(pc.STOP_PAD, pc.COLOR_DARK_GRAY, pc.STATE_STATIC)
        else:
            lp.lightPad(pc.STOP_PAD, pc.COLOR_RED, pc.STATE_STATIC)
        
    if transport.isRecording():
        lp.lightPad(pc.RECORD_PAD, pc.COLOR_RED, pc.STATE_STATIC)
    else:
        lp.lightPad(pc.RECORD_PAD, pc.COLOR_DARKER_RED, pc.STATE_STATIC)
    
    if pv.mode in pc.MODES:
        lp.lightPad(pc.RETURN_PAD, pc.COLOR_RED, pc.STATE_STATIC)
    else:
        lp.lightPad(pc.RETURN_PAD, pc.COLOR_OFF, pc.STATE_STATIC)
    
    if pv.mode == pc.MIXER_MODE:
        altViewColor = pc.COLOR_DARK_GRAY if not pv.altViewMode else pc.COLOR_WHITE
        lp.lightPad(pc.ALTVIEW_PAD, altViewColor, pc.STATE_STATIC)
    else:
        lp.lightPad(pc.ALTVIEW_PAD, pc.COLOR_OFF, pc.STATE_STATIC)
