#open socials through macro
import subprocess

#define the filepath's here
discord_file_path = '/Applications/Discord.app'
mail_file_path= '/Applications/Mail.app'

def openDiscord(): #open discord in new window
    subprocess.Popen(discord_file_path, '-new-tab')

def openMail(): #open mail in new window
    subprocess.Popen(mail_file_path, '-new-tab')

#main
if __name__ == '__main__':
    openDiscord()