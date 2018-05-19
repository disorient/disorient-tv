#!/usr/bin/env python3

'''Play folder

Play all .mov and .mp4 files in a folder
'''

import os
from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep

def play_it(file):
    path = Path(file)
    player = OMXPlayer(path)
    sleep(player.duration())
    player.quit()

# Get .mov and .mp4 files in folder
folder = "/home/pi/Documents/disorient-tv/"
 
files = os.listdir(folder)

for f in files:
    s = Path(f).suffix
    if s in ('.mov', '.mp4'):
        play_it(folder + f)
