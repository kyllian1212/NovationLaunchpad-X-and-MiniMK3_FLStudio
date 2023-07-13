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

launchpad_sysexid = pc.LAUNCHPADMINIMK3_SYSEXID if "LPMINIMK3" in device.getName().upper() else pc.LAUNCHPADX_SYSEXID

mode = pc.MENU_MODE

bpm = mixer.getCurrentTempo(0)

waitMode = False #when project is loading or init is occuring

altView1Mode = False
altView2Mode = False

textScrolling = False

buttonPressed = {}

for x in range(1, 10):
    for y in range(1, 10):
        number = int(str(x)+str(y))
        buttonPressed[number] = False

def resetPresses():
    for x in range(1, 10):
        for y in range(1, 10):
            number = int(str(x)+str(y))
            buttonPressed[number] = False

projectLoading = False

triggerNote = False

# mixer mode
flTrack1 = 1
flTrack2 = 2
flTrack3 = 3 
flTrack4 = 4
flSelectedTrack = -1

# def to increment/decrement the tracks

alt1Setting = 0

# channel rack mode
flChannelRack1 = 0
flChannelRack2 = 1
flChannelRack3 = 2
flChannelRack4 = 3
flSelectedChannelRack = -1

# def to increment/decrement the tracks

channelCount = 0

channelRackSequencerPage = 1
channelRackAltViewPage = 1

channelRackStepEditMode = False
channelRackStepEditGridBit = -1
channelRackStepEditRack = -1

channelRackAltViewRefresh = False

# def to enable and disable grid edit mode

# patterns mode
patternPage = 1
patternQueued = -1
patternQueueHandled = False