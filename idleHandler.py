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

import idle.mainSidebar as iMainSidebar
import idle.shift as iShift
import idle.menu as iMenu
import idle.flTransport as iFlTransport
import idle.metronome as iMetro
import idle.lpMixer as iLpMixer

import sys
import time

#this is everything that handles displaying on the launchpad
def idleHandler():
    iMainSidebar.mainSidebar()
    iShift.shift()
    iMetro.metronome()

    if pv.mode == pc.MENU_MODE:
        iMenu.menu()
    
    if pv.mode == pc.FLTRANSPORT_MODE:
        iFlTransport.flTransport()
    
    if pv.mode == pc.MIXER_MODE:
        iLpMixer.lpMixer()