####                PASSWORD VALIDATOR              ####

def main():
    sName = input("Enter your first and last name: ").strip()
    sInitials = sName[0] + sName[sName.find(" ") + 1]
    print(f"\nThank you, {sName}!")

    while True:
        listErrors = []
        sPassword = input("Please enter your desired password: ")

    # Password has to be between 8 - 12
        if len(sPassword) < 8 or len(sPassword) > 12:
            listErrors.append("Password must be between 8 and 12 characters.")

        # Check for 'pass' in password
        if sPassword.lower().startswith("pass"):
            listErrors.append("Password can't start with Pass.")

        # Check for uppercase in password
        if not any(c.isupper() for c in sPassword):
            listErrors.append("Password must contain at least 1 uppercase letter.")

        # Check for lowercase
        if not any(c.islower() for c in sPassword):
            listErrors.append("Password must contain at least 1 lowercase letter.")

        # Check if password contains at least 1 number
        if not any(c.isdigit() for c in sPassword):
            listErrors.append("Password must contain at least 1 number.")

        # Check for specific special characters
        sSpecialChar = "!@#$%^"
        if not any(c in sSpecialChar for c in sPassword):
            listErrors.append("Password must contain at least 1 of these special characters: ! @ # $ % ^")

        # Check for initials
        if sInitials.lower() in sPassword.lower():
            listErrors.append("Password must not contain user initials.")

        # Check for duplicate characters and create a dictionary for the duplicate char
        duplicateChar = {}
        for char in sPassword.lower():
            duplicateChar[char] = duplicateChar.get(char, 0) + 1

        duplicates = {char: count for char, count in duplicateChar.items() if count > 1}
        if duplicates:
            msg = "These characters appear more than once: "
            for char, count in duplicates.items():
                msg += f"'{char}': {count} times"
            listErrors.append(msg)
        print()
        if listErrors:
            for error in listErrors:
                print("-", error)
            print()
        else:
            print("Password is valid and OK to use.")
            break

main()