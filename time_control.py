from keyboard import is_pressed

def update_time(time,tic,toc):
    passed_time = round(toc - tic)
    hours = time[0]
    minutes = time[1]
    seconds = time[2] + passed_time

    if seconds > 59:
        minutes += round(seconds/60)
        seconds = seconds%60

    if minutes > 59:
        hours += round(minutes/60)
        minutes = minutes%60
        
    if hours > 23:
        hours = hours%24
    
    return hours,minutes,seconds

def pause_time():
    print("Time paused! Hit Enter to start time again.")
    while True:
        if is_pressed("ENTER"):
            print("Time restarted successfully.")
            break