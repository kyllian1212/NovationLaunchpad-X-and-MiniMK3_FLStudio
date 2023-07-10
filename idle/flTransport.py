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

shiftLighting = False

def flTransport():
    global shiftLighting

    # bpm
    currentBpm = list(str(mixer.getCurrentTempo(0)))

    if len(currentBpm) == 6:
        currentBpm[0] = "s" + currentBpm[0]
    else:
        currentBpm.insert(0, "empty")
    currentBpm[3] = "s" + currentBpm[3]
    
    if mixer.getCurrentTempo(1) != pv.bpm:
        pvBpm = list(str(pv.bpm))
        if len(pvBpm) == 6:
            pvBpm[0] = "s" + pvBpm[0]
        else:
            pvBpm.insert(0, "s0")
        pvBpm[3] = "s" + pvBpm[3]
        
        pv.bpm = mixer.getCurrentTempo(0)
        
        if pvBpm[0] != currentBpm[0] or (pv.buttonPressed[pc.SHIFT_PAD] and pvBpm[3] != currentBpm[3]):
            lp.resetPartialLighting(51, 82)
        
        if pvBpm[1] != currentBpm[1] or (pv.buttonPressed[pc.SHIFT_PAD] and pvBpm[4] != currentBpm[4]):
            lp.resetPartialLighting(53, 85)
        
        if pvBpm[2] != currentBpm[2] or (pv.buttonPressed[pc.SHIFT_PAD] and pvBpm[5] != currentBpm[5]):
            lp.resetPartialLighting(56, 88)
        
    if not pv.buttonPressed[pc.SHIFT_PAD]:
        if shiftLighting:
            lp.resetPartialLighting(51, 98)
            shiftLighting = False
        lp.lightPredefinedPads(lp.character[currentBpm[0]], pc.COLOR_LIGHT_AZURE, pc.STATE_STATIC, 40)
        lp.lightPredefinedPads(lp.character[currentBpm[1]], pc.COLOR_WHITE, pc.STATE_STATIC, 42)
        lp.lightPredefinedPads(lp.character[currentBpm[2]], pc.COLOR_LIGHT_AZURE, pc.STATE_STATIC, 45)
    else:
        if not shiftLighting:
            lp.resetPartialLighting(51, 98)
            shiftLighting = True
        lp.lightPredefinedPads(lp.character[currentBpm[3]], pc.COLOR_LIGHT_YELLOW, pc.STATE_STATIC, 40)
        lp.lightPredefinedPads(lp.character[currentBpm[4]], pc.COLOR_WHITE, pc.STATE_STATIC, 42)
        lp.lightPredefinedPads(lp.character[currentBpm[5]], pc.COLOR_LIGHT_YELLOW, pc.STATE_STATIC, 45)

    if not pv.buttonPressed[pc.UP_PAD]:
        if not pv.buttonPressed[pc.SHIFT_PAD]:
            lp.lightPad(pc.UP_PAD, pc.COLOR_DARK_GRAY, pc.STATE_STATIC)
        else:
            lp.lightPad(pc.UP_PAD, pc.COLOR_DARKER_YELLOW, pc.STATE_STATIC)
    elif pv.buttonPressed[pc.UP_PAD] and not pv.buttonPressed[pc.SHIFT_PAD]:
        lp.lightPad(pc.UP_PAD, pc.COLOR_WHITE, pc.STATE_STATIC)
    elif pv.buttonPressed[pc.UP_PAD] and pv.buttonPressed[pc.SHIFT_PAD]:
        lp.lightPad(pc.UP_PAD, pc.COLOR_LIGHT_YELLOW, pc.STATE_STATIC)

    if not pv.buttonPressed[pc.DOWN_PAD]:
        if not pv.buttonPressed[pc.SHIFT_PAD]:
            lp.lightPad(pc.DOWN_PAD, pc.COLOR_DARK_GRAY, pc.STATE_STATIC)
        else:
            lp.lightPad(pc.DOWN_PAD, pc.COLOR_DARKER_YELLOW, pc.STATE_STATIC)
    elif pv.buttonPressed[pc.DOWN_PAD] and not pv.buttonPressed[pc.SHIFT_PAD]:
        lp.lightPad(pc.DOWN_PAD, pc.COLOR_WHITE, pc.STATE_STATIC)
    elif pv.buttonPressed[pc.DOWN_PAD] and pv.buttonPressed[pc.SHIFT_PAD]:
        lp.lightPad(pc.DOWN_PAD, pc.COLOR_LIGHT_YELLOW, pc.STATE_STATIC)
    
    if not pv.buttonPressed[pc.LEFT_PAD]:
        if not pv.buttonPressed[pc.SHIFT_PAD]:
            lp.lightPad(pc.LEFT_PAD, pc.COLOR_DARKER_AZURE, pc.STATE_STATIC)
        else:
            lp.lightPad(pc.LEFT_PAD, pc.COLOR_OFF, pc.STATE_STATIC)
    elif pv.buttonPressed[pc.LEFT_PAD] and not pv.buttonPressed[pc.SHIFT_PAD]:
        lp.lightPad(pc.LEFT_PAD, pc.COLOR_LIGHT_AZURE, pc.STATE_STATIC)
    
    if not pv.buttonPressed[pc.RIGHT_PAD]:
        if not pv.buttonPressed[pc.SHIFT_PAD]:
            lp.lightPad(pc.RIGHT_PAD, pc.COLOR_DARKER_AZURE, pc.STATE_STATIC)
        else:
            lp.lightPad(pc.RIGHT_PAD, pc.COLOR_OFF, pc.STATE_STATIC)
    elif pv.buttonPressed[pc.RIGHT_PAD] and not pv.buttonPressed[pc.SHIFT_PAD]:
        lp.lightPad(pc.RIGHT_PAD, pc.COLOR_LIGHT_AZURE, pc.STATE_STATIC)
    

    # for fl transport stuff
    state = pc.STATE_STATIC if not pv.buttonPressed[pc.SHIFT_PAD] else pc.STATE_PULSING

    # metronome
    metronomeColor = pc.COLOR_DARKER_ORANGE if not ui.isMetronomeEnabled() else pc.COLOR_LIGHT_ORANGE
    lp.lightPad(pc.METRONOME_PAD, metronomeColor, state)

    # wait for input to start playing
    waitForInputColor = pc.COLOR_DARKER_ORANGE if not ui.isStartOnInputEnabled() else pc.COLOR_LIGHT_ORANGE
    lp.lightPad(pc.WAIT_FOR_INPUT_PAD, waitForInputColor, state)
    
    # countdown before recording
    countdownColor = pc.COLOR_DARKER_ORANGE if not ui.isPrecountEnabled() else pc.COLOR_LIGHT_ORANGE
    lp.lightPad(pc.COUNTDOWN_PAD, countdownColor, state)
    
    # overdub (helper not available rn?)
    '''
    overdubColor = pc.COLOR_DARKER_ORANGE if not (overdub?) else pc.COLOR_LIGHT_ORANGE:
    lp.lightPad(pc.OVERDUB_PAD, overdubColor, state)
    '''
    overdubColor = pc.COLOR_DARK_GRAY if not pv.buttonPressed[pc.OVERDUB_PAD] else pc.COLOR_WHITE
    lp.lightPad(pc.OVERDUB_PAD, overdubColor, state)

    # loop recording
    loopRecordingColor = pc.COLOR_DARKER_ORANGE if not ui.isLoopRecEnabled() else pc.COLOR_LIGHT_ORANGE
    lp.lightPad(pc.LOOPRECORDING_PAD, loopRecordingColor, state)

    # step edit mode
    stepEditColor = pc.COLOR_DARKER_ORANGE if not ui.getStepEditMode() else pc.COLOR_LIGHT_ORANGE
    lp.lightPad(pc.STEPEDIT_PAD, stepEditColor, state)

    # rest with no feature
    '''
    lp.lightPad(21, pc.COLOR_DARK_GRAY, state)
    lp.lightPad(22, pc.COLOR_DARK_GRAY, state)
    lp.lightPad(24, pc.COLOR_DARK_GRAY, state)
    lp.lightPad(25, pc.COLOR_DARK_GRAY, state)
    '''

    # undo/redo
    undoPossible = True if general.getUndoHistoryLast() != general.getUndoHistoryCount()-1 else False
    redoPossible = True if general.getUndoHistoryLast() != 0 else False

    undoColor = pc.COLOR_RED if undoPossible else pc.COLOR_DARK_GRAY 
    if pv.buttonPressed[pc.UNDO_PAD]:
         undoColor = pc.COLOR_WHITE  
    
    redoColor = pc.COLOR_GREEN if redoPossible else pc.COLOR_DARK_GRAY 
    if pv.buttonPressed[pc.REDO_PAD]:
         redoColor = pc.COLOR_WHITE

    lp.lightPad(pc.UNDO_PAD, undoColor, state)
    lp.lightPad(pc.REDO_PAD, redoColor, state)

    # tap tempo
    tapTempoColor = pc.COLOR_DARKER_AZURE if not pv.buttonPressed[pc.TAPTEMPO_PAD] else pc.COLOR_LIGHT_AZURE
    lp.lightPad(pc.TAPTEMPO_PAD, tapTempoColor, state)

    # playlist/piano roll/channel rack/mixer/browser window focus
    closeWindowColor = pc.COLOR_DARKER_RED if not pv.buttonPressed[pc.UICLOSEWINDOW_PAD] else pc.COLOR_RED
    lp.lightPad(pc.UICLOSEWINDOW_PAD, closeWindowColor, pc.STATE_STATIC)

    playlistColor = pc.COLOR_DARKER_YELLOW if not ui.getFocused(2) else pc.COLOR_LIGHT_YELLOW
    if not ui.getVisible(2):
        playlistColor = pc.COLOR_DARK_GRAY
    if pv.buttonPressed[pc.UICLOSEWINDOW_PAD] and ui.getVisible(2):
        playlistColor = pc.COLOR_RED if not ui.getFocused(2) else pc.COLOR_LIGHT_RED
    
    pianoRollColor = pc.COLOR_DARKER_YELLOW if not ui.getFocused(3) else pc.COLOR_LIGHT_YELLOW
    if not ui.getVisible(3):
        pianoRollColor = pc.COLOR_DARK_GRAY
    if pv.buttonPressed[pc.UICLOSEWINDOW_PAD] and ui.getVisible(3):
        pianoRollColor = pc.COLOR_RED if not ui.getFocused(3) else pc.COLOR_LIGHT_RED
    
    channelRackColor = pc.COLOR_DARKER_YELLOW if not ui.getFocused(1) else pc.COLOR_LIGHT_YELLOW
    if not ui.getVisible(1):
        channelRackColor = pc.COLOR_DARK_GRAY
    if pv.buttonPressed[pc.UICLOSEWINDOW_PAD] and ui.getVisible(1):
        channelRackColor = pc.COLOR_RED if not ui.getFocused(1) else pc.COLOR_LIGHT_RED
    
    mixerColor = pc.COLOR_DARKER_YELLOW if not ui.getFocused(0) else pc.COLOR_LIGHT_YELLOW
    if not ui.getVisible(0):
        mixerColor = pc.COLOR_DARK_GRAY
    if pv.buttonPressed[pc.UICLOSEWINDOW_PAD] and ui.getVisible(0):
        mixerColor = pc.COLOR_RED if not ui.getFocused(0) else pc.COLOR_LIGHT_RED
    
    browserColor = pc.COLOR_DARKER_YELLOW if not ui.getFocused(4) else pc.COLOR_LIGHT_YELLOW
    if not ui.getVisible(4):
        browserColor = pc.COLOR_DARK_GRAY
    if pv.buttonPressed[pc.UICLOSEWINDOW_PAD] and ui.getVisible(4):
        browserColor = pc.COLOR_RED if not ui.getFocused(4) else pc.COLOR_LIGHT_RED
        

    lp.lightPad(pc.UIPLAYLIST_PAD, playlistColor, state)
    lp.lightPad(pc.UIPIANOROLL_PAD, pianoRollColor, state)
    lp.lightPad(pc.UICHANNELRACK_PAD, channelRackColor, state)
    lp.lightPad(pc.UIMIXER_PAD, mixerColor, state)
    lp.lightPad(pc.UIBROWSER_PAD, browserColor, state)