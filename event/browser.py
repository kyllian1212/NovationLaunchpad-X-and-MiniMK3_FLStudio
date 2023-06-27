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

def browser(event):
    ui.setFocused(4)

    if e.buttonPressedCheck(pc.UP_PAD, event):
        ui.navigateBrowser(midi.FPT_Up, 0)
    if e.buttonPressedCheck(pc.DOWN_PAD, event):
        ui.navigateBrowser(midi.FPT_Down, 0)
    if e.buttonPressedCheck(pc.LEFT_PAD, event):
        ui.navigateBrowser(midi.FPT_Left, 0)
    if e.buttonPressedCheck(pc.RIGHT_PAD, event):
        ui.navigateBrowser(midi.FPT_Right, 1)