from tkinter import *

def convert():
    miles = float(input.get())
    result = miles * 1.60934    
    label3.config(text=f"{result}")

window = Tk()
window.minsize(width=300, height=300)
window.title("Mile to Km Converter")

input = Entry(width=10, text=0)
input.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="0")
label3.grid(column=1, row=1)

label4 = Label(text="Km")
label4.grid(column=2, row=1)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)




window.mainloop()