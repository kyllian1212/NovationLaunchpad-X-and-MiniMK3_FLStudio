# name=Novation Launchpad Mini MK3 Midi
import device

import launchpad as lp

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
        pass

    def OnMidiMsg(self, event):
        event.handled = False
        print('--------------------------------')
        print('midi id:', event.midiId, '| midi status:', event.status, '| midi channel:', event.midiChan, 
        '| midi data1:', event.data1, '| midi data2:', event.data2, '| midi controlNum:', event.controlNum, 
        '| midi controlVal:', event.controlVal, '| midi sysex:', event.sysex)

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
