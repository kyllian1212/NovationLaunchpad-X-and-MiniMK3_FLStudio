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

previousMode = 0
maxPatternCount = 0

def lpPatterns(tick):
    global previousMode
    global maxPatternCount
    if not pv.altView1Mode:
        if previousMode == 1:
            lp.resetPartialLighting(11, 98)
            previousMode = 0

        # pattern number
        currentPattern = list(str(patterns.patternNumber()))

        if len(currentPattern) == 1:
            currentPattern.insert(0, "s0")
            currentPattern.insert(1, "0")
        elif len(currentPattern) == 2:
            currentPattern.insert(0, "s0")
        else:
            currentPattern[0] = "s" + currentPattern[0]
        
        if patterns.patternNumber() != pv.patternIndex:
            pvPatternIndex = list(str(pv.patternIndex))

            if len(pvPatternIndex) == 1:
                pvPatternIndex.insert(0, "s0")
                pvPatternIndex.insert(1, "0")
            elif len(pvPatternIndex) == 2:
                pvPatternIndex.insert(0, "s0")
            else:
                pvPatternIndex[0] = "s" + pvPatternIndex[0]

            pv.patternIndex = patterns.patternNumber()
            
            if pvPatternIndex[0] != currentPattern[0]:
                lp.resetPartialLighting(51, 82)
            
            if pvPatternIndex[1] != currentPattern[1]:
                lp.resetPartialLighting(53, 85)
            
            if pvPatternIndex[2] != currentPattern[2]:
                lp.resetPartialLighting(56, 88)
        
        patternColor = lp.rgbColorToPaletteColor(patterns.getPatternColor(patterns.patternNumber()), pc.COLOR_EMPRESS)
        
        lp.lightPredefinedPads(lp.character[currentPattern[0]], patternColor, pc.STATE_STATIC, 40)
        lp.lightPredefinedPads(lp.character[currentPattern[1]], pc.COLOR_WHITE, pc.STATE_STATIC, 42)
        lp.lightPredefinedPads(lp.character[currentPattern[2]], patternColor, pc.STATE_STATIC, 45)

        upArrowColor = patternColor
        if pv.buttonPressed[pc.UP_PAD]:
            upArrowColor = pc.COLOR_WHITE
        if pv.patternIndex == 999:
            upArrowColor = pc.COLOR_OFF
        
        downArrowColor = patternColor
        if pv.buttonPressed[pc.DOWN_PAD]:
            downArrowColor = pc.COLOR_WHITE
        if pv.patternIndex == 1:
            downArrowColor = pc.COLOR_OFF

        lp.lightPad(pc.UP_PAD, upArrowColor, pc.STATE_STATIC)
        lp.lightPad(pc.DOWN_PAD, downArrowColor, pc.STATE_STATIC)

        lp.lightPad(pc.PATTERNNAME_PAD, patternColor, pc.STATE_STATIC)

        patternRenameColor = pc.COLOR_DARK_GRAY if not pv.buttonPressed[pc.PATTERNRENAME_PAD] else pc.COLOR_WHITE

        lp.lightPad(pc.PATTERNRENAME_PAD, patternRenameColor, pc.STATE_STATIC)

        patternCloneColor = pc.COLOR_DARK_YELLOW if not pv.buttonPressed[pc.PATTERNCLONE_PAD] else pc.COLOR_YELLOW

        lp.lightPad(pc.PATTERNCLONE_PAD, patternCloneColor, pc.STATE_STATIC)
    else:
        if previousMode == 0 or maxPatternCount != patterns.patternCount():
            lp.resetPartialLighting(11, 98)
            previousMode = 1

        upArrowColor = pc.COLOR_DARK_GRAY
        if pv.buttonPressed[pc.UP_PAD]:
            upArrowColor = pc.COLOR_WHITE
        if pv.page == 1:
            upArrowColor = pc.COLOR_OFF
        
        downArrowColor = pc.COLOR_DARK_GRAY
        if pv.buttonPressed[pc.DOWN_PAD]:
            downArrowColor = pc.COLOR_WHITE
        if patterns.patternCount() <= 64*pv.page:
            downArrowColor = pc.COLOR_OFF

        lp.lightPad(pc.UP_PAD, upArrowColor, pc.STATE_STATIC)
        lp.lightPad(pc.DOWN_PAD, downArrowColor, pc.STATE_STATIC)

        patternNumber = 1
        loopBreak = False
        if True in pv.buttonPressed: #something like that
            for x in range(8, 0, -1):
                for y in range(1, 9):
                    patternColor = lp.rgbColorToPaletteColor(patterns.getPatternColor(patternNumber), pc.COLOR_EMPRESS)
                    padXy = int(str(x)+str(y))
                    if patternNumber <= patterns.patternCount():
                        lp.lightPad(padXy, patternColor if not patterns.patternNumber() == patternNumber else pc.COLOR_WHITE, pc.STATE_STATIC)
                        patternNumber += 1
                        if patternNumber == 64:
                            maxPatternCount = patterns.patternCount()
                    else:
                        maxPatternCount = patterns.patternCount()
                        loopBreak = True
                        break 
                if loopBreak:
                    break