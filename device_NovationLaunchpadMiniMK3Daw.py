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

import lighting as l

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
        #print(f"{g.grid['pad11']}: {g.grid['pad11'].x} {g.grid['pad11'].y} {g.grid['pad11'].color.value} {g.grid['pad11'].prevColor.value} {g.grid['pad11'].state.value} {g.grid['pad11'].prevState.value} {g.grid['pad11'].type.value}")
        pass

    def OnMidiMsg(self, event):
        event.handled = False
        print('--------------------------------')
        print('midi id:', event.midiId, '| midi status:', event.status, '| midi channel:', event.midiChan, 
        '| midi data1:', event.data1, '| midi data2:', event.data2, '| midi controlNum:', event.controlNum, 
        '| midi controlVal:', event.controlVal, '| midi sysex:', event.sysex)

        #move the midi msg processing to another file
        if event.data2 > 0:
            l.LightPad(event.data1, lp.color["white"], lp.state["static"])
        if event.data2 == 0:
            l.RevertPad(event.data1)
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
