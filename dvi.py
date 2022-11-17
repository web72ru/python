import os
import time

clear = lambda: os.system('clear')
# clear()

ezdok = 'Ё'
naprava = True
for i in range(100):
    
    if len(ezdok) == 10:
        naprava = False
    if len(ezdok) == 1:
        naprava = True

    if naprava:
        ezdok = ' ' + ezdok
        print(ezdok)
    else:
        ezdok = ezdok[1:]
        print(ezdok)
    time.sleep(0.1)
    clear()