import customtkinter as ctk
from checker import check_password
from suggestions import get_suggestions
import random
import string
from PIL import Image
from report import save_report
from datetime import datetime


# =========================================================
# APP SETUP
# =========================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Password Strength Checker")
app.geometry("700x760")
app.resizable(False, False)

try:
    app.iconbitmap("logo.ico")
except:
    pass


# =========================================================
# COLORS
# =========================================================

BG = "#080B12"
CARD = "#111722"
CARD2 = "#171E2B"

TEXT = "#F5F7FA"
SUBTEXT = "#8E99AA"

BLUE = "#4C8DFF"
CYAN = "#00D9FF"
GREEN = "#20E39A"
ORANGE = "#FFB84D"
RED = "#FF4D67"

BUTTON = "#1D2738"
BUTTON_HOVER = "#29364C"


# =========================================================
# BACKGROUND IMAGE
# =========================================================

try:

    bg_image = ctk.CTkImage(
        light_image=Image.open("Raju.png"),
        dark_image=Image.open("Raju.png"),
        size=(700, 760)
    )

    bg_label = ctk.CTkLabel(
        app,
        image=bg_image,
        text=""
    )

    bg_label.place(
        x=0,
        y=0
    )

except:

    app.configure(
        fg_color=BG
    )


# =========================================================
# MAIN CARD SHADOW
# =========================================================

shadow = ctk.CTkFrame(
    app,
    width=590,
    height=690,
    corner_radius=32,
    fg_color="#030509"
)

shadow.place(
    relx=0.5,
    rely=0.5,
    anchor="center",
    x=7,
    y=8
)


# =========================================================
# MAIN CARD
# =========================================================

card = ctk.CTkFrame(
    app,
    width=590,
    height=690,
    corner_radius=32,
    fg_color=CARD,
    border_width=1,
    border_color="#273247"
)

card.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)


# =========================================================
# TITLE
# =========================================================

title = ctk.CTkLabel(
    card,
    text="PASSWORD",
    font=("Arial", 28, "bold"),
    text_color=TEXT
)

title.place(
    relx=0.5,
    y=35,
    anchor="center"
)


title2 = ctk.CTkLabel(
    card,
    text="STRENGTH CHECKER",
    font=("Arial", 15, "bold"),
    text_color=CYAN
)

title2.place(
    relx=0.5,
    y=67,
    anchor="center"
)


subtitle = ctk.CTkLabel(
    card,
    text="Check your password security instantly",
    font=("Arial", 11),
    text_color=SUBTEXT
)

subtitle.place(
    relx=0.5,
    y=94,
    anchor="center"
)


# =========================================================
# PASSWORD INPUT SHADOW
# =========================================================

entry_shadow = ctk.CTkFrame(
    card,
    width=470,
    height=58,
    corner_radius=16,
    fg_color="#05070B"
)

entry_shadow.place(
    relx=0.5,
    y=148,
    anchor="center"
)


# =========================================================
# PASSWORD INPUT FRAME
# =========================================================

password_frame = ctk.CTkFrame(
    card,
    width=470,
    height=58,
    corner_radius=16,
    fg_color=CARD2,
    border_width=1,
    border_color="#2B3A50"
)

password_frame.place(
    relx=0.5,
    y=145,
    anchor="center"
)


# =========================================================
# LOCK ICON
# =========================================================

lock_label = ctk.CTkLabel(
    password_frame,
    text="🔐",
    font=("Arial", 19)
)

lock_label.pack(
    side="left",
    padx=(15, 5)
)


# =========================================================
# PASSWORD ENTRY
# =========================================================

password_entry = ctk.CTkEntry(
    password_frame,
    width=340,
    height=42,
    border_width=0,
    fg_color="transparent",
    placeholder_text="Enter your password",
    placeholder_text_color="#687487",
    text_color=TEXT,
    show="*",
    font=("Arial", 14)
)

password_entry.pack(
    side="left",
    padx=5
)


# =========================================================
# SHOW / HIDE PASSWORD
# =========================================================

def show_password():

    if password_entry.cget("show") == "*":

        password_entry.configure(
            show=""
        )

        show_button.configure(
            text="🙈"
        )

    else:

        password_entry.configure(
            show="*"
        )

        show_button.configure(
            text="👁"
        )


show_button = ctk.CTkButton(
    password_frame,
    text="👁",
    width=45,
    height=35,
    corner_radius=10,
    fg_color="transparent",
    hover_color=BUTTON_HOVER,
    text_color=TEXT,
    command=show_password
)

show_button.pack(
    side="right",
    padx=8
)


# =========================================================
# CIRCULAR / MOON SCORE METER
# =========================================================

score_canvas = ctk.CTkCanvas(
    card,
    width=190,
    height=190,
    bg=CARD,
    highlightthickness=0
)

