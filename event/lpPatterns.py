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
    if not pv.altView1Mode:
        if e.buttonPressedCheck(pc.UP_PAD, event):
            patterns.jumpToPattern(patterns.patternNumber()+1) if not pv.buttonPressed[pc.SHIFT_PAD] else patterns.jumpToPattern(patterns.patternNumber()+10)
        if e.buttonPressedCheck(pc.DOWN_PAD, event):
            patterns.jumpToPattern(patterns.patternNumber()-1) if not pv.buttonPressed[pc.SHIFT_PAD] else patterns.jumpToPattern(patterns.patternNumber()-10)

        patternColor = lp.rgbColorToPaletteColor(patterns.getPatternColor(patterns.patternNumber()), pc.COLOR_EMPRESS)

        if e.buttonPressedCheck(pc.PATTERNNAME_PAD, event):
            lp.scrollText(patterns.getPatternName(patterns.patternNumber()), patternColor, 11)
        
        
        if e.buttonPressedCheck(pc.PATTERNRENAME_PAD, event):
            if ui.getFocusedFormCaption() == f"Pattern {patterns.patternNumber()} name":
                ui.enter()
            else:
                try:
                    ui.setFocused(2)
                    patterns.selectPattern(patterns.patternNumber(), 1)
                    transport.globalTransport(midi.FPT_PatternJog, 0)
                    transport.globalTransport(midi.FPT_F2, 1)               
                except:
                    pass
        
        if e.buttonPressedCheck(pc.PATTERNRENAMECANCEL_PAD, event) and ui.getFocusedFormCaption() == f"Pattern {patterns.patternNumber()} name":
            ui.escape()
            
        if e.buttonPressedCheck(pc.PATTERNCLONE_PAD, event):
            patterns.clonePattern(patterns.patternNumber())

    else:
        if e.buttonPressedCheck(pc.UP_PAD, event) and pv.patternPage != 1:
            pv.patternPage -= 1
        if e.buttonPressedCheck(pc.DOWN_PAD, event) and patterns.patternCount() > 64*pv.patternPage:
            pv.patternPage += 1

        patternNumber = (64*(pv.patternPage-1))+1
        for x in range(8, 0, -1):
            for y in range(1, 9):
                padXy = int(str(x)+str(y))
                if e.buttonPressedCheck(padXy, event) and patternNumber <= patterns.patternCount():
                    patterns.jumpToPattern(patternNumber)
                patternNumber += 1