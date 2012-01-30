import kaa.metadata.audio.eyeD3 as eyeD3
import os
import song

class folder(song):

   count = 0
   foldername = u""
   songlist = []

   #todojuke write docs 
   def get_nth_song(self,n):
      return self.songlist[n]

   def addsong(self,song_obj):
      self.songlist.append(song_obj)
      self.count += 1

   def getcount(self):
      return self.count

   def getfoldername(self):
      return self.foldername

   def createfolder(self,folder_name):

      #checking if the folder exists

      if not os.path.isdir(folder_name):
         raise IOError( "Specified directory does not exist . . .")

      else:

         filelist = os.listdir(folder_name)

         self.foldername = folder_name

         song1 = song()
         
         for f in filelist: # todojuke test for empty folder
            ext = os.path.splitext(f)
            path = folder_name + f
            
            if ext[1] == '.mp3' or ext[1] == '.ogg':
               song1.create_from_file(path)
               self.addsong(song1)

            elif os.path.splitext(f)[1] == '.flac':
               self.createfolder_from_flac(f)


   def createfolder_from_flac(self,flac_file):
      pass
