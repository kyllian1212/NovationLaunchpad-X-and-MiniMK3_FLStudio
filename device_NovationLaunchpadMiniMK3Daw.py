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

import sys
import time

class Launchpad:
    def __init__(self):
        return
    
    def OnInit(self):
        device.setHasMeters()
        device.midiOutSysex(bytes([240, 0, 32, 41, 2, 13, 16, 1, 247]))

    def OnDeInit(self):
        device.midiOutSysex(bytes([240, 0, 32, 41, 2, 13, 18, 1, 0, 1, 247]))
        device.midiOutSysex(bytes([240, 0, 32, 41, 2, 13, 16, 0, 247]))
    
    def OnMidiMsg(self, event):
        event.handled = False
        print('--------------------------------')
        print('midi id:', event.midiId, '| midi status:', event.status, '| midi channel:', event.midiChan, 
        '| midi data1:', event.data1, '| midi data2:', event.data2, '| midi controlNum:', event.controlNum, 
        '| midi controlVal:', event.controlVal, '| midi sysex:', event.sysex)
        #device.midiOutMsg(state1(normal pad)/state2(CC Pad), state2(CC Pad)/state1(normal pad), pad, color)
        #state1 and state2 need to be set together BUT switches up position depending on which type of pad you set
        #normal pads are the 64 main pads, cc pads are the top/right "setting" pads + novation logo
        #idk why it needs to be set like this but yeah
        #state1: 144 = static, 145 = flash, 146 = pulse
        #state2: 176 = static, 177 = flash, 178 = pulse
        device.midiOutMsg(176, 144, 91, 5)
        device.midiOutMsg(176, 144, 92, 6)
        device.midiOutMsg(176, 144, 93, 5)
        device.midiOutMsg(176, 144, 94, 44)
        device.midiOutMsg(178, 146, 99, 45)
        device.midiOutMsg(178, 146, 89, 24)
        device.midiOutMsg(176, 144, 79, 45)
        device.midiOutMsg(176, 146, 24, 24)
        device.midiOutMsg(146, 176, 24, 24)
        event.handled = True

lp = Launchpad()

def OnInit():
    lp.OnInit()

def OnDeInit():
    lp.OnDeInit()

def OnMidiMsg(event):
    lp.OnMidiMsg(event)