score_canvas.place(
    relx=0.5,
    y=320,
    anchor="center"
)


def draw_score(score):

    score_canvas.delete("all")

    center = 95
    radius = 70

    # Score color
    if score <= 3:
        color = RED
    elif score <= 7:
        color = ORANGE
    else:
        color = GREEN

    # Clock-style outer circle
    score_canvas.create_oval(
        center - radius,
        center - radius,
        center + radius,
        center + radius,
        outline="#273142",
        width=10
    )

    # Clock ticks from 0 to 10
    import math

    for i in range(11):
        angle = math.radians(-135 + (i * 27))

        outer_x = center + 64 * math.cos(angle)
        outer_y = center + 64 * math.sin(angle)

        inner_x = center + 54 * math.cos(angle)
        inner_y = center + 54 * math.sin(angle)

        tick_color = color if i <= score else "#273142"

        score_canvas.create_line(
            inner_x,
            inner_y,
            outer_x,
            outer_y,
            fill=tick_color,
            width=4
        )

    # Needle moves according to score
    needle_angle = math.radians(-135 + (score * 27))

    needle_length = 48

    needle_x = center + needle_length * math.cos(needle_angle)
    needle_y = center + needle_length * math.sin(needle_angle)

    score_canvas.create_line(
        center,
        center,
        needle_x,
        needle_y,
        fill=color,
        width=5
    )

    # Needle center
    score_canvas.create_oval(
        center - 7,
        center - 7,
        center + 7,
        center + 7,
        fill=color,
        outline=""
    )

    # Score number
    score_canvas.create_text(
        center,
        86,
        text=str(score),
        fill=TEXT,
        font=("Arial", 30, "bold")
    )

    # /10
    score_canvas.create_text(
        center,
        118,
        text="/ 10",
        fill=SUBTEXT,
        font=("Arial", 11)
    )


draw_score(0)


# =========================================================
# RESULT LABEL
# =========================================================

result_label = ctk.CTkLabel(
    card,
    text="CHECK YOUR PASSWORD",
    font=("Arial", 17, "bold"),
    text_color=TEXT
)

result_label.place(
    relx=0.5,
    y=355,
    anchor="center"
)


# =========================================================
# REQUIREMENTS
# =========================================================

requirements_label = ctk.CTkLabel(
    card,
    text=(
        "○  8+ Characters     ○  Uppercase\n"
        "○  Lowercase         ○  Number\n"
        "○  Special Character"
    ),
    font=("Arial", 11),
    text_color=SUBTEXT,
    justify="left"
)

requirements_label.place(
    relx=0.5,
    y=405,
    anchor="center"
)


# =========================================================
# BUTTON CREATOR WITH SHADOW
# =========================================================

def create_shadow_button(
    parent,
    text,
    command,
    x,
    y,
    width=215
):

    # Shadow layer
    button_shadow = ctk.CTkFrame(
        parent,
        width=width,
        height=43,
        corner_radius=13,
        fg_color="#05070B"
    )

    button_shadow.place(
        x=x + 4,
        y=y + 4
    )

    # Actual button
    button = ctk.CTkButton(
        parent,
        text=text,
        width=width,
        height=43,
        corner_radius=13,
        fg_color=BUTTON,
        hover_color=BUTTON_HOVER,
        border_width=1,
        border_color="#33435C",
        text_color=TEXT,
        font=("Arial", 12, "bold"),
        command=command
    )

    button.place(
        x=x,
        y=y
    )

    return button


# =========================================================
# GENERATE PASSWORD
# =========================================================

def generate_password():

    length = 16

    chars = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = (
        random.choice(string.ascii_uppercase) +
        random.choice(string.ascii_lowercase) +
        random.choice(string.digits) +
        random.choice(string.punctuation)
    )

    password += ''.join(
        random.choice(chars)
        for _ in range(length - 4)
    )

    password_entry.delete(
        0,
        "end"
    )

    password_entry.insert(
        0,
        password
    )

    check()


# =========================================================
# COPY PASSWORD
# =========================================================

def copy_password():

    password = password_entry.get()

    if password == "":

        result_label.configure(
            text="ENTER PASSWORD FIRST!",
            text_color=ORANGE
        )

        return

    app.clipboard_clear()

    app.clipboard_append(
        password
    )

    result_label.configure(
        text="✓ PASSWORD COPIED",
        text_color=GREEN
    )


# =========================================================
# CHECK PASSWORD
# =========================================================

