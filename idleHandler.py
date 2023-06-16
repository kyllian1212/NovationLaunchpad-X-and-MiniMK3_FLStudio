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

import idle.flTransport as iFlT
import idle.shift as iS
import idle.menu as iM
import idle.bpm as iB

import sys
import time

def idleHandler():
    iFlT.flTransport()
    iS.shift()

    if pv.mode == pc.MENU_MODE:
        iM.menu()
    
    if pv.mode == pc.BPM_MODE:
        iB.bpm()