#! python3
#mapit.py - launches Google Street with passed address

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    #get address from the command line
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

print('Адрес для поиска: '+address)
webbrowser.open('https://www.google.com/maps/place/' + address)
