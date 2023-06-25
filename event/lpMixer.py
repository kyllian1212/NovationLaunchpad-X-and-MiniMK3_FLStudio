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

import eventHandler as e

import sys
import time

def lpMixer(event):
    if e.buttonPressedCheck(pc.UP_PAD, event):
        if pv.flTrack4+4 <= 125:
            pv.flTrack1 += 4
            pv.flTrack2 += 4
            pv.flTrack3 += 4
            pv.flTrack4 += 4
            if pv.flSelectedTrack != -1:
                pv.flSelectedTrack += 4
    if e.buttonPressedCheck(pc.DOWN_PAD, event):
        if pv.flTrack1-4 >= 1:
            pv.flTrack1 -= 4
            pv.flTrack2 -= 4
            pv.flTrack3 -= 4
            pv.flTrack4 -= 4
            if pv.flSelectedTrack != -1:
                pv.flSelectedTrack -= 4
    if e.buttonPressedCheck(pc.LEFT_PAD, event):
        if pv.flTrack1 > 1:
            pv.flTrack1 -= 1
            pv.flTrack2 -= 1
            pv.flTrack3 -= 1
            pv.flTrack4 -= 1
            if pv.flSelectedTrack != -1:
                pv.flSelectedTrack -= 1
    if e.buttonPressedCheck(pc.RIGHT_PAD, event):
        if pv.flTrack4 < 125:
            pv.flTrack1 += 1
            pv.flTrack2 += 1
            pv.flTrack3 += 1
            pv.flTrack4 += 1
            if pv.flSelectedTrack != -1:
                pv.flSelectedTrack += 1
    
    ui.miDisplayRect(pv.flTrack1, pv.flTrack4, 4000)

    if not pv.altViewMode:
        pv.flSelectedTrack = -1

        if e.buttonPressedCheck(pc.TRACK1_MUTE, event):
            mixer.muteTrack(pv.flTrack1) if not pv.buttonPressed[pc.SHIFT_PAD] else mixer.soloTrack(pv.flTrack1)
        if e.buttonPressedCheck(pc.TRACK2_MUTE, event):
            mixer.muteTrack(pv.flTrack2) if not pv.buttonPressed[pc.SHIFT_PAD] else mixer.soloTrack(pv.flTrack2)
        if e.buttonPressedCheck(pc.TRACK3_MUTE, event):
            mixer.muteTrack(pv.flTrack3) if not pv.buttonPressed[pc.SHIFT_PAD] else mixer.soloTrack(pv.flTrack3)
        if e.buttonPressedCheck(pc.TRACK4_MUTE, event):
            mixer.muteTrack(pv.flTrack4) if not pv.buttonPressed[pc.SHIFT_PAD] else mixer.soloTrack(pv.flTrack4)

        if e.buttonPressedCheck(pc.TRACK1_ARMED, event):
            mixer.armTrack(pv.flTrack1)
        if e.buttonPressedCheck(pc.TRACK2_ARMED, event):
            mixer.armTrack(pv.flTrack2)
        if e.buttonPressedCheck(pc.TRACK3_ARMED, event):
            mixer.armTrack(pv.flTrack3)
        if e.buttonPressedCheck(pc.TRACK4_ARMED, event):
            mixer.armTrack(pv.flTrack4)
    else:
        if e.buttonPressedCheckGroup(11, 82, event):
            pv.flSelectedTrack = pv.flTrack1
        if e.buttonPressedCheckGroup(13, 84, event):
            pv.flSelectedTrack = pv.flTrack2
            pv.flTrack1 += 1
            pv.flTrack2 += 1
            pv.flTrack3 += 1
            pv.flTrack4 += 1
        if e.buttonPressedCheckGroup(15, 86, event):
            pv.flSelectedTrack = pv.flTrack3
            pv.flTrack1 += 2
            pv.flTrack2 += 2
            pv.flTrack3 += 2
            pv.flTrack4 += 2
        if e.buttonPressedCheckGroup(17, 88, event):
            pv.flSelectedTrack = pv.flTrack4
            pv.flTrack1 += 3
            pv.flTrack2 += 3
            pv.flTrack3 += 3
            pv.flTrack4 += 3
    
    
    