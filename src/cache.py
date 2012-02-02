import kaa.metadata.audio.eyeD3 as eyeD3
import os
import sqlite3
import song 
from config import *
class cache:
   
   def connectDB(self , DBpath = default_DBpath  ):

     """ 
     This function takes a path name as input '/tmp/JukeBoxDB' as default path name
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
              c.execute('create table CachedList(FolderName text)')
              conn.commit()
              return conn
     else :
          try :
               conn = sqlite3.connect(DBpath)
               return conn
          except sqlite3.OperationalError:
               raise IOError(' Unable to open a database file at %s'%DBpath) 
          
       
 
  

   def is_cached_folder(self,foldername):
      """  
           This function takes a folder name as input and return  true if 
           the folder given is cached else returns false  
      """
      conn = self.connectDB()
      c    = conn.cursor()
      try : 
          c.execute("select * from CachedList where FolderName = '%s' " %foldername)
      except sqlite3.OperationalError: 
            #creating cached list will be done by self.connect()
            raise IOError('The database does not contain CachedList')
      else :
	r = c.fetchone()
	if (r  == None) : 
          return False
	else :
          return True 
   
   
   def is_cached_song(self,songname):
      """  
           This function takes a folder name as input and return  true if 
           the song given is cached else returns false  
      """
      
      conn = self.connectDB()
      c    = conn.cursor()
      foldername = os.path.dirname(songname)
      if( self.is_cached_folder( foldername) ) : 
             #try :   # todo clear after error clarification 
             #print foldername.replace('/','_')
             #print songname
             c.execute("select * from {0} where filename = '{1}' ".format(foldername.replace('/','_'),songname))
             #except  sqlite3.OperationalError:
             #     raise  IOError( " The folder name is cached but no folder table named %s is present in cache "%foldername)

      	     r = c.fetchone()
      	     if (r  == None) : 
                  return False
             else :
                  return True

      else :      
         raise  IOError( " The folder named %s is not cached "%foldername) 
         
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
	if not (self.is_cached_folder(os.path.dirname(songname))):
	     self.create_folder( os.path.dirname( songname ) )
	     
        try :
	     iscached = self.is_cached_song(songname)
	except  IOError,error:
             raise IOError(" cannot insert the song object filename = {0} because {1} ".format(song_object.get_filename() ,error))          
        if ( iscached ) :
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
             print "kkkkkk"
             print row[0]
             print os.path.dirname(row[0]).replace('/','_')
	     print "kkkkkkkkkkkkkkkkkkkkkkkk"
             #for i in range(15):
             #  print row[i] 
             #  print i
            
             for i in range(15):
               print crow[i] 
               print i






            
             c.execute("insert into %s values ( ?,?,?,?,?,?,?,?,?,?,?,?,?,?,? )" %os.path.dirname(row[0]).replace('/','_'), crow)
                        
            
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
       self.create_folder( foldername)
       file_list = filter( lambda n : n.endswith(".mp3") or n.endswith(".ogg") or n.endswith(".flac") ,os.listdir(foldername) )
       for song_file in file_list :
	     self.insert_song( foldername +"/"+ song_file)
    
    
   def create_folder(self , foldername ):
        """
           This function takes a folder name and creates a data table for that folder.
           If the table is already present this function will truncate all data present in 
           that table.  
        
        """ 
        conn = self.connectDB()
        c    = conn.cursor()
        #todo check whether the given foldername exists
        if not (self.is_cached_folder( foldername ) ) :
           c.execute( " insert into CachedList values( '%s')" %foldername )
           c.execute('''create table %s ( title text, media text , artist text , mime text, 
                        samplerate real,length real, codec text , bitrate real,fourcc text ,
                        trackno text,album text , genre text ,lyrics text , image_path text ,
                        filename text)''' % foldername.replace('/','_') )    

        else :
            c.execute("drop table %s " %foldername.replace('/','_' ))
            c.execute('''create table %s ( title text, media text , artist text , mime text, 
                         samplerate real,length real, codec text , bitrate real,fourcc text ,
                         trackno text,album text , genre text ,lyrics text , image_path text ,
                         filename text)''' % foldername.replace('/','_') )
            


     
   def read_song( self,songname ):
      """  
           This function takes a song name as input and return the song object from the cache  
           if the song given is not cached the function will raise error 
      """
      song_object = song.song()
      conn = self.connectDB()
      c    = conn.cursor()
      foldername = os.path.dirname(songname)
      if( self.is_cached_folder( foldername) ) : 
             try :
                  c.execute("select * from {0} where filename = '{1}' " .format(foldername.replace('/','_') ,songname))
             except  sqlite3.OperationalError:
                  raise  IOError( " The folder name is cached but no folder table named %s is present in cache "%foldername)

      	     r = c.fetchone()
      	     if (r  == None) : 
                  raise IOError( " Cannot read this file , The file named %s is not cached "%songname) 
             else :
                  song_object.create_from_row(r)  
                  return song_object
      else :      
         raise  IOError( " The folder named %s is not cached "%foldername) 
       
   def songfromrow(self,row):
      song_object = song.song()
      song_object.create_from_row(row)
      return song_object
        
   def read_folder( self,foldername,order ):
      """  
           This function takes a song name as input and return the song object from the cache  
           if the song given is not cached the function will raise error 
      """
      conn = self.connectDB()
      c = conn.cursor()
      if( self.is_cached_folder( foldername) ) : 
             
             c.execute("select * from {0} order by {1}".format(foldername.replace('/','_'),order))             
             song_list   = []
	     for row in c :
		song_list.append(self.songfromrow(row))
             
             return song_list
      else :      
         raise  IOError( " The folder named %s is not cached "%foldername) 
   

