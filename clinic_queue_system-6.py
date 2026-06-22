"""
RuralCare Clinic Queue System
------------------------------------------------------
A GUI application that helps rural health clinics in Sierra Leone
manage patient waiting queues fairly, prioritizing emergencies.

Aligned with SDG 3: Good Health and Well-Being.

This program demonstrates structured programming principles:
- Variables and constants
- Data types (string, int, list, dictionary, boolean)
- Decision structures (if / else)
- Loops (for)
- Logical calculations (estimated wait time)
- Multiple user-defined functions
------------------------------------------------------
"""

import tkinter as tk
from tkinter import messagebox

# ---------------------------------------------------------
# CONSTANTS
# ---------------------------------------------------------
MAX_QUEUE_SIZE = 50
EMERGENCY = "Emergency"
NORMAL = "Normal"
AVERAGE_MINUTES_PER_PATIENT = 10

# ---------------------------------------------------------
# GLOBAL VARIABLE
# ---------------------------------------------------------
patient_queue = []


# ---------------------------------------------------------
# FUNCTION 1: Add a patient to the queue
# ---------------------------------------------------------
def add_patient():

    name = entry_name.get().strip()
    age = entry_age.get().strip()
    reason = entry_reason.get().strip()
    priority = priority_var.get()

    # Check that every field is filled in
    if name == "" or age == "" or reason == "":
        messagebox.showwarning(
            "Missing Information",
            "Please fill in all fields."
        )
        return

    # Validate age
    if not age.isdigit():
        messagebox.showwarning(
            "Invalid Age",
            "Age must be a valid number."
        )
        return

    age = int(age)

    if age < 1 or age > 120:
        messagebox.showwarning(
            "Invalid Age",
            "Please enter an age between 1 and 120."
        )
        return

    # Check queue size
    if len(patient_queue) >= MAX_QUEUE_SIZE:
        messagebox.showwarning(
            "Queue Full",
            "The clinic queue is full."
        )
        return

    # Prevent duplicate patients
    for existing_patient in patient_queue:
        if (
            existing_patient["name"].lower() == name.lower()
            and existing_patient["age"] == age
        ):
            messagebox.showwarning(
                "Duplicate Patient",
                "This patient is already in the queue."
            )
            return

    patient = {
        "name": name,
        "age": age,
        "reason": reason,
        "priority": priority
    }

    # Emergencies are prioritised,
    # but maintain the order in which they arrive.
    if priority == EMERGENCY:

        insert_position = 0

        for existing_patient in patient_queue:
            if existing_patient["priority"] == EMERGENCY:
                insert_position += 1
            else:
                break

        patient_queue.insert(insert_position, patient)

    else:
        patient_queue.append(patient)

    clear_inputs()
    update_queue_display()


# ---------------------------------------------------------
# FUNCTION 2: Call the next patient
# ---------------------------------------------------------
def call_next_patient():

    if len(patient_queue) == 0:
        messagebox.showinfo(
            "Queue Empty",
            "There are no patients waiting."
        )
        return

    next_patient = patient_queue.pop(0)

    messagebox.showinfo(
        "Next Patient",
        f"Now calling: {next_patient['name']} (Age {next_patient['age']})\n"
        f"Reason: {next_patient['reason']}"
    )

    update_queue_display()


# ---------------------------------------------------------
# FUNCTION 3: Calculate estimated wait time
# ---------------------------------------------------------
def calculate_wait_time(position):

    return position * AVERAGE_MINUTES_PER_PATIENT


# ---------------------------------------------------------
# FUNCTION 4: Refresh the queue display
# ---------------------------------------------------------
def update_queue_display():

    queue_listbox.delete(0, tk.END)

    if len(patient_queue) == 0:
        queue_listbox.insert(
            tk.END,
            "No patients in queue."
        )
        return

    # Display every patient currently waiting
    for index, patient in enumerate(patient_queue, start=1):

        wait = calculate_wait_time(index - 1)

        line = (
            f"{index}. "
            f"{patient['name']} "
            f"(Age {patient['age']}) - "
            f"{patient['reason']} "
            f"[{patient['priority']}] "
            f"- Est. wait: {wait} min"
        )

        queue_listbox.insert(tk.END, line)# ---------------------------------------------------------
