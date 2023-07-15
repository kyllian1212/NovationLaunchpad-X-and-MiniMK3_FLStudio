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

lastButtonPressed = 0
padLevel = 4

def gridBit(flChannelRack: int, lpChannelRack: int, event, getBit: bool = False):
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
    
    p = (16*(pv.channelRackSequencerPage-1))+0
    for gridStep in rack_sequencer:
        if e.buttonPressedCheck(gridStep, event):
            if getBit:
                return p
            channels.setGridBit(flChannelRack, p, True) if not channels.getGridBit(flChannelRack, p) else channels.setGridBit(flChannelRack, p, False)
        p += 1
    
    return None

def channelRack(event):
    global lastButtonPressed
    global padLevel

    if pv.channelRackStepEditMode:
        if e.buttonPressedCheck(pc.CHANNELRACKSTEPEDITMODE_RETURN, event):
            pv.disableChannelRackStepEditMode()
            lastButtonPressed = 0
            padLevel = 4
        
        if e.buttonPressedCheckGroup(51, 88, event):
            if pv.buttonPressed[pc.SHIFT_PAD]:
                channels.setStepParameterByIndex(pv.channelRackStepEditRack, patterns.patternNumber(), pv.channelRackStepEditGridBit, 1, 100)
            else:
                velCheck = 0
                loopBreak = False
                for x in range(8, 4, -1):
                    for y in range(1, 9):
                        padXy = int(str(x)+str(y))
                        if e.buttonPressedCheck(padXy, event):
                            if lastButtonPressed != padXy:
                                lastButtonPressed = padXy
                                padLevel = 4
                            else:
                                if padLevel == 4:
                                    padLevel = 0
                                else: 
                                    padLevel += 1

                            finalVelocity = velCheck+padLevel

                            channels.setStepParameterByIndex(pv.channelRackStepEditRack, patterns.patternNumber(), pv.channelRackStepEditGridBit, 1, finalVelocity)

                            loopBreak = True
                            
                            break

                        velCheck += 4
                    if loopBreak:
                        break
        
    elif not pv.altView1Mode and not pv.altView2Mode:
        ui.crDisplayRect(16*(pv.channelRackSequencerPage-1), pv.flChannelRack1, 16, 4, 4000, 0)

        if e.buttonPressedCheckGroup(71, 88, event):
            if pv.buttonPressed[pc.SHIFT_PAD]:
                bit = gridBit(pv.flChannelRack1, 1, event, True)
                pv.enableChannelRackStepEditMode(bit, pv.flChannelRack1)
            else:
                gridBit(pv.flChannelRack1, 1, event)
        elif e.buttonPressedCheckGroup(51, 68, event):
            if pv.buttonPressed[pc.SHIFT_PAD]:
                bit = gridBit(pv.flChannelRack2, 2, event, True)
                pv.enableChannelRackStepEditMode(bit, pv.flChannelRack2)
            else:
                gridBit(pv.flChannelRack2, 2, event)
        elif e.buttonPressedCheckGroup(31, 48, event):
            if pv.buttonPressed[pc.SHIFT_PAD]:
                bit = gridBit(pv.flChannelRack3, 3, event, True)
                pv.enableChannelRackStepEditMode(bit, pv.flChannelRack3)
            else:
                gridBit(pv.flChannelRack3, 3, event)
        elif e.buttonPressedCheckGroup(11, 28, event):
            if pv.buttonPressed[pc.SHIFT_PAD]:
                bit = gridBit(pv.flChannelRack4, 4, event, True)
                pv.enableChannelRackStepEditMode(bit, pv.flChannelRack4)
            else:
                gridBit(pv.flChannelRack4, 4, event)
        
        if e.buttonPressedCheck(pc.UP_PAD, event):
            if pv.flChannelRack1 != 0 and not pv.buttonPressed[pc.SHIFT_PAD]:
                pv.incrementFlChannelRackByValue(-1)
            elif pv.flChannelRack1 > 3 and pv.buttonPressed[pc.SHIFT_PAD]:
                pv.incrementFlChannelRackByValue(-4)
        if e.buttonPressedCheck(pc.DOWN_PAD, event):
            if pv.flChannelRack4+1 < channels.channelCount() and not pv.buttonPressed[pc.SHIFT_PAD]:
                pv.incrementFlChannelRackByValue(1)
            elif pv.flChannelRack4+4 < channels.channelCount() and pv.buttonPressed[pc.SHIFT_PAD]:
                pv.incrementFlChannelRackByValue(4)
        if e.buttonPressedCheck(pc.LEFT_PAD, event):
            if pv.channelRackSequencerPage > 1 and not pv.buttonPressed[pc.SHIFT_PAD]:
                pv.channelRackSequencerPage -= 1
            elif pv.channelRackSequencerPage > 1 and pv.buttonPressed[pc.SHIFT_PAD]:
                pv.channelRackSequencerPage = 1
        if e.buttonPressedCheck(pc.RIGHT_PAD, event):
            if pv.channelRackSequencerPage < 65 and not pv.buttonPressed[pc.SHIFT_PAD]:
                pv.channelRackSequencerPage += 1
            elif pv.channelRackSequencerPage < 65 and pv.buttonPressed[pc.SHIFT_PAD]:
                pv.channelRackSequencerPage = 65

    elif pv.altView1Mode:
        if e.buttonPressedCheck(pc.UP_PAD, event) and pv.channelRackAltViewPage != 1:
            pv.channelRackAltViewPage -= 1
        if e.buttonPressedCheck(pc.DOWN_PAD, event) and channels.channelCount() > 64*pv.channelRackAltViewPage:
            pv.channelRackAltViewPage += 1

        track = (64*(pv.channelRackAltViewPage-1))
        for x in range(8, 0, -1):
            for y in range(1, 9):
                padXy = int(str(x)+str(y))
                if e.buttonPressedCheck(padXy, event) and channels.channelCount() > track:
                    pv.channelRackAltViewRefresh = False
                    pv.triggerNote = True
                    event.data1 = 60
                    channels.selectOneChannel(track)
                elif e.buttonReleasedCheck(padXy, event) and channels.channelCount() > track:
                    pv.channelRackAltViewRefresh = False
                    pv.triggerNote = True
                    event.data1 = 60
                track += 1
                    