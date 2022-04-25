from tkinter import *
from classes.gui import App

root = Tk()

app = App(root, 1000, 1000)


def main():
    app.create_txt("This Gui Arabic NLP Pipline Simulation", 0, 5)
    app.create_button(1, 9, "images/segment.png", 150, 150)
    app.create_button(2, 9, "images/tokenize.png", 150, 150)
    app.create_button(3, 9, "images/stopremoval.png", 150, 150)
    app.create_button(4, 9, "images/stem.png", 150, 150)
    app.create_button(5, 9, "images/lema.png", 150, 150)


main()

root.mainloop()
