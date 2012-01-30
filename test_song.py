import cache
import song
import sqlite3
import os

extru = song.extract()
song_obj = extru.extract_file("/home/nikhcc/neeyam.mp3")
print song_obj.get_info()
