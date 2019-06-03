import datetime

print(dir(datetime), "\n") #list all class which is inside in datetime package

#print(help(datetime.date))

#date(year, month, day)
mydate = datetime.date(1998, 12, 3) #At when legends born 
print( "mydate: ", mydate, "\n")

#year
print("year: ", mydate.year)

#month
print("month: ", mydate.month)

#day
print("day: ", mydate.day, "\n")

#datetime.timedelta which lets you to substract/add time and date from any date
mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100)
print("datetime.timedelta(100): ", mill + dt, "\n")

#default format date(yyy,mm,d)
#Day-name, Month-name Day-#, Year
print(mydate.strftime("%A %B %d, %Y")) 

message = "Legends are born on {:%A %B %d, %Y}."
print(message.format(mydate))

#launch datetime = 1996-05-31 10:56:00

launch_date = datetime.date(1996,5,31)
launch_time = datetime.time(10,56,0)
launch_datetime = datetime.datetime(1996,5,31,10,56,0)

print(launch_date)
print(launch_time)
print(launch_datetime)

#hour
print(launch_time.hour)

#minute
print(launch_time.minute)

#secound
print(launch_time.second)

#current datetime:
now = datetime.datetime.today()
print(now)

#convert string to datetime: method:strptime()
demonitization_string = "11/8/2016"
demonitization_datetime = datetime.datetime.strptime(demonitization_string,"%m/%d/%Y")
print(demonitization_datetime)


