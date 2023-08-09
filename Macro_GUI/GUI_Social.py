#open socials through macro on mac
import os

#define the filepath's here
discord_file_path = '/Applications/Discord.app'

class Object:
    def openDiscord(): #open discord in new window
        os.system("open -a" + discord_file_path)

#main
if __name__ == '__main__':
    D = Object #D- discord obj
    try:
        D.openDiscord() #call openDiscord
    except:
        print("Failed to open")