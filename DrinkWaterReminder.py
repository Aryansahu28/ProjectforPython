import time
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
# We are making Drink Water time reminder. Here we are taking initial time as input and after each hour or some time given by the user then we remind them
print("Enter the time to start the timer for Drink water reminder and here the time is in the format of 24 hours format ")
set_time_hour = int(input("Enter the hour to start :"))
set_time_min = int(input("Enter the minute to start :"))

s_hour = int(time.strftime("%H"))
s_min = int(time.strftime("%M"))


if s_hour == set_time_hour and s_min == set_time_min :
        speaker.speak("Time to Drink Water")
        while True:
            if s_hour == set_time_hour + 1 and s_min == set_time_min:
                speaker.speak("Time to Drink Water")
                keep_moving = int(input("If you want to continue the remainder enter 1 : "))
                if keep_moving == 1:
                     continue
                else:
                     break    
                



