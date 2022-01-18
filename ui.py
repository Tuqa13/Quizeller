from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, my_quiz: QuizBrain):
        self.quiz = my_quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Score:
        self.score = Label(text=f'Score: 0 ', bg=THEME_COLOR, fg='white', font=('Arial', 15, 'bold'))
        self.score.grid(column=1, row=0, sticky=E)

        # Buttons:
        true_img = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_img, bg=THEME_COLOR,
                                  highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)
        false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_img, bg=THEME_COLOR,
                                   highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        # Canvas:
        self.canvas = Canvas(height=250, width=300, bg='white')
        self.my_text = self.canvas.create_text(150,
                                               125,
                                               width=280,
                                               text=self.quiz.next_question(),
                                               fill='#222831',
                                               font=('Arial', 18, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.window.mainloop()

        self.get_next_question(self.quiz)

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            self.score.config(text=f'Score: {self.quiz.score}')
            new_text = self.quiz.next_question()
            self.canvas.itemconfig(self.my_text, text=new_text)
        else:
            self.canvas.itemconfig(self.my_text, text='You have reached the end of the Quiz')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('true'))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('false'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)






