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

altViewMode = False

textScrolling = False

buttonPressed = {}

for x in range(1, 10):
    for y in range(1, 10):
        number = int(str(x)+str(y))
        buttonPressed[number] = False

projectLoading = False

# mixer mode
flTrack1 = 1
flTrack2 = 2
flTrack3 = 3 
flTrack4 = 4
flSelectedTrack = -1

altSetting = 0