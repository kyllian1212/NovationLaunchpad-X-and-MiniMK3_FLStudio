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

import sys
import time

lightingReset = 0

def grid(flChannelRack: int, lpChannelRack: int):
    color = None
    noChannel = False
    
    try:
        color = lp.rgbColorToPaletteColor(channels.getChannelColor(flChannelRack))
    except:
        noChannel = True

    songPosFormula = (16*(transport.getSongPos(3)-1))+transport.getSongPos(4)

    playColor = pc.COLOR_GREEN
    playGridColor = pc.COLOR_LIGHT_GREEN

    # no match case because fl studio's python is 3.9
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

    if noChannel:
        lp.resetPartialLighting(rack_sequencer[8], rack_sequencer[7])
    else:
        p = (16*(pv.page-1))+0
        for pad1 in rack_sequencer:
            if channels.getGridBit(flChannelRack, p):
                if transport.isPlaying() and transport.getLoopMode() == 0 and p+1 == songPosFormula:          
                    lp.lightPad(pad1, playGridColor, pc.STATE_STATIC)
                else:
                    lp.lightPad(pad1, pc.COLOR_WHITE, pc.STATE_STATIC if color is not pc.COLOR_WHITE else pc.STATE_PULSING)
            else:
                if transport.isPlaying() and transport.getLoopMode() == 0 and p+1 == songPosFormula:
                    lp.lightPad(pad1, playColor, pc.STATE_STATIC)
                else:
                    lp.lightPad(pad1, color, pc.STATE_STATIC)
            p += 1


def channelRack():
    global lightingReset

    if not pv.altView1Mode and not pv.altView2Mode:
        if lightingReset != 0:
            lp.resetPartialLighting(11, 98)
            lightingReset = 0
        grid(pv.flChannelRack1, 1)
        grid(pv.flChannelRack2, 2)
        grid(pv.flChannelRack3, 3)
        grid(pv.flChannelRack4, 4)
    elif pv.altView1Mode:
        if lightingReset != 1:
            lp.resetPartialLighting(11, 98)
            lightingReset = 1
        
        track = 0
        for x in range(8, 0, -1):
            for y in range(1, 8):
                if channels.channelCount() > track:
                    padXy = int(str(x)+str(y))
                    color = lp.rgbColorToPaletteColor(channels.getChannelColor(track)) if not pv.buttonPressed[padXy] else pc.COLOR_WHITE
                    lp.lightPad(padXy, color, pc.STATE_STATIC)
                track += 1
    elif pv.altView2Mode:
        if lightingReset != 2:
            lp.resetPartialLighting(11, 98)
            lightingReset = 2
    
    