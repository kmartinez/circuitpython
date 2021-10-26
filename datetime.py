# learn about real time clock
# without an external RTC it resets on power cycles
import rtc
import time

t = rtc.RTC()
print("before we set it:")
print(t.datetime)
t.datetime = time.struct_time((2021, 10, 26, 14, 4, 15, 0, -1, -1))
print("after we set it:")
print(t.datetime)
print("date is: %s/%s/%s" % (t.datetime.tm_year,  t.datetime.tm_mon, t.datetime.tm_mday) )
print("time is: %s:%s:%s" % (t.datetime.tm_hour,  t.datetime.tm_min, t.datetime.tm_sec) )
