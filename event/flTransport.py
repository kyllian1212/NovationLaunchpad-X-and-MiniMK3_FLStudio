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
    if e.buttonPressedCheck(pc.UP_PAD, event):
        transport.globalTransport(midi.FPT_TempoJog, 1) if pv.buttonPressed[pc.SHIFT_PAD] else transport.globalTransport(midi.FPT_TempoJog, 100)
    
    if e.buttonPressedCheck(pc.DOWN_PAD, event):
        transport.globalTransport(midi.FPT_TempoJog, -1) if pv.buttonPressed[pc.SHIFT_PAD] else transport.globalTransport(midi.FPT_TempoJog, -100)
    
    if e.buttonPressedCheck(pc.LEFT_PAD, event) and not pv.buttonPressed[pc.SHIFT_PAD]:
        #no shift function until something is implemented for 0.01 bpms increments in fl studio's api
        transport.globalTransport(midi.FPT_TempoJog, -10)

    if e.buttonPressedCheck(pc.RIGHT_PAD, event) and not pv.buttonPressed[pc.SHIFT_PAD]:
        #no shift function until something is implemented for 0.01 bpms increments in fl studio's api
        transport.globalTransport(midi.FPT_TempoJog, 10)
    
    # metronome
    if e.buttonPressedCheck(pc.METRONOME_PAD, event):
        if pv.buttonPressed[pc.SHIFT_PAD] and ui.isMetronomeEnabled():
            lp.scrollText("Metronome -> Off", pc.COLOR_LIGHT_ORANGE)
        elif pv.buttonPressed[pc.SHIFT_PAD] and not ui.isMetronomeEnabled():
            lp.scrollText("Metronome -> On", pc.COLOR_LIGHT_ORANGE)
        transport.globalTransport(midi.FPT_Metronome, 1)
    
    # wait for input to start playing
    if e.buttonPressedCheck(pc.WAIT_FOR_INPUT_PAD, event):
        if pv.buttonPressed[pc.SHIFT_PAD] and ui.isStartOnInputEnabled():
            lp.scrollText("Wait for input to start playing -> Off", pc.COLOR_LIGHT_ORANGE, 11)
        elif pv.buttonPressed[pc.SHIFT_PAD] and not ui.isStartOnInputEnabled():
            lp.scrollText("Wait for input to start playing -> On", pc.COLOR_LIGHT_ORANGE, 11)
        transport.globalTransport(midi.FPT_WaitForInput, 1)

    # countdown before recording
    if e.buttonPressedCheck(pc.COUNTDOWN_PAD, event):
        if pv.buttonPressed[pc.SHIFT_PAD] and ui.isPrecountEnabled():
            lp.scrollText("Countdown before recording -> Off", pc.COLOR_LIGHT_ORANGE, 11)
        elif e.buttonPressedCheck(pc.SHIFT_PAD, event) and not ui.isPrecountEnabled():
            lp.scrollText("Countdown before recording -> On", pc.COLOR_LIGHT_ORANGE, 11)
        transport.globalTransport(midi.FPT_CountDown, 1)
    
    # overdub (helper not available rn?)
    '''
    if e.buttonPressedCheck(pc.OVERDUB_PAD, event):
        if pv.buttonPressed[pc.SHIFT_PAD] and (?):
            lp.scrollText("Overdub -> Off", pc.COLOR_LIGHT_ORANGE)
        elif pv.buttonPressed[pc.SHIFT_PAD] and not (?):
            lp.scrollText("Overdub -> On", pc.COLOR_LIGHT_ORANGE)
        transport.globalTransport(midi.FPT_Overdub, 1)
    '''
    if e.buttonPressedCheck(pc.OVERDUB_PAD, event):
        if pv.buttonPressed[pc.SHIFT_PAD]:
            lp.scrollText("Overdub toggled (launchpad indicator not available)", pc.COLOR_WHITE, 13)
        transport.globalTransport(midi.FPT_Overdub, 1)

    # loop recording
    if e.buttonPressedCheck(pc.LOOPRECORDING_PAD, event):
        if pv.buttonPressed[pc.SHIFT_PAD] and ui.isLoopRecEnabled():
            lp.scrollText("Loop recording -> Off", pc.COLOR_LIGHT_ORANGE, 11)
        elif pv.buttonPressed[pc.SHIFT_PAD] and not ui.isLoopRecEnabled():
            lp.scrollText("Loop recording -> On", pc.COLOR_LIGHT_ORANGE, 11)
        transport.globalTransport(midi.FPT_LoopRecord, 1)
    
    # step edit
    if e.buttonPressedCheck(pc.STEPEDIT_PAD, event):
        if pv.buttonPressed[pc.SHIFT_PAD] and ui.getStepEditMode():
            lp.scrollText("Step editing mode -> Off", pc.COLOR_LIGHT_ORANGE, 11)
        elif pv.buttonPressed[pc.SHIFT_PAD] and not ui.getStepEditMode():
            lp.scrollText("Step editing mode -> On", pc.COLOR_LIGHT_ORANGE, 11)
        transport.globalTransport(midi.FPT_StepEdit, 1)

    # undo/redo
    undoPossible = True if general.getUndoHistoryLast() != general.getUndoHistoryCount()-1 else False
    redoPossible = True if general.getUndoHistoryLast() != 0 else False

    if e.buttonPressedCheck(pc.UNDO_PAD, event):
        if pv.buttonPressed[pc.SHIFT_PAD]:
            lp.scrollText(f"Undone last action", pc.COLOR_RED, 11) if undoPossible else lp.scrollText(f"Nothing to undo", pc.COLOR_RED, 11)
        if undoPossible:
            general.undoUp()
    
    if e.buttonPressedCheck(pc.REDO_PAD, event):
        if pv.buttonPressed[pc.SHIFT_PAD]:
            lp.scrollText(f"Redone last action", pc.COLOR_GREEN, 11) if redoPossible else lp.scrollText(f"Nothing to redo", pc.COLOR_GREEN, 11)
        if redoPossible:
            general.undoDown()
    
    # tap tempo
    if e.buttonPressedCheck(pc.TAPTEMPO_PAD, event):
        if pv.buttonPressed[pc.SHIFT_PAD]:
            lp.scrollText("Tap tempo", pc.COLOR_LIGHT_AZURE)
        else:
            transport.globalTransport(midi.FPT_TapTempo, 1)
    
    # playlist/piano roll/channel rack/mixer/browser window focus
    e.buttonPressedCheck(pc.UICLOSEWINDOW_PAD, event)

    if e.buttonPressedCheck(pc.UIPLAYLIST_PAD, event):
        if pv.buttonPressed[pc.UICLOSEWINDOW_PAD]:
            ui.hideWindow(2)
        else:
            if pv.buttonPressed[pc.SHIFT_PAD]:
                lp.scrollText("Playlist window focused", pc.COLOR_LIGHT_YELLOW, 11)
            if not ui.getVisible(2):
                ui.showWindow(2)
            ui.setFocused(2)
        
    if e.buttonPressedCheck(pc.UIPIANOROLL_PAD, event):
        if pv.buttonPressed[pc.UICLOSEWINDOW_PAD]:
            ui.hideWindow(3)
        else:
            if pv.buttonPressed[pc.SHIFT_PAD]:
                lp.scrollText("Piano roll window focused", pc.COLOR_LIGHT_YELLOW, 11)
            if not ui.getVisible(3):
                ui.showWindow(3)
            ui.setFocused(3)
    
    if e.buttonPressedCheck(pc.UICHANNELRACK_PAD, event):
        if pv.buttonPressed[pc.UICLOSEWINDOW_PAD]:
            ui.hideWindow(1)
        else:
            if pv.buttonPressed[pc.SHIFT_PAD]:
                lp.scrollText("Channel rack window focused", pc.COLOR_LIGHT_YELLOW, 11)
            if not ui.getVisible(1):
                ui.showWindow(1)
            ui.setFocused(1)
    
    if e.buttonPressedCheck(pc.UIMIXER_PAD, event):
        if pv.buttonPressed[pc.UICLOSEWINDOW_PAD]:
            ui.hideWindow(0)
        else:
            if pv.buttonPressed[pc.SHIFT_PAD]:
                lp.scrollText("Mixer window focused", pc.COLOR_LIGHT_YELLOW, 11)
            if not ui.getVisible(0):
                ui.showWindow(0)
            ui.setFocused(0)

    if e.buttonPressedCheck(pc.UIBROWSER_PAD, event):
        if pv.buttonPressed[pc.UICLOSEWINDOW_PAD]:
            ui.hideWindow(4)
        else:
            if pv.buttonPressed[pc.SHIFT_PAD]:
                lp.scrollText("Browser focused", pc.COLOR_LIGHT_YELLOW, 11)
            if not ui.getVisible(4):
                ui.showWindow(4)
            ui.setFocused(4)
    
