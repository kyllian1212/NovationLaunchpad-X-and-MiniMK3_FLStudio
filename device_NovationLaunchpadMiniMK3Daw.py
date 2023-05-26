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
        eventEdit = event
        eventEdit.status = 178 #flash/static/pulse
        eventEdit.controlNum = 99 #pad
        eventEdit.controlVal = 15 #color
        device.midiOutMsg(145, 177, 81, 5) #flash
        device.midiOutMsg(144, 176, 82, 6) #static
        device.midiOutMsg(146, 178, 83, 7) #pulse
        device.midiOutMsg(144, 176, 84, 75)
        device.midiOutMsg(144, 176, 85, 45)
        device.midiOutMsg(144, 176, 86, 12)
        device.midiOutMsg(144, 176, 87, 54)
        device.midiOutMsg(144, 176, 88, 48)
        device.midiOutMsg(144, 176, 76, 21)
        device.midiOutMsg(144, 176, 92, 45)
        device.directFeedback(eventEdit)
        event.handled = True



lp = Launchpad()

def OnInit():
    lp.OnInit()

def OnDeInit():
    lp.OnDeInit()

def OnMidiMsg(event):
    lp.OnMidiMsg(event)
