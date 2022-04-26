from tkinter import *
from classes.gui import App
from classes.back import *
from awesometkinter.bidirender import add_bidi_support, render_text

root = Tk()
app = App(root, 1000, 1000)

inp_txt = app.create_txt_box(5, 50, 10, 10, 5, 1)
def segment_btn_act():
    seg = segment_text(inp_txt.get(1.0, "end-1c"))
    box = app.create_txt_box(5, 50, 10, 10, 5, 3)
    for i in seg:
        box.insert(-1.0, render_text(""+i + f"  : {seg.index(i) + 1} "))
    app.canva.itemconfigure(app.segment, outline='white', fill="#94b53c")
    app.canva.itemconfigure(app.segment_bar, outline='#94b53c', fill="#94b53c")


def main():
    app.create_txt("This Gui Arabic NLP Pipline Simulation", 0, 5)
    app.create_button(1, 7, wid=10, hig=2, txt="Load File")
    app.create_button(2, 7, wid=10, hig=2, txt="Simulate")
    app.create_button(1, 9, "images/segment.png", 120, 120, segment_btn_act)
    app.create_button(2, 9, "images/tokenize.png", 120, 120)
    app.create_button(3, 9, "images/stopremoval.png", 120, 120)
    app.create_button(4, 9, "images/stem.png", 120, 120)
    app.create_button(5, 9, "images/lema.png", 120, 120)
    # app.create_button(6, 9, 120, 120, "images/lema.png")
    # app.create_button(7, 9, 120, 120, "images/lema.png")


if __name__ == "__main__":
    main()

root.mainloop()
