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

trackSelected = False
previousMode = 0
currentTrackVolume = None
currentTrackPan = None
currentTrackStereo = None

def peakCalc(flTrack: int, lpTrack: int):
    volPeak = 1/19

    peaksL = []
    peaksR = []

    trackPeakL = mixer.getTrackPeaks(flTrack, 0)
    trackPeakR = mixer.getTrackPeaks(flTrack, 1)

    peakColorClip = pc.COLOR_RED
    peakColorWarn1 = pc.COLOR_ORANGE
    peakColorWarn2 = pc.COLOR_DARK_ORANGE
    peakColorWarn3 = pc.COLOR_DARKER_ORANGE
    peakColorOk1 = pc.COLOR_GREEN
    peakColorOk2 = pc.COLOR_DARK_GREEN
    peakColorOk3 = pc.COLOR_DARKER_GREEN
    peakOff = pc.COLOR_OFF

    ''' fl studio's python version is 3.9 so it cannot use match cases
    match lpTrack:
        case 1:
            for pL in range(7):
                peaksL[pL] = pc.TRACK1L[pL]
            for pR in range(7):
                peaksR[pL] = pc.TRACK1R[pR]
        case 2:
            for pL in range(7):
                peaksL[pL] = pc.TRACK2L[pL]
            for pR in range(7):
                peaksR[pL] = pc.TRACK2R[pR]
        case 3:
            for pL in range(7):
                peaksL[pL] = pc.TRACK3L[pL]
            for pR in range(7):
                peaksR[pL] = pc.TRACK3R[pR]
        case 4:
            for pL in range(7):
                peaksL[pL] = pc.TRACK4L[pL]
            for pR in range(7):
                peaksR[pL] = pc.TRACK4R[pR]
        case _:
            raise Exception("not a valid lpTrack number")
    '''

    if lpTrack == 1:
        for pL in range(7):
            peaksL.append(pc.TRACK1L[pL])
        for pR in range(7):
            peaksR.append(pc.TRACK1R[pR])
    elif lpTrack == 2:
        for pL in range(7):
            peaksL.append(pc.TRACK2L[pL])
        for pR in range(7):
            peaksR.append(pc.TRACK2R[pR])
    elif lpTrack == 3:
        for pL in range(7):
            peaksL.append(pc.TRACK3L[pL])
        for pR in range(7):
            peaksR.append(pc.TRACK3R[pR])
    elif lpTrack == 4:
        for pL in range(7):
            peaksL.append(pc.TRACK4L[pL])
        for pR in range(7):
            peaksR.append(pc.TRACK4R[pR])
    else:
        raise Exception("invalid lpTrack number")
    
    # L pan
    lp.lightPad(peaksL[6], peakColorClip, pc.STATE_PULSING) if trackPeakL > 1 else lp.lightPad(peaksL[6], peakOff, pc.STATE_PULSING)
    
    cL = 1
    for pL in range(0, 6):
        if trackPeakL > volPeak*(cL+2):
            lp.lightPad(peaksL[pL], peakColorOk1 if pL < 4 else peakColorWarn1, pc.STATE_STATIC)
        elif trackPeakL > volPeak*(cL+1):
            lp.lightPad(peaksL[pL], peakColorOk2 if pL < 4 else peakColorWarn2, pc.STATE_STATIC)
        elif trackPeakL > volPeak*cL:
            lp.lightPad(peaksL[pL], peakColorOk3 if pL < 4 else peakColorWarn3, pc.STATE_STATIC)
        else:
            lp.lightPad(peaksL[pL], peakOff, pc.STATE_STATIC)
        
        cL += 3

    # R pan
    lp.lightPad(peaksR[6], peakColorClip, pc.STATE_PULSING) if trackPeakR > 1 else lp.lightPad(peaksR[6], peakOff, pc.STATE_PULSING)

    cR = 1
    for pR in range(0, 6):
        if trackPeakR > volPeak*(cR+2):
            lp.lightPad(peaksR[pR], peakColorOk1 if pR < 4 else peakColorWarn1, pc.STATE_STATIC)
        elif trackPeakR > volPeak*(cR+1):
            lp.lightPad(peaksR[pR], peakColorOk2 if pR < 4 else peakColorWarn2, pc.STATE_STATIC)
        elif trackPeakR > volPeak*cR:
            lp.lightPad(peaksR[pR], peakColorOk3 if pR < 4 else peakColorWarn3, pc.STATE_STATIC)
        else:
            lp.lightPad(peaksR[pR], peakOff, pc.STATE_STATIC)
        
        cR += 3

