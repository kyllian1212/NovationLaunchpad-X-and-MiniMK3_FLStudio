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

import idle.mainSideBar as iMainSideBar
import idle.shift as iShift
import idle.menu as iMenu
import idle.bpm as iBpm
import idle.metronome as iMetro

import sys
import time

#this is everything that handles displaying on the launchpad
def idleHandler():
    iMainSideBar.mainSideBar()
    iShift.shift()
    iMetro.metronome()

    if pv.mode == pc.MENU_MODE:
        iMenu.menu()
    
    if pv.mode == pc.BPM_MODE:
        iBpm.bpm()