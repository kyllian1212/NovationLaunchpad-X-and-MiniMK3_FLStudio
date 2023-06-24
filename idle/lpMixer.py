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
        raise Exception("not a valid lpTrack number")
    
    # L pan
    lp.lightPad(peaksL[6], peakColorClip, pc.STATE_PULSING) if trackPeakL > 1 else lp.lightPad(peaksL[6], peakOff, pc.STATE_PULSING)

    if trackPeakL > volPeak*18:
        lp.lightPad(peaksL[5], peakColorWarn1, pc.STATE_STATIC)
    elif trackPeakL > volPeak*17:
        lp.lightPad(peaksL[5], peakColorWarn2, pc.STATE_STATIC)
    elif trackPeakL > volPeak*16:
        lp.lightPad(peaksL[5], peakColorWarn3, pc.STATE_STATIC)
    else:
        lp.lightPad(peaksL[5], peakOff, pc.STATE_STATIC)

    if trackPeakL > volPeak*15:
        lp.lightPad(peaksL[4], peakColorWarn1, pc.STATE_STATIC)
    elif trackPeakL > volPeak*14:
        lp.lightPad(peaksL[4], peakColorWarn2, pc.STATE_STATIC)
    elif trackPeakL > volPeak*13:
        lp.lightPad(peaksL[4], peakColorWarn3, pc.STATE_STATIC)
    else:
        lp.lightPad(peaksL[4], peakOff, pc.STATE_STATIC)
    
    if trackPeakL > volPeak*12:
        lp.lightPad(peaksL[3], peakColorOk1, pc.STATE_STATIC)
    elif trackPeakL > volPeak*11:
        lp.lightPad(peaksL[3], peakColorOk2, pc.STATE_STATIC)
    elif trackPeakL > volPeak*10:
        lp.lightPad(peaksL[3], peakColorOk3, pc.STATE_STATIC)
    else:
        lp.lightPad(peaksL[3], peakOff, pc.STATE_STATIC)

    if trackPeakL > volPeak*9:
        lp.lightPad(peaksL[2], peakColorOk1, pc.STATE_STATIC)
    elif trackPeakL > volPeak*8:
        lp.lightPad(peaksL[2], peakColorOk2, pc.STATE_STATIC)
    elif trackPeakL > volPeak*7:
        lp.lightPad(peaksL[2], peakColorOk3, pc.STATE_STATIC)
    else:
        lp.lightPad(peaksL[2], peakOff, pc.STATE_STATIC)

    if trackPeakL > volPeak*6:
        lp.lightPad(peaksL[1], peakColorOk1, pc.STATE_STATIC)
    elif trackPeakL > volPeak*5:
        lp.lightPad(peaksL[1], peakColorOk2, pc.STATE_STATIC)
    elif trackPeakL > volPeak*4:
        lp.lightPad(peaksL[1], peakColorOk3, pc.STATE_STATIC)
    else:
        lp.lightPad(peaksL[1], peakOff, pc.STATE_STATIC)

    if trackPeakL > volPeak*3:
        lp.lightPad(peaksL[0], peakColorOk1, pc.STATE_STATIC)
    elif trackPeakL > volPeak*2:
        lp.lightPad(peaksL[0], peakColorOk2, pc.STATE_STATIC)
    elif trackPeakL > volPeak*1:
        lp.lightPad(peaksL[0], peakColorOk3, pc.STATE_STATIC)
    else:
        lp.lightPad(peaksL[0], peakOff, pc.STATE_STATIC)
    
    # R pan
    lp.lightPad(peaksR[6], peakColorClip, pc.STATE_PULSING) if trackPeakR > 1 else lp.lightPad(peaksR[6], peakOff, pc.STATE_PULSING)

    if trackPeakR > volPeak*18:
        lp.lightPad(peaksR[5], peakColorWarn1, pc.STATE_STATIC)
    elif trackPeakR > volPeak*17:
        lp.lightPad(peaksR[5], peakColorWarn2, pc.STATE_STATIC)
    elif trackPeakR > volPeak*16:
        lp.lightPad(peaksR[5], peakColorWarn3, pc.STATE_STATIC)
    else:
        lp.lightPad(peaksR[5], peakOff, pc.STATE_STATIC)

    if trackPeakR > volPeak*15:
        lp.lightPad(peaksR[4], peakColorWarn1, pc.STATE_STATIC)
    elif trackPeakR > volPeak*14:
        lp.lightPad(peaksR[4], peakColorWarn2, pc.STATE_STATIC)
    elif trackPeakR > volPeak*13:
        lp.lightPad(peaksR[4], peakColorWarn3, pc.STATE_STATIC)
    else:
        lp.lightPad(peaksR[4], peakOff, pc.STATE_STATIC)
    
    if trackPeakR > volPeak*12:
        lp.lightPad(peaksR[3], peakColorOk1, pc.STATE_STATIC)
    elif trackPeakR > volPeak*11:
        lp.lightPad(peaksR[3], peakColorOk2, pc.STATE_STATIC)
    elif trackPeakR > volPeak*10:
        lp.lightPad(peaksR[3], peakColorOk3, pc.STATE_STATIC)
    else:
        lp.lightPad(peaksR[3], peakOff, pc.STATE_STATIC)

    if trackPeakR > volPeak*9:
        lp.lightPad(peaksR[2], peakColorOk1, pc.STATE_STATIC)
    elif trackPeakR > volPeak*8:
        lp.lightPad(peaksR[2], peakColorOk2, pc.STATE_STATIC)
    elif trackPeakR > volPeak*7:
        lp.lightPad(peaksR[2], peakColorOk3, pc.STATE_STATIC)
    else:
        lp.lightPad(peaksR[2], peakOff, pc.STATE_STATIC)

    if trackPeakR > volPeak*6:
        lp.lightPad(peaksR[1], peakColorOk1, pc.STATE_STATIC)
    elif trackPeakR > volPeak*5:
        lp.lightPad(peaksR[1], peakColorOk2, pc.STATE_STATIC)
    elif trackPeakR > volPeak*4:
        lp.lightPad(peaksR[1], peakColorOk3, pc.STATE_STATIC)
    else:
        lp.lightPad(peaksR[1], peakOff, pc.STATE_STATIC)

    if trackPeakR > volPeak*3:
        lp.lightPad(peaksR[0], peakColorOk1, pc.STATE_STATIC)
    elif trackPeakR > volPeak*2:
        lp.lightPad(peaksR[0], peakColorOk2, pc.STATE_STATIC)
    elif trackPeakR > volPeak*1:
        lp.lightPad(peaksR[0], peakColorOk3, pc.STATE_STATIC)
    else:
        lp.lightPad(peaksR[0], peakOff, pc.STATE_STATIC)

