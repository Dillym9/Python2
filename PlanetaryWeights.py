# Planetary Weights

import pickle

def main():
            # Dictionary with planets conversions
    dict_Planet_Grav = {
        'Mercury': 0.38,
        'Venus': 0.91,
        'Moon': 0.165,
        'Mars': 0.38,
        'Jupiter': 2.34,
        'Saturn': 0.93,
        'Uranus': 0.92,
        'Neptune': 1.12,
        'Pluto': 0.066,
    }

    # Open up the pickling file with try / except
    try:
        with open('dmPlanetaryWeights.db', 'rb') as file:
            dictPlanetHistory = pickle.load(file)
    except FileNotFoundError:
        dictPlanetHistory = {}

        # Prompt the user to see previous history
    sHistory = input("Do you wish to see previous Planetary Weights? (Y/N): ").lower()
    if sHistory == 'y':          # print out previous entries
        for sName, fWeights in dictPlanetHistory.items():
            print(f"{sName}, here are your weights on our solar system's planets. ")
            print("\n".join(f"Weight on {sPlanet:10}: {fWeights:10.2f}" for sPlanet, fWeights in fWeights.items()))
            print()

        # While true to prompt user for unique name and enter to quit
    while True:
        sName = input("Enter a unique name (or press Enter to quit): ").strip()
        if sName == "":
            break
        if any(sUniqueName.lower() == sName.lower() for sUniqueName in dictPlanetHistory.keys()):
            print("Name already exists. Please enter a new unique name.")
            continue
            # check for valid weight input
        bValidWeight = False
        while not bValidWeight:
            try:
                fEarthWeight = float(input("Enter your current Earth weight: "))
                bValidWeight = True
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

            # Make a new Dictionary for our weight calcs using other dictionary
        dictPersonWeights = {}
        for sPlanet, fGravWeight in dict_Planet_Grav.items():
            dictPersonWeights[sPlanet] = fEarthWeight * fGravWeight

            #add / update dictPlanetHistory
        dictPlanetHistory[sName] = dictPersonWeights

    # print out name and weights for the planets
        print(f"{sName}, here are your weights on our solar system's planets.")
        for sPlanet, fGravWeight in dictPersonWeights.items():
            print(f"{sPlanet:10}: {fGravWeight:10.2f}")
        print()

        # write to file
        with open('dmPlanetaryWeights.db', 'wb') as file:
            pickle.dump(dictPlanetHistory, file)

main()









