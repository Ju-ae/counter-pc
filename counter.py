"""
Simple Python Calculator
made by Juae Bae
"""

from tkinter import *


class Counter:
    def __init__(self, master):
        self.count = 0
        self.lbl1 = Label(master, text="COUNTER\n")
        self.lbl2 = Label(master, text="")
        self.btn1 = Button(master, text="+", command=self.output, width=16)

        self.lbl1.grid(row=0, column=0)
        self.lbl2.grid(row=1, column=0)
        self.btn1.grid(row=2, column=0)
        self.output()
    def output(self):
        self.lbl2['text']=self.count
        self.count = self.count + 1

def main():
    root = Tk()
    cnt = Counter(root)
    root.mainloop()


if __name__ == '__main__':main()
