#open visual studio code through macro on mac
import os

#define the filepath here
file_path = '/Users/prince/Downloads/Visual Studio Code.app'

class Object:
    def openVSC(): #open in new window
        os.system("open -a" + file_path)

#main
if __name__ == '__main__':
    V = Object()
    try:
        V.openVSC()
    except:
        print("Failed to open")