def volCalc(flSelectedTrack: int):
    volIncr = 1/50

    colorOff = pc.COLOR_EMPRESS
    colorIncr1 = pc.COLOR_DARK_GRAY
    colorIncr2 = pc.COLOR_LIGHT_GRAY
    colorIncr3 = pc.COLOR_WHITE
    colorDefault = pc.COLOR_GREEN

    trackVolume = mixer.getTrackVolume(flSelectedTrack)

    volPads = pc.TRACK_VERTICAL

    c = 2
    for p in range(0, 16):
        if trackVolume > volIncr*c or trackVolume == 1:
            lp.lightPad(volPads[p], colorIncr3, pc.STATE_STATIC)
        elif trackVolume > volIncr*(c-1):
            lp.lightPad(volPads[p], colorIncr2, pc.STATE_STATIC)
        elif trackVolume > volIncr*(c-2):
            lp.lightPad(volPads[p], colorIncr1, pc.STATE_STATIC)
        else:
            lp.lightPad(volPads[p], colorOff, pc.STATE_STATIC)
        
        if round(trackVolume, 2) == 0.80:
            lp.lightPad(volPads[12], colorDefault, pc.STATE_STATIC)
            lp.lightPad(volPads[13], colorDefault, pc.STATE_STATIC)

        c += 3

        #print(f"{round(trackVolume, 5)}, {round(volIncr*(c-2), 5)}, {round(volIncr*(c-1), 5)}, {round(volIncr*c, 5)}, {c}")
    #print("--")

def panStereoCalc(flSelectedTrack: int, pan: bool = True):
    panStereoIncrL = -1/25
    panStereoIncrR = 1/25

    colorOff = pc.COLOR_EMPRESS
    if pan == True:
        colorIncr1L = pc.COLOR_DARKER_ORANGE
        colorIncr2L = pc.COLOR_DARK_ORANGE
        colorIncr3L = pc.COLOR_ORANGE
        colorIncr1R = pc.COLOR_DARKER_RED
        colorIncr2R = pc.COLOR_DARK_RED
        colorIncr3R = pc.COLOR_RED
    else:
        colorIncr1L = pc.COLOR_DARKER_TURQUOISE
        colorIncr2L = pc.COLOR_DARK_TURQUOISE
        colorIncr3L = pc.COLOR_TURQUOISE
        colorIncr1R = pc.COLOR_DARKER_COBALT
        colorIncr2R = pc.COLOR_DARK_COBALT
        colorIncr3R = pc.COLOR_COBALT

    trackPan = mixer.getTrackPan(flSelectedTrack)
    trackStereo = mixer.getTrackStereoSep(flSelectedTrack)

    trackSetting = trackPan if pan else trackStereo

    panStereoPads = pc.TRACK_HORIZONTAL

    cL = 2
    for pL in range(7, -1, -1):
        if trackSetting < panStereoIncrL*cL:
            lp.lightPad(panStereoPads[pL], colorIncr3L, pc.STATE_STATIC)
        elif trackSetting < panStereoIncrL*(cL-1):
            lp.lightPad(panStereoPads[pL], colorIncr2L, pc.STATE_STATIC)
        elif trackSetting < panStereoIncrL*(cL-2):
            lp.lightPad(panStereoPads[pL], colorIncr1L, pc.STATE_STATIC)
        else:
            lp.lightPad(panStereoPads[pL], colorOff, pc.STATE_STATIC)
        
        cL += 3
    
    cR = 2
    for pR in range(8, 16):
        if trackSetting > panStereoIncrR*cR:
            lp.lightPad(panStereoPads[pR], colorIncr3R, pc.STATE_STATIC)
        elif trackSetting > panStereoIncrR*(cR-1):
            lp.lightPad(panStereoPads[pR], colorIncr2R, pc.STATE_STATIC)
        elif trackSetting > panStereoIncrR*(cR-2):
            lp.lightPad(panStereoPads[pR], colorIncr1R, pc.STATE_STATIC)
        else:
            lp.lightPad(panStereoPads[pR], colorOff, pc.STATE_STATIC)
        
        cR += 3
    
    if trackSetting == 0:
        lp.lightPad(panStereoPads[6], colorIncr3L, pc.STATE_STATIC)
        lp.lightPad(panStereoPads[7], colorIncr3L, pc.STATE_STATIC)
        lp.lightPad(panStereoPads[8], colorIncr3R, pc.STATE_STATIC)
        lp.lightPad(panStereoPads[9], colorIncr3R, pc.STATE_STATIC)


