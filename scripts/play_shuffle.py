#!/usr/bin/env python3

'''Shuffle and play files in loop

Play all .mov and .mp4 files in a folder
'''

import os
from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep
from random import shuffle

def play_it(file):
    path = Path(file)
    player = OMXPlayer(path)
    sleep(player.duration())
    player.quit()

# Clear screen
os.system('clear')

# Get .mov and .mp4 files in folder
folder = "/home/pi/Documents/disorient-tv/"
files = os.listdir(folder)

# Never repeat a video twice in a row
last_video = False

while True:
    file_list = files

    shuffled = False
    while not shuffled:
        shuffle(file_list)
        shuffled = file_list[0] != last_video

    for f in file_list:
        s = Path(f).suffix
        if s in ('.mov', '.mp4'):
            last_video = s
            play_it(folder + f)
