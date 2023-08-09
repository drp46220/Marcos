#open music player through macro on mac
import os

#define the filepath here
file_path = "/Applications/Spotify.app"

class SoundPlayer:
    def __init__(self, f):
        self.f = file_path

    def openAudio(): #open in new window
        os.system("open -a" + file_path)

#main
if __name__ == '__main__':
    spotify = SoundPlayer(file_path)
    try:
        SoundPlayer.openAudio()
    except:
        print("Failed to open")