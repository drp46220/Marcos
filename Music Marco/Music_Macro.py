#open music player through macro on mac
import os

#define the filepath here
file_path = "/Applications/Spotify.app"

def openAudio(): #open in new window
    os.system("open -a" + file_path)

#main
if __name__ == '__main__':
    try:
        openAudio()
    except:
        print("Failed to open")