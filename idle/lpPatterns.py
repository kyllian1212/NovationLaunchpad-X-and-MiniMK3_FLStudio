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
patternNumberMain = 0
patternNumberAlt = 0
patternPageAlt = 0

def lpPatterns(tick):
    global previousMode
    global maxPatternCount
    global patternNumberMain
    global patternNumberAlt
    global patternPageAlt

    if not pv.altView1Mode:
        if previousMode == 1:
            lp.resetPartialLighting(11, 98)
            previousMode = 0
            patternNumberMain = 0
            patternNumberAlt = 0
            maxPatternCount = 0
            patternPageAlt = 0

        # pattern number
        currentPattern = list(str(patterns.patternNumber()))

        if len(currentPattern) == 1:
            currentPattern.insert(0, "empty")
            currentPattern.insert(1, "0")
        elif len(currentPattern) == 2:
            currentPattern.insert(0, "empty")
        else:
            currentPattern[0] = "s" + currentPattern[0]
        
        if patterns.patternNumber() != patternNumberMain:
            patternIndex = list(str(patternNumberMain))

            if len(patternIndex) == 1:
                patternIndex.insert(0, "empty")
                patternIndex.insert(1, "0")
            elif len(patternIndex) == 2:
                patternIndex.insert(0, "empty")
            else:
                patternIndex[0] = "s" + patternIndex[0]

            patternNumberMain = patterns.patternNumber()
            
            if patternIndex[0] != currentPattern[0]:
                lp.resetPartialLighting(51, 82)
            
            if patternIndex[1] != currentPattern[1]:
                lp.resetPartialLighting(53, 85)
            
            if patternIndex[2] != currentPattern[2]:
                lp.resetPartialLighting(56, 88)
        
        patternColor = lp.rgbColorToPaletteColor(patterns.getPatternColor(patterns.patternNumber()), pc.COLOR_EMPRESS)
        
        lp.lightPredefinedPads(lp.character[currentPattern[0]], patternColor, pc.STATE_STATIC, 40)
        lp.lightPredefinedPads(lp.character[currentPattern[1]], pc.COLOR_WHITE, pc.STATE_STATIC, 42)
        lp.lightPredefinedPads(lp.character[currentPattern[2]], patternColor, pc.STATE_STATIC, 45)

        upArrowColor = patternColor
        if pv.buttonPressed[pc.UP_PAD]:
            upArrowColor = pc.COLOR_WHITE
        if patterns.patternNumber() == 999:
            upArrowColor = pc.COLOR_OFF
        
        downArrowColor = patternColor
        if pv.buttonPressed[pc.DOWN_PAD]:
            downArrowColor = pc.COLOR_WHITE
        if patterns.patternNumber() == 1:
            downArrowColor = pc.COLOR_OFF

        lp.lightPad(pc.UP_PAD, upArrowColor, pc.STATE_STATIC)
        lp.lightPad(pc.DOWN_PAD, downArrowColor, pc.STATE_STATIC)

        lp.lightPad(pc.PATTERNNAME_PAD, patternColor, pc.STATE_STATIC)

        patternRenameColor = pc.COLOR_DARK_GRAY if not pv.buttonPressed[pc.PATTERNRENAME_PAD] else pc.COLOR_WHITE

        if ui.getFocusedFormCaption() == f"Pattern {patterns.patternNumber()} name":
            lp.lightPad(pc.PATTERNRENAME_PAD, pc.COLOR_GREEN, pc.STATE_PULSING)
            lp.lightPad(pc.PATTERNRENAMECANCEL_PAD, pc.COLOR_RED, pc.STATE_PULSING)
        else:
            lp.lightPad(pc.PATTERNRENAME_PAD, patternRenameColor, pc.STATE_STATIC)
            lp.lightPad(pc.PATTERNRENAMECANCEL_PAD, pc.COLOR_OFF, pc.STATE_PULSING)

        patternCloneColor = pc.COLOR_DARK_YELLOW if not pv.buttonPressed[pc.PATTERNCLONE_PAD] else pc.COLOR_YELLOW

        lp.lightPad(pc.PATTERNCLONE_PAD, patternCloneColor, pc.STATE_STATIC)
    else:
        if previousMode == 0:
            lp.resetPartialLighting(11, 98)
            previousMode = 1
            patternNumberMain = 0
            patternNumberAlt = 0
            maxPatternCount = 0

        upArrowColor = pc.COLOR_DARK_GRAY
        if pv.buttonPressed[pc.UP_PAD]:
            upArrowColor = pc.COLOR_WHITE
        if pv.patternPage == 1:
            upArrowColor = pc.COLOR_OFF
        
        downArrowColor = pc.COLOR_DARK_GRAY
        if pv.buttonPressed[pc.DOWN_PAD]:
            downArrowColor = pc.COLOR_WHITE
        if patterns.patternCount() <= 64*pv.patternPage:
            downArrowColor = pc.COLOR_OFF

        lp.lightPad(pc.UP_PAD, upArrowColor, pc.STATE_STATIC)
        lp.lightPad(pc.DOWN_PAD, downArrowColor, pc.STATE_STATIC)

        patternNumberLoop = (64*(pv.patternPage-1))+1
        if patternPageAlt != pv.patternPage or maxPatternCount != patterns.patternCount() or patternNumberAlt != patterns.patternNumber():
            patternPageAlt = pv.patternPage
            patternNumberAlt = patterns.patternNumber()

            for x in range(8, 0, -1):
                for y in range(1, 9):
                    patternColor = lp.rgbColorToPaletteColor(patterns.getPatternColor(patternNumberLoop), pc.COLOR_EMPRESS)
                    padXy = int(str(x)+str(y))

                    if patternNumberLoop <= patterns.patternCount():
                        lp.lightPad(padXy, patternColor if not patterns.patternNumber() == patternNumberLoop else pc.COLOR_WHITE, pc.STATE_STATIC)
                        if patternNumberLoop == 64*pv.patternPage:
                            maxPatternCount = patterns.patternCount()
                        patternNumberLoop += 1
                    else:
                        maxPatternCount = patterns.patternCount()
                        lp.lightPad(padXy, pc.COLOR_OFF, pc.STATE_STATIC)