# name=Novation Launchpad Mini MK3 Midi
import device

class MidiLaunchpad:
    def __init__(self):
        self.tick = 0
        return
    
    def OnInit(self):
        device.setHasMeters()

    def OnDeInit(self):
        pass
    
    def OnIdle(self):
        self.tick += 1
        pass

    def OnMidiMsg(self, event):
        print('--------------------------------')
        print('midi id:', event.midiId, '| midi status:', event.status, '| midi channel:', event.midiChan, 
        '| midi data1:', event.data1, '| midi data2:', event.data2, '| midi controlNum:', event.controlNum, 
        '| midi controlVal:', event.controlVal, '| midi sysex:', event.sysex)

midiLp = MidiLaunchpad()

def OnInit():
    midiLp.OnInit()

def OnDeInit():
    midiLp.OnDeInit()

def OnIdle():
    midiLp.OnIdle()

def OnMidiMsg(event):
    midiLp.OnMidiMsg(event)
