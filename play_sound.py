from playsound3 import playsound

def play_alarm_sound():
    try:
        playsound('./alarms/alarm1.mp3')
    except Exception as e:
        print(f"Error playing sound: {e}")