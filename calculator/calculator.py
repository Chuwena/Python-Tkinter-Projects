from tkinter import *
from PIL import ImageTk


class MyCalculator:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x550")
        self.root.resizable(False, False)
        self.root.title("My Calculator")
        self.variable = StringVar()
        self.entry_value = ""

        bg = ImageTk.PhotoImage(file="bg-cutebackground.jpg")
        bgLabel = Label(self.root, image=bg)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        inputNum = Entry(self.root,width=612, font=("Arial", 30), textvariable=self.variable)
        inputNum.pack(anchor="center", padx=10, pady=10)

        buttonFrame = Frame(self.root)
        buttonFrame.pack(padx=10, pady=10)
        buttonFrame.columnconfigure(0, weight=1)
        buttonFrame.columnconfigure(1, weight=1)
        buttonFrame.columnconfigure(2, weight=1)
        buttonFrame.columnconfigure(3, weight=1)

        btn1 = Button(buttonFrame,width=11, height=3, text="AC", font=("Arial", 15), relief=GROOVE, background="#ADD8E6", command=lambda:self.clear_field())
        btn1.grid(row=0, column=0, sticky=W + E)
        btn2 = Button(buttonFrame,width=11, height=3, text="^", font=("Arial", 15), relief=GROOVE, background="#ADD8E6", command=lambda:self.add_to_calculation("**"))
        btn2.grid(row=0, column=1, sticky=W + E)
        btn3 = Button(buttonFrame,width=11, height=3, text="%", font=("Arial", 15), relief=GROOVE, background="#ADD8E6", command=lambda:self.add_to_calculation("%"))
        btn3.grid(row=0, column=2, sticky=W + E)
        btn4 = Button(buttonFrame, width=11, height=3, text="√", font=("Arial", 15), relief=GROOVE, background="#ADD8E6", command=lambda: self.add_to_calculation("**0.5"))
        btn4.grid(row=0, column=3, sticky=W + E)

        btn5 = Button(buttonFrame,width=11, height=3, text="7", font=("Arial", 15), relief=GROOVE, command=lambda:self.add_to_calculation("7"))
        btn5.grid(row=1, column=0, sticky=W + E)
        btn6 = Button(buttonFrame,width=11, height=3, text="8", font=("Arial", 15), relief=GROOVE, command=lambda:self.add_to_calculation("8"))
        btn6.grid(row=1, column=1, sticky=W + E)
        btn7 = Button(buttonFrame,width=11, height=3, text="9", font=("Arial", 15), relief=GROOVE, command=lambda:self.add_to_calculation("9"))
        btn7.grid(row=1, column=2, sticky=W + E)
        btn8 = Button(buttonFrame, width=11, height=3, text="/", font=("Arial", 15), relief=GROOVE, background="#ADD8E6", command=lambda: self.add_to_calculation("/"))
        btn8.grid(row=1, column=3, sticky=W + E)

        btn9 = Button(buttonFrame,width=11, height=3, text="4", font=("Arial", 15), relief=GROOVE, command=lambda:self.add_to_calculation("4"))
        btn9.grid(row=2, column=0, sticky=W + E)
        btn10 = Button(buttonFrame,width=11, height=3, text="5", font=("Arial", 15), relief=GROOVE, command=lambda:self.add_to_calculation("5"))
        btn10.grid(row=2, column=1, sticky=W + E)
        btn11 = Button(buttonFrame,width=11, height=3, text="6", font=("Arial", 15), relief=GROOVE, command=lambda:self.add_to_calculation("6"))
        btn11.grid(row=2, column=2, sticky=W + E)
        btn12 = Button(buttonFrame, width=11, height=3, text="x", font=("Arial", 15), relief=GROOVE, background="#ADD8E6", command=lambda: self.add_to_calculation("*"))
        btn12.grid(row=2, column=3, sticky=W + E)

        btn13 = Button(buttonFrame,width=11, height=3, text="1", font=("Arial", 15), relief=GROOVE, command=lambda:self.add_to_calculation("1"))
        btn13.grid(row=3, column=0, sticky=W + E)
        btn14 = Button(buttonFrame,width=11, height=3, text="2", font=("Arial", 15), relief=GROOVE, command=lambda:self.add_to_calculation("2"))
        btn14.grid(row=3, column=1, sticky=W + E)
        btn15 = Button(buttonFrame,width=11, height=3, text="3", font=("Arial", 15), relief=GROOVE, command=lambda:self.add_to_calculation("3"))
        btn15.grid(row=3, column=2, sticky=W + E)
        btn16 = Button(buttonFrame, width=11, height=3, text="-", font=("Arial", 15), relief=GROOVE, background="#ADD8E6", command=lambda: self.add_to_calculation("-"))
        btn16.grid(row=3, column=3, sticky=W + E)

        btn17 = Button(buttonFrame,width=11, height=3, text="0", font=("Arial", 15), relief=GROOVE, command=lambda:self.add_to_calculation("0"))
        btn17.grid(row=4, column=0, sticky=W + E)
        btn18 = Button(buttonFrame,width=11, height=3, text=".", font=("Arial", 15), relief=GROOVE, command=lambda:self.add_to_calculation("."))
        btn18.grid(row=4, column=1, sticky=W + E)
        btn19 = Button(buttonFrame, width=11, height=3, text="+", font=("Arial", 15), relief=GROOVE, background="#ADD8E6", command=lambda: self.add_to_calculation("+"))
        btn19.grid(row=4, column=3, sticky=W + E)
        btn20 = Button(buttonFrame, width=11, height=3, text="=", font=("Arial", 15), relief=GROOVE, background="#ADD8E6", command=lambda: self.evaluate_calculation())
        btn20.grid(row=4, column=2, sticky=W + E)

        buttonFrame.pack(fill="x")

        owner = Label(self.root, text="@2023, Chuwena Calculator")
        owner.pack(side=BOTTOM, anchor="ne")
        self.root.mainloop()

    def add_to_calculation(self, symbol):
        self.entry_value += str(symbol)
        self.variable.set(self.entry_value)

    def evaluate_calculation(self):
        result = eval(self.entry_value)
        self.variable.set(result)

    def clear_field(self):
        self.entry_value = ""
        self.variable.set(self.entry_value)


MyCalculator()
