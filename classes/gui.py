"""
File Name: gui.py
Classes: App
This file contains the classes for the GUI.
used in: main.py
"""

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from pandastable import Table


class App:
    """
    Class for the GUI.
    contains the main window,buttons,labels,images,Pipline shape,etc.
    this class contain : 1 init Function and 7 functions for the gui
    """

    def __init__(self, parent, width=1000, height=1000, columns=10, rows=10,
                 photo_path="images/Back.png", canvas_type='pack'):
        """
        init function for the gui
        :param parent: tkinter parent (main window)
        :param width: width of the main window(default=1000)(int)
        :param height: height of the main window(default=1000)(int)
        :param columns: columns of the main window(default=10)(int)
        :param rows: rows of the main window(default=10)(int)
        :param photo_path: path of the background image(default="images/Back.png")(str)
        :param canvas_type: type of the canvas(default="pack")(str)
        """

        self.canvas_type = canvas_type
        self.parent = parent
        self.width = width
        self.height = height
        self.columns = columns
        self.rows = rows
        self.photo_path = photo_path
        self.images = []
        self.img_num = 0
        self.circle_width = None
        self.circle_height = None
        self.lemmatize = None
        self.stemming = None
        self.stop_word_removal = None
        self.tokenize = None
        self.segment = None
        self.ml_process = None
        self.segment_bar = None
        self.tokenize_bar = None
        self.stop_word_bar = None
        self.stemming_bar = None
        self.lemmatize_bar = None
        self.ml_process_bar = None
        self.bg_image = None
        self.canva = None
        self.create_canvas(self.photo_path, self.canvas_type)

    def create_canvas(self, photo, canvas_type):
        """
        create the canvas for the gui
        :param canvas_type: type of the canvas(default="pack")(str)
        :param photo: background image path(str)
        :create: canvas With the background image
        """

        self.canva = Canvas(self.parent, width=self.width, height=self.height)
        img = Image.open(photo)
        self.bg_image = ImageTk.PhotoImage(img.resize((self.height, self.width)))
        self.canva.create_image(0, 0, anchor=NW, image=self.bg_image)
        if canvas_type == 'pack':
            self.canva.pack()
        else:
            self.canva.grid(columnspan=self.columns, rowspan=self.rows)

    def create_txt(self, txt, x, y, font_type='Raleway', font_color="#23a9f2"):
        """
        create a label with the given text
        :param txt: text to be displayed(str)
        :param x: x coordinate(int)
        :param y: y coordinate(int)
        :param font_type: type of font(default="Raleway")(str)
        :param font_color: color of the font(default="#23a9f2")(str)
        :create: label with the given text
        """
        txt = Label(self.parent, text=txt, font=font_type, bg=font_color)
        if self.canvas_type == 'pack':
            txt.place(x=x, y=y)
        else:
            txt.grid(row=y, column=x)

    def create_txt_box(self, hei, wid, pad_x, pad_y, x, y):
        """
        create a text box
        :param y: y coordinate(int)
        :param x: x coordinate(int)
        :param hei: height of the text box(int)
        :param wid: width of the text box(int)
        :param pad_x: padding x(int)
        :param pad_y: padding y(int)
        :return: text box(tkinter text)
        """
        txt_box = Text(self.parent, height=hei, width=wid, padx=pad_x, pady=pad_y)
        if self.canvas_type == 'pack':
            txt_box.place(x=x, y=y)

        else:
            txt_box.grid(row=y, column=x)
        return txt_box

    def create_button(self, x, y, button_photo=None, wid=200, hig=200, func=None, txt=""):
        """
        create a button
        :param x: x coordinate(int)
        :param y: y coordinate(int)
        :param button_photo: photo of the button(default=None)(str)
        :param wid: width of the button(default=200)(int)
        :param hig: height of the button(default=200)(int)
        :param func: function to be called when the button is clicked(default=None)(function)
        :param txt: text to be displayed on the button(default="")(str)
        :create: button with the given properties
        """
        if button_photo is not None:
            img = Image.open(button_photo)
            ph = ImageTk.PhotoImage(img.resize((wid, hig)))
            self.images.append(ph)
        else:
            self.images.append(None)

        btn_label = StringVar()
        btn = Button(self.parent, textvariable=btn_label, command=func, font='Raleway', bg='#CCB0D5', fg='#3c4043',
                     height=hig, width=wid, image=self.images[self.img_num])
        btn_label.set(txt)
        if self.canvas_type == 'pack':
            btn.place(x=x, y=y)
        else:
            btn.grid(row=y, column=x)
        self.img_num += 1

    def show_table(self, df, width, height):
        """ show the dataframe in a table format """

        pt = Table(self.parent, dataframe=df, showtoolbar=True,
                   showstatusbar=True, width=width, height=height)
        pt.show()

    def show_pipline(self, visible=False):
        """
        create the pipline for the gui
        :use: create_circle,create_bars
        :create: pipline with the given properties
        """
        if visible:
            self.circle_height = self.height / 5
            self.circle_width = self.width / 5

            self.create_circles(self.circle_height, self.circle_width)
            self.create_bars(self.circle_height, self.circle_width)

    def create_circles(self, circle_height, circle_width):
        """
        create the circles for the pipline
        :param circle_height: height of the circle(int)
        :param circle_width: width of the circle(int)
        :create: circles with the given properties
        """
        self.segment = self.canva.create_oval(10, 0, circle_width, circle_height,
                                              outline="white", fill="white",
                                              width=2)
        self.tokenize = self.canva.create_oval(10, circle_height + 10, circle_width, circle_height * 2,
                                               outline="white", fill="white",
                                               width=2)
        self.stop_word_removal = self.canva.create_oval(10, (circle_height * 2 + 10), circle_width, circle_height * 3,
                                                        outline="white", fill="white",
                                                        width=2)
        self.stemming = self.canva.create_oval(10, (circle_height * 3 + 10), circle_width, circle_height * 4,
                                               outline="white", fill="white",
                                               width=2)

        self.lemmatize = self.canva.create_oval(10, (circle_height * 4 + 10), circle_width, circle_height * 5,
                                                outline="white", fill="white",
                                                width=2)

        self.ml_process = self.canva.create_oval(circle_width + 40, (circle_height * 4 + 10),
                                                 circle_width * 2 + 30, circle_height * 5,
                                                 outline="white", fill="white",
                                                 width=2)

    def create_bars(self, circle_height, circle_width):
        """
        create the bars for the pipline
        :param circle_height: circle height(int)
        :param circle_width: circle width(int)
        :create: bars with the given properties
        """
        start_x = circle_width * (1 / 3)
        end_x = circle_width * (3 / 4)
        start_y = circle_height * 5 - circle_height * (2 / 3)
        end_y = circle_height * 5 - circle_height * (1 / 4)

        self.segment_bar = self.canva.create_rectangle(start_x, circle_height - 20, end_x, circle_height + 20,
                                                       outline="white", fill="white",
                                                       width=2)

        self.tokenize_bar = self.canva.create_rectangle(start_x, circle_height * 2 - 20, end_x, circle_height * 2 + 20,
                                                        outline="white", fill="white",
                                                        width=2)

        self.stop_word_bar = self.canva.create_rectangle(start_x, circle_height * 3 - 20, end_x, circle_height * 3 + 20,
                                                         outline="white", fill="white",
                                                         width=2)

        self.stemming_bar = self.canva.create_rectangle(start_x, circle_height * 4 - 20, end_x, circle_height * 4 + 20,
                                                        outline="white", fill="white",
                                                        width=2)

        self.lemmatize_bar = self.canva.create_rectangle(circle_width - 10, start_y, circle_width * 1.25, end_y,
                                                         outline="white", fill="white",
                                                         width=2)

    def close_window(self):
        """
        close the window
        """
        self.parent.withdraw()

    def show_window(self):
        """
        show the window
        """
        self.parent.deiconify()

    def destroy_window(self):
        """
        destroy the window
        """
        self.parent.destroy()

    def construct_window(self):
        """
        construct the window
        """
        self.parent.tkraise()

    def window_status(self):
        """
        check if the window is open
        """

        return self.parent.state()

    def on_close(self):
        """
        close the window
        """
        response = messagebox.askyesno('Exit', 'Are you sure you want to exit?')
        if response:
            self.parent.destroy()