def lpMixer():
    global trackSelected
    
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
    
    if not pv.altViewMode:
        peakCalc(pv.flTrack1, 1)
        peakCalc(pv.flTrack2, 2)
        peakCalc(pv.flTrack3, 3)
        peakCalc(pv.flTrack4, 4)

        colorTrack1Mute = lp.rgbColorToPaletteColor(mixer.getTrackColor(pv.flTrack1), pc.COLOR_EMPRESS) if not mixer.isTrackMuted(pv.flTrack1) else pc.COLOR_OFF
        colorTrack2Mute = lp.rgbColorToPaletteColor(mixer.getTrackColor(pv.flTrack2), pc.COLOR_EMPRESS) if not mixer.isTrackMuted(pv.flTrack2) else pc.COLOR_OFF
        colorTrack3Mute = lp.rgbColorToPaletteColor(mixer.getTrackColor(pv.flTrack3), pc.COLOR_EMPRESS) if not mixer.isTrackMuted(pv.flTrack3) else pc.COLOR_OFF
        colorTrack4Mute = lp.rgbColorToPaletteColor(mixer.getTrackColor(pv.flTrack4), pc.COLOR_EMPRESS) if not mixer.isTrackMuted(pv.flTrack4) else pc.COLOR_OFF

        colorTrack1Armed = pc.COLOR_DARKER_RED if not mixer.isTrackArmed(pv.flTrack1) else pc.COLOR_LIGHT_RED
        colorTrack2Armed = pc.COLOR_DARKER_RED if not mixer.isTrackArmed(pv.flTrack2) else pc.COLOR_LIGHT_RED
        colorTrack3Armed = pc.COLOR_DARKER_RED if not mixer.isTrackArmed(pv.flTrack3) else pc.COLOR_LIGHT_RED
        colorTrack4Armed = pc.COLOR_DARKER_RED if not mixer.isTrackArmed(pv.flTrack4) else pc.COLOR_LIGHT_RED

        lp.lightPad(pc.TRACK1_MUTE, colorTrack1Mute, pc.STATE_STATIC)
        lp.lightPad(pc.TRACK1_ARMED, colorTrack1Armed, pc.STATE_STATIC)

        lp.lightPad(pc.TRACK2_MUTE, colorTrack2Mute, pc.STATE_STATIC)
        lp.lightPad(pc.TRACK2_ARMED, colorTrack2Armed, pc.STATE_STATIC)

        lp.lightPad(pc.TRACK3_MUTE, colorTrack3Mute, pc.STATE_STATIC)
        lp.lightPad(pc.TRACK3_ARMED, colorTrack3Armed, pc.STATE_STATIC)

        lp.lightPad(pc.TRACK4_MUTE, colorTrack4Mute, pc.STATE_STATIC)
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