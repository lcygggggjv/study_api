

import time
import datetime


day_time=datetime.datetime.now()


times=int(round(time.time() * 1000 ))  #*1000 是秒转成毫秒


min_timestamp1= datetime.datetime.combine(datetime.datetime.now(),datetime.time.min).timestamp()
max_timestamp2= datetime.datetime.combine(datetime.datetime.now(),datetime.time.max).timestamp()

min_timestamp=int(round(min_timestamp1) *1000)
max_timestamp=int(round(max_timestamp2) *1000)

# print(min_timestamp,max_timestamp)
#
# print(min_timestamp1,max_timestamp2)


local_time1=time.localtime(1671724800000)  
local_time2=time.localtime(1671724800)  #公式通过秒，上面字符串是毫秒，需要转换成秒


new1_time=time.strftime("%Y-%m-%d %H:%M:%S",local_time1)
new2_time=time.strftime("%Y-%m-%d %H:%M:%S",local_time2)

print(new2_time,new1_time)