def display_menu():
        print("\nWhat do you want to do?")
        print("1 - Display time")
        print("2 - Set current time")
        print("3 - Set alarm time")
        print("4 - Switch 24h / 12h AM-PM")
        print("5 - Exit")
        while(True):
            try:
                menu_index = int(input("Your choice: "))
                if menu_index > 0 and menu_index < 6:
                    return menu_index
                else:
                    print("Please choose between 1-5.")
            except:
                print("Wrong input,please try again.")

def display_current_time(current_time, am_pm):
    h, m, s = current_time
    suffix = ""

    if am_pm:  # mode 12h
        if h == 0:
            hours = "12"
            suffix = " AM"
        elif h < 12:
            hours = f"{h:02d}"
            suffix = " AM"
        elif h == 12:
            hours = "12"
            suffix = " PM"
        else:
            hours = f"{h-12:02d}"
            suffix = " PM"
    else:  # mode 24h
        hours = f"{h:02d}"

    if m < 10:
        minutes = "0" + str(m)
    else:
        minutes = str(m)

    if s < 10:
        seconds = "0" + str(s)
    else:
        seconds = str(s)

    print(f"  {hours}:{minutes}:{seconds}{suffix}", end='\r')