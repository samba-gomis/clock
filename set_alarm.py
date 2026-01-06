def set_alarm_time(time_provided):
    
    hour, minute, second = time_provided
    alarm_time = (hour, minute, second)
    print("Alarm time successfully set!")
    return alarm_time
