from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Some Question',
            font=('Arial', 20, 'italic'),
            fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        tick_image = PhotoImage(file='true.png')
        cross_image = PhotoImage(file='false.png')
        self.tick_button = Button(image=tick_image, highlightthickness=0, command=self.check_if_true)
        self.tick_button.grid(column=0, row=2)
        self.cross_button = Button(image=cross_image, highlightthickness=0, command=self.check_if_false)
        self.cross_button.grid(column=1, row=2)

        self.score = Label(text='Score:0', bg=THEME_COLOR, highlightthickness=0)
        self.score.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end!\nYour score: {self.quiz.score}")
            self.score.config(text='')
            self.tick_button.config(state='disabled')
            self.cross_button.config(state='disabled')

    def check_if_true(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def check_if_false(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
