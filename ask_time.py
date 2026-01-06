def ask_time():
    hour = 0
    minute = 0
    second = 0
    while(True):
        try:
            hour = int(input("Veuillez entrer l'heure : "))
            minute = int(input("Veuillez entrer les minutes : "))
            second = int(input("Veuillez entrer les secondes : "))
            if hour > 0 and hour < 24 and minute > 0 and minute < 60 and second > 0 and second < 60:
                return hour,minute,second
            else:
                print("\n les nombres supérieurs à 24 pour l'heure et 60 pour les minutes/secondes sont interdits.\n")
                print("Recommencez !\n")
        except:
            print("L'Entrée que vous venez de saisir est éronnée.")


time = ask_time()
print(time)
