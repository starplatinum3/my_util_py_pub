
import datetime

now=datetime.datetime.now()

time1=now+datetime.timedelta(minutes=46)
print (time1)

# end_time=datetime.datetime(year=2022,hour=3, minute=0, second=0)
# end_time=datetime.datetime.now()
# end_time=datetime.time(hour=3, minute=0, second=0)
end_time=datetime.datetime(year=now.year,month=now.month,day=now.day,hour=3, minute=0, second=0)
# now.hour=3
# now.minute=0
# now.second=0
start_time=end_time-datetime.timedelta(minutes=46)
print ("start_time")
print (start_time)
# 2022-07-11 13:37:48.587907
# start_time
# 2022-07-11 02:14:00