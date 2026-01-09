from time import perf_counter
from ask_time import ask_time
from time_control import update_time, pause_time
from display import display_menu, display_current_time
from set import set_current_time, set_alarm_time
from keyboard import is_pressed
from play_sound import play_alarm_sound
import threading

def main():
    time_provided = ask_time()
    alarm_time = (24, 0, 0)
    am_pm = False
    current_time = set_current_time(time_provided)
    tic = perf_counter()
    alarm_playing = False
    
    while True:
        try:
            menu_index = display_menu()
            toc = perf_counter()
            current_time = update_time(current_time, tic, toc)
            
            match menu_index:
                case 1:
                    print("Hit SpaceBar to stop time.")
                    while True:
                        toc = 0
                        display_current_time(current_time, am_pm)
                        tic = perf_counter()
                        
                        while (toc - tic) < 1:
                            if is_pressed("SPACEBAR"):
                                display_current_time(current_time, am_pm, update_mode=False)
                                pause_time()
                                tic = perf_counter()
                            toc = perf_counter()
                        
                        current_time = update_time(current_time, tic, toc)
                        
                        if current_time == alarm_time and not alarm_playing:
                            alarm_playing = True
                            
                            # Launch sound in a thread to avoid blocking
                            sound_thread = threading.Thread(target=play_alarm_sound)
                            sound_thread.daemon = True
                            sound_thread.start()
                            
                            tic = perf_counter()
                            """ input("ALARM! Press Enter to stop...") """
                            alarm_playing = False
                            toc = perf_counter()
                            current_time = update_time(current_time, tic, toc)
                
                case 2:
                    time_provided = ask_time()
                    current_time = set_current_time(time_provided)
                
                case 3:
                    print("Alarm setup:")
                    time_provided = ask_time()
                    alarm_time = set_alarm_time(time_provided)
                    alarm_playing = False
                
                case 4:
                    am_pm = not am_pm
                    if am_pm:
                        print("Switch display to AM/PM mode.")
                    else:
                        print("Switch display to 24h mode.")
                
                case 5:
                    quit()
        
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    main()