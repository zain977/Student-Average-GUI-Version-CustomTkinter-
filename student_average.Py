import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")  

def calculate_avg():
    marks = []
    for entry in entries:
        value = entry.get()
        if value.strip() != "":  # لو الخانة مش فاضية
            try:
                marks.append(float(value))
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers")
                return
    if marks:
        avg = sum(marks) / len(marks)
        messagebox.showinfo("Result", f"Average mark for {name_entry.get()} is: {avg}")
    else:
        messagebox.showwarning("Warning", "Please enter at least one mark")

def focus_next(event, idx):
    if idx + 1 < len(entries):
        entries[idx + 1].focus()

# النافذة
app = ctk.CTk()
app.title("Student Average Calculator")
app.geometry("500x700")

# العنوان
title_label = ctk.CTkLabel(app, text="📊 Student Average Calculator", font=("Arial", 22, "bold"))
title_label.pack(pady=20)

# إدخال الاسم
name_entry = ctk.CTkEntry(app, placeholder_text="Enter Student Name", width=300, height=40, font=("Arial", 16))
name_entry.pack(pady=10)

# 10 خانات للدرجات
entries = []
for i in range(10):
    entry = ctk.CTkEntry(app, placeholder_text=f"Enter Mark {i+1}", width=300, height=40, font=("Arial", 16))
    entry.pack(pady=5)
    entry.bind("<Return>", lambda event, idx=i: focus_next(event, idx))  # لما تدوس Enter ينزل عالخانة اللي بعدها
    entries.append(entry)

# زرار الحساب
calc_button = ctk.CTkButton(app, text="Calculate Average", command=calculate_avg, width=200, height=40, font=("Arial", 16, "bold"))
calc_button.pack(pady=20)

app.mainloop()