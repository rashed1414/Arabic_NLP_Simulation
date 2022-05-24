"""
File Name: main.py
Author: Rashed Mohamed
This is the main file for the project.Used to run the program,and connect gui with the working functions.
uses the following classes:back.py,gui.py
"""
import sys
from tkinter import *
from awesometkinter.bidirender import render_text
from classes.back import AppWork
from classes.gui import App

do = AppWork()
root = Tk()
app = App(root)
morph_screen = App(Toplevel(), canvas_type='grid')

inp_txt = app.create_txt_box(hei=7, wid=50, pad_x=10, pad_y=4, x=250, y=160)
out_txt = app.create_txt_box(hei=15, wid=50, pad_x=10, pad_y=4, x=250, y=420)


def show_output(lst):
    """
    This function is used to check if the system is linux or windows.
    and print the text in the text box. Depending on the system.
    """

    for i in lst:
        if sys.platform == 'linux':
            out_txt.insert('1.0', render_text(i + ", "))
        else:
            out_txt.insert('1.0', i + ", ")


def load_txt_btn():
    """
    This function is used to load the text from the file.When the button is clicked.
    """
    try:
        txt = do.load_file()
        if sys.platform == 'linux':
            inp_txt.insert(-1.0, render_text(txt))
        else:
            inp_txt.insert('1.0', txt)
    except(TypeError, AttributeError):
        do.create_msg_box("Please Choose txt fil with .txt extension", "Alert")


def segment_btn_act():
    """
    This function is used to segment the text.When the button is clicked.
    """
    out_txt.delete(1.0, END)
    seg = do.segment_text(inp_txt.get(-1.0, END))
    show_output(seg)
    app.canva.itemconfigure(app.segment, outline='white', fill="#94b53c")
    app.canva.itemconfigure(app.segment_bar, outline='#94b53c', fill="#94b53c")
    app.canva.create_text(app.circle_width / 2, app.circle_height / 2, text=" Segmented ",
                          fill="darkblue", font="Times 20 italic bold")


def tokenize_btn_act():
    """
    This function is used to tokenize the text.When the button is clicked.
    """
    out_txt.delete(1.0, END)
    tok = do.tokenize_text(inp_txt.get(1.0, END))
    show_output(tok)
    app.canva.itemconfigure(app.tokenize, outline='white', fill="#94b53c")
    app.canva.itemconfigure(app.tokenize_bar, outline='#94b53c', fill="#94b53c")
    app.canva.create_text(app.circle_width / 2, app.circle_height * 1.5, text=" Tokenized ",
                          fill="darkblue", font="Times 20 italic bold")


def stopword_remove_btn():
    """
    This function is used to remove stopwords from text.When the button is clicked.
    """
    out_txt.delete(1.0, END)
    stop = do.stopword_removal(inp_txt.get(1.0, END))
    show_output(stop)
    app.canva.itemconfigure(app.stop_word_removal, outline='white', fill="#94b53c")
    app.canva.itemconfigure(app.stop_word_bar, outline='#94b53c', fill="#94b53c")
    app.canva.create_text(app.circle_width / 2, app.circle_height * 2.5, text=" Stop Word Removed ",
                          fill="darkblue", font="Times 15 italic bold")


def stem_btn_act():
    """
    This function is used to stem the text.When the button is clicked.
    """
    out_txt.delete(1.0, END)
    stem = do.stem_text(inp_txt.get(1.0, END))
    show_output(stem)
    app.canva.itemconfigure(app.stemming, outline='white', fill="#94b53c")
    app.canva.itemconfigure(app.stemming_bar, outline='#94b53c', fill="#94b53c")
    app.canva.create_text(app.circle_width / 2, app.circle_height * 3.5, text=" Stemmed ",
                          fill="darkblue", font="Times 20 italic bold")


def lemma_btn_act():
    """
    This function is used to lemmatize the text.When the button is clicked.
    """
    out_txt.delete(1.0, END)
    lemma = do.lemmatize_text(inp_txt.get(1.0, END))
    show_output(lemma)
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


def morph_analysis():
    """
    This function is used to perform morphological analysis.When the button is clicked.
    """
    morph_screen.show_table(do.morph_analysis_txt(inp_txt.get(1.0, END)), width=300, height=500)


def next_screen():
    """
    This function is used to show the next screen.
    """
    if morph_screen.window_status() == 'closed':
        app.close_window()
        morph_screen.construct_window()
    else:
        app.close_window()
        morph_screen.show_window()


def back_screen():
    """
    This function is used to show the previous screen.
    """
    morph_screen.close_window()
    app.show_window()


def main():
    """
    This function is used to create the main function of the program,and it's the starting point of the program.
    """

    morph_screen.close_window()
    app.create_txt(txt="This Gui Arabic NLP Pipline Simulation", x=400, y=50)
    app.create_button(x=650, y=150, wid=10, hig=2, func=load_txt_btn, txt="Load File")
    app.create_button(x=650, y=250, wid=10, hig=2, func=simulate_btn, txt="Simulate")
    app.create_button(x=800, y=50, button_photo="images/segment.png", wid=120, hig=120, func=segment_btn_act)
    app.create_button(x=800, y=175, button_photo="images/tokenize.png", wid=120, hig=120, func=tokenize_btn_act)
    app.create_button(x=800, y=300, button_photo="images/stopremoval.png", wid=120, hig=120, func=stopword_remove_btn)
    app.create_button(x=800, y=475, button_photo="images/stem.png", wid=120, hig=120, func=stem_btn_act)
    app.create_button(x=800, y=600, button_photo="images/lemma.png", wid=120, hig=120, func=lemma_btn_act)
    app.create_button(x=800, y=775, button_photo="images/predict.png", wid=120, hig=120, func=ml_btn_act)
    app.create_button(x=800, y=925, wid=10, hig=2, func=next_screen, txt="Next ->")

    # morph_screen Components
    morph_screen.create_txt(txt="This Gui Arabic NLP Pipline Simulation", x=4, y=0)
    morph_screen.create_button(x=9, y=9, wid=10, hig=2, func=back_screen, txt="<- Back")
    morph_screen.create_button(x=9, y=1, wid=30, hig=4, func=morph_analysis, txt="Show Morphological Analysis")
    app.show_pipline(visible=True)

    # TODO : Configure the windows transitions && window flexibility
    root.protocol('WM_DELETE_WINDOW', app.on_close)
    root.protocol('WM_DELETE_WINDOW', morph_screen.on_close)


if __name__ == "__main__":
    main()

root.mainloop()
