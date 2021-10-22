# circuitpython shows free ram and flash
import gc, os

print("Memory Info - gc.mem_free()")
print("{} kBytes\n".format(gc.mem_free()/1024))

flash = os.statvfs('/')
flash_size = flash[0] * flash[2]
flash_free = flash[0] * flash[3]
print("Flash - os.statvfs('/')")
print("Size: {} MBytes\nFree: {} MBytes\n".format(flash_size/(1024*1024), flash_free/(1024*1024)))