def lpMixer():
    global trackSelected
    global currentTrackVolume
    global currentTrackPan
    global currentTrackStereo
    global previousMode
    
    upArrowColor = pc.COLOR_DARKER_AZURE
    if pv.buttonPressed[pc.UP_PAD]:
        upArrowColor = pc.COLOR_LIGHT_AZURE
    if pv.flTrack4+4 > 125:
        upArrowColor = pc.COLOR_OFF
    
    downArrowColor = pc.COLOR_DARKER_AZURE
    if pv.buttonPressed[pc.DOWN_PAD]:
        downArrowColor = pc.COLOR_LIGHT_AZURE
    if pv.flTrack1-4 < 1:
        downArrowColor = pc.COLOR_OFF
    
    leftArrowColor = pc.COLOR_DARK_GRAY
    if pv.buttonPressed[pc.LEFT_PAD]:
        leftArrowColor = pc.COLOR_WHITE
    if pv.flTrack1 == 1:
        leftArrowColor = pc.COLOR_OFF
    
    rightArrowColor = pc.COLOR_DARK_GRAY
    if pv.buttonPressed[pc.RIGHT_PAD]:
        rightArrowColor = pc.COLOR_WHITE
    if pv.flTrack4 == 125:
        rightArrowColor = pc.COLOR_OFF

    lp.lightPad(pc.UP_PAD, upArrowColor, pc.STATE_STATIC)
    lp.lightPad(pc.DOWN_PAD, downArrowColor, pc.STATE_STATIC)
    lp.lightPad(pc.LEFT_PAD, leftArrowColor, pc.STATE_STATIC)
    lp.lightPad(pc.RIGHT_PAD, rightArrowColor, pc.STATE_STATIC)
    
    if not pv.altView1Mode:
        trackSelected = False
        currentTrackVolume = None
        currentTrackPan = None
        currentTrackStereo = None

        peakCalc(pv.flTrack1, 1)
        peakCalc(pv.flTrack2, 2)
        peakCalc(pv.flTrack3, 3)
        peakCalc(pv.flTrack4, 4)

        colorTrack1Mute = lp.rgbColorToPaletteColor(mixer.getTrackColor(pv.flTrack1), pc.COLOR_EMPRESS) if not mixer.isTrackMuted(pv.flTrack1) else pc.COLOR_OFF
        colorTrack2Mute = lp.rgbColorToPaletteColor(mixer.getTrackColor(pv.flTrack2), pc.COLOR_EMPRESS) if not mixer.isTrackMuted(pv.flTrack2) else pc.COLOR_OFF
        colorTrack3Mute = lp.rgbColorToPaletteColor(mixer.getTrackColor(pv.flTrack3), pc.COLOR_EMPRESS) if not mixer.isTrackMuted(pv.flTrack3) else pc.COLOR_OFF
        colorTrack4Mute = lp.rgbColorToPaletteColor(mixer.getTrackColor(pv.flTrack4), pc.COLOR_EMPRESS) if not mixer.isTrackMuted(pv.flTrack4) else pc.COLOR_OFF

        stateTrack1Solo = pc.STATE_STATIC if not mixer.isTrackSolo(pv.flTrack1) else pc.STATE_PULSING
        stateTrack2Solo = pc.STATE_STATIC if not mixer.isTrackSolo(pv.flTrack2) else pc.STATE_PULSING
        stateTrack3Solo = pc.STATE_STATIC if not mixer.isTrackSolo(pv.flTrack3) else pc.STATE_PULSING
        stateTrack4Solo = pc.STATE_STATIC if not mixer.isTrackSolo(pv.flTrack4) else pc.STATE_PULSING

        colorTrack1Armed = pc.COLOR_DARKER_RED if not mixer.isTrackArmed(pv.flTrack1) else pc.COLOR_LIGHT_RED
        colorTrack2Armed = pc.COLOR_DARKER_RED if not mixer.isTrackArmed(pv.flTrack2) else pc.COLOR_LIGHT_RED
        colorTrack3Armed = pc.COLOR_DARKER_RED if not mixer.isTrackArmed(pv.flTrack3) else pc.COLOR_LIGHT_RED
        colorTrack4Armed = pc.COLOR_DARKER_RED if not mixer.isTrackArmed(pv.flTrack4) else pc.COLOR_LIGHT_RED

        lp.lightPad(pc.TRACK1_MUTE, colorTrack1Mute, stateTrack1Solo)
        lp.lightPad(pc.TRACK1_ARMED, colorTrack1Armed, pc.STATE_STATIC)

        lp.lightPad(pc.TRACK2_MUTE, colorTrack2Mute, stateTrack2Solo)
        lp.lightPad(pc.TRACK2_ARMED, colorTrack2Armed, pc.STATE_STATIC)

        lp.lightPad(pc.TRACK3_MUTE, colorTrack3Mute, stateTrack3Solo)
        lp.lightPad(pc.TRACK3_ARMED, colorTrack3Armed, pc.STATE_STATIC)

        lp.lightPad(pc.TRACK4_MUTE, colorTrack4Mute, stateTrack4Solo)
        lp.lightPad(pc.TRACK4_ARMED, colorTrack4Armed, pc.STATE_STATIC)
    else:
        if pv.flSelectedTrack == -1:
            colorTrack1 = lp.rgbColorToPaletteColor(mixer.getTrackColor(pv.flTrack1), pc.COLOR_EMPRESS)
            colorTrack2 = lp.rgbColorToPaletteColor(mixer.getTrackColor(pv.flTrack2), pc.COLOR_EMPRESS) 
            colorTrack3 = lp.rgbColorToPaletteColor(mixer.getTrackColor(pv.flTrack3), pc.COLOR_EMPRESS) 
            colorTrack4 = lp.rgbColorToPaletteColor(mixer.getTrackColor(pv.flTrack4), pc.COLOR_EMPRESS)

            lp.lightGroup(11, 82, colorTrack1, pc.STATE_PULSING)
            lp.lightGroup(13, 84, colorTrack2, pc.STATE_PULSING)
            lp.lightGroup(15, 86, colorTrack3, pc.STATE_PULSING)
            lp.lightGroup(17, 88, colorTrack4, pc.STATE_PULSING)
        else:
            if not trackSelected:
                lp.resetPartialLighting(11, 98)
                trackSelected = True
            
            if previousMode != pv.alt1Setting:
                lp.resetPartialLighting(14, 85)
                lp.resetPartialLighting(41, 58)
                currentTrackVolume = None
                currentTrackPan = None
                currentTrackStereo = None
                previousMode = pv.alt1Setting
            
            if currentTrackVolume != mixer.getTrackVolume(pv.flSelectedTrack) and pv.alt1Setting == 0:
                volCalc(pv.flSelectedTrack)
                currentTrackVolume = mixer.getTrackVolume(pv.flSelectedTrack)
            if currentTrackPan != mixer.getTrackPan(pv.flSelectedTrack) and pv.alt1Setting == 1:
                panStereoCalc(pv.flSelectedTrack, True)
                currentTrackPan = mixer.getTrackPan(pv.flSelectedTrack)
            if currentTrackStereo != mixer.getTrackStereoSep(pv.flSelectedTrack) and pv.alt1Setting == 2:
                panStereoCalc(pv.flSelectedTrack, False)
                currentTrackStereo = mixer.getTrackStereoSep(pv.flSelectedTrack)

            colorTrackMute = lp.rgbColorToPaletteColor(mixer.getTrackColor(pv.flSelectedTrack), pc.COLOR_EMPRESS) if not mixer.isTrackMuted(pv.flSelectedTrack) else pc.COLOR_OFF
            stateTrackSolo = pc.STATE_STATIC if not mixer.isTrackSolo(pv.flSelectedTrack) else pc.STATE_PULSING
            colorTrackArmed = pc.COLOR_DARKER_RED if not mixer.isTrackArmed(pv.flTrack1) else pc.COLOR_LIGHT_RED

            lp.lightPad(pc.SELECTEDTRACK_MUTE, colorTrackMute, stateTrackSolo)
            lp.lightPad(pc.SELECTEDTRACK_ARMED, colorTrackArmed, pc.STATE_STATIC)

            lp.lightPad(pc.ALTSETTING_VOLUMEPAD, pc.COLOR_DARKER_GREEN if pv.alt1Setting != 0 else pc.COLOR_GREEN, pc.STATE_STATIC)
            lp.lightPad(pc.ALTSETTING_PANPAD, pc.COLOR_DARKER_ORANGE if pv.alt1Setting != 1 else pc.COLOR_ORANGE, pc.STATE_STATIC)
            lp.lightPad(pc.ALTSETTING_STEREOPAD, pc.COLOR_DARKER_TURQUOISE if pv.alt1Setting != 2 else pc.COLOR_TURQUOISE, pc.STATE_STATIC)
