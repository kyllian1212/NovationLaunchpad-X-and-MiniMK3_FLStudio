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

# "always on" pad consts
SHIFT_PAD = 89

# transport pad consts
PATTERN_PAD = 79
PLAYPAUSE_PAD = 69
STOP_PAD = 59
RECORD_PAD  = 49

TRANSPORT_PADS = [PATTERN_PAD, PLAYPAUSE_PAD, STOP_PAD, RECORD_PAD]

# arrow pad consts
UP_PAD = 91
DOWN_PAD = 92
LEFT_PAD = 93
RIGHT_PAD = 94

ARROW_PADS = [UP_PAD, DOWN_PAD, LEFT_PAD, RIGHT_PAD]

# return pad const
RETURN_PAD = 19

# metronome "pad" const
METRONOME_PAD = 99

# mode + pads consts
MENU_MODE = 0

BPM_MODE = 1
BPM_MENUPAD = 81

MODES = [BPM_MODE]
