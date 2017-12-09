import random
import time

def randomDelay(minSec = 0, maxSec = 0):
    if(minSec >= maxSec):
        return True;
    # get rand time
    t = random.randint(minSec,maxSec);
    # sleep for rand-time
    time.sleep(t);
    
    return True;
