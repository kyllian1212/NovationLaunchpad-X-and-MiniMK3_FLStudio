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
import idle.lpPatterns as iLpPatterns
import idle.channelRack as iChannelRack
import idle.browser as iBrowser

import sys
import time

#this is everything that handles displaying on the launchpad
def idleHandler(tick):
    iMainSidebar.mainSidebar()
    iShift.shift()
    iMetro.metronome()

    if pv.mode == pc.MENU_MODE:
        iMenu.menu()
    
    if pv.mode == pc.FLTRANSPORT_MODE:
        iFlTransport.flTransport()
    
    if pv.mode == pc.MIXER_MODE:
        iLpMixer.lpMixer()
    
    if pv.mode == pc.CHANNELRACK_MODE:
        iChannelRack.channelRack()

    if pv.mode == pc.PATTERNS_MODE:
        iLpPatterns.lpPatterns(tick)
    
    if pv.mode == pc.BROWSER_MODE:
        iBrowser.browser()

    # pattern queue handler, so that it changes even if not on the pattern menu
    patternLengthDiffCheck = True if pv.patternQueued != -1 and patterns.getPatternLength(pv.patternQueued) != patterns.getPatternLength(patterns.patternNumber()) else False
    patternSwitchNumber = 1 if patternLengthDiffCheck else patterns.getPatternLength(patterns.patternNumber())  
    if transport.isPlaying() and transport.getLoopMode() == 0 and pv.patternQueued != -1 and (16*(transport.getSongPos(3)-1))+transport.getSongPos(4) == patternSwitchNumber:
            patterns.jumpToPattern(pv.patternQueued)
            pv.patternQueued = -1
            pv.patternQueueHandled = False
    elif (not transport.isPlaying() or transport.getLoopMode() == 1) and pv.patternQueued != -1:
        patterns.jumpToPattern(pv.patternQueued)
        pv.patternQueued = -1
        pv.patternQueueHandled = False