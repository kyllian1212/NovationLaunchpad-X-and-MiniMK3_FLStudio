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

    if e.buttonPressedCheck(pc.ALTVIEW1_PAD, event) and (pv.mode == pc.MIXER_MODE or pv.mode == pc.CHANNELRACK_MODE):
        if not pv.altView1Mode:
            pv.altView1Mode = True
            pv.altView2Mode = False
        else: 
            pv.altView1Mode = False
    
    '''
    if e.buttonPressedCheck(pc.ALTVIEW2_PAD, event) and pv.mode == pc.CHANNELRACK_MODE:
        if not pv.altView2Mode:
            pv.altView2Mode = True
            pv.altView1Mode = False
        else:
            pv.altView2Mode = False
    '''

    if e.buttonPressedCheck(pc.RETURN_PAD, event) and pv.mode != pc.MENU_MODE:
        pv.altView1Mode = False
        pv.altView2Mode = False
        lp.modeChange(pc.MENU_MODE)