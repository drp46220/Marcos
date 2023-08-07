#open music player through macro
import subprocess

#define the filepath here
file_path = '/Applications/Spotify.app'

def openAudio(): #open in new window
    subprocess.open(file_path)

#main
if __name__ == '__main__':
    openAudio()