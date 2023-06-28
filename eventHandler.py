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
import event.lpMixer as eLpMixer
import event.channelRack as eChannelRack
import event.browser as eBrowser

import sys
import time

#this is everything that handles events (inputs etc)
def buttonPressedCheck(number: int, event):
    if event.data1 == number:
        pv.buttonPressed[number] = True if event.data2 > 0 else False
        return pv.buttonPressed[number]
    else:
        return None

def buttonPressedCheckGroup(xyStart: int, xyEnd: int, event):
    result = False
    for padkey, padvalues in lp.grid.items():
        xStart = int(str(xyStart)[0])
        yStart = int(str(xyStart)[1])
        xEnd = int(str(xyEnd)[0])
        yEnd = int(str(xyEnd)[1])
        padXy = int(str(padvalues.x)+str(padvalues.y))
        if (xStart <= padvalues.x <= xEnd and yStart <= padvalues.y <= yEnd) and not result:
            result = True if buttonPressedCheck(padXy, event) else False
    return result

def anyButtonPressedCheck(event):
    return True if event.data2 > 0 else False

def eventHandler(event):
    if pv.textScrolling and anyButtonPressedCheck(event):
        device.midiOutSysex(bytes([240, 0, 32, 41, 2, 13, 7, 247])) #end text scroll if it was ongoing
        pv.textScrolling = False

    eMainSidebar.mainSidebar(event)
    eShift.shift(event)

    if pv.mode == pc.MENU_MODE:
        eMenu.menu(event)
    
    if pv.mode == pc.FLTRANSPORT_MODE:
        eFlTransport.flTransport(event)

    if pv.mode == pc.MIXER_MODE:
        eLpMixer.lpMixer(event)
    
    if pv.mode == pc.CHANNELRACK_MODE:
        eChannelRack.channelRack(event)
    
    if pv.mode == pc.BROWSER_MODE:
        eBrowser.browser(event)