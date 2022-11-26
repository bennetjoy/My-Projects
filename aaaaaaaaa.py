from pygame import mixer #import mixer module from pygame
import sys #import sys module
 
def musicController():
        print("p : play/pause")#display options
        print("s : stop")
        play=True#initialisation of boolean value play
        while(True):
                query=input()
                if(query=='p'):
                        if(play):
                                mixer.music.pause()# pause the playback of the audio
                                play=False #set play to False
                        else:
                                mixer.music.unpause()#resume the paused playback of the audio
                                play=True #set play to True
                elif(query=='s'):
                        mixer.music.stop() #stop the audio
                        break
                else:
                        print("You selected an invalid option")
                        mixer.music.stop() #stop the audio
                        break
                        
                        
 
 
 
 
print("This is a music player developed using python")
print("Enter your choice")#display the options
print("1.Start the music")
print("2.Exit the program")
n=input()
 
if(int(n)<1 and int(n)>2):#invalid choice
        print("Invalid Option")
        sys.exit()
elif(n=='1'):
            mixer.init()#initialize the mixer module
            mixer.music.load("audiofile.mp3")#load the audio file
            mixer.music.play()#play the loaded audio files
            musicController()#call the function musicController()
 
elif(n=='2'):
            sys.exit()#exit
else:
        print("You selected an invalid option")
        sys.exit()#exit