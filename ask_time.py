def ask_time():
    hour = 0
    minute = 0
    second = 0
    while(True):
        try:
            hour = int(input("Please provide the hour: "))
            minute = int(input("Please provide the minute: "))
            second = int(input("Please provide the second: "))
            if hour >= 0 and hour < 24 and minute >= 0 and minute < 60 and second >= 0 and second < 60:
                return hour,minute,second
            else:
                print("\n The numbers higher than 24 for the hour and 60 for the minutes/seconds are forbidden.\n")
                print("Please try again !\n")
        except:
            print("Wrong input. Please try again.")


#time = ask_time()
#print(time)
