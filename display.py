def display_menu():
        print("\nWhat do you want to do?")
        print("1 - Display time")
        print("2 - Set current time")
        print("3 - Set alarm time")
        print("4 - Exit")
        while(True):
            try:
                menu_index = int(input("Your choice: "))
                if menu_index > 0 and menu_index < 5:
                    return menu_index
                else:
                    print("Please choose between 1-4.")
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