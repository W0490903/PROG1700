mydict = {
    "First Name:":"",
    "Last Name:":"",
    "Home Town:":"",
    "Favourite Food:":"",
    "Favourite Band:":"",
    "Favourite Sport:":""
}

def Firstname():
    Firstname = input("What is your first name?: ").strip()
    mydict.update({"First Name:": Firstname})

def Lastname():
    Lastname = input("What is your last name?: ").strip()
    mydict.update({"Last Name:": Lastname})

def Hometown():
    Hometown = input("What is your home town?: ").strip()
    mydict.update({"Home Town:": Hometown})

def FavFood():
    FavFood = input("What is your favourite food?: ").strip()
    mydict.update({"Favourite Food:": FavFood})

def FavBand():
    FavBand = input("What is your favourite band?: ").strip()
    mydict.update({"Favourite Band:": FavBand})

def FavSport():
    FavSport = input("What is your favourite sport?: ").strip()
    mydict.update({"Favourite Sport:": FavSport})

replay = "yes"

# Main
while replay == "yes":
    Firstname()
    Lastname()
    Hometown()
    FavFood()
    FavBand()
    FavSport()
    print()
    print("Your Bibliography")
    for keys,value in mydict.items():
        print(keys, value)
    replay = input("Would you like to play again? (yes/no): ").lower().strip()