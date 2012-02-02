from cache1 import cache
import song
import sqlite3
import os

## testing connectDB ##################
'''
con = cache.cache()
ob = con.connectDB()
c = ob.cursor()
c.execute("select * from _home_deepak_Downloads_Arabic.mp3 ")
r = c.fetchone()
print r
'''
#######################################

#____ the test to is_cached_folder()________#
#con = cache.cache()
#print con.is_cached_folder("/home/deepak/Downloads")
#print con.is_cached_song("/home/deepak/Downloads/Arabic.mp3")


##########################

#testing create_folder
#con = cache.cache()
#con.create_folder("/home/deepak/Downloads")



#testing create_folder
con = cache()
song_obj  = song.song()
con.insert_folder("/media/New Volume_/Songs")
gen  = con.getAlbumItemList('Rock' ,None)
#gen = con.getArtistList()
#//print song_list.__len__()
for son in gen :
   print son
#   /print "\n\n"



#____ the test to is_cached_folder()________#

#print con.is_cached_song("/home/deepak/Downloads/Arabic.mp3")
#song_obj  = song.song()
#song_obj.create_from_file("/home/deepak/Downloads/am.mp3")




#print os.path.dirname(song_obj.get_filename()).replace('/','_')
