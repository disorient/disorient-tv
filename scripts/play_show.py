#!/usr/bin/env python3

'''Shuffle and play files in loop

Play all .mov and .mp4 files in a folder
'''

import datetime
import os
from omxplayer.player import OMXPlayer
from pathlib import Path
from random import shuffle
from time import sleep

def create_playlist_generator(playlist):
    '''Create a shuffled playlist generator'''

    L = playlist
    index = 0

    while True:
        last_played = L[index]
        yield last_played
        index = (index + 1) % len(L)

        # Shuffle after all videos have cycled
        if index == 0:
            # Prevents videos playing twice in a row
            while True:
                shuffle(L)
                if last_played != L[0]:
                    break

def next_video():
    '''Returns filename of next video to play'''

    hour = datetime.datetime.now().hour
    if hour < 5:
        return playlist_night.next()
    elif hour < 7 :
        return playlist_sunrise.next()
    elif hour < 20 :
        return playlist_day.next()
    else:
        return playlist_night.next()


def play_it(file):
    try:
        path = Path(file)
        player = OMXPlayer(path)
        sleep(player.duration())
        # sleep(3)
        player.quit()
        sleep(1)
    except:
        print('oops all berries')
        sleep(1)

def get_video_list_from_folder(folder):
    '''Returns a list of .mov and .mp4 files in a folder'''

    file_types = ('.mov', '.mp4')
    file_list = os.listdir(folder)

    # Filter by extension
    L = list(filter(lambda f : Path(f).suffix in file_types, file_list))

    # Ignore hidden files
    L = list(filter(lambda f : f[0] != '.', L))

    # Add path and return
    return [folder + f for f in L]

if __name__ == '__main__':
    os.system('clear')

    # Setup playlist
    last_played = None
    media_folder = '/home/pi/Documents/disorient-tv/'
    playlist_files = get_video_list_from_folder(media_folder)
    playlist = create_playlist_generator(playlist_files)

    while True:
        play_it(next(playlist))
