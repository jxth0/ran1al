import pytube
import pyfiglet
#import #colorama
from colorama import Back,Fore,Style
text=pyfiglet.print_figlet(text=' @ALI',
                           colors='BLUE')

text=pyfiglet.print_figlet(text=' HI IN THE VIDEO DOWNLOAD',
                           colors='RED')


#link=input('ENTER LINL : ')
#pytube.YouTube(link).streams.get_highest_resolution().download('//home/jxth/Desktop/VIDEO /')
#('DONE ...')

x1=input('ENTER 1 OR 2 , 1 = VIDEO : , 2 = AUDIO :')

if x1=='1':
    link=input("ENTER LINK :")
    pytube.YouTube(link).streams.get_highest_resolution().download("/home/jxth/Desktop/VIDEO /")
    print(Fore.RED+'DONE DOWNLOAD VIDEO')

elif x1 == '2':
    link=input("ENTER LINK :")
    pytube.YouTube(link).streams.get_audio_only().download("/home/jxth/Desktop/VIDEO /")
    print(Fore.RED+'DONE DOWNLOAD AUDIO')