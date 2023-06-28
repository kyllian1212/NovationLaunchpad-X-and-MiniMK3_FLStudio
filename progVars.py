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

alt1Setting = 0

# channel rack mode
flChannelRack1 = 0
flChannelRack2 = 1
flChannelRack3 = 2
flChannelRack4 = 3
flSelectedChannelRack = -1

page = 1