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

import launchpad as lp

### version
VERSION = "alpha"
VERSION_MENUPAD = 11

### colors
COLOR_OFF = lp.color["off"]
COLOR_DARK_GRAY = lp.color["dark_gray"] 
COLOR_LIGHT_GRAY = lp.color["light_gray"]
COLOR_WHITE = lp.color["white"] 

COLOR_LIGHT_RED = lp.color["light_red"] 
COLOR_RED = lp.color["red"]
COLOR_DARK_RED = lp.color["dark_red"] 
COLOR_DARKER_RED = lp.color["darker_red"]

COLOR_LIGHT_ORANGE = lp.color["light_orange"] 
COLOR_ORANGE = lp.color["orange"]
COLOR_DARK_ORANGE = lp.color["dark_orange"]
COLOR_DARKER_ORANGE = lp.color["darker_orange"]

COLOR_LIGHT_YELLOW = lp.color["light_yellow"]
COLOR_YELLOW = lp.color["yellow"]
COLOR_DARK_YELLOW = lp.color["dark_yellow"]
COLOR_DARKER_YELLOW = lp.color["darker_yellow"]

COLOR_LIGHT_LIME_GREEN = lp.color["light_lime_green"] 
COLOR_LIME_GREEN = lp.color["lime_green"]
COLOR_DARK_LIME_GREEN = lp.color["dark_lime_green"] 
COLOR_DARKER_LIME_GREEN = lp.color["darker_lime_green"] 

COLOR_LIGHT_GREEN = lp.color["light_green"]
COLOR_GREEN = lp.color["green"]
COLOR_DARK_GREEN = lp.color["dark_green"]
COLOR_DARKER_GREEN = lp.color["darker_green"]

COLOR_LIGHT_BLUE_GREEN = lp.color["light_blue_green"] 
COLOR_BLUE_GREEN = lp.color["blue_green"]
COLOR_DARK_BLUE_GREEN = lp.color["dark_blue_green"]
COLOR_DARKER_BLUE_GREEN = lp.color["darker_blue_green"] 

COLOR_LIGHT_AQUA = lp.color["light_aqua"] 
COLOR_AQUA = lp.color["aqua"] 
COLOR_DARK_AQUA = lp.color["dark_aqua"] 
COLOR_DARKER_AQUA = lp.color["darker_aqua"]

COLOR_LIGHT_CYAN = lp.color["light_cyan"] 
COLOR_CYAN = lp.color["cyan"] 
COLOR_DARK_CYAN = lp.color["dark_cyan"] 
COLOR_DARKER_CYAN = lp.color["darker_cyan"]

COLOR_LIGHT_TURQUOISE = lp.color["light_turquoise"] 
COLOR_TURQUOISE = lp.color["turquoise"] 
COLOR_DARK_TURQUOISE = lp.color["dark_turquoise"]
COLOR_DARKER_TURQUOISE = lp.color["darker_turquoise"]

COLOR_LIGHT_AZURE = lp.color["light_azure"] 
COLOR_AZURE = lp.color["azure"] 
COLOR_DARK_AZURE = lp.color["dark_azure"] 
COLOR_DARKER_AZURE = lp.color["darker_azure"] 

COLOR_LIGHT_BLUE = lp.color["light_blue"]
COLOR_BLUE = lp.color["blue"] 
COLOR_DARK_BLUE = lp.color["dark_blue"] 
COLOR_DARKER_BLUE = lp.color["darker_blue"] 

COLOR_LIGHT_COBALT = lp.color["light_cobalt"] 
COLOR_COBALT = lp.color["cobalt"] 
COLOR_DARK_COBALT = lp.color["dark_cobalt"] 
COLOR_DARKER_COBALT = lp.color["darker_cobalt"] 

COLOR_LIGHT_PURPLE = lp.color["light_purple"] 
COLOR_PURPLE = lp.color["purple"] 
COLOR_DARK_PURPLE = lp.color["dark_purple"] 
COLOR_DARKER_PURPLE = lp.color["darker_purple"] 

