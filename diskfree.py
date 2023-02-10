# how to find out flash-remaining in circuitpython
import os

def diskfree():
    info = os.statvfs("/")
    return(info[0] * info[3])
    
print(f"bytes free: ",diskfree())
