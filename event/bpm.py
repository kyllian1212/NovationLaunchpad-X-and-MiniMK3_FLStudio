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

def bpm(event):
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

    if event.data1 == pc.UP_PAD:
        if e.buttonPressed(event):
            pv.upPressed = True
            if pv.shiftPressed:
                transport.globalTransport(midi.FPT_TempoJog, 1)
            else:
                transport.globalTransport(midi.FPT_TempoJog, 100)
        else:
            pv.upPressed = False
    
    if event.data1 == pc.DOWN_PAD:
        if e.buttonPressed(event):
            pv.downPressed = True
            if pv.shiftPressed:
                transport.globalTransport(midi.FPT_TempoJog, -1)
            else:
                transport.globalTransport(midi.FPT_TempoJog, -100)
        else:
            pv.downPressed = False
    
    if event.data1 == pc.LEFT_PAD:
        if e.buttonPressed(event):
            pv.leftPressed = True
            if pv.shiftPressed:
                pass #until a proper bpm change setting is implemented in fl studio's api
            else:
                transport.globalTransport(midi.FPT_TempoJog, -10)
        else:
            pv.leftPressed = False
    
    if event.data1 == pc.RIGHT_PAD:
        if e.buttonPressed(event):
            pv.rightPressed = True
            if pv.shiftPressed:
                pass #until a proper bpm change setting is implemented in fl studio's api
            else:
                transport.globalTransport(midi.FPT_TempoJog, 10)
        else:
            pv.rightPressed = False