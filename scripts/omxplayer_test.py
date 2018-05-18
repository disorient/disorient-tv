#!/usr/bin/env python3

'''omxplayer_test.py

Modified example from:
http://python-omxplayer-wrapper.readthedocs.io/en/latest/
'''

from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep

VIDEO_PATH = Path("/home/pi/Documents/disorient-tv/DTV-Pornj-Walk-With-Me.mov")
player = OMXPlayer(VIDEO_PATH)
sleep(5)
player.quit()