COLOR_LIGHT_PINK = lp.color["light_pink"] 
COLOR_PINK = lp.color["pink"] 
COLOR_DARK_PINK = lp.color["dark_pink"] 
COLOR_DARKER_PINK = lp.color["darker_pink"] 

COLOR_PURE_ORANGE = lp.color["pure_orange"] 
COLOR_YELLOW_ORANGE = lp.color["yellow_orange"] 
COLOR_YELLOW_GREEN = lp.color["yellow_green"]
COLOR_APPLE_GREEN = lp.color["apple_green"] 

COLOR_ALT_DARKER_GREEN = lp.color["alt_darker_green"] 
COLOR_SILVER_TREE = lp.color["silver_tree"] 
COLOR_DANUBE = lp.color["danube"] 
COLOR_ALT_BLUE = lp.color["alt_blue"] 

COLOR_TRADEWIND = lp.color["tradewind"] 
COLOR_CORNFLOWER_BLUE = lp.color["cornflower_blue"] 
COLOR_LILY = lp.color["lily"] 
COLOR_EMPRESS = lp.color["empress"] 

COLOR_ALT_RED = lp.color["alt_red"] 
COLOR_MILAN = lp.color["milan"]
COLOR_CANARY = lp.color["canary"] 
COLOR_GREENER_CANARY = lp.color["greener_canary"] 

COLOR_PASTEL_GREEN = lp.color["pastel_green"] 
COLOR_ALT_AQUA = lp.color["alt_aqua"] 
COLOR_MALIBU = lp.color["malibu"]
COLOR_BLUER_MALIBU = lp.color["bluer_malibu"]

COLOR_HELIOTROPE = lp.color["heliotrope"] 
COLOR_LAVENDER = lp.color["lavender"] 
COLOR_LAVENDER_MAGENTA = lp.color["lavender_magenta"] 
COLOR_BROWN = lp.color["brown"] 

COLOR_ATOMIC_TANGERINE = lp.color["atomic_tangerine"] 
COLOR_LIGHT_CANARY = lp.color["light_canary"]
COLOR_REEF = lp.color["reef"] 
COLOR_ALT_GREEN = lp.color["alt_green"]

COLOR_GREENER_REEF = lp.color["greener_reef"] 
COLOR_SNOWY_MINT = lp.color["snowy_mint"] 
COLOR_AERO_BLUE = lp.color["aero_blue"] 
COLOR_ONAHAU = lp.color["onahau"]

COLOR_PERANO = lp.color["perano"]
COLOR_PERFUME = lp.color["perfume"]
COLOR_PINK_HELIOTROPE = lp.color["pink_heliotrope"]
COLOR_HOT_PINK = lp.color["hot_pink"]

COLOR_KOROMIKO = lp.color["koromiko"]
COLOR_PORTICA = lp.color["portica"]
COLOR_LEMON = lp.color["lemon"]
COLOR_GOLD = lp.color["gold"]

COLOR_TEAK = lp.color["teak"]
COLOR_FERN = lp.color["fern"]
COLOR_DE_YORK = lp.color["de_york"]
COLOR_WATERLOO = lp.color["waterloo"]

COLOR_POLO_BLUE = lp.color["polo_blue"]
COLOR_TAN = lp.color["tan"]
COLOR_ALT_DARK_RED = lp.color["alt_dark_red"]
COLOR_ROSE_BUD = lp.color["rose_bud"]

COLOR_RAJAH = lp.color["rajah"]
COLOR_DOLLY = lp.color["dolly"]
COLOR_TEXAS = lp.color["texas"]
COLOR_SULU = lp.color["sulu"]

COLOR_ALT_WATERLOO = lp.color["alt_waterloo"]
COLOR_CITRINE_WHITE = lp.color["citrine_white"]
COLOR_SCANDAL = lp.color["scandal"]
COLOR_TITAN_WHITE = lp.color["titan_white"]

