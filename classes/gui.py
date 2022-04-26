from tkinter import *
from PIL import ImageTk, Image


class App:

    def __init__(self, parent, width=600, height=800, columns=10, rows=10, photo_path="images/Back.png"):
        self.parent = parent
        self.width = width
        self.height = height
        self.columns = columns
        self.rows = rows
        self.photo_path = photo_path
        self.imgs = []
        self.img_num = 0
        self.lemmatize = None
        self.stemming = None
        self.stop_word_removal = None
        self.tokenize = None
        self.segment = None
        self.pos_tagging = None
        self.ml_process = None
        self.segment_bar = None
        self.tokenize_bar = None
        self.stop_word_bar = None
        self.stemming_bar = None
        self.lemmatize_bar = None
        self.pos_tagging_bar = None
        self.bg_image = None
        self.canva = None
        self.create_canvas(self.photo_path)

    def create_canvas(self, photo):
        self.canva = Canvas(self.parent, width=self.width, height=self.height)
        img = Image.open(photo)
        self.bg_image = ImageTk.PhotoImage(img.resize((self.height, self.width)))
        self.canva.create_image(0, 0, anchor=NW, image=self.bg_image)
        self.canva.grid(columnspan=self.columns, rowspan=self.rows)
        self.create_pipline()

    def create_txt(self, txt, x, y, font_type='Raleway', font_color="#23a9f2"):
        txt = Label(self.parent, text=txt, font=font_type, bg=font_color)
        txt.grid(column=y, row=x)

    def create_txt_box(self, hei, wid, pad_x, pad_y, col, ro):
        txt_box = Text(self.parent, height=hei, width=wid, padx=pad_x, pady=pad_y)
        txt_box.grid(column=col, row=ro)
        return txt_box

    def create_button(self, x, y, button_photo=None, wid=200, hig=200, func=None, txt=""):
        if button_photo is not None:
            img = Image.open(button_photo)
            ph = ImageTk.PhotoImage(img.resize((wid, hig)))
            self.imgs.append(ph)
        else:
            self.imgs.append(None)

        btn_label = StringVar()
        btn = Button(self.parent, textvariable=btn_label, command=func, font='Raleway', bg='#CCB0D5', fg='#3c4043',
                     height=hig, width=wid, image=self.imgs[self.img_num])
        btn_label.set(txt)
        btn.grid(column=y, row=x)
        self.img_num += 1

    def create_pipline(self):
        circle_height = self.height / 5
        circle_width = self.width / 5

        self.create_circles(circle_height, circle_width)
        self.create_bars(circle_height, circle_width)

    def create_circles(self, circle_height, circle_width):
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

        self.pos_tagging = self.canva.create_oval(circle_width + 40, (circle_height * 4 + 10),
                                                  circle_width * 2 + 30, circle_height * 5,
                                                  outline="white", fill="white",
                                                  width=2)

        self.ml_process = self.canva.create_oval(circle_width * 2 + 70, (circle_height * 4 + 10),
                                                 circle_width * 3 + 60, circle_height * 5,
                                                 outline="white", fill="white",
                                                 width=2)

    def create_bars(self, circle_height, circle_width):
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

        self.pos_tagging_bar = self.canva.create_rectangle(circle_width * 2 + 20, start_y, circle_width * 2.4, end_y,
                                                           outline="white", fill="white",
                                                           width=2)
