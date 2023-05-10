print("Welcome to the tip calculator.")
bill = float(input("What was the total? $"))
totalpeople = int(input("How many people to split the bill? "))
optiontip = [10,12,15]

while True:
    selectedtip = int(input("What percent would you like to give 10, 12, or 15? " ))
    if selectedtip not in optiontip:
        print("Invalid Option")
        
    else:
        break

tip = (selectedtip/100)

whateveryonepays = (bill*tip) + bill

print(f"Each person pays {round(whateveryonepays,2)}, with %{float(tip)} as a tip")