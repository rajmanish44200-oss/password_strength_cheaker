# ==============================
# Password Strength Checker
# Main File
# ==============================

from checker import check_password
from suggestions import get_suggestions
from generator import generate_password
from report import save_report

def main():
    print("=" * 50)
    print("     PASSWORD STRENGTH CHECKER")
    print("=" * 50)

    while True:
        print("\n1. Check Password")
        print("2. Generate Strong Password")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            password = input("\nEnter Password: ")

            score, strength = check_password(password)

            print("\n----------------------------")
            print("Password Score :", score, "/10")
            print("Password Strength :", strength)

            suggestions = get_suggestions(password)
            save_report(password, score, strength, suggestions)

            if suggestions:
                print("\nSuggestions:")
                for item in suggestions:
                    print("•", item)
            else:
                print("\nExcellent! Your password is secure.")

            print("----------------------------")

        elif choice == "2":
            strong_password = generate_password()
            print("\nGenerated Password :", strong_password)

        elif choice == "3":
            print("\nThank you for using Password Strength Checker.")
            break

        else:
            print("\nInvalid Choice! Please try again.")

if __name__ == "__main__":
    main()