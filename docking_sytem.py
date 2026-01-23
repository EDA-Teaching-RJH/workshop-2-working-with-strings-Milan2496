#docking system
def name():
    shipname = input("What is the name of the ship?")
    shipname = shipname.upper()
    shipname = shipname.replace(" ", "_")
    print(shipname)

def value():
    cargovalue = input("What is the value of the cargo stating the currency?")
    cargovalue = float(cargovalue[1:])
    print(cargovalue)

def reg():
    reg_number = int(input("What is the ship's registration number"))
    if reg_number % 2 == 0:
        print("Starboard Bay")
    else:
        print("Port Bay")

def integrity():
    shieldintegrity = int(input("What is the ship's shield integrity percentage?"))

    if shieldintegrity > 100 or shieldintegrity < 0:
        print("Invalid answer")
    else:
        if shieldintegrity > 89:
            print("Priority Clearance")
        elif shieldintegrity > 49:
            print("Standard Clearance")
        elif shieldintegrity > 19:
            print("Restricted Clearance")
        else:
            print("Docking Denied - Unsafe")

def Divsion():

    DivCode = input("What is your division code")

    match DivCode:
        case "CMD" | "NAV":
            print("Deck 1 Bridge")
        case "ENG":
            print("Deck 5 - Engineering")
        case "SCI" | "MED" :
            print("Deck 3 - Labs")
        case _:
            print("Deck 10 - General Quarters")

name()
value()
reg()
integrity()
Divsion()
    


    









