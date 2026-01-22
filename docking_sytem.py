#docking system

shipname = input("What is the name of the ship?")
shipname = shipname.upper()
shipname = shipname.replace(" ", "_")
print(shipname)

cargovalue = input("What is the value of the cargo stating the currency?")
cargovalue = float(cargovalue[1:])
print(cargovalue)

reg_number = int(input("What is the ship's registration number"))
if reg_number % 2 == 0:
    print("Starboard Bay")
else:
    print("Port Bay")

shieldintegrity = input("What is the ship's shield integrity percentage?")

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

DivCode = input("Whta is your division code")

match DivCode
    case DivCode= ("CMD") or ("NAV")
        print("Deck 1 Bridge")
    









