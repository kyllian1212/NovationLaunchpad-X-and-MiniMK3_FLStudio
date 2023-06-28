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

def gridSet(flChannelRack: int, lpChannelRack: int):
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

def channelRack(event):
    if not pv.altView1Mode and not pv.altView2Mode:
        
        pass
    elif pv.altView1Mode:
        track = 0
        for x in range(8, 0, -1):
            for y in range(1, 8):
                padXy = int(str(x)+str(y))
                if e.buttonPressedCheck(padXy, event) and channels.channelCount() > track:
                    print(padXy)
                    pv.triggerNote = True
                    event.data1 = 60
                    channels.selectOneChannel(track)
                track += 1
                    