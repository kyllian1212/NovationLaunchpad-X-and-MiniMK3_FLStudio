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

### "always on" pad consts
SHIFT_PAD = 89

### transport pad consts
PATTERN_PAD = 79
PLAYPAUSE_PAD = 69
STOP_PAD = 59
RECORD_PAD  = 49

TRANSPORT_PADS = [PATTERN_PAD, PLAYPAUSE_PAD, STOP_PAD, RECORD_PAD]

### arrow pad consts
UP_PAD = 91
DOWN_PAD = 92
LEFT_PAD = 93
RIGHT_PAD = 94

ARROW_PADS = [UP_PAD, DOWN_PAD, LEFT_PAD, RIGHT_PAD]

### return pad const
RETURN_PAD = 19

### metronome "pad" const
METRONOME_DISPLAYPAD = 99

### mode + pads consts
MENU_MODE = 0

# fl transport
FLTRANSPORT_MODE = 1
FLTRANSPORT_MENUPAD = 81

METRONOME_PAD = 21
WAIT_FOR_INPUT_PAD = 22
COUNTDOWN_PAD = 23
OVERDUB_PAD = 24
LOOPRECORDING_PAD = 25
STEPEDIT_PAD = 26
UIPLAYLIST_PAD = 11
UIPIANOROLL_PAD = 12
UICHANNELRACK_PAD = 13
UIMIXER_PAD = 14
UIBROWSER_PAD = 15
UICLOSEWINDOW_PAD = 16
UITAPTEMPO_PAD = 18
TAPTEMPO_PAD = 28
UNDO_PAD = 37
REDO_PAD = 38

MODES = [FLTRANSPORT_MODE]
