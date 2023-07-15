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

previousSnap = -1

def flSnap():
    global previousSnap
    
    colorAltCharacter = pc.COLOR_WHITE

    colorBarPad = pc.COLOR_DARK_BLUE
    colorBarSelected = pc.COLOR_BLUE

    colorBeatPad = pc.COLOR_DARKER_TURQUOISE
    colorBeatSelected = pc.COLOR_TURQUOISE

    colorStepPad = pc.COLOR_DARKER_GREEN
    colorStepSelected = pc.COLOR_GREEN

    colorNonePad = pc.COLOR_DARKER_RED
    colorNoneSelected = pc.COLOR_RED

    colorCellPad = pc.COLOR_DARKER_YELLOW
    colorCellSelected = pc.COLOR_YELLOW
    
    colorLinePad = pc.COLOR_DARKER_PURPLE
    colorLineSelected = pc.COLOR_PURPLE

    # no case match right now in fl studio's python version so...
    # writing handler
    if ui.getSnapMode() != previousSnap:
        previousSnap = ui.getSnapMode()
        lp.resetPartialLighting(41, 88)

    if ui.getSnapMode() == 0: # line
        lp.lightPredefinedPads(lp.character["l"], colorLineSelected, pc.STATE_STATIC, 40)
        lp.lightPredefinedPads(lp.character["i"], colorAltCharacter, pc.STATE_STATIC, 42)
        lp.lightPredefinedPads(lp.character["n"], colorLineSelected, pc.STATE_STATIC, 43)
        lp.lightPredefinedPads(lp.character["e"], colorAltCharacter, pc.STATE_STATIC, 46)
    elif ui.getSnapMode() == 1: # cell
        lp.lightPredefinedPads(lp.character["c"], colorCellSelected, pc.STATE_STATIC, 40)
        lp.lightPredefinedPads(lp.character["e"], colorAltCharacter, pc.STATE_STATIC, 42)
        lp.lightPredefinedPads(lp.character["l"], colorCellSelected, pc.STATE_STATIC, 44)
        lp.lightPredefinedPads(lp.character["l"], colorAltCharacter, pc.STATE_STATIC, 46)
    elif ui.getSnapMode() == 3: # none
        lp.lightPredefinedPads(lp.character["n"], colorNoneSelected, pc.STATE_STATIC, 41)
        lp.lightPredefinedPads(lp.character["o"], colorAltCharacter, pc.STATE_STATIC, 45)
    elif pv.stepSnap() or pv.beatSnap(): # step & beat
        color = colorStepSelected if pv.stepSnap() else colorBeatSelected

        if ui.getSnapMode() == 8:
            lp.lightPredefinedPads(lp.character["s"], color, pc.STATE_STATIC, 40)
            lp.lightPredefinedPads(lp.character["t"], colorAltCharacter, pc.STATE_STATIC, 42)
            lp.lightPredefinedPads(lp.character["e"], color, pc.STATE_STATIC, 44)
            lp.lightPredefinedPads(lp.character["p"], colorAltCharacter, pc.STATE_STATIC, 46)
        elif ui.getSnapMode() == 13:
            lp.lightPredefinedPads(lp.character["b"], color, pc.STATE_STATIC, 40)
            lp.lightPredefinedPads(lp.character["e"], colorAltCharacter, pc.STATE_STATIC, 42)
            lp.lightPredefinedPads(lp.character["a"], color, pc.STATE_STATIC, 44)
            lp.lightPredefinedPads(lp.character["t"], colorAltCharacter, pc.STATE_STATIC, 46)
        else:
            lp.lightPredefinedPads(lp.character["1"], color, pc.STATE_STATIC, 40)
            lp.lightPredefinedPads(lp.character["/"], colorAltCharacter, pc.STATE_STATIC, 43)

            if ui.getSnapMode() == 4 or ui.getSnapMode() == 9:
                lp.lightPredefinedPads(lp.character["6"], color, pc.STATE_STATIC, 45)
            elif ui.getSnapMode() == 5 or ui.getSnapMode() == 10:
                lp.lightPredefinedPads(lp.character["4"], color, pc.STATE_STATIC, 45)
            elif ui.getSnapMode() == 6 or ui.getSnapMode() == 11:
                lp.lightPredefinedPads(lp.character["3"], color, pc.STATE_STATIC, 45)
            elif ui.getSnapMode() == 7 or ui.getSnapMode() == 12:
                lp.lightPredefinedPads(lp.character["2"], color, pc.STATE_STATIC, 45)
    elif ui.getSnapMode() == 14: # bar
        lp.lightPredefinedPads(lp.character["b"], colorBarSelected, pc.STATE_STATIC, 40)
        lp.lightPredefinedPads(lp.character["a"], colorAltCharacter, pc.STATE_STATIC, 43)
        lp.lightPredefinedPads(lp.character["r"], colorBarSelected, pc.STATE_STATIC, 46)

    # choice handler
    lp.lightPad(pc.LINE_PAD, colorLineSelected if ui.getSnapMode() == 0 else colorLinePad, pc.STATE_STATIC)
    lp.lightPad(pc.CELL_PAD, colorCellSelected if ui.getSnapMode() == 1 else colorCellPad, pc.STATE_STATIC)
    lp.lightPad(pc.NONE_PAD, colorNoneSelected if ui.getSnapMode() == 3 else colorNonePad, pc.STATE_STATIC)
    lp.lightPad(pc.STEP_PAD, colorStepSelected if pv.stepSnap() else colorStepPad, pc.STATE_STATIC)
    lp.lightPad(pc.BEAT_PAD, colorBeatSelected if pv.beatSnap() else colorBeatPad, pc.STATE_STATIC)
    lp.lightPad(pc.BAR_PAD, colorBarSelected if ui.getSnapMode() == 14 else colorBarPad, pc.STATE_STATIC)

    if pv.beatSnap() or pv.stepSnap():
        colorPad = colorStepPad if pv.stepSnap() else colorBeatPad
        colorSelected = colorStepSelected if pv.stepSnap() else colorBeatSelected

        lp.lightPad(pc.FULL_PAD, colorSelected if ui.getSnapMode() == 8 or ui.getSnapMode() == 13 else colorPad, pc.STATE_STATIC)
        lp.lightPad(pc.HALF_PAD, colorSelected if ui.getSnapMode() == 7 or ui.getSnapMode() == 12 else colorPad, pc.STATE_STATIC)
        lp.lightPad(pc.THIRD_PAD, colorSelected if ui.getSnapMode() == 6 or ui.getSnapMode() == 11 else colorPad, pc.STATE_STATIC)
        lp.lightPad(pc.QUARTER_PAD, colorSelected if ui.getSnapMode() == 5 or ui.getSnapMode() == 10 else colorPad, pc.STATE_STATIC)
        lp.lightPad(pc.SIXTH_PAD, colorSelected if ui.getSnapMode() == 4 or ui.getSnapMode() == 9 else colorPad, pc.STATE_STATIC)
    else:
        lp.resetPartialLighting(pc.FULL_PAD, pc.SIXTH_PAD)