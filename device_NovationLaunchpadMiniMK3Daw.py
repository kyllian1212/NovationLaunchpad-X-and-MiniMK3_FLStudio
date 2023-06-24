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

import progVars as pv
import progConst as pc
import launchpad as lp

import idleHandler as i
import eventHandler as e

import sys
import time

class DawLaunchpad:
    def __init__(self):
        self.tick = 0
        return
    
    def OnInit(self):
        device.setHasMeters()
        lp.enableDawMode()
        lp.resetLighting(True, True)

    def OnDeInit(self):
        lp.disableDawMode()
    
    def OnIdle(self):
        self.tick += 1
        i.idleHandler()

    def OnMidiMsg(self, event):
        event.handled = False
        print('--------------------------------')
        print('midi id:', event.midiId, '| midi status:', event.status, '| midi channel:', event.midiChan, 
        '| midi data1:', event.data1, '| midi data2:', event.data2, '| midi controlNum:', event.controlNum, 
        '| midi controlVal:', event.controlVal, '| midi sysex:', event.sysex)

        e.eventHandler(event)

        event.handled = True
    
    def OnUpdateMeters(self):
        i.idleHandler()

    def OnDoFullRefresh(self):
        i.idleHandler()
    
    def OnProjectLoad(self, status):
        if status == 0:
            pv.projectLoading = True
            print("load")
        if status == 100 or status == 101:
            pv.projectLoading = False
            print("end")

dawLp = DawLaunchpad()

def OnInit():
    dawLp.OnInit()

def OnDeInit():
    dawLp.OnDeInit()

def OnIdle():
    dawLp.OnIdle()

def OnMidiMsg(event):
    dawLp.OnMidiMsg(event)

def OnUpdateMeters():
    dawLp.OnUpdateMeters()

def OnDoFullRefresh():
    dawLp.OnDoFullRefresh()

def OnProjectLoad(status):
    dawLp.OnProjectLoad(status)