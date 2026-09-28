import customtkinter as ctk
from checker import check_password
from suggestions import get_suggestions
import random
import string
from PIL import Image


# Window Setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Password Strength Checker")
app.geometry("600x500")
app.iconbitmap("logo.ico")
bg_image = ctk.CTkImage(
    light_image=Image.open("scurity.png"),
    dark_image=Image.open("scurity.png"),
    size=(1700,900)
)

bg_label = ctk.CTkLabel(
    app,
    image=bg_image,
    text=""
)

bg_label.place(x=0, y=0)


# Generate Password Function
def generate_password():
    length = 12

    chars = string.ascii_letters + string.digits + string.punctuation

    password = (
        random.choice(string.ascii_uppercase) +
        random.choice(string.ascii_lowercase) +
        random.choice(string.digits) +
        random.choice(string.punctuation)
    )

    password += ''.join(random.choice(chars) for i in range(length-4))

    password_entry.delete(0, "end")
    password_entry.insert(0, password)


# Copy Password Function
def copy_password():
    password = password_entry.get()

    app.clipboard_clear()
    app.clipboard_append(password)

    result_label.configure(text="Password Copied!")


# Check Password Function
def check():

    password = password_entry.get()

    score, strength = check_password(password)

    suggestions = get_suggestions(password)

    result_label.configure(
        text=f"Score: {score}/10\nStrength: {strength}"
    )

    suggestion_label.configure(
        text=suggestions
    )

    progress.set(score/10)


    # Automatic Color Change
    if score <= 3:
        result_label.configure(text_color="red")
        progress.configure(progress_color="red")

    elif score <= 7:
        result_label.configure(text_color="orange")
        progress.configure(progress_color="orange")

    else:
        result_label.configure(text_color="green")
        progress.configure(progress_color="green")

# Save Report Function
def save_report():

    password = password_entry.get()

    score, strength = check_password(password)

    suggestions = get_suggestions(password)

    with open("Password_Report.txt", "w") as file:

        file.write("Password Strength Report\n")
        file.write("-------------------------\n")
        file.write(f"Score: {score}/10\n")
        file.write(f"Strength: {strength}\n")
        file.write(f"Suggestions: {suggestions}")

    result_label.configure(
        text="Report Saved Successfully!"
    )


# Title
title = ctk.CTkLabel(
    app,
    text="Password Strength Checker",
    font=("Arial", 25)
)

title.pack(pady=20)


# Password Entry
password_entry = ctk.CTkEntry(
    app,
    width=350,
    height=40,
    placeholder_text="Enter Password",
    show="*"
)
def show_password():
    if password_entry.cget("show") == "*":
        password_entry.configure(show="")
        show_button.configure(text="Hide Password")
    else:
        password_entry.configure(show="*")
        show_button.configure(text="Show Password")


show_button = ctk.CTkButton(
    app,
    text="Show Password",
    command=show_password
)
show_button.pack(pady=10)

password_entry.pack(pady=10)


# Buttons

check_button = ctk.CTkButton(
    app,
    text="Check Password",
    command=check,
    
    
)

check_button.pack(pady=5)



generate_button = ctk.CTkButton(
    app,
    text="Generate Strong Password",
    command=generate_password
)

generate_button.pack(pady=5)



copy_button = ctk.CTkButton(
    app,
    text="Copy Password",
    command=copy_password
)

copy_button.pack(pady=5)



save_button = ctk.CTkButton(
    app,
    text="Save Report",
    command=save_report
)

save_button.pack(pady=5)


# Result Label

result_label = ctk.CTkLabel(
    app,
    text="",
    font=("Arial",18)
)

result_label.pack(pady=15)



# Suggestion Label

suggestion_label = ctk.CTkLabel(
    app,
    text="",
    wraplength=500
)

suggestion_label.pack(pady=5)



# Progress Bar

progress = ctk.CTkProgressBar(
    app,
    width=400
)

progress.pack(pady=20)

progress.set(0)


# Appearance Mode Change

def change_mode(choice):
    ctk.set_appearance_mode(choice)


mode_menu = ctk.CTkOptionMenu(
    app,
    values=["Dark", "Light", "System"],
    command=change_mode
)

mode_menu.pack(pady=10)
app.mainloop()