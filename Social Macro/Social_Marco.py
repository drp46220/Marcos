#open socials through macro on mac
import os

#define the filepath's here
discord_file_path = 'Applications/Discord.app'
mail_file_path= 'Applications/Mail.app'

def openDiscord(): #open discord in new window
    os.system("open -a" + discord_file_path)

def openMail(): #open mail in new window
    os.system("open -a" + mail_file_path)


#main
if __name__ == '__main__':
    openDiscord()
    openMail()