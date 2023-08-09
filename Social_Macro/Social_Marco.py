#open socials through macro on mac
import os

#define the filepath's here
discord_file_path = '/Applications/Discord.app'
# mail_file_path = '/Applications/Mail.app'

class Object:
    def openDiscord(): #open discord in new window
        os.system("open -a" + discord_file_path)

##### cannot use os to open system applications #####
    # def openMail(): #open mail in new window
    #     os.system("""osascript -e 'tell app "Mail" to open'""")
    #     os.system("open -a" + mail_file_path)
##### cannot use os to open system applications #####

#main
if __name__ == '__main__':
    #make 2 different objects:
    D = Object #D- discord obj
    M = Object #M- mail obj
    try:
        D.openDiscord() #call openDiscord
        # M.openMail()    #call openMail
    except:
        print("Failed to open")