#To be run in cmd prompt by calling python
#One can use this for a experimental physics or problem solving console for experiments.

import sys
import time
import random
def delete_last_line():
    "Use this function to delete the last line in the STDOUT"

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')


########## FOR DEMO ################
if __name__ == "__main__":

    
    
    for i in range(10):
        print(random.randint(1,36))
        
        time.sleep(1)
        delete_last_line()
    
####################################
