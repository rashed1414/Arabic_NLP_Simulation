"""
File Name: main.py
Author: Rashed Mohamed
This is the main file for the project.Used to run the program,and connect gui with the working functions.
uses the following classes:back.py,gui.py
"""

from tkinter import *
from awesometkinter.bidirender import render_text
from classes.back import AppWork
from classes.gui import App

do = AppWork()
root = Tk()
app = App(root)

inp_txt = app.create_txt_box(5, 50, 10, 10, 5, 1)


def load_txt_btn():
    """
    This function is used to load the text from the file.When the button is clicked.
    """
    try:
        txt = do.load_file()
        inp_txt.insert(-1.0, txt)
    except(TypeError, AttributeError):
        do.create_msg_box("Please Choose txt fil with .txt extension", "Alert")


def segment_btn_act():
    """
    This function is used to segment the text.When the button is clicked.
    """
    out_txt_seg = app.create_txt_box(4, 50, 10, 10, 5, 2)
    seg = do.segment_text(inp_txt.get(-1.0, END))
    out_txt_seg.insert(-1.0, render_text(" " + str(seg) + ", "))
    app.canva.itemconfigure(app.segment, outline='white', fill="#94b53c")
    app.canva.itemconfigure(app.segment_bar, outline='#94b53c', fill="#94b53c")
    app.canva.create_text(app.circle_width / 2, app.circle_height / 2, text=" Segmented ",
                          fill="darkblue", font="Times 20 italic bold")


def tokenize_btn_act():
    """
    This function is used to tokenize the text.When the button is clicked.
    """
    out_txt_tok = app.create_txt_box(4, 50, 10, 10, 5, 3)
    tok = do.tokenize_text(inp_txt.get(1.0, END))
    for i in tok:
        out_txt_tok.insert('1.0', render_text("" + i + ", "))
    app.canva.itemconfigure(app.tokenize, outline='white', fill="#94b53c")
    app.canva.itemconfigure(app.tokenize_bar, outline='#94b53c', fill="#94b53c")

    app.canva.create_text(app.circle_width / 2, app.circle_height * 1.5, text=" Tokenized ",
                          fill="darkblue", font="Times 20 italic bold")


def stopword_remove_btn():
    """
    This function is used to remove stopwords from text.When the button is clicked.
    """
    out_txt_stop = app.create_txt_box(4, 50, 10, 10, 5, 4)
    stop = do.stopword_removal(inp_txt.get(1.0, END))
    for i in stop:
        out_txt_stop.insert('-1.0', render_text("" + i + ", "))
    app.canva.itemconfigure(app.stop_word_removal, outline='white', fill="#94b53c")
    app.canva.itemconfigure(app.stop_word_bar, outline='#94b53c', fill="#94b53c")
    app.canva.create_text(app.circle_width / 2, app.circle_height * 2.5, text=" Stop Word Removed ",
                          fill="darkblue", font="Times 15 italic bold")


def stem_btn_act():
    """
    This function is used to stem the text.When the button is clicked.
    """
    out_txt_stem = app.create_txt_box(4, 50, 10, 10, 5, 5)
    stem = do.stem_text(inp_txt.get(1.0, END))
    for i in stem:
        out_txt_stem.insert('-1.0', render_text("" + i + ", "))
    app.canva.itemconfigure(app.stemming, outline='white', fill="#94b53c")
    app.canva.itemconfigure(app.stemming_bar, outline='#94b53c', fill="#94b53c")
    app.canva.create_text(app.circle_width / 2, app.circle_height * 3.5, text=" Stemmed ",
                          fill="darkblue", font="Times 20 italic bold")


def lemma_btn_act():
    """
    This function is used to lemmatize the text.When the button is clicked.
    """
    out_txt_lemma = app.create_txt_box(4, 50, 10, 10, 5, 5)
    lemma = do.lemmatize_text(inp_txt.get(1.0, END))
    for i in lemma:
        out_txt_lemma.insert('-1.0', render_text("" + i + ", "))
    app.canva.itemconfigure(app.lemmatize, outline='white', fill="#94b53c")
    app.canva.itemconfigure(app.lemmatize_bar, outline='#94b53c', fill="#94b53c")
    app.canva.create_text(app.circle_width / 2, app.circle_height * 4.5, text=" Lemmatized ",
                          fill="darkblue", font="Times 20 italic bold")


def ml_btn_act():
    """
    This function is used to perform machine learning prediction.When the button is clicked.
    """
    app.canva.itemconfigure(app.ml_process, outline='white', fill="#94b53c")
    app.canva.create_text(app.circle_width * 1.5, app.circle_height * 4.6,
                          text=render_text(do.predict_txt(inp_txt.get('1.0', END))),
                          fill="darkblue", font="Times 20 italic bold")


def simulate_btn():
    """
    This function is used to simulate the process.When the button is clicked.
    :uses:segment_btn_act(), tokenize_btn_act(), stopword_remove_btn(), stem_btn_act(), lemma_btn_act(), ml_btn_act()
    """
    segment_btn_act()
    tokenize_btn_act()
    stopword_remove_btn()
    stem_btn_act()
    lemma_btn_act()
    ml_btn_act()


def main():
    """
    This function is used to create the main function of the program,and it's the starting point of the program.
    """
    app.create_txt("This Gui Arabic NLP Pipline Simulation", 0, 5)
    app.create_button(x=1, y=7, wid=10, hig=2, func=load_txt_btn, txt="Load File")
    app.create_button(x=2, y=7, wid=10, hig=2, func=simulate_btn, txt="Simulate")
    app.create_button(1, 9, "images/segment.png", 120, 120, segment_btn_act)
    app.create_button(2, 9, "images/tokenize.png", 120, 120, tokenize_btn_act)
    app.create_button(3, 9, "images/stopremoval.png", 120, 120, stopword_remove_btn)
    app.create_button(4, 9, "images/stem.png", 120, 120, stem_btn_act)
    app.create_button(5, 9, "images/lemma.png", 120, 120, lemma_btn_act)
    app.create_button(6, 9, "images/predict.png", 120, 120, ml_btn_act)


if __name__ == "__main__":
    main()

root.mainloop()
