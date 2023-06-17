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

def shift(event):
    if e.buttonPressed(event) and e.buttonNumber(pc.SHIFT_PAD, event):
        pv.shiftPressed = True
    elif not e.buttonPressed(event) and e.buttonNumber(pc.SHIFT_PAD, event):
        pv.shiftPressed = False