def check():

    password = password_entry.get()

    if password == "":

        result_label.configure(
            text="ENTER PASSWORD FIRST!",
            text_color=ORANGE
        )

        draw_score(0)

        requirements_label.configure(
            text=(
                "○  8+ Characters     ○  Uppercase\n"
                "○  Lowercase         ○  Number\n"
                "○  Special Character"
            ),
            text_color=SUBTEXT
        )

        return

    # Backend checking
    score, strength = check_password(
        password
    )

    suggestions = get_suggestions(
        password
    )

    # Circular meter
    draw_score(score)

    # -----------------------------------------
    # Strength Color
    # -----------------------------------------

    if score <= 3:

        color = RED

    elif score <= 7:

        color = ORANGE

    else:

        color = GREEN

    # -----------------------------------------
    # Result
    # -----------------------------------------

    result_label.configure(
        text=strength.upper(),
        text_color=color
    )

    # -----------------------------------------
    # Requirements
    # -----------------------------------------

    length_check = len(password) >= 8

    upper_check = any(
        c.isupper()
        for c in password
    )

    lower_check = any(
        c.islower()
        for c in password
    )

    digit_check = any(
        c.isdigit()
        for c in password
    )

    special_check = any(
        c in string.punctuation
        for c in password
    )

    requirements_label.configure(
        text=(
            f"{'✓' if length_check else '○'}  8+ Characters     "
            f"{'✓' if upper_check else '○'}  Uppercase\n"
            f"{'✓' if lower_check else '○'}  Lowercase         "
            f"{'✓' if digit_check else '○'}  Number\n"
            f"{'✓' if special_check else '○'}  Special Character"
        ),
        text_color=color
    )


# =========================================================
# SAVE REPORT
# =========================================================

def save_report_gui():

    password = password_entry.get()

    if password == "":
        result_label.configure(
            text="ENTER PASSWORD FIRST!",
            text_color=RED
        )
        return

    score, strength = check_password(password)
    suggestions = get_suggestions(password)

    # report.py ka function call
    save_report(
        password,
        score,
        strength,
        suggestions
    )

    # Success message
    result_label.configure(
        text="✓ REPORT SAVED SUCCESSFULLY",
        text_color=GREEN
    )

    # Report window
    report_window = ctk.CTkToplevel(app)
    report_window.title("Password Report")
    report_window.geometry("500x550")
    report_window.resizable(False, False)

    report_title = ctk.CTkLabel(
        report_window,
        text="PASSWORD STRENGTH REPORT",
        font=ctk.CTkFont(
            size=20,
            weight="bold"
        )
    )

    report_title.pack(pady=(25, 15))

    report_box = ctk.CTkTextbox(
        report_window,
        width=440,
        height=400,
        corner_radius=12,
        font=ctk.CTkFont(
            family="Consolas",
            size=12
        )
    )

    report_box.pack(
        padx=20,
        pady=10
    )

    now = datetime.now()

    if suggestions:
        suggestion_text = suggestions
    else:
        suggestion_text = "No Suggestions. Password is Secure."

    report_text = f"""
========================================
       PASSWORD STRENGTH REPORT
========================================

Date : {now.strftime('%d-%m-%Y')}
Time : {now.strftime('%H:%M:%S')}

Password : {password}
Score : {score}/10
Strength : {strength}

Suggestions:
{suggestion_text}

========================================
"""

    report_box.insert(
        "1.0",
        report_text
    )

    report_box.configure(
        state="disabled"
    )

    close_button = ctk.CTkButton(
        report_window,
        text="CLOSE",
        width=150,
        height=40,
        corner_radius=10,
        command=report_window.destroy
    )

    close_button.pack(pady=10)


# =========================================================
# BUTTONS
# =========================================================

check_button = create_shadow_button(
    card,
    "🔍  CHECK PASSWORD",
    check,
    45,
    470
)


generate_button = create_shadow_button(
    card,
    "⚡  GENERATE STRONG",
    generate_password,
    320,
    470
)


copy_button = create_shadow_button(
    card,
    "📋  COPY PASSWORD",
    copy_password,
    45,
    525
)


save_button = create_shadow_button(
    card,
    "💾  SAVE REPORT",
    save_report_gui,
    320,
    525
)


# =========================================================
# THEME MENU
# =========================================================

mode_menu = ctk.CTkOptionMenu(
    card,
    values=[
        "Dark",
        "Light",
        "System"
    ],
    width=130,
    height=30,
    corner_radius=10,
    fg_color=BUTTON,
    button_color=BLUE,
    button_hover_color=BUTTON_HOVER,
    command=lambda choice:
        ctk.set_appearance_mode(choice)
)

mode_menu.set("Dark")

mode_menu.place(
    relx=0.5,
    y=620,
    anchor="center"
)


# =========================================================
# FOOTER
# =========================================================

footer = ctk.CTkLabel(
    card,
    text="SECURITY • PRIVACY • PASSWORD PROTECTION",
    font=("Arial", 9),
    text_color="#536074"
)

footer.place(
    relx=0.5,
    y=660,
    anchor="center"
)


# =========================================================
# START APPLICATION
# =========================================================

app.mainloop()
