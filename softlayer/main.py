'''
@author Ahmed Hassan Koshek
'''
#import Cloud as cloud
import SoftLayer
from pprint import pprint as pp
import os
import controller

clear = lambda: os.system('cls')

if __name__ == '__main__':
    clear()

    try:
        while (True):
            control = controller.controller()

    except KeyboardInterrupt:
        clear()
        print("The application is Exiting")
        raise SystemExit




    #spaces
