from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quizBrain:QuizBrain):
        self.flag = True
        self.quiz = quizBrain
        self.scoreTxt = self.quiz.score
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.iconbitmap("./images/logo.ico")
        self.score = Label(text=f"Score : {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, text="question", fill="black", font=("Arial", 20), width=250)
        self.canvas.grid(column=0, row=1, columnspan=3, pady=50)
        
        self.trueImg = PhotoImage(file="./images/true.png")
        self.trueBtn = Button(image=self.trueImg, highlightthickness=0, width=100, height=100, bg=THEME_COLOR,borderwidth=0,command=self.right)
        self.trueBtn.grid(column=0,row=2,pady=10)
        
        self.falseImg = PhotoImage(file="./images/false.png")
        self.falseBtn = Button(image=self.falseImg, highlightthickness=0, width=100, height=100, bg=THEME_COLOR,borderwidth=0,command=self.wrong)
        self.falseBtn.grid(column=2, row=2)
        self.getNxtQues()
        
        self.window.mainloop()
        
    def right(self):
        ans, scr = self.quiz.check_answer("True")
        if ans:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.score.configure( text=f"Score : {self.quiz.score}")
        self.window.after(1000,self.getNxtQues)
    
    def wrong(self):
        ans, scr = self.quiz.check_answer("False")
        if ans:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.score.configure( text=f"Score : {self.quiz.score}")
        self.window.after(1000,self.getNxtQues)
   
    def getNxtQues(self):
        if self.quiz.still_has_questions():
            self.canvas.configure(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.configure(bg="white")
            q_text = f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}"
            self.canvas.itemconfig(self.question, text=q_text)
            self.trueBtn.config(state="disabled")
            self.falseBtn.config(state="disabled")