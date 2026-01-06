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




