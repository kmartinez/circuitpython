# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
# Example on using SD card on a metro M4 grand central
# should probably storage.unmount after completion
import os
import busio
import digitalio
import board
import busio
import sdcardio
import storage

def appenddata(d):
    with open("/sd/datafile.txt", "a") as fp:
        fp.write(d)

def mountsd():
    spi = busio.SPI(board.SD_SCK, MOSI=board.SD_MOSI, MISO=board.SD_MISO)
    cs = board.SD_CS
    sdcard = sdcardio.SDCard(spi, cs)
    vfs = storage.VfsFat(sdcard)
    storage.mount(vfs, "/sd")


# ls SD
def print_directory(path, tabs=0):
    for file in os.listdir(path):
        stats = os.stat(path + "/" + file)
        filesize = stats[6]
        isdir = stats[0] & 0x4000

        if filesize < 1000:
            sizestr = str(filesize) + " bytes"
        elif filesize < 1000000:
            sizestr = "%0.1f KB" % (filesize / 1000)
        else:
            sizestr = "%0.1f MB" % (filesize / 1000000)

        prettyprintname = ""
        for _ in range(tabs):
            prettyprintname += "   "
        prettyprintname += file
        if isdir:
            prettyprintname += "/"
        print("{0:<40} Size: {1:>10}".format(prettyprintname, sizestr))

        # recursively print directory contents
        if isdir:
            print_directory(path + "/" + file, tabs + 1)

def diskfree():
    info = os.statvfs("/sd")
    return(info[0] * info[3])

mountsd()
print("Files on filesystem:")
print_directory("/sd")

print(f"bytes free: ",diskfree())
