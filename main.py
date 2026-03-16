from tkinter import *
import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="pomodoro-timer/tomato.png")
canvas.create_image(100, 112, image= tomato_img)
rep = 0
def reset_timer():
    window.after_cancel(timer)
    global rep
    rep = 0
    
    canvas.itemconfig(timer_count, text="00:00")
    check_mark.config(text="", fg= GREEN)
    my_label_timer.config(text="Timer", fg= GREEN)
    

def start_timer():
    global rep
    rep += 1
    

    work_rep = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    # if rep is 1,3,5,7 then do work

    # if its the 8th rep
    if rep % 8 == 0:      
        count_down(long_break)
        rep = 0
        my_label_timer.config(text="Long Break", fg= RED)
    # if its the 2, 4, 6
    elif rep % 2 == 0:    
        count_down(short_break)
        my_label_timer.config(text="Short Break", fg= PINK)
    else:
        count_down(WORK_MIN * 60)
        my_label_timer.config(text="Timer", fg= GREEN)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    ## pass in the timer count 
    canvas.itemconfig(timer_count, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(rep / 2)
        for _ in range(work_session):
            mark += "✓"
            check_mark.config(text=mark, fg= GREEN)
            



timer_count = canvas.create_text(100,112, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(column=1, row=1)


my_label_timer = tkinter.Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
my_label_timer.grid(column=1, row=0)

start_button = tkinter.Button(text="Start",  font=(FONT_NAME, 14, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset",  font=(FONT_NAME, 14, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = tkinter.Label(text="", font=(FONT_NAME, 13, "bold", ), bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3)


window.mainloop()