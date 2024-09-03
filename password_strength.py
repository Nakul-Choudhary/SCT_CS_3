import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    criteria = [length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria]
    score = sum(criteria)
    
    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    elif score >= 2:
        return "Weak"
    else:
        return "Very Weak"

def update_strength_indicator(*args):
    password = password_entry.get()
    strength = assess_password_strength(password)
    
    if strength == "Strong":
        strength_label.config(text="Strength: Strong", fg="green")
    elif strength == "Moderate":
        strength_label.config(text="Strength: Moderate", fg="orange")
    elif strength == "Weak":
        strength_label.config(text="Strength: Weak", fg="red")
    else:
        strength_label.config(text="Strength: Very Weak", fg="darkred")
    
    update_requirement_indicator(length_criteria, len(password) >= 8)
    update_requirement_indicator(upper_criteria, re.search(r'[A-Z]', password) is not None)
    update_requirement_indicator(lower_criteria, re.search(r'[a-z]', password) is not None)
    update_requirement_indicator(digit_criteria, re.search(r'\d', password) is not None)
    update_requirement_indicator(special_criteria, re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None)

def update_requirement_indicator(label, condition):
    if condition:
        label.config(fg="green")
        checkmark = "✓"
    else:
        label.config(fg="red")
        checkmark = "✗"
    label.config(text=f"{checkmark} {label.cget('text').split(' ', 1)[-1]}")

def check_password_strength():
    password = password_entry.get()
    strength = assess_password_strength(password)
    messagebox.showinfo("Password Strength", f"Password strength: {strength}")

root = tk.Tk()
root.title("Password Strength Checker")

canvas = tk.Canvas(root, width=500, height=400)
canvas.pack(fill="both", expand=True)

gradient_colors = ["#e0f7fa", "#b2ebf2", "#80deea", "#4dd0e1"]
for i, color in enumerate(gradient_colors):
    canvas.create_rectangle(0, i * (400 // len(gradient_colors)), 500, (i + 1) * (400 // len(gradient_colors)),
                            fill=color, outline="")

frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=350)

tk.Label(frame, text="Enter your password:", bg="#ffffff").grid(row=0, column=0, columnspan=2, pady=10)

password_entry = tk.Entry(frame, show="*", width=40)
password_entry.grid(row=1, column=0, columnspan=2, pady=5)
password_entry.bind("<KeyRelease>", update_strength_indicator)

strength_label = tk.Label(frame, text="Strength: Not Checked", fg="black", bg="#ffffff")
strength_label.grid(row=2, column=0, columnspan=2, pady=10)

requirements = [
    "At least 8 characters",
    "At least one uppercase letter",
    "At least one lowercase letter",
    "At least one digit",
    "At least one special character"
]
for i, req in enumerate(requirements):
    label = tk.Label(frame, text=f"✗ {req}", bg="#ffffff")
    label.grid(row=3 + i, column=0, columnspan=2, sticky="w", pady=2)
    requirements[i] = label

length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria = requirements

check_button = tk.Button(frame, text="Check Strength", command=check_password_strength)
check_button.grid(row=8, column=0, columnspan=2, pady=20)

root.mainloop()
