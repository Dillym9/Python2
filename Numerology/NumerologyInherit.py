from NumerologyLifePathDetails import NumerologyLifePathDetails

def main():
    # Get user's full name with validation for format and alphabetical characters
    while True:
        sName = input("Enter you first and last name!: ")
        if len(sName.split()) != 2:
            print("Please enter first and last name.")
            continue
        if sName.replace(' ', '').isalpha():
            break
        else:
            print("Name can only contain letters! ")

    # Get date of birth with validation for format, separators, and numeric values
    while True:
        sDOB = input("Enter your date of birth (MM/DD/YYYY): ")
        Seperator = sDOB[2]
        StrippedDOB = (sDOB.replace('-', '').replace('/', ''))
        if not StrippedDOB.isdigit() or len(StrippedDOB) != 8:
            print(f"Only enter numbers using MM/DD/YYYY or mm-dd-yyyy ")
            continue
        if Seperator not in ['-', '/'] or sDOB[5] != Seperator:
            print(f"Use / to seperate DOB like MM/DD/YYYY or mm-dd-yyyy  ")
            continue
        break

    # Print output
    numerInherit = NumerologyLifePathDetails(sName, sDOB)
    print(numerInherit)

main()