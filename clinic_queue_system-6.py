import tkinter as tk
from tkinter import messagebox

# constants for the program
MAX_QUEUE_SIZE = 50
EMERGENCY = "Emergency"
NORMAL = "Normal"
AVERAGE_MINUTES_PER_PATIENT = 10

# this list holds all the patients waiting
patient_queue = []


def add_patient():
    name = entry_name.get()
    age = entry_age.get()
    reason = entry_reason.get()
    priority = priority_var.get()

    # check if any field is empty
    if name == "" or age == "" or reason == "":
        messagebox.showwarning("Missing Info", "Please fill in all the fields")
        return

    if age.isdigit() == False:
        messagebox.showwarning("Invalid Age", "Age must be a number")
        return

    if len(patient_queue) >= MAX_QUEUE_SIZE:
        messagebox.showwarning("Queue Full", "Sorry the queue is full right now")
        return

    new_patient = {"name": name, "age": int(age), "reason": reason, "priority": priority}

    # emergency patients go first
    if priority == EMERGENCY:
        patient_queue.insert(0, new_patient)
    else:
        patient_queue.append(new_patient)

    clear_inputs()
    update_queue_display()


def call_next_patient():
    if len(patient_queue) == 0:
        messagebox.showinfo("Empty", "No patients waiting right now")
        return

    next_patient = patient_queue.pop(0)
    messagebox.showinfo("Next Patient", "Now calling " + next_patient["name"] + ", age " + str(next_patient["age"]) + "\nReason: " + next_patient["reason"])
    update_queue_display()


def calculate_wait_time(position):
    # just multiplying position by average time per patient
    return position * AVERAGE_MINUTES_PER_PATIENT


def update_queue_display():
    queue_listbox.delete(0, tk.END)

    if len(patient_queue) == 0:
        queue_listbox.insert(tk.END, "No patients in queue")
        return

    count = 1
    for patient in patient_queue:
        if patient["priority"] == EMERGENCY:
            tag = "EMERGENCY"
        else:
            tag = "Normal"
        wait = calculate_wait_time(count)
        text = str(count) + ". " + patient["name"] + " (Age " + str(patient["age"]) + ") - " + patient["reason"] + " [" + tag + "] - Wait: " + str(wait) + " min"
        queue_listbox.insert(tk.END, text)
        count = count + 1


def clear_inputs():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_reason.delete(0, tk.END)
    priority_var.set(NORMAL)


def exit_app():
    answer = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if answer == True:
        window.destroy()


# setting up the window
window = tk.Tk()
window.title("RuralCare Clinic Queue System")
window.geometry("560x560")
window.configure(bg="#eaf6f6")

title_label = tk.Label(window, text="RuralCare Clinic Queue System", font=("Arial", 16, "bold"), bg="#eaf6f6")
title_label.pack(pady=10)

form_frame = tk.Frame(window, bg="#eaf6f6")
form_frame.pack(pady=5)

tk.Label(form_frame, text="Patient Name:", bg="#eaf6f6").grid(row=0, column=0, sticky="w", pady=3)
entry_name = tk.Entry(form_frame, width=30)
entry_name.grid(row=0, column=1, pady=3)

tk.Label(form_frame, text="Age:", bg="#eaf6f6").grid(row=1, column=0, sticky="w", pady=3)
entry_age = tk.Entry(form_frame, width=30)
entry_age.grid(row=1, column=1, pady=3)

tk.Label(form_frame, text="Reason for Visit:", bg="#eaf6f6").grid(row=2, column=0, sticky="w", pady=3)
entry_reason = tk.Entry(form_frame, width=30)
entry_reason.grid(row=2, column=1, pady=3)

tk.Label(form_frame, text="Priority:", bg="#eaf6f6").grid(row=3, column=0, sticky="w", pady=3)
priority_var = tk.StringVar(value=NORMAL)
tk.OptionMenu(form_frame, priority_var, NORMAL, EMERGENCY).grid(row=3, column=1, sticky="w", pady=3)

button_frame = tk.Frame(window, bg="#eaf6f6")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Patient", width=13, command=add_patient, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=4)
tk.Button(button_frame, text="Call Next", width=13, command=call_next_patient, bg="#2196F3", fg="white").grid(row=0, column=1, padx=4)
tk.Button(button_frame, text="Clear", width=13, command=clear_inputs, bg="#FF9800", fg="white").grid(row=0, column=2, padx=4)
tk.Button(button_frame, text="Exit", width=13, command=exit_app, bg="#f44336", fg="white").grid(row=0, column=3, padx=4)

tk.Label(window, text="Current Queue:", font=("Arial", 12, "bold"), bg="#eaf6f6").pack(pady=(10, 0))
queue_listbox = tk.Listbox(window, width=60, height=15)
queue_listbox.pack(pady=5)

update_queue_display()

window.mainloop()
