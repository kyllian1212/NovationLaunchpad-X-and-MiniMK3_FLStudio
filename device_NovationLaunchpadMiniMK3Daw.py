# name=Novation Launchpad Mini MK3 Daw
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

import launchpad as lp

import idleHandler as i

import sys
import time

class DawLaunchpad:
    def __init__(self):
        self.tick = 0
        return
    
    def OnInit(self):
        device.setHasMeters()
        lp.enableDawMode()

    def OnDeInit(self):
        lp.disableDawMode()
    
    def OnIdle(self):
        self.tick += 1
        lp.lightPad(11, lp.rgbColorToPaletteColor(mixer.getTrackColor(1)), lp.state["static"])
        i.idleHandler()
        pass

    def OnMidiMsg(self, event):
        event.handled = False
        print('--------------------------------')
        print('midi id:', event.midiId, '| midi status:', event.status, '| midi channel:', event.midiChan, 
        '| midi data1:', event.data1, '| midi data2:', event.data2, '| midi controlNum:', event.controlNum, 
        '| midi controlVal:', event.controlVal, '| midi sysex:', event.sysex)

        #move the midi msg processing to another file
        if event.data2 > 0:
            #lp.lightPad(event.data1, lp.color["white"], lp.state["static"])
            #lp.lightAllPadsTest()
            lp.lightPad(99, lp.color["white"], lp.state["flashing"])
            #lp.rgbColorToPaletteColor(0x1F54E8)
        #if event.data2 == 0:
            #lp.revertPad(event.data1)

        event.handled = True

dlp = DawLaunchpad()

def OnInit():
    dlp.OnInit()

def OnDeInit():
    dlp.OnDeInit()

def OnIdle():
    dlp.OnIdle()

def OnMidiMsg(event):
    dlp.OnMidiMsg(event)
