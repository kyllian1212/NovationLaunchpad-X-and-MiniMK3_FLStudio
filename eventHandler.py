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

import event.mainSidebar as eMainSidebar
import event.shift as eShift
import event.menu as eMenu
import event.flTransport as eFlTransport

import sys
import time

#this is everything that handles events (inputs etc)
#rewrite this part bc its a mess
def oldButtonPressed(event):
    if event.data2 > 1:
        return True
    elif event.data2 == 0:
        return False
    
def buttonNumber(number: int, event):
    if event.data1 == number:
        return True
    else: 
        return False

def buttonPressed(number: int, event):
    mainPads = []
    for x in range(1, 9):
        for y in range(1, 9):
            mainPads.append(int(str(x)+str(y)))

    if number in mainPads:
        pv.buttonPressed[number] = True if event.data2 > 0 else False
        return pv.buttonPressed[number]
    else:
        return True if event.data2 > 0 else False

def eventHandler(event):
    if pv.textScrolling and oldButtonPressed(event):
        device.midiOutSysex(bytes([240, 0, 32, 41, 2, 13, 7, 247])) #end text scroll if it was ongoing
        pv.textScrolling = False

    eMainSidebar.mainSidebar(event)
    eShift.shift(event)

    if pv.mode == pc.MENU_MODE:
        eMenu.menu(event)
    
    if pv.mode == pc.FLTRANSPORT_MODE:
        eFlTransport.flTransport(event)
    
    '''
    if buttonPressed(event): 
        if event.data1 not in pc.TRANSPORT_PADS and event.data1 not in pc.ARROW_PADS and event.data1 != pc.RETURN_PAD:
            lp.lightPad(event.data1, lp.color["white"], lp.state["static"])
    else:
        lp.revertPad(event.data1)
    '''
