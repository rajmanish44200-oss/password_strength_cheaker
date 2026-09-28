from datetime import datetime


def save_report(password, score, strength, suggestions):

    now = datetime.now()

    filename = "password_report.txt"

    with open(filename, "a") as file:

        file.write("=" * 40 + "\n")
        file.write("PASSWORD STRENGTH REPORT\n")
        file.write("=" * 40 + "\n")

        file.write(f"Date : {now.strftime('%d-%m-%Y')}\n")
        file.write(f"Time : {now.strftime('%H:%M:%S')}\n\n")

        file.write(f"Password : {password}\n")
        file.write(f"Score : {score}/10\n")
        file.write(f"Strength : {strength}\n\n")

        file.write("Suggestions:\n")

        if suggestions:
            for item in suggestions:
                file.write(f"- {item}\n")
        else:
            file.write("No Suggestions. Password is Secure.\n")

        file.write("\n")
        file.write("=" * 40 + "\n\n")

    print("\nReport Saved Successfully!")