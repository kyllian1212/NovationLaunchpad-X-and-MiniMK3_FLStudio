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

import sys
import time

def flTransport():
    if transport.getLoopMode() == 0:
        lp.lightPad(59, lp.color["orange"], lp.state["static"])
    else:
        lp.lightPad(59, lp.color["lime_green"], lp.state["static"])

    if transport.isPlaying():
        lp.lightPad(49, lp.color["green"], lp.state["static"])
    else:
        lp.lightPad(49, lp.color["darker_green"], lp.state["static"])
    
    lp.lightPad(39, lp.color["red"], lp.state["static"])
    
    if transport.isRecording():
        lp.lightPad(29, lp.color["red"], lp.state["static"])
    else:
        lp.lightPad(29, lp.color["coral_tree"], lp.state["static"])
