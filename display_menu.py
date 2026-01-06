import time

def display_menu():
    
    print("\nWhat do you want to do?")
    print("1 - Display time")
    print("2 - Set current time")
    print("3 - Set the alarm time")

    menu_index = int(input("Your choice: "))
    toc = time.perf_counter()

    return menu_index, toc
