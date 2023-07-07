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

def lpPatterns(event):
    if e.buttonPressedCheck(pc.UP_PAD, event):
        patterns.jumpToPattern(pv.patternIndex+1) if not pv.buttonPressed[pc.SHIFT_PAD] else patterns.jumpToPattern(pv.patternIndex+10)
    if e.buttonPressedCheck(pc.DOWN_PAD, event):
        patterns.jumpToPattern(pv.patternIndex-1) if not pv.buttonPressed[pc.SHIFT_PAD] else patterns.jumpToPattern(pv.patternIndex-10)

    patternColor = lp.rgbColorToPaletteColor(patterns.getPatternColor(patterns.patternNumber()), pc.COLOR_EMPRESS)

    if e.buttonPressedCheck(pc.PATTERNNAME_PAD, event):
        lp.scrollText(patterns.getPatternName(pv.patternIndex), patternColor, 11)
    
    if e.buttonPressedCheck(pc.PATTERNRENAME_PAD, event):
        try:
            print(ui.getFocusedFormCaption()) # prints the pattern name window !!! :eyes:
            ui.setFocused(2)
            patterns.selectPattern(pv.patternIndex, 1)
            transport.globalTransport(midi.FPT_PatternJog, 0)
            transport.globalTransport(midi.FPT_F2, 1)
            
        except:
            pass
        
    if e.buttonPressedCheck(pc.PATTERNCLONE_PAD, event):
        patterns.clonePattern(pv.patternIndex)
    