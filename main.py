import time
from ask_time import ask_time
from set_current_time import set_current_time
from set_alarm import set_alarm_time
from display_current_time import display_current_time
from display_menu import display_menu
from update_time import update_time

time_provided = ask_time()
current_time = set_current_time(time_provided)
tic = time.perf_counter()
while True:
    try:
        menu_index,toc = display_menu()
        current_time = update_time(current_time,tic,toc)
        match menu_index:
            case 1:
                while True:
                    toc = 0
                    display_current_time(current_time)
                    tic = time.perf_counter()
                    while (toc - tic) < 1:
                        toc = time.perf_counter()
                    current_time = update_time(current_time,tic,toc)
            case 2:
                time_provided = ask_time()
                current_time = set_current_time(time_provided)
            case 3:
                time_provided = ask_time()
                alarm_time = set_alarm_time(time_provided)
    except KeyboardInterrupt:
        pass