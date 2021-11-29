from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.text = self.canvas.create_text(150, 125, text="Question text!", font=("Arial", 15, "italic"), width=270)
        self.canvas.grid(row=2, column=1, columnspan=2, padx=30, pady=30)

        self.score_label = Label(text="Score: ", font=("Arial", 10, "bold"), bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=1, column=2)

        check_image = PhotoImage(file='images/true.png')
        self.check_button = Button(image=check_image, command=self.true_pressed)
        self.check_button.grid(row=3, column=1)

        cross_image = PhotoImage(file='images/false.png')
        self.cross_button = Button(image=cross_image, command=self.false_pressed)
        self.cross_button.grid(row=3, column=2)

        self.get_question()
        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the quiz.")
            self.canvas.config(bg='green')
            self.check_button.config(state='disabled')
            self.cross_button.config(state='disabled')

    def true_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.result(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.result(is_right)

    def result(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_question)
