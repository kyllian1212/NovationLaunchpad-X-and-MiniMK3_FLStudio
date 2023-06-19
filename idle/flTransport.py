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
        
        if pvBpm[0] != currentBpm[0] or (pv.shiftPressed and pvBpm[3] != currentBpm[3]):
            lp.resetPartialLighting(51, 82)
        
        if pvBpm[1] != currentBpm[1] or (pv.shiftPressed and pvBpm[4] != currentBpm[4]):
            lp.resetPartialLighting(53, 85)
        
        if pvBpm[2] != currentBpm[2] or (pv.shiftPressed and pvBpm[5] != currentBpm[5]):
            lp.resetPartialLighting(56, 88)
        
    if pv.shiftPressed == False:
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

    if not pv.upPressed:
        if not pv.shiftPressed:
            lp.lightPad(pc.UP_PAD, lp.color["dark_gray"], lp.state["static"])
        else:
            lp.lightPad(pc.UP_PAD, lp.color["darker_yellow"], lp.state["static"])
    elif pv.upPressed and not pv.shiftPressed:
        lp.lightPad(pc.UP_PAD, lp.color["white"], lp.state["static"])
    elif pv.upPressed and pv.shiftPressed:
        lp.lightPad(pc.UP_PAD, lp.color["light_yellow"], lp.state["static"])

    if not pv.downPressed:
        if not pv.shiftPressed:
            lp.lightPad(pc.DOWN_PAD, lp.color["dark_gray"], lp.state["static"])
        else:
            lp.lightPad(pc.DOWN_PAD, lp.color["darker_yellow"], lp.state["static"])
    elif pv.downPressed and not pv.shiftPressed:
        lp.lightPad(pc.DOWN_PAD, lp.color["white"], lp.state["static"])
    elif pv.downPressed and pv.shiftPressed:
        lp.lightPad(pc.DOWN_PAD, lp.color["light_yellow"], lp.state["static"])
    
    if not pv.leftPressed:
        if not pv.shiftPressed:
            lp.lightPad(pc.LEFT_PAD, lp.color["darker_azure"], lp.state["static"])
        else:
            lp.lightPad(pc.LEFT_PAD, lp.color["off"], lp.state["static"])
    elif pv.leftPressed and not pv.shiftPressed:
        lp.lightPad(pc.LEFT_PAD, lp.color["light_azure"], lp.state["static"])
    
    if not pv.rightPressed:
        if not pv.shiftPressed:
            lp.lightPad(pc.RIGHT_PAD, lp.color["darker_azure"], lp.state["static"])
        else:
            lp.lightPad(pc.RIGHT_PAD, lp.color["off"], lp.state["static"])
    elif pv.rightPressed and not pv.shiftPressed:
        lp.lightPad(pc.RIGHT_PAD, lp.color["light_azure"], lp.state["static"])
    

    # for fl transport stuff
    state = lp.state["static"] if not pv.shiftPressed else lp.state["pulsing"]

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
    overdubColor = lp.color["red"] if not pv.buttonPressed[pc.OVERDUB_PAD] else lp.color["white"]
    lp.lightPad(pc.OVERDUB_PAD, overdubColor, state)

    # loop recording
    loopRecordingColor = lp.color["darker_orange"] if not ui.isLoopRecEnabled() else lp.color["light_orange"]
    lp.lightPad(pc.LOOPRECORDING_PAD, loopRecordingColor, state)