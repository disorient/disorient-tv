#!/usr/bin/env python3

'''Play two files

Example of playing two files back to back with duration.
'''

from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep

def play_it(file):
    path = Path(file)
    player = OMXPlayer(path)
    #player.set_aspect_mode("stretch")
    sleep(player.duration())

play_it("/home/pi/Documents/disorient-tv/DTV-Pornj-Walk-With-Me.mov")
play_it("/home/pi/Documents/disorient-tv/DTV-Mono-Skull.mov")
player.quit()
