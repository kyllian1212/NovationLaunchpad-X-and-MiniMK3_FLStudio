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

def gridSet(flChannelRack: int, lpChannelRack: int, event):
    if lpChannelRack == 1:
        rack_sequencer = pc.CHANNELRACK1_SEQUENCER
    elif lpChannelRack == 2:
        rack_sequencer = pc.CHANNELRACK2_SEQUENCER
    elif lpChannelRack == 3:
        rack_sequencer = pc.CHANNELRACK3_SEQUENCER
    elif lpChannelRack == 4:
        rack_sequencer = pc.CHANNELRACK4_SEQUENCER
    else:
        raise Exception("invalid lpChannelRack number")
    
    p = (16*(pv.page-1))+0
    for gridStep in rack_sequencer:
        if e.buttonPressedCheck(gridStep, event):
            channels.setGridBit(flChannelRack, p, True) if not channels.getGridBit(flChannelRack, p) else channels.setGridBit(flChannelRack, p, False)
        p += 1

def channelRack(event):
    if not pv.altView1Mode and not pv.altView2Mode:
        ui.crDisplayRect(16*(pv.page-1), pv.flChannelRack1, 16, 4, 4000, 0)

        if e.buttonPressedCheckGroup(71, 88, event):
            gridSet(pv.flChannelRack1, 1, event)
        elif e.buttonPressedCheckGroup(51, 68, event):
            gridSet(pv.flChannelRack2, 2, event)
        elif e.buttonPressedCheckGroup(31, 48, event):
            gridSet(pv.flChannelRack3, 3, event)
        elif e.buttonPressedCheckGroup(11, 28, event):
            gridSet(pv.flChannelRack4, 4, event)
        
        if e.buttonPressedCheck(pc.UP_PAD, event):
            if pv.flChannelRack1 != 0 and not pv.buttonPressed[pc.SHIFT_PAD]:
                pv.flChannelRack1 -= 1
                pv.flChannelRack2 -= 1
                pv.flChannelRack3 -= 1
                pv.flChannelRack4 -= 1
            elif pv.flChannelRack1 > 3 and pv.buttonPressed[pc.SHIFT_PAD]:
                pv.flChannelRack1 -= 4
                pv.flChannelRack2 -= 4
                pv.flChannelRack3 -= 4
                pv.flChannelRack4 -= 4
        if e.buttonPressedCheck(pc.DOWN_PAD, event):
            if pv.flChannelRack4+1 < channels.channelCount() and not pv.buttonPressed[pc.SHIFT_PAD]:
                pv.flChannelRack1 += 1
                pv.flChannelRack2 += 1
                pv.flChannelRack3 += 1
                pv.flChannelRack4 += 1
            elif pv.flChannelRack4+4 < channels.channelCount() and pv.buttonPressed[pc.SHIFT_PAD]:
                pv.flChannelRack1 += 4
                pv.flChannelRack2 += 4
                pv.flChannelRack3 += 4
                pv.flChannelRack4 += 4
        if e.buttonPressedCheck(pc.LEFT_PAD, event):
            if pv.page > 1 and not pv.buttonPressed[pc.SHIFT_PAD]:
                pv.page -= 1
            elif pv.page > 1 and pv.buttonPressed[pc.SHIFT_PAD]:
                pv.page = 1
        if e.buttonPressedCheck(pc.RIGHT_PAD, event):
            if pv.page < 65 and not pv.buttonPressed[pc.SHIFT_PAD]:
                pv.page += 1
            elif pv.page < 65 and pv.buttonPressed[pc.SHIFT_PAD]:
                pv.page = 65

        print(pv.page)

    elif pv.altView1Mode:
        track = 0
        for x in range(8, 0, -1):
            for y in range(1, 9):
                padXy = int(str(x)+str(y))
                if e.buttonPressedCheck(padXy, event) and channels.channelCount() > track:
                    pv.triggerNote = True
                    event.data1 = 60
                    channels.selectOneChannel(track)
                elif e.buttonReleasedCheck(padXy, event) and channels.channelCount() > track:
                    pv.triggerNote = True
                    event.data1 = 60
                track += 1
                    