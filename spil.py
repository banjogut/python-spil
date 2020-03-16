import random

sviner = [
    "ussel",
    "nederdrægtig",
    "kujonagtig",
    "bananformet",
    "Dummernik din"
]

navne = [
    "Batman",
    "Habakuk",
    "Hexia",
    "Gnier",
    "Julemanden",
    
]

egenskaber = [
    "Ærværdige",
    "Ildelugtende",
    "Kloge",
    "Dumme",
]

def nyt_navn():
    navn = random.choice(navne)
    egenskab = random.choice(egenskaber)
    return f"{navn}, den {egenskab}"

fjende_navn = nyt_navn()
fjende_liv = random.randint(900, 1000)

liv = 1000


def kamp(liv, fjende_liv):
    handling = ""

    while handling != "f":
        print(f"Din fjende er {fjende_navn}, han har {fjende_liv} liv.")
        print(f"Du har {liv}, han har {fjende_liv}")

        handling = input("a for at angribe, f for at flygte: ")
        if handling == "a": 
            fjende_skade = random.randint(100, 400)
            fjende_liv = fjende_liv - fjende_skade
            print (f"Du skadede ham {fjende_skade}")
            if fjende_liv <= 0:
                print("DU VANDT")
                kamp(liv, fjende_liv)
                return
            print (f"{fjende_navn} har nu {fjende_liv} liv")
        elif handling == "f": 
            print(f"Du flygter som en {random.choice(sviner)}, lille kujon")
        
        liv = liv - random.randint(50, 300)
        if liv <= 0:
            print("DU TABTE")
            return



kamp(liv, fjende_liv)
print("Spillet er slut!")