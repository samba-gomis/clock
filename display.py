import time

def display_menu():


        print("\nWhat do you want to do?")
        print("1 - Display time")
        print("2 - Set current time")
        print("3 - Set the alarm time")
        while(True):
            try:
                menu_index = int(input("Your choice: "))
                if menu_index > 0 and menu_index < 4:
                    toc = time.perf_counter()
                    return menu_index, toc
                else:
                    print("Please choose between 1-3.")
            except:
                print("Wrong input,please try again.")

def display_current_time(current_time):
    if current_time[0] < 10:
        hours = "0"+str(current_time[0])
    else:
        hours = str(current_time[0])
    if current_time[1] < 10:
        minutes = "0"+str(current_time[1])
    else:
        minutes = str(current_time[1])
    if current_time[2] < 10:
        seconds = "0"+str(current_time[2])
    else:
        seconds = str(current_time[2])

    print(f"  {hours}:{minutes}:{seconds}", end='\r')