# FUNCTION 5: Clear the input fields
# ---------------------------------------------------------
def clear_inputs():

    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_reason.delete(0, tk.END)

    priority_var.set(NORMAL)


# ---------------------------------------------------------
# FUNCTION 6: Exit the application safely
# ---------------------------------------------------------
def exit_app():

    confirm = messagebox.askyesno(
        "Exit",
        "Are you sure you want to exit?"
    )

    if confirm:
        window.destroy()


# ---------------------------------------------------------
# GUI SETUP
# ---------------------------------------------------------
window = tk.Tk()

window.title("RuralCare Clinic Queue System")
window.geometry("560x560")
window.configure(bg="#eaf6f6")


# ---------------------------------------------------------
# Title
# ---------------------------------------------------------
tk.Label(
    window,
    text="RuralCare Clinic Queue System",
    font=("Arial", 16, "bold"),
    bg="#eaf6f6"
).pack(pady=10)


# ---------------------------------------------------------
# Input Form
# ---------------------------------------------------------
form_frame = tk.Frame(window, bg="#eaf6f6")
form_frame.pack(pady=5)

tk.Label(
    form_frame,
    text="Patient Name:",
    bg="#eaf6f6"
).grid(row=0, column=0, sticky="w", pady=3)

entry_name = tk.Entry(form_frame, width=30)
entry_name.grid(row=0, column=1, pady=3)


tk.Label(
    form_frame,
    text="Age:",
    bg="#eaf6f6"
).grid(row=1, column=0, sticky="w", pady=3)

entry_age = tk.Entry(form_frame, width=30)
entry_age.grid(row=1, column=1, pady=3)


tk.Label(
    form_frame,
    text="Reason for Visit:",
    bg="#eaf6f6"
).grid(row=2, column=0, sticky="w", pady=3)

entry_reason = tk.Entry(form_frame, width=30)
entry_reason.grid(row=2, column=1, pady=3)


tk.Label(
    form_frame,
    text="Priority:",
    bg="#eaf6f6"
).grid(row=3, column=0, sticky="w", pady=3)

priority_var = tk.StringVar(value=NORMAL)

tk.OptionMenu(
    form_frame,
    priority_var,
    NORMAL,
    EMERGENCY
).grid(row=3, column=1, sticky="w", pady=3)


# ---------------------------------------------------------
# Buttons
# ---------------------------------------------------------
button_frame = tk.Frame(window, bg="#eaf6f6")
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Add Patient",
    width=13,
    command=add_patient,
    bg="#4CAF50",
    fg="white"
).grid(row=0, column=0, padx=4)

tk.Button(
    button_frame,
    text="Call Next",
    width=13,
    command=call_next_patient,
    bg="#2196F3",
    fg="white"
).grid(row=0, column=1, padx=4)

tk.Button(
    button_frame,
    text="Clear",
    width=13,
    command=clear_inputs,
    bg="#FF9800",
    fg="white"
).grid(row=0, column=2, padx=4)

tk.Button(
    button_frame,
    text="Exit",
    width=13,
    command=exit_app,
    bg="#f44336",
    fg="white"
).grid(row=0, column=3, padx=4)


# ---------------------------------------------------------
# Queue Display
# ---------------------------------------------------------
tk.Label(
    window,
    text="Current Queue:",
    font=("Arial", 12, "bold"),
    bg="#eaf6f6"
).pack(pady=(10, 0))

queue_listbox = tk.Listbox(
    window,
    width=60,
    height=15
)

queue_listbox.pack(pady=5)


# ---------------------------------------------------------
# Start the program
# ---------------------------------------------------------
update_queue_display()

window.mainloop()
