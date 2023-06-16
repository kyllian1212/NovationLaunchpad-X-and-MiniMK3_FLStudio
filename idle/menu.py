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

def menu():
    lp.lightPad(pc.BPM_MENUPAD, lp.color["dark_gray"], lp.state["static"])