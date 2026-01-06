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

#current_time=(20,59,23)
#display_current_time(current_time)