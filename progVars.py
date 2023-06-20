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

textScrolling = False

shiftPressed = False

stopPressed = False

upPressed = False
downPressed = False
leftPressed = False
rightPressed = False

returnPressed = False

buttonPressed = {}

for x in range(1, 9):
    for y in range(1, 9):
        number = int(str(x)+str(y))
        buttonPressed[number] = False

projectLoading = False