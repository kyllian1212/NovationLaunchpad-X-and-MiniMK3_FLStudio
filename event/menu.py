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
    if e.buttonReleasedCheck(pc.FLTRANSPORT_MENUPAD, event):
        lp.modeChange(pc.FLTRANSPORT_MODE) if not pv.buttonPressed[pc.SHIFT_PAD] else lp.scrollText("FL Transport Mode", pc.COLOR_WHITE)
    
    if e.buttonReleasedCheck(pc.MIXER_MENUPAD, event):
        lp.modeChange(pc.MIXER_MODE) if not pv.buttonPressed[pc.SHIFT_PAD] else lp.scrollText("Mixer Mode", pc.COLOR_WHITE)

    if e.buttonReleasedCheck(pc.CHANNELRACK_MENUPAD, event):
        lp.modeChange(pc.CHANNELRACK_MODE) if not pv.buttonPressed[pc.SHIFT_PAD] else lp.scrollText("Channel Rack Mode", pc.COLOR_WHITE)
    
    if e.buttonReleasedCheck(pc.BROWSER_MENUPAD, event):
        lp.modeChange(pc.BROWSER_MODE) if not pv.buttonPressed[pc.SHIFT_PAD] else lp.scrollText("Browser Mode", pc.COLOR_WHITE)
        ui.setFocused(4)
    
    if e.buttonPressedCheck(pc.VERSION_MENUPAD, event):
        lp.scrollText(f"Version -> {pc.VERSION}  Check for updates on FL Studio's MIDI scripting forum", pc.COLOR_AQUA, 11)