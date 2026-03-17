# 🍅 Pomodoro Timer (Python Tkinter)

A **Pomodoro Timer desktop application** built with **Python and Tkinter** that helps users manage their time using the **Pomodoro productivity technique**.

The application automatically alternates between **work sessions and breaks**, helping users maintain focus while avoiding burnout.

This project demonstrates **GUI development, event-driven programming, countdown timers, and session management in Python**.

---
<img width="544" height="467" alt="image" src="https://github.com/user-attachments/assets/0aeb3132-b57d-4d4f-9a7e-a5b8000f69d7" />


## Features

- Pomodoro work session timer
- Short break and long break automation
- Countdown timer display
- Visual checkmarks for completed work sessions
- Reset functionality
- Simple and clean graphical user interface
- Tomato-themed Pomodoro design

---

## Technologies Used

- Python 3
- Tkinter (GUI framework)
- Math module
- Event-driven programming

---

## 📂 Project Structure

```bash
pomodoro-timer/
│
├── main.py                # Main application code
├── pomodoro-timer/
│   └── tomato.png         # Pomodoro tomato image used in UI
│
└── README.md
```

---

## Requirements

Make sure **Python 3.x** is installed.

Download Python:

https://www.python.org/downloads/

Check installation:

#### Windows

```bash
python --version
```

#### Mac / Linux

```bash
python3 --version
```

Tkinter usually comes **pre-installed with Python**, so no additional installation is required.

---

## How to Run the Application

### Clone the Repository

```bash
git clone https://github.com/adebayoadesugba/pomodoro-timer.git
```

### Navigate into the Project Folder

```bash
cd pomodoro-timer
```

### Run the Program

#### Windows

```bash
python main.py
```

#### Mac / Linux

```bash
python3 main.py
```

The Pomodoro timer window will open.

---

## How the Pomodoro Technique Works

The Pomodoro technique divides work into focused intervals:

1. **Work Session** – 25 minutes of focused work  
2. **Short Break** – 5 minutes rest  
3. Repeat this cycle 4 times  
4. **Long Break** – 15–30 minutes after 4 work sessions  

This application automates the cycle.

---

## How to Use

1. Click **Start** to begin the Pomodoro timer.
2. The timer starts with a **work session**.
3. After each session, the timer automatically switches to a **break session**.
4. Completed work sessions are marked with **✓ checkmarks**.
5. Click **Reset** to stop and restart the timer.

---

## Key Concepts Demonstrated

This project demonstrates several important programming concepts:

- GUI development using **Tkinter**
- Event-driven programming
- Countdown timers with `after()`
- Session tracking using counters
- Dynamic UI updates
- Managing asynchronous callbacks

---

## Future Improvements

Possible upgrades for this project:

- Add customizable work and break durations
- Add sound notification when sessions end
- Add task tracking
- Add desktop notifications
- Add dark mode UI
- Export productivity reports

---

## 👨‍💻 Author

**Adebayo Adesugba**

Full Stack Developer  
Python | JavaScript | React | Node.js | AI Development

---

⭐ If you like this project, feel free to **star the repository on GitHub**.
