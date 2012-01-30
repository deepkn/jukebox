import kaa.metadata.audio.eyeD3 as eyeD3
import os
import sqlite3
import song 
from config import *
class cache:
   
   def connectDB(self , DBpath=default_DBpath  ):

     """ 
     This function takes a path name as input  default path name
     and returns the connection object that connected to database ,this function
     will raise error if the given path does not exist. If the database is creating
     for the first time it also sets its initial setings such as creating table such as CachedList 
     """
     
     if not (  os.path.exists(os.path.dirname(DBpath))):
       raise IOError('Default database path %s to create JukeBox database does not exist'%os.path.dirname(DBpath))  	
     
         
     if not (os.path.exists(DBpath) ):      # no database is created yet . 
        try:
             conn = sqlite3.connect(DBpath)
            
        except sqlite3.OperationalError:
            raise IOError(' Cannot create a JukeBox database file at %s ' %DBpath )
        else :    
              #______ initial setings________#
              c = conn.cursor() 
              c.execute('''create table CachedList( title text, media text , artist text , mime text, 
                        samplerate real,length real, codec text , bitrate real,fourcc text ,
                        trackno text,album text , genre text ,lyrics text , image_path text ,
                        filename text)''' )    
              conn.commit()
              return conn
     else :
          try :
               conn = sqlite3.connect(DBpath)
               return conn
          except sqlite3.OperationalError:
               raise IOError(' Unable to open a database file at %s'%DBpath) 
          
       
 
  

  # def is_cached_folder(self,foldername):
  #    """  
  #         This function takes a folder name as input and return  true if 
  #         the folder given is cached else returns false  
  #    """
  #    conn = self.connectDB()
  #    c    = conn.cursor()
  #    c.execute("SELECT * FROM CachedList WHERE filename LIKE ''%s'%' " %foldername) 
  #    r = c.fetchone()
  #    if (r  == None) : 
  #       return False
  #    else :
  #       return True 
  # 
   def is_cached_song(self,songname):
      """  
           This function takes a folder name as input and return  true if 
           the folder given is cached else returns false  
      """
      conn = self.connectDB()
      c    = conn.cursor()
      print songname
      c.execute("SELECT * FROM CachedList WHERE filename = '{0}' ".format(songname.replace('/','_'))) 
      r = c.fetchone()
      if (r  == None) : 
         return False
      else :
         return True 
  
############################# todo #####################################   

   def filt(self, row) :
       ara = [0,1,2,3,4,7,9,10,11,12,13,14]
       modrow = []
       for k in ara :
           m = row[k]
           for s in m :
               try:
                   s.decode("utf-8")
               except :
                   #m = m.replace(s,u'_')
                   #i = m.index(s)
                   try:
                       m = m.replace(s,u'_')
                   except :
                       m = row[k].partition(s)[0]
                   print m
                   #modrow.append(m)
               #else:
               #    m = row[k]
           modrow.append(m)
       modrow.insert(5,row[5])
       modrow.insert(6,row[6])
       modrow.insert(8,row[8])
       print"\n\n\n"
       for i in range( 15 ):
          print modrow[i] 
       print "\n\n\n\n"
       print row
       print "\n\n\n\n"
       return modrow     