COLOR_FOG = lp.color["fog"]
COLOR_ALT_DARK_GRAY = lp.color["alt_dark_gray"]
COLOR_GRAY = lp.color["gray"]
COLOR_NEAR_WHITE = lp.color["near_white"]

COLOR_MANDY = lp.color["mandy"]
COLOR_CORAL_TREE = lp.color["coral_tree"]
COLOR_SCREAMIN_GREEN = lp.color["screamin_green"]
COLOR_ALT2_DARKER_GREEN = lp.color["alt2_darker_green"]

COLOR_ALT_PORTICA = lp.color["alt_portica"]
COLOR_ALT_TEAK = lp.color["alt_teak"]
COLOR_RONCHI = lp.color["ronchi"]
COLOR_CONTESSA = lp.color["contessa"]

### states
STATE_STATIC = lp.state["static"]
STATE_FLASHING = lp.state["flashing"]
STATE_PULSING = lp.state["pulsing"]

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

### alt view 1 const
ALTVIEW1_PAD = 39

### alt view 2 const
ALTVIEW2_PAD = 29

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
TAPTEMPO_PAD = 18
UNDO_PAD = 27
REDO_PAD = 28

# mixer
MIXER_MODE = 2
MIXER_MENUPAD = 82

TRACK1L = [21, 31, 41, 51, 61, 71, 81]
TRACK1R = [22, 32, 42, 52, 62, 72, 82]
TRACK1_MUTE = 11
TRACK1_ARMED = 12

TRACK2L = [23, 33, 43, 53, 63, 73, 83]
TRACK2R = [24, 34, 44, 54, 64, 74, 84]
TRACK2_MUTE = 13
TRACK2_ARMED = 14

TRACK3L = [25, 35, 45, 55, 65, 75, 85]
TRACK3R = [26, 36, 46, 56, 66, 76, 86]
TRACK3_MUTE = 15
TRACK3_ARMED = 16

TRACK4L = [27, 37, 47, 57, 67, 77, 87]
TRACK4R = [28, 38, 48, 58, 68, 78, 88]
TRACK4_MUTE = 17
TRACK4_ARMED = 18

TRACK_VERTICAL = [14, 15, 24, 25, 34, 35, 44, 45, 54, 55, 64, 65, 74, 75, 84, 85]
TRACK_HORIZONTAL = [51, 41, 52, 42, 53, 43, 54, 44, 55, 45, 56, 46, 57, 47, 58, 48]

SELECTEDTRACK_MUTE = 17
SELECTEDTRACK_ARMED = 27

ALTSETTING_VOLUME = 0
ALTSETTING_VOLUMEPAD = 18
ALTSETTING_PAN = 1
ALTSETTING_PANPAD = 28
ALTSETTING_STEREO = 2
ALTSETTING_STEREOPAD = 38

# browser
BROWSER_MODE = 8
BROWSER_MENUPAD = 88

# channel/sequencer
CHANNELRACK_MODE = 3
CHANNELRACK_MENUPAD = 83

CHANNELRACK1_SEQUENCER = [81, 82, 83, 84, 85, 86, 87, 88, 71, 72, 73, 74, 75, 76, 77, 78]
CHANNELRACK2_SEQUENCER = [61, 62, 63, 64, 65, 66, 67, 68, 51, 52, 53, 54, 55, 56, 57, 58]
CHANNELRACK3_SEQUENCER = [41, 42, 43, 44, 45, 46, 47, 48, 31, 32, 33, 34, 35, 36, 37, 38]
CHANNELRACK4_SEQUENCER = [21, 22, 23, 24, 25, 26, 27, 28, 11, 12, 13, 14, 15, 16, 17, 18]

# patterns
PATTERNS_MODE = 4
PATTERNS_MENUPAD = 84

PATTERNNAME_PAD = 21
PATTERNRENAME_PAD = 22

PATTERNCLONE_PAD = 11

MODES = [FLTRANSPORT_MODE, MIXER_MODE, CHANNELRACK_MODE, PATTERNS_MODE, BROWSER_MODE]
