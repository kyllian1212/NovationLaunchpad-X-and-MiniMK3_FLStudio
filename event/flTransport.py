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

def flTransport(event):
    ''' keeping this as comment bc might see to move in a different file
    if event.data1 == pc.UP_PAD:
        if e.buttonPressed(event):
            pv.upPressed = True
        else:
            pv.upPressed = False
    
    if event.data1 == pc.DOWN_PAD:
        if e.buttonPressed(event):
            pv.downPressed = True
        else:
            pv.downPressed = False
    
    if event.data1 == pc.LEFT_PAD:
        if e.buttonPressed(event):
            pv.leftPressed = True
        else:
            pv.leftPressed = False
    
    if event.data1 == pc.RIGHT_PAD:
        if e.buttonPressed(event):
            pv.rightPressed = True
        else:
            pv.rightPressed = False
    '''

    if e.buttonNumber(pc.UP_PAD, event):
        if e.buttonPressed(event):
            pv.upPressed = True
            if pv.shiftPressed:
                transport.globalTransport(midi.FPT_TempoJog, 1)
            else:
                transport.globalTransport(midi.FPT_TempoJog, 100)
        else:
            pv.upPressed = False
    
    if e.buttonNumber(pc.DOWN_PAD, event):
        if e.buttonPressed(event):
            pv.downPressed = True
            if pv.shiftPressed:
                transport.globalTransport(midi.FPT_TempoJog, -1)
            else:
                transport.globalTransport(midi.FPT_TempoJog, -100)
        else:
            pv.downPressed = False
    
    if e.buttonNumber(pc.LEFT_PAD, event):
        if e.buttonPressed(event):
            pv.leftPressed = True
            if pv.shiftPressed:
                pass #until a proper bpm change setting is implemented in fl studio's api
            else:
                transport.globalTransport(midi.FPT_TempoJog, -10)
        else:
            pv.leftPressed = False
    
    if e.buttonNumber(pc.RIGHT_PAD, event):
        if e.buttonPressed(event):
            pv.rightPressed = True
            if pv.shiftPressed:
                pass #until a proper bpm change setting is implemented in fl studio's api
            else:
                transport.globalTransport(midi.FPT_TempoJog, 10)
        else:
            pv.rightPressed = False
    
    # metronome
    if e.buttonPressed(event) and e.buttonNumber(pc.METRONOME_PAD, event):
        if pv.shiftPressed and ui.isMetronomeEnabled():
            lp.scrollText("Metronome -> Off", lp.color["light_orange"])
        elif pv.shiftPressed and not ui.isMetronomeEnabled():
            lp.scrollText("Metronome -> On", lp.color["light_orange"])
        transport.globalTransport(midi.FPT_Metronome, 1)
    
    # wait for input to start playing
    if e.buttonPressed(event) and e.buttonNumber(pc.WAIT_FOR_INPUT_PAD, event):
        if pv.shiftPressed and ui.isStartOnInputEnabled():
            lp.scrollText("Wait for input to start playing -> Off", lp.color["light_orange"], 11)
        elif pv.shiftPressed and not ui.isStartOnInputEnabled():
            lp.scrollText("Wait for input to start playing -> On", lp.color["light_orange"], 11)
        transport.globalTransport(midi.FPT_WaitForInput, 1)

    # countdown before recording
    if e.buttonPressed(event) and e.buttonNumber(pc.COUNTDOWN_PAD, event):
        if pv.shiftPressed and ui.isPrecountEnabled():
            lp.scrollText("Countdown before recording -> Off", lp.color["light_orange"], 11)
        elif pv.shiftPressed and not ui.isPrecountEnabled():
            lp.scrollText("Countdown before recording -> On", lp.color["light_orange"], 11)
        transport.globalTransport(midi.FPT_CountDown, 1)
    
    # overdub (helper not available rn?)
    '''
    if e.buttonPressed(event) and e.buttonNumber(24, event):
        if pv.shiftPressed and ui.isble():
            lp.scrollText("Overdub -> Off", lp.color["light_orange"])
        elif pv.shiftPressed and not ui.isLoopRecEnabled():
            lp.scrollText("Overdub -> On", lp.color["light_orange"])
        transport.globalTransport(midi.FPT_Overdub, 1)
    '''
    if e.buttonPressed(event) and e.buttonNumber(pc.OVERDUB_PAD, event):
        if pv.shiftPressed:
            lp.scrollText("Overdub toggled (launchpad indicator not available)", lp.color["red"], 13)
        transport.globalTransport(midi.FPT_Overdub, 1)
        pv.buttonPressed[pc.OVERDUB_PAD] = True
    if not e.buttonPressed(event) and e.buttonNumber(pc.OVERDUB_PAD, event):
        pv.buttonPressed[pc.OVERDUB_PAD] = False

    # loop recording
    if e.buttonPressed(event) and e.buttonNumber(pc.LOOPRECORDING_PAD, event):
        if pv.shiftPressed and ui.isLoopRecEnabled():
            lp.scrollText("Loop recording -> Off", lp.color["light_orange"], 11)
        elif pv.shiftPressed and not ui.isLoopRecEnabled():
            lp.scrollText("Loop recording -> On", lp.color["light_orange"], 11)
        transport.globalTransport(midi.FPT_LoopRecord, 1)