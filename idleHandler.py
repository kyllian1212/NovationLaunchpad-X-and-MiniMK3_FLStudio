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

import idle.flTransport as iFlT
import idle.shift as iS

import sys
import time

def idleHandler():
    iFlT.flTransport()
    iS.shift()
