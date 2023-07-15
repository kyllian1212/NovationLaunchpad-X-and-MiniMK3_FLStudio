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
padLevel = 3

#add reverse polarity etc buttons
def lpMixer(event, mixerMasterTrig: bool = False):
    if not pv.mixerMasterMode:
        if e.buttonPressedCheck(pc.UP_PAD, event):
            if pv.flTrack4+4 <= 125:
                pv.incrementFlTrackByValue(4)
                if pv.flSelectedTrack != -1:
                    pv.flSelectedTrack += 4
        if e.buttonPressedCheck(pc.DOWN_PAD, event):
            if pv.flTrack1-4 >= 1:
                pv.incrementFlTrackByValue(-4)
                if pv.flSelectedTrack != -1:
                    pv.flSelectedTrack -= 4
        if e.buttonPressedCheck(pc.LEFT_PAD, event):
            if pv.flTrack1 > 1:
                pv.incrementFlTrackByValue(-1)
                if pv.flSelectedTrack != -1:
                    pv.flSelectedTrack -= 1
        if e.buttonPressedCheck(pc.RIGHT_PAD, event):
            if pv.flTrack4 < 125:
                pv.incrementFlTrackByValue(1)
                if pv.flSelectedTrack != -1:
                    pv.flSelectedTrack += 1

    if not pv.altView1Mode and not pv.mixerMasterMode:
        ui.miDisplayRect(pv.flTrack1, pv.flTrack4, 4000)
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
        altViewModeMixer(event)
            
def altViewModeMixer(event):
    global lastButtonPressed
    global padLevel

    if pv.flSelectedTrack == -1:
        if e.buttonPressedCheckGroup(11, 82, event):
            pv.flSelectedTrack = pv.flTrack1
        if e.buttonPressedCheckGroup(13, 84, event):
            pv.flSelectedTrack = pv.flTrack2
            pv.incrementFlTrackByValue(1)
        if e.buttonPressedCheckGroup(15, 86, event):
            pv.flSelectedTrack = pv.flTrack3
            pv.incrementFlTrackByValue(2)
        if e.buttonPressedCheckGroup(17, 88, event):
            pv.flSelectedTrack = pv.flTrack4
            pv.incrementFlTrackByValue(3)      
        
        ui.miDisplayRect(pv.flTrack1, pv.flTrack4, 4000)
    else:
        ui.miDisplayRect(pv.flSelectedTrack, pv.flSelectedTrack, 4000)

        if e.buttonPressedCheck(pc.ALTSETTING_VOLUMEPAD, event):
            pv.alt1Setting = 0
            lastButtonPressed = 0
            padLevel = 3
        elif e.buttonPressedCheck(pc.ALTSETTING_PANPAD, event):
            pv.alt1Setting = 1
            lastButtonPressed = 0
            padLevel = 3
        elif e.buttonPressedCheck(pc.ALTSETTING_STEREOPAD, event):
            pv.alt1Setting = 2
            lastButtonPressed = 0
            padLevel = 3

        if pv.alt1Setting == 0:
            volumeCalc(event)
        elif pv.alt1Setting == 1:
            panStereoCalc(event, True)
        elif pv.alt1Setting == 2:
            panStereoCalc(event, False)

        if e.buttonPressedCheck(pc.SELECTEDTRACK_MUTE, event):
            mixer.muteTrack(pv.flSelectedTrack) if not pv.buttonPressed[pc.SHIFT_PAD] else mixer.soloTrack(pv.flSelectedTrack)
        if e.buttonPressedCheck(pc.SELECTEDTRACK_ARMED, event):
            mixer.armTrack(pv.flSelectedTrack)
        if e.buttonPressedCheck(pc.SELECTEDTRACK_REVERSEPOLARITY, event):
            mixer.revTrackPolarity(pv.flSelectedTrack, True) if not mixer.isTrackRevPolarity(pv.flSelectedTrack) else mixer.revTrackPolarity(pv.flSelectedTrack, False)
        if e.buttonPressedCheck(pc.SELECTEDTRACK_SWAPLEFTRIGHT, event):
            mixer.swapTrackChannels(pv.flSelectedTrack, True) if not mixer.isTrackSwapChannels(pv.flSelectedTrack) else mixer.swapTrackChannels(pv.flSelectedTrack, False)
        

def volumeCalc(event):
    global lastButtonPressed
    global padLevel

    volIncr = 1/50

    if e.buttonPressedCheckGroup(14, 85, event):
        if pv.buttonPressed[pc.SHIFT_PAD]:
            mixer.setTrackVolume(pv.flSelectedTrack, 0.8)
        else:
            c = 0
            for x in range(1, 9):
                for y in range(4, 6):
                    padXy = int(str(x)+str(y))
                    if e.buttonPressedCheck(padXy, event):
                        if lastButtonPressed != padXy:
                            lastButtonPressed = padXy
                            padLevel = 3
                        else:
                            if padLevel == 3:
                                padLevel = 0  
                            else: 
                                padLevel += 1

                        finalVolume = 1 if e.buttonPressedCheck(85, event) and padLevel == 3 else ((volIncr*(c+padLevel))-0.01)

                        mixer.setTrackVolume(pv.flSelectedTrack, finalVolume)
                
                    c += 3

def panStereoCalc(event, pan: bool = True):
    global lastButtonPressed
    global padLevel

    panStereoIncrL = -1/25
    panStereoIncrR = 1/25

    if e.buttonPressedCheckGroup(41, 58, event):
        if pv.buttonPressed[pc.SHIFT_PAD]:
            mixer.setTrackPan(pv.flSelectedTrack, 0) if pan else mixer.setTrackStereoSep(pv.flSelectedTrack, 0)
        else:
            cL = 21
            for y in range(1, 5):
                for x in range(5, 3, -1):
                    padXy = int(str(x)+str(y))
                    if e.buttonPressedCheck(padXy, event):
                        if lastButtonPressed != padXy:
                            lastButtonPressed = padXy
                            padLevel = 3
                        else:
                            if padLevel == 3:
                                padLevel = 0  
                            else: 
                                padLevel += 1

                        formula = ((panStereoIncrL*(cL+padLevel))+0.01)
                        if e.buttonPressedCheck(51, event) and padLevel == 3:
                            finalSetting = -1
                        else: 
                            finalSetting = 0 if formula == 0.01 else formula
                        
                        mixer.setTrackPan(pv.flSelectedTrack, finalSetting) if pan else mixer.setTrackStereoSep(pv.flSelectedTrack, finalSetting)
                
                    cL -= 3
            
            cR = 0
            for y in range(5, 9):
                for x in range(5, 3, -1):
                    padXy = int(str(x)+str(y))
                    if e.buttonPressedCheck(padXy, event):
                        if lastButtonPressed != padXy:
                            lastButtonPressed = padXy
                            padLevel = 3
                        else:
                            if padLevel == 3:
                                padLevel = 0  
                            else: 
                                padLevel += 1
                        
                        formula = ((panStereoIncrR*(cR+padLevel))-0.01)
                        if e.buttonPressedCheck(48, event) and padLevel == 3:
                            finalSetting = 1 
                        else:
                            finalSetting = 0 if formula == -0.01 else formula

                        mixer.setTrackPan(pv.flSelectedTrack, finalSetting) if pan else mixer.setTrackStereoSep(pv.flSelectedTrack, finalSetting)
                
                    cR += 3