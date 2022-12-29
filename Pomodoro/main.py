from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
cnt = 0
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_clicked():
    print("Reset button pressed")
    window.after_cancel(timer)
    lbl1.config(text="Timer")
    lbl2.config(text=" ")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    print("Start button pressed")
    countdown(1*60)

def start_clicked():
    global reps 
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        lbl1.config(text="Long Break!!! Enjoy")
        countdown(long_break_sec)
        lbl2.config(text="✓✓✓✓")
    elif reps % 2 == 0:
        lbl1.config(text="Short Break")
        countdown(short_break_sec)
        if reps==2:
            lbl2.config(text="✓")
        elif reps==4:
            lbl2.config(text="✓✓")
        elif reps==6:
            lbl2.config(text="✓✓✓")
    else:
        lbl1.config(text="Work")
        countdown(work_sec)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(cnt):
    cnt_min = math.floor(cnt/60)
    cnt_sec = cnt%60
    if cnt_sec==0:
        cnt_sec="00"
    elif cnt_sec<10:
        cnt_sec = "0"+str(cnt_sec)
    if cnt_min==0:
        cnt_min="00"
    elif cnt_min<10:
        cnt_min = "0"+str(cnt_min)
    canvas.itemconfig(timer_text, text=f"{cnt_min}:{cnt_sec}")
    if cnt>0:
        global timer
        timer = window.after(1000, countdown, cnt-1)
    else:
        start_clicked()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


lbl1 = Label(text="Timer",font=(FONT_NAME, 32, "bold"), fg=GREEN, bg=YELLOW)
lbl1.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
# countdown(5)
start = Button(text="Start", command=start_clicked, bg=GREEN,fg=YELLOW,bd=1, width=8, height=1, activebackground=PINK, activeforeground=GREEN, font=(FONT_NAME, 11, "bold"), highlightthickness=0)
start.grid(column=0, row=2)

lbl2 = Label(text=" ",font=(FONT_NAME, 11, "bold"), fg=GREEN, bg=YELLOW,pady=10)
lbl2.grid(column=1, row=2)

reset = Button(text="Reset", command=reset_clicked, bg=GREEN,fg=YELLOW,bd=1, width=8, height=1, activebackground=PINK, activeforeground=GREEN, font=(FONT_NAME, 11, "bold"), highlightthickness=0)
reset.grid(column=2, row=2)














window.mainloop()