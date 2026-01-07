def ask_time():
    hour = 0
    minute = 0
    second = 0
    while(True):
        try:

            hour = int(input("Please provide the hour: "))

            if hour >= 0 and hour < 24:
                while(True):
                    try:


                        minute = int(input("Please provide the minute: "))
                        if minute >= 0 and minute < 60:
                            while(True):
                                try:
                                    second = int(input("Please provide the second: "))
                                    if second >= 0 and second < 60:
                                        return hour,minute,second
                                    else:
                                        print("You must choose the second superior 0 and inferior 60.")
                                except:
                                        print("Your input must be a number.")
                        else:
                            print("You must choose the minute superior 0 and inferior 60.")
                    except:
                            print("Your input must be a number,please try again.")
            else:
                print("You must choose hour superior 0 and inferior 24.")
        except:
            print("Your input must be a number,please try again.")

#time = ask_time()
#print(time)
