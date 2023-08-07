#open visual studio code through macro
import subprocess

#define the filepath here
file_path = '/Users/prince/Downloads/Visual Studio Code.app'

def openVSC(): #open in new window
    subprocess.Popen(file_path, '-new-tab')

#main
if __name__ == '__main__':
    openVSC()