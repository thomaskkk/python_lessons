from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
SOURCE_DATA = "kanji.csv"
MINUTES_TO_FLIP = 3
LIST_OF_WORDS_TO_LEARN = "words_to_learn.csv"

word = {}

# Read csv -------------------
def read_data():
    try:
        df = pandas.read_csv(f"data/{LIST_OF_WORDS_TO_LEARN}")
    except FileNotFoundError:
        try:
            df = pandas.read_csv(f"data/{SOURCE_DATA}")
        except FileNotFoundError:
            print("No source files found!")
            quit()
    finally:
        dict = df.to_dict(orient="records")
        return dict


def pick_word():
    global word, timer
    screen.after_cancel(timer)
    dict = read_data()
    word = random.choice(dict)
    card.itemconfig(image_id, image=card_front_img)
    card.itemconfig(first_txt_id, text=list(word.keys())[0], fill="black")
    card.itemconfig(second_txt_id, text=list(word.values())[0],  fill="black", font=("MS Gothic", 60))
    timer = screen.after(1000 * (MINUTES_TO_FLIP * 60), func=flip_card)

def flip_card():
    global word
    card.itemconfig(image_id, image=card_back_img)
    card.itemconfig(first_txt_id, text=list(word.keys())[1],  fill="white")
    card.itemconfig(second_txt_id, text=list(word.values())[1],  fill="white",  font=("MS Gothic", 30))

def known_word():
    global word
    dict = read_data()
    dict.remove(word)
    df = pandas.DataFrame.from_dict(dict)
    df.to_csv(f"data/{LIST_OF_WORDS_TO_LEARN}", index=False)
    pick_word()
    

# UI -------------------
screen = Tk()
screen.title("Flash cards")
screen.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)

timer = screen.after(1000 * (MINUTES_TO_FLIP * 60), func=flip_card)

card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
image_id = card.create_image(400, 263, image=card_front_img)
first_txt_id = card.create_text(400, 150, text="", font=("Arial", 35, "italic"))
second_txt_id = card.create_text(400, 263, text="", font=("MS Gothic", 60))
pick_word()
card.grid(row=0, column=0, columnspan=2)


no_img = PhotoImage(file="images/wrong.png")
no_button = Button(image=no_img, highlightthickness=0, bg=BACKGROUND_COLOR, border=0, command=pick_word)
no_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_img, highlightthickness=0, bg=BACKGROUND_COLOR, border=0, command=known_word)
check_button.grid(row=1, column=1)

screen.mainloop()