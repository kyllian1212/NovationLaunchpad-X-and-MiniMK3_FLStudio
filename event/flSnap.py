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
import progVars as pv
import launchpad as lp

import eventHandler as e

import sys
import time

def flSnap(event):
    if e.buttonPressedCheck(pc.BAR_PAD, event):
        ui.setSnapMode(14)
    if e.buttonPressedCheck(pc.BEAT_PAD, event):
        ui.setSnapMode(13)
    if e.buttonPressedCheck(pc.STEP_PAD, event):
        ui.setSnapMode(8)
    if e.buttonPressedCheck(pc.NONE_PAD, event):
        ui.setSnapMode(3)
    if e.buttonPressedCheck(pc.CELL_PAD, event):
        ui.setSnapMode(1)
    if e.buttonPressedCheck(pc.LINE_PAD, event):
        ui.setSnapMode(0)

    if pv.stepSnap():
        if e.buttonPressedCheck(pc.FULL_PAD, event):
            ui.setSnapMode(8)
        if e.buttonPressedCheck(pc.HALF_PAD, event):
            ui.setSnapMode(7)
        if e.buttonPressedCheck(pc.THIRD_PAD, event):
            ui.setSnapMode(6) 
        if e.buttonPressedCheck(pc.QUARTER_PAD, event):
            ui.setSnapMode(5)
        if e.buttonPressedCheck(pc.SIXTH_PAD, event):
            ui.setSnapMode(4)
    
    if pv.beatSnap():
        if e.buttonPressedCheck(pc.FULL_PAD, event):
            ui.setSnapMode(13)
        if e.buttonPressedCheck(pc.HALF_PAD, event):
            ui.setSnapMode(12)
        if e.buttonPressedCheck(pc.THIRD_PAD, event):
            ui.setSnapMode(11) 
        if e.buttonPressedCheck(pc.QUARTER_PAD, event):
            ui.setSnapMode(10)
        if e.buttonPressedCheck(pc.SIXTH_PAD, event):
            ui.setSnapMode(9)