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
channelRackPageAlt = 0

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
        p = (16*(pv.channelRackSequencerPage-1))+0
        for pad1 in rack_sequencer:
            if channels.getGridBit(flChannelRack, p):
                if transport.isPlaying() and transport.getLoopMode() == 0 and p+1 == songPosFormula:          
                    lp.lightPad(pad1, playGridColor, pc.STATE_STATIC if not pv.buttonPressed[pc.SHIFT_PAD] else pc.STATE_PULSING)
                else:
                    lp.lightPad(pad1, pc.COLOR_WHITE, pc.STATE_STATIC if not pv.buttonPressed[pc.SHIFT_PAD] else pc.STATE_PULSING)
            else:
                if transport.isPlaying() and transport.getLoopMode() == 0 and p+1 == songPosFormula:
                    lp.lightPad(pad1, playColor, pc.STATE_STATIC)
                else:
                    lp.lightPad(pad1, color, pc.STATE_STATIC)
            p += 1


def channelRack():
    global lightingReset
    global channelRackPageAlt

    if pv.channelRackStepEditMode:
        if lightingReset != 3:
            lp.resetPartialLighting(11, 98)
            lightingReset = 3
        
        velColor1 = pc.COLOR_DARK_GRAY
        velColor2 = pc.COLOR_GRAY
        velColor3 = pc.COLOR_LIGHT_GRAY
        velColor4 = pc.COLOR_WHITE
        velColorOff = pc.COLOR_EMPRESS

        stepVel = channels.getCurrentStepParam(pv.channelRackStepEditRack, pv.channelRackStepEditGridBit, 1)
        velCheck = 0
        for x in range(8, 4, -1):
            for y in range(1, 9):
                padXy = int(str(x)+str(y))
                if stepVel >= velCheck+4:
                    lp.lightPad(padXy, velColor4 if stepVel != 100 else pc.COLOR_LIGHT_GREEN, pc.STATE_STATIC)
                elif stepVel >= velCheck+3:
                    lp.lightPad(padXy, velColor3, pc.STATE_STATIC)
                elif stepVel >= velCheck+2:
                    lp.lightPad(padXy, velColor2, pc.STATE_STATIC)
                elif stepVel >= velCheck+1:
                    lp.lightPad(padXy, velColor1, pc.STATE_STATIC)
                else:
                    lp.lightPad(padXy, velColorOff, pc.STATE_STATIC)
                velCheck += 4

        lp.lightPad(pc.CHANNELRACKSTEPEDITMODE_RETURN, pc.COLOR_DARK_RED, pc.STATE_STATIC)

        if not channels.getGridBit(pv.channelRackStepEditRack, pv.channelRackStepEditGridBit):
            pv.channelRackStepEditMode = False
            pv.channelRackStepEditGridBit = -1
            pv.channelRackStepEditRack = -1

    elif not pv.altView1Mode and not pv.altView2Mode:
        pv.channelCount = channels.channelCount()
        if lightingReset != 0:
            lp.resetPartialLighting(11, 98)
            lightingReset = 0
            pv.channelRackAltViewRefresh = False
            channelRackPageAlt = 0
        grid(pv.flChannelRack1, 1)
        grid(pv.flChannelRack2, 2)
        grid(pv.flChannelRack3, 3)
        grid(pv.flChannelRack4, 4)

        if pv.buttonPressed[pc.SHIFT_PAD]:
            colorUpPad = pc.COLOR_DARK_GRAY if pv.flChannelRack1 > 3 else pc.COLOR_OFF
            if pv.flChannelRack1 > 3 and pv.buttonPressed[pc.UP_PAD]:
                colorUpPad = pc.COLOR_WHITE      
        else:
            colorUpPad = pc.COLOR_DARK_GRAY if pv.flChannelRack1 != 0 else pc.COLOR_OFF
            if pv.flChannelRack1 != 0 and pv.buttonPressed[pc.UP_PAD]:
                colorUpPad = pc.COLOR_WHITE 
        
        if pv.buttonPressed[pc.SHIFT_PAD]:
            colorDownPad = pc.COLOR_DARK_GRAY if pv.flChannelRack4+4 < channels.channelCount() else pc.COLOR_OFF
            if pv.flChannelRack4+4 < channels.channelCount() and pv.buttonPressed[pc.DOWN_PAD]:
                colorDownPad = pc.COLOR_WHITE
        else:
            colorDownPad = pc.COLOR_DARK_GRAY if pv.flChannelRack4+1 < channels.channelCount() else pc.COLOR_OFF
            if pv.flChannelRack4+1 < channels.channelCount() and pv.buttonPressed[pc.DOWN_PAD]:
                colorDownPad = pc.COLOR_WHITE
        
        colorLeftPad = pc.COLOR_DARK_RED if not pv.buttonPressed[pc.LEFT_PAD] else pc.COLOR_LIGHT_RED
        colorRightPad = pc.COLOR_DARK_RED if not pv.buttonPressed[pc.RIGHT_PAD] else pc.COLOR_LIGHT_RED

        lp.lightPad(pc.UP_PAD, colorUpPad, pc.STATE_STATIC)
        lp.lightPad(pc.DOWN_PAD, colorDownPad, pc.STATE_STATIC)
        lp.lightPad(pc.LEFT_PAD, colorLeftPad if pv.channelRackSequencerPage > 1 else pc.COLOR_OFF, pc.STATE_STATIC)
        lp.lightPad(pc.RIGHT_PAD, colorRightPad if pv.channelRackSequencerPage < 65 else pc.COLOR_OFF, pc.STATE_STATIC)

    elif pv.altView1Mode:
        if lightingReset != 1:
            lp.resetPartialLighting(11, 98)
            lightingReset = 1
            pv.channelCount = channels.channelCount()
        
        upArrowColor = pc.COLOR_DARK_GRAY
        if pv.buttonPressed[pc.UP_PAD]:
            upArrowColor = pc.COLOR_WHITE
        if pv.channelRackAltViewPage == 1:
            upArrowColor = pc.COLOR_OFF
        
        downArrowColor = pc.COLOR_DARK_GRAY
        if pv.buttonPressed[pc.DOWN_PAD]:
            downArrowColor = pc.COLOR_WHITE
        if channels.channelCount() <= 64*pv.channelRackAltViewPage:
            downArrowColor = pc.COLOR_OFF
        
        lp.lightPad(pc.UP_PAD, upArrowColor, pc.STATE_STATIC)
        lp.lightPad(pc.DOWN_PAD, downArrowColor, pc.STATE_STATIC)
        
        if channelRackPageAlt != pv.channelRackAltViewPage or not pv.channelRackAltViewRefresh or pv.channelCount != channels.channelCount():
            pv.channelRackAltViewRefresh = True
            pv.channelCount = channels.channelCount()
            channelRackPageAlt = pv.channelRackAltViewPage
            track = (64*(pv.channelRackAltViewPage-1))
            for x in range(8, 0, -1):
                for y in range(1, 9):
                    padXy = int(str(x)+str(y))
                    if channels.channelCount() > track:
                        color = lp.rgbColorToPaletteColor(channels.getChannelColor(track)) if not pv.buttonPressed[padXy] else pc.COLOR_WHITE
                        lp.lightPad(padXy, color, pc.STATE_STATIC)
                    else:
                        lp.lightPad(padXy, pc.COLOR_OFF, pc.STATE_STATIC)
                    track += 1
    elif pv.altView2Mode:
        pv.channelCount = channels.channelCount()
        if lightingReset != 2:
            lp.resetPartialLighting(11, 98)
            lightingReset = 2
            pv.channelRackAltViewRefresh = False
    
    