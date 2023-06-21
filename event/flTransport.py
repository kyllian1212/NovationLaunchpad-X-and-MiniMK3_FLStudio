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
        if e.oldButtonPressed(event):
            pv.upPressed = True
            if pv.shiftPressed:
                transport.globalTransport(midi.FPT_TempoJog, 1)
            else:
                transport.globalTransport(midi.FPT_TempoJog, 100)
        else:
            pv.upPressed = False
    
    if e.buttonNumber(pc.DOWN_PAD, event):
        if e.oldButtonPressed(event):
            pv.downPressed = True
            if pv.shiftPressed:
                transport.globalTransport(midi.FPT_TempoJog, -1)
            else:
                transport.globalTransport(midi.FPT_TempoJog, -100)
        else:
            pv.downPressed = False
    
    if e.buttonNumber(pc.LEFT_PAD, event):
        if e.oldButtonPressed(event):
            pv.leftPressed = True
            if pv.shiftPressed:
                pass #until a proper bpm change setting is implemented in fl studio's api
            else:
                transport.globalTransport(midi.FPT_TempoJog, -10)
        else:
            pv.leftPressed = False
    
    if e.buttonNumber(pc.RIGHT_PAD, event):
        if e.oldButtonPressed(event):
            pv.rightPressed = True
            if pv.shiftPressed:
                pass #until a proper bpm change setting is implemented in fl studio's api
            else:
                transport.globalTransport(midi.FPT_TempoJog, 10)
        else:
            pv.rightPressed = False
    
    # metronome
    if e.oldButtonPressed(event) and e.buttonNumber(pc.METRONOME_PAD, event):
        if pv.shiftPressed and ui.isMetronomeEnabled():
            lp.scrollText("Metronome -> Off", lp.color["light_orange"])
        elif pv.shiftPressed and not ui.isMetronomeEnabled():
            lp.scrollText("Metronome -> On", lp.color["light_orange"])
        transport.globalTransport(midi.FPT_Metronome, 1)
    
    # wait for input to start playing
    if e.oldButtonPressed(event) and e.buttonNumber(pc.WAIT_FOR_INPUT_PAD, event):
        if pv.shiftPressed and ui.isStartOnInputEnabled():
            lp.scrollText("Wait for input to start playing -> Off", lp.color["light_orange"], 11)
        elif pv.shiftPressed and not ui.isStartOnInputEnabled():
            lp.scrollText("Wait for input to start playing -> On", lp.color["light_orange"], 11)
        transport.globalTransport(midi.FPT_WaitForInput, 1)

    # countdown before recording
    if e.oldButtonPressed(event) and e.buttonNumber(pc.COUNTDOWN_PAD, event):
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
    if e.oldButtonPressed(event) and e.buttonNumber(pc.OVERDUB_PAD, event):
        if pv.shiftPressed:
            lp.scrollText("Overdub toggled (launchpad indicator not available)", lp.color["white"], 13)
        transport.globalTransport(midi.FPT_Overdub, 1)
        pv.buttonPressed[pc.OVERDUB_PAD] = True
    if not e.oldButtonPressed(event) and e.buttonNumber(pc.OVERDUB_PAD, event):
        pv.buttonPressed[pc.OVERDUB_PAD] = False

    # loop recording
    if e.oldButtonPressed(event) and e.buttonNumber(pc.LOOPRECORDING_PAD, event):
        if pv.shiftPressed and ui.isLoopRecEnabled():
            lp.scrollText("Loop recording -> Off", lp.color["light_orange"], 11)
        elif pv.shiftPressed and not ui.isLoopRecEnabled():
            lp.scrollText("Loop recording -> On", lp.color["light_orange"], 11)
        transport.globalTransport(midi.FPT_LoopRecord, 1)
    
    # step edit
    if e.oldButtonPressed(event) and e.buttonNumber(pc.STEPEDIT_PAD, event):
        if pv.shiftPressed and ui.getStepEditMode():
            lp.scrollText("Step editing mode -> Off", lp.color["light_orange"], 11)
        elif pv.shiftPressed and not ui.getStepEditMode():
            lp.scrollText("Step editing mode -> On", lp.color["light_orange"], 11)
        transport.globalTransport(midi.FPT_StepEdit, 1)
    
    # not available yet
    '''
    if e.buttonPressed(event) and (
        e.buttonNumber(21, event)
        or e.buttonNumber(22, event)
        or e.buttonNumber(24, event)
        or e.buttonNumber(25, event)
    ) and pv.shiftPressed:
        lp.scrollText("Not available", lp.color["red"], 11)
    '''

    # undo/redo
    undoPossible = True if general.getUndoHistoryLast() != general.getUndoHistoryCount()-1 else False
    redoPossible = True if general.getUndoHistoryLast() != 0 else False

    if e.oldButtonPressed(event) and e.buttonNumber(pc.UNDO_PAD, event):
        if pv.shiftPressed:
            lp.scrollText(f"Undone last action", lp.color["red"], 11) if undoPossible else lp.scrollText(f"Nothing to undo", lp.color["red"], 11)
        if undoPossible:
            general.undoUp()
        pv.buttonPressed[pc.UNDO_PAD] = True
    elif not e.oldButtonPressed(event) and e.buttonNumber(pc.UNDO_PAD, event):
        pv.buttonPressed[pc.UNDO_PAD] = False
    
    if e.oldButtonPressed(event) and e.buttonNumber(pc.REDO_PAD, event):
        if pv.shiftPressed:
            lp.scrollText(f"Redone last action", lp.color["green"], 11) if redoPossible else lp.scrollText(f"Nothing to redo", lp.color["green"], 11)
        if redoPossible:
            general.undoDown()
        pv.buttonPressed[pc.REDO_PAD] = True
    elif not e.oldButtonPressed(event) and e.buttonNumber(pc.REDO_PAD, event):
        pv.buttonPressed[pc.REDO_PAD] = False
    
    # tap tempo
    if e.oldButtonPressed(event) and e.buttonNumber(pc.TAPTEMPO_PAD, event):
        if pv.shiftPressed:
            lp.scrollText("Tap tempo", lp.color["light_azure"])
        else:
            transport.globalTransport(midi.FPT_TapTempo, 1)
            pv.buttonPressed[pc.TAPTEMPO_PAD] = True
    elif not e.oldButtonPressed(event) and e.buttonNumber(pc.TAPTEMPO_PAD, event):
        pv.buttonPressed[pc.TAPTEMPO_PAD] = False
    
    # playlist/piano roll/channel rack/mixer/browser window focus
    if e.oldButtonPressed(event) and e.buttonNumber(pc.UICLOSEWINDOW_PAD, event):
        pv.buttonPressed[pc.UICLOSEWINDOW_PAD] = True
    elif not e.oldButtonPressed(event) and e.buttonNumber(pc.UICLOSEWINDOW_PAD, event):
        pv.buttonPressed[pc.UICLOSEWINDOW_PAD] = False

    if e.oldButtonPressed(event) and e.buttonNumber(pc.UIPLAYLIST_PAD, event):
        if pv.shiftPressed:
            lp.scrollText("Playlist window focused", lp.color["light_yellow"], 11)
        if not ui.getVisible(2):
            ui.showWindow(2)
        ui.setFocused(2)
    
    if e.oldButtonPressed(event) and e.buttonNumber(pc.UIPIANOROLL_PAD, event):
        if pv.shiftPressed:
            lp.scrollText("Piano roll window focused", lp.color["light_yellow"], 11)
        if not ui.getVisible(3):
            ui.showWindow(3)
        ui.setFocused(3)
    
    if e.oldButtonPressed(event) and e.buttonNumber(pc.UICHANNELRACK_PAD, event):
        if pv.shiftPressed:
            lp.scrollText("Channel rack window focused", lp.color["light_yellow"], 11)
        if not ui.getVisible(1):
            ui.showWindow(1)
        ui.setFocused(1)
    
    if e.oldButtonPressed(event) and e.buttonNumber(pc.UIMIXER_PAD, event):
        if pv.shiftPressed:
            lp.scrollText("Mixer window focused", lp.color["light_yellow"], 11)
        if not ui.getVisible(0):
            ui.showWindow(0)
        ui.setFocused(0)

    if e.oldButtonPressed(event) and e.buttonNumber(pc.UIBROWSER_PAD, event):
        pv.buttonPressed[pc.UIBROWSER_PAD] = True
        if pv.buttonPressed[pc.UICLOSEWINDOW_PAD]:
            ui.hideWindow(4)
        else:
            if pv.shiftPressed:
                lp.scrollText("Browser focused", lp.color["light_yellow"], 11)
            if not ui.getVisible(4):
                ui.showWindow(4)
            ui.setFocused(4)
    elif not e.oldButtonPressed(event) and e.buttonNumber(pc.UIBROWSER_PAD, event):
        pv.buttonPressed[pc.UIBROWSER_PAD] = False
    
