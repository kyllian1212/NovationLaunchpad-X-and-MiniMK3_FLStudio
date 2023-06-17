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

projectLoading = False

shiftPressed = False

stopPressed = False

upPressed = False
downPressed = False
leftPressed = False
rightPressed = False

returnPressed = False