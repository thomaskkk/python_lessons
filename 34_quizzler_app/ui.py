from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        self.card = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.card_txt = self.card.create_text(150, 125, width=280, text="some text", font=("Arial", 15, "italic"))
        self.card.grid(row=1, column=0, columnspan=2, pady=50)

        check_img = PhotoImage(file="images/true.png")
        self.check_button = Button(
            image=check_img,
            highlightthickness=0,
            bg=THEME_COLOR,
            border=0,
            command=self.set_answer_true
        )
        self.check_button.grid(row=2, column=0)

        no_img = PhotoImage(file="images/false.png")
        self.no_button = Button(
            image=no_img,
            highlightthickness=0,
            bg=THEME_COLOR,
            border=0,
            command=self.set_answer_false
        )
        self.no_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.card.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.card.itemconfig(self.card_txt, text=q_text)
        else:
            self.card.itemconfig(self.card_txt, text="You've reached the end of the quiz.")
            self.check_button.config(state="disabled")
            self.no_button.config(state="disabled")

    def set_answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def set_answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.card.config(bg="green")
        else:
            self.card.config(bg="red")
        self.window.after(1000, self.get_next_question)
        
