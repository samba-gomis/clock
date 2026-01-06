def update_time(time,tic,toc):
    passed_time = round(toc - tic)
    hours = time[0]
    minutes = time[1]
    seconds = time[2] + passed_time

    if seconds > 60:
        minutes += (seconds/60)
        seconds = (seconds%60)

    if minutes > 60:
        hours += (minutes/60)
        minutes = (minutes%60)
        
    if hours > 24:
        hours = (hours%24)
    
    return hours,minutes,seconds