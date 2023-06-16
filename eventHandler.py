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

import event.flTransport as eFlT
import event.shift as eS
import event.menu as eM

import sys
import time

def buttonPressed(event):
    if event.data2 > 1:
        return True
    elif event.data2 == 0:
        return False
    
def buttonNumber(number: int, event):
    if event.data1 == number:
        return True
    else: 
        return False

def eventHandler(event):
    eFlT.flTransport(event)
    eS.shift(event)
    eM.menu(event)
    
    if buttonPressed(event): 
        if event.data1 not in pc.TRANSPORT_PADS:
            lp.lightPad(event.data1, lp.color["white"], lp.state["static"])
    else:
        lp.revertPad(event.data1)