##########################################################################
    
   def insert_song(self , songname ):
        """
           This function takes a song object and insert the data into apropriate  table
           if the table where song has to insert are not present the function will raise
           error specifing the problem . It will also raise error message for an attempt 
           to cache a particular song more than ones.  
        
        """ 
        extract_object = song.extract()
        song_object = extract_object.extract_file(songname)
        
        if not ( os.path.exists(songname)):
             raise IOError(" The file named %s not found" %songname)
	#if not (self.is_cached_folder(os.path.dirname(songname))):
	#     self.create_folder( os.path.dirname( songname ) )
	     
	iscached = self.is_cached_song(songname)
        if ( self.is_cached_song(songname)) :
             raise IOError(" Attempt to insert an already cached file : %s " %song_object.get_filename())
        else :
	     conn = self.connectDB()
	     c    = conn.cursor()
             mrow = song_object.get_info() 
             row  = self.filt(mrow)
             crow = (
                        row[1],row[2],row[3],row[4],row[5],row[6],
                        row[7],row[8],row[9],row[10],row[11],row[12],
                        row[13],row[14],row[0] ) 
             #print "kkkkkk"
             #print row[0]
             #print os.path.dirname(row[0]).replace('/','_')
	     #print "kkkkkkkkkkkkkkkkkkkkkkkk"
             #for i in range(15):
             #  print row[i] 
             #  print i
            
             #for i in range(15):
             #  print crow[i] 
             #  print i






            
             c.execute("""insert into CachedList values 
                          ( ?,?,?,?,?,?,?,?,?,?,?,?,?,?
                          ,? )""",crow)
                        
            
	     #c.execute(""" insert into {0} values   
             #      ( '{1}','{2}','{3}','{4}',{5},{6},'{7}',{8},
             #        '{9}','{10}','{11}','{12}','{13}','{14}' ,'{15}' )""".format(
             #           os.path.dirname(row[14]).replace('/','_'),
             #           row[1],row[2],row[3],row[4],row[5],row[6],
             #           row[7],row[8],row[9],row[10],row[11],row[12],
             #           row[13],row[14],row[0] ) )                        
             
             #except : pass        
	     conn.commit()
	     print " properly inserted "  # todo not needed step #
	#c.execute("select * from %s" %os.path.dirname(songname).replace('/','_') )
	#r = c.fetchone()
	#print r

   def insert_folder( self , foldername) :
       file_list = filter( lambda n : n.endswith(".mp3") or n.endswith(".ogg") or n.endswith(".flac") ,os.listdir(foldername) )
       for song_file in file_list :
	     self.insert_song( foldername +"/"+ song_file)
   


   def getAlbumItemList( self , genre , artist, searchstring ) :
     
      conn = self.connectDB()
      c    = conn.cursor()
              
      if genre == None and artist == None:
         c.execute( """SELECT album,image_path FROM CachedList 
 		        WHERE album LIKE "%{0}%" ORDER BY album """.format(searchstring)) 
      if genre == None and not artist == None:
         c.execute( """ SELECT album,image_path FROM CachedList WHERE artist = "{0}"
                       AND album LIKE "%{1}%" ORDER BY album""".format(artist,searchstring))
      if not genre == None and artist == None:
         c.execute( """ SELECT album,image_path FROM CachedList WHERE genre = "{0}"
                       AND album LIKE "%{1}%" ORDER BY album""".format(genre,searchstring))
      if not genre == None and not artist == None:     
         c.execute( """ SELECT album,image_path FROM CachedList WHERE artist = "{0}" AND
                       genre = '{1}' AND album LIKE "%{2}%"ORDER BY album""".format(artist,genre,searchstring))

      albumset = []
      optAlbumItemList = []
      for row in c :
         if row[0] not in albumset : 
            optAlbumItemList.append(row)
            albumset.append(row[0])
    
      return optAlbumItemList

   def getGenreList( self ,artist = None ) :
     
      conn = self.connectDB()
      c    = conn.cursor()
              
      if artist == None : 
         c.execute( """ SELECT distinct genre FROM CachedList 
 		       ORDER BY genre """) 
      else :
         c.execute( """ SELECT distinct genre FROM CachedList WHERE artist = "{0}"
                       ORDER BY genre """.format(artist))
      
      genrelist = []
      for row in c :
         genrelist.append(row[0])
    
      return genrelist





   def getArtistList( self ,genre = None ) :
     
      conn = self.connectDB()
      c    = conn.cursor()
              
      if genre == None : 
         c.execute( """ SELECT distinct artist FROM CachedList 
 		       ORDER BY artist """) 
      else :
         c.execute( """ SELECT distinct artist FROM CachedList WHERE genre = "{0}"
                       ORDER BY artist """.format(genre))
      
      artistlist = []
      for row in c :
         artistlist.append(row[0])
    
      return artistlist

   def getSongItemList( self ,album ) :
     
      conn = self.connectDB()
      c    = conn.cursor()
               
      c.execute( """ SELECT filename,title,image_path FROM CachedList 
 		     WHERE album = "{0}" ORDER BY title """.format(album)) 
      
      songitemlist = []
      for row in c :
         songitemlist.append(row)
    
      return songitemlist
   
           


