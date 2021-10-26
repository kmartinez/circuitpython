# try deep sleep - it wakes up and restarts
import time
import alarm
import board
import digitalio

blueled = digitalio.DigitalInOut(board.LED)
blueled.direction = digitalio.Direction.OUTPUT

# light blue LED so we know it is up for 3s
blueled.value = True
time.sleep(3)

# Set an alarm for 10 seconds from now.
time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 10)

# Deep sleep until the alarm goes off. Then restart the program.
alarm.exit_and_deep_sleep_until_alarms(time_alarm)

