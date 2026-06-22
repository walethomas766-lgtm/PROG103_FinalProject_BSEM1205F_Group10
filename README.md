# RuralCare Clinic Queue System

A GUI-based Python application that helps rural and peri-urban health clinics in Sierra Leone manage patient waiting queues fairly, automatically prioritizing emergency cases over routine visits.

**Course:** PROG103 – Principles of Structured Programming
**Institution:** Limkokwing University of Creative Technology, Sierra Leone
**Aligned SDG:** SDG 3 – Good Health and Well-Being (Target 3.8: Universal Health Coverage)

## Problem

Many small clinics in Sierra Leone manage patient queues using paper sign-in sheets or no formal system at all. This means emergency cases can end up waiting behind routine ones, records get lost, and staff have no quick overview of who is waiting. RuralCare Clinic Queue System replaces this with a simple, structured digital queue.

## Features

- Register patients with name, age, reason for visit, and priority level
- Emergency patients are automatically moved to the front of the queue
- Estimated wait time calculated and displayed per patient
- "Call Next" feature to process patients in the correct order
- Input validation to prevent incomplete or invalid records
- Clean, simple tkinter GUI requiring no internet connection or special hardware

## How to Run

1. Make sure Python 3 is installed (tkinter is included by default).
2. Clone this repository or download `clinic_queue_system.py`.
3. Run it:
   ```
   python clinic_queue_system.py
   ```
   or open and run it directly in PyCharm / any Python IDE.

## Structured Programming Concepts Demonstrated

- **Variables & Constants** – e.g. `patient_queue`, `MAX_QUEUE_SIZE`, `AVERAGE_MINUTES_PER_PATIENT`
- **Data Types** – strings, integers, lists, dictionaries, booleans
- **Decision Structures** – `if / elif / else` for validation and priority sorting
- **Iteration** – `for` loop to render the queue display
- **Logical Calculations** – estimated wait time per patient
- **User-Defined Functions** – six functions, each with a single responsibility

## Data, Privacy & Compliance

Patient data is kept in memory only for the duration of a session and is never transmitted externally, limiting exposure of sensitive health information. The interface uses plain, accessible language for ease of use by staff with varying digital literacy.

## License

This project is released under the MIT License — see the LICENSE file for details. It may be freely used, adapted, and improved by other developers, clinics, or NGOs.

## Authors

Hansel O.M Weston
Churchill Wallace
Joseph Ibrahim M'beteh
Limkokwing University of Creative Technology, Sierra Leone
