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
        currentBpm.insert(0, "s0")
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
        lp.lightGroup(lp.character[currentBpm[0]], lp.color["light_azure"], lp.state["static"], 40)
        lp.lightGroup(lp.character[currentBpm[1]], lp.color["white"], lp.state["static"], 42)
        lp.lightGroup(lp.character[currentBpm[2]], lp.color["light_azure"], lp.state["static"], 45)
    else:
        if not shiftLighting:
            lp.resetPartialLighting(51, 98)
            shiftLighting = True
        lp.lightGroup(lp.character[currentBpm[3]], lp.color["light_yellow"], lp.state["static"], 40)
        lp.lightGroup(lp.character[currentBpm[4]], lp.color["white"], lp.state["static"], 42)
        lp.lightGroup(lp.character[currentBpm[5]], lp.color["light_yellow"], lp.state["static"], 45)

    if not pv.buttonPressed[pc.UP_PAD]:
        if not pv.buttonPressed[pc.SHIFT_PAD]:
            lp.lightPad(pc.UP_PAD, lp.color["dark_gray"], lp.state["static"])
        else:
            lp.lightPad(pc.UP_PAD, lp.color["darker_yellow"], lp.state["static"])
    elif pv.buttonPressed[pc.UP_PAD] and not pv.buttonPressed[pc.SHIFT_PAD]:
        lp.lightPad(pc.UP_PAD, lp.color["white"], lp.state["static"])
    elif pv.buttonPressed[pc.UP_PAD] and pv.buttonPressed[pc.SHIFT_PAD]:
        lp.lightPad(pc.UP_PAD, lp.color["light_yellow"], lp.state["static"])

    if not pv.buttonPressed[pc.DOWN_PAD]:
        if not pv.buttonPressed[pc.SHIFT_PAD]:
            lp.lightPad(pc.DOWN_PAD, lp.color["dark_gray"], lp.state["static"])
        else:
            lp.lightPad(pc.DOWN_PAD, lp.color["darker_yellow"], lp.state["static"])
    elif pv.buttonPressed[pc.DOWN_PAD] and not pv.buttonPressed[pc.SHIFT_PAD]:
        lp.lightPad(pc.DOWN_PAD, lp.color["white"], lp.state["static"])
    elif pv.buttonPressed[pc.DOWN_PAD] and pv.buttonPressed[pc.SHIFT_PAD]:
        lp.lightPad(pc.DOWN_PAD, lp.color["light_yellow"], lp.state["static"])
    
    if not pv.buttonPressed[pc.LEFT_PAD]:
        if not pv.buttonPressed[pc.SHIFT_PAD]:
            lp.lightPad(pc.LEFT_PAD, lp.color["darker_azure"], lp.state["static"])
        else:
            lp.lightPad(pc.LEFT_PAD, lp.color["off"], lp.state["static"])
    elif pv.buttonPressed[pc.LEFT_PAD] and not pv.buttonPressed[pc.SHIFT_PAD]:
        lp.lightPad(pc.LEFT_PAD, lp.color["light_azure"], lp.state["static"])
    
    if not pv.buttonPressed[pc.RIGHT_PAD]:
        if not pv.buttonPressed[pc.SHIFT_PAD]:
            lp.lightPad(pc.RIGHT_PAD, lp.color["darker_azure"], lp.state["static"])
        else:
            lp.lightPad(pc.RIGHT_PAD, lp.color["off"], lp.state["static"])
    elif pv.buttonPressed[pc.RIGHT_PAD] and not pv.buttonPressed[pc.SHIFT_PAD]:
        lp.lightPad(pc.RIGHT_PAD, lp.color["light_azure"], lp.state["static"])
    

    # for fl transport stuff
    state = lp.state["static"] if not pv.buttonPressed[pc.SHIFT_PAD] else lp.state["pulsing"]

    # metronome
    metronomeColor = lp.color["darker_orange"] if not ui.isMetronomeEnabled() else lp.color["light_orange"]
    lp.lightPad(pc.METRONOME_PAD, metronomeColor, state)

    # wait for input to start playing
    waitForInputColor = lp.color["darker_orange"] if not ui.isStartOnInputEnabled() else lp.color["light_orange"]
    lp.lightPad(pc.WAIT_FOR_INPUT_PAD, waitForInputColor, state)
    
    # countdown before recording
    countdownColor = lp.color["darker_orange"] if not ui.isPrecountEnabled() else lp.color["light_orange"]
    lp.lightPad(pc.COUNTDOWN_PAD, countdownColor, state)
    
    # overdub (helper not available rn?)
    '''
    overdubColor = lp.color["darker_orange"] if not (overdub?) else lp.color["light_orange"]:
    lp.lightPad(pc.OVERDUB_PAD, overdubColor, state)
    '''
    overdubColor = lp.color["dark_gray"] if not pv.buttonPressed[pc.OVERDUB_PAD] else lp.color["white"]
    lp.lightPad(pc.OVERDUB_PAD, overdubColor, state)

    # loop recording
    loopRecordingColor = lp.color["darker_orange"] if not ui.isLoopRecEnabled() else lp.color["light_orange"]
    lp.lightPad(pc.LOOPRECORDING_PAD, loopRecordingColor, state)

    # step edit mode
    stepEditColor = lp.color["darker_orange"] if not ui.getStepEditMode() else lp.color["light_orange"]
    lp.lightPad(pc.STEPEDIT_PAD, stepEditColor, state)

    # rest with no feature
    '''
    lp.lightPad(21, lp.color["dark_gray"], state)
    lp.lightPad(22, lp.color["dark_gray"], state)
    lp.lightPad(24, lp.color["dark_gray"], state)
    lp.lightPad(25, lp.color["dark_gray"], state)
    '''

    # undo/redo
    undoPossible = True if general.getUndoHistoryLast() != general.getUndoHistoryCount()-1 else False
    redoPossible = True if general.getUndoHistoryLast() != 0 else False

    undoColor = lp.color["red"] if undoPossible else lp.color["dark_gray"] 
    if pv.buttonPressed[pc.UNDO_PAD]:
         undoColor = lp.color["white"]  
    
    redoColor = lp.color["darker_green"] if redoPossible else lp.color["dark_gray"] 
    if pv.buttonPressed[pc.REDO_PAD]:
         redoColor = lp.color["white"]

    lp.lightPad(pc.UNDO_PAD, undoColor, state)
    lp.lightPad(pc.REDO_PAD, redoColor, state)

    # tap tempo
    tapTempoColor = lp.color["darker_azure"] if not pv.buttonPressed[pc.TAPTEMPO_PAD] else lp.color["light_azure"]
    lp.lightPad(pc.TAPTEMPO_PAD, tapTempoColor, state)

    # playlist/piano roll/channel rack/mixer/browser window focus
    closeWindowColor = lp.color["darker_red"] if not pv.buttonPressed[pc.UICLOSEWINDOW_PAD] else lp.color["red"]
    lp.lightPad(pc.UICLOSEWINDOW_PAD, closeWindowColor, lp.state["static"])

    playlistColor = lp.color["darker_yellow"] if not ui.getFocused(2) else lp.color["light_yellow"]
    if not ui.getVisible(2):
        playlistColor = lp.color["dark_gray"]
    
    pianoRollColor = lp.color["darker_yellow"] if not ui.getFocused(3) else lp.color["light_yellow"]
    if not ui.getVisible(3):
        pianoRollColor = lp.color["dark_gray"]
    
    channelRackColor = lp.color["darker_yellow"] if not ui.getFocused(1) else lp.color["light_yellow"]
    if not ui.getVisible(1):
        channelRackColor = lp.color["dark_gray"]
    
    mixerColor = lp.color["darker_yellow"] if not ui.getFocused(0) else lp.color["light_yellow"]
    if not ui.getVisible(0):
        mixerColor = lp.color["dark_gray"]
    
    browserColor = lp.color["darker_yellow"] if not ui.getFocused(4) else lp.color["light_yellow"]
    if not ui.getVisible(4):
        browserColor = lp.color["dark_gray"]
    if pv.buttonPressed[pc.UICLOSEWINDOW_PAD] and pv.buttonPressed[pc.UIBROWSER_PAD]:
        browserColor = lp.color["red"]

    lp.lightPad(pc.UIPLAYLIST_PAD, playlistColor, state)
    lp.lightPad(pc.UIPIANOROLL_PAD, pianoRollColor, state)
    lp.lightPad(pc.UICHANNELRACK_PAD, channelRackColor, state)
    lp.lightPad(pc.UIMIXER_PAD, mixerColor, state)
    lp.lightPad(pc.UIBROWSER_PAD, browserColor, state)