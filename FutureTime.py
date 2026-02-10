#FutureTime.py
#Name: Mia Garcia
#Date: 01/29/26
#Assignment: Lab 2 

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  #Ask user for minutes
  newtimehour = int(input("How many hours into the future would you like me to calculate?"))

  newtimeminutes = int(input("How many minutes into the future would you like me to calculate?"))
  #Calculate the time after the user-supplied time has passed.


  futuretimeminutes = (currentMinute + newtimeminutes) % 60 
  extrahour = (currentMinute + newtimeminutes) // 60 

  futuretimehour = (currentHour + newtimehour + extrahour) % 24

  hour = str(futuretimehour)
  if futuretimehour < 10:
   hour = "0" + str(futuretimehour)
  minutes = str (futuretimeminutes)
  if futuretimeminutes < 10:
   minutes = "0" + str(futuretimeminutes)
  
  print("the time is now", hour + ":" + minutes)


  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"

if __name__ == '__main__':
  main()
