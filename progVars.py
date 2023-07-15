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

# might have to turn a lot of this into classes + separate files

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

# fl snap mode
def beatSnap():
    return True if ui.getSnapMode() >= 9 and ui.getSnapMode() <= 13 else False

def stepSnap():
    return True if ui.getSnapMode() >= 4 and ui.getSnapMode() <= 8 else False

# mixer mode
flTrack1 = 1
flTrack2 = 2
flTrack3 = 3 
flTrack4 = 4
flSelectedTrack = -1

mixerMasterMode = False

def incrementFlTrackByValue(value: int):
    global flTrack1
    global flTrack2
    global flTrack3
    global flTrack4
    global flSelectedTrack

    flTrack1 += value
    flTrack2 += value
    flTrack3 += value
    flTrack4 += value

alt1Setting = 0

# channel rack mode
flChannelRack1 = 0
flChannelRack2 = 1
flChannelRack3 = 2
flChannelRack4 = 3
flSelectedChannelRack = -1

def incrementFlChannelRackByValue(value: int):
    global flChannelRack1
    global flChannelRack2
    global flChannelRack3
    global flChannelRack4

    flChannelRack1 += value
    flChannelRack2 += value
    flChannelRack3 += value
    flChannelRack4 += value

channelCount = 0

channelRackSequencerPage = 1
channelRackAltViewPage = 1

channelRackStepEditMode = False
channelRackStepEditGridBit = -1
channelRackStepEditRack = -1

channelRackAltViewRefresh = False

def enableChannelRackStepEditMode(bit: int, rack: int):
    global channelRackStepEditMode
    global channelRackStepEditGridBit
    global channelRackStepEditRack

    channelRackStepEditMode = True
    channelRackStepEditGridBit = bit
    channelRackStepEditRack = rack

def disableChannelRackStepEditMode():
    global channelRackStepEditMode
    global channelRackStepEditGridBit
    global channelRackStepEditRack

    channelRackStepEditMode = False
    channelRackStepEditGridBit = -1
    channelRackStepEditRack = -1
    
# patterns mode
patternPage = 1
patternQueued = -1
patternQueueHandled = False