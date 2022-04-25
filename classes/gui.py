from tkinter import *
from PIL import ImageTk, Image


class App:

    def __init__(self, parent, width=600, height=800, columns=10, rows=10, photo_path="images/Back.png"):
        self.oval5 = None
        self.oval4 = None
        self.oval3 = None
        self.oval2 = None
        self.oval1 = None
        self.ph = None
        self.bg = None
        self.canva = None
        self.parent = parent
        self.width = width
        self.height = height
        self.columns = columns
        self.rows = rows
        self.photo_path = photo_path
        self.create_canvas(self.photo_path)
        self.imgs = []
        self.img_num = 0

    def create_canvas(self, photo):
        self.canva = Canvas(self.parent, width=self.width, height=self.height)
        img = Image.open(photo)
        self.bg = ImageTk.PhotoImage(img.resize((self.height, self.width)))
        self.canva.create_image(0, 0, anchor=NW, image=self.bg)
        self.canva.grid(columnspan=self.columns, rowspan=self.rows)
        self.create_pipline()

    def create_txt(self, txt, x, y, font_type='Raleway', font_color="#23a9f2"):
        txt = Label(self.parent, text=txt, font=font_type, bg=font_color)
        txt.grid(column=y, row=x)

    def create_txt_box(self, hei, wid, pad_x, pad_y, col, ro):
        input_txt_box = Text(self.parent, height=hei, width=wid, padx=pad_x, pady=pad_y)
        input_txt_box.grid(column=col, row=ro)

    def create_button(self, x, y, button_photo, wid=200, hig=200, txt=""):
        img = Image.open(button_photo)
        ph = ImageTk.PhotoImage(img.resize((wid, hig)))
        self.imgs.append(ph)
        button_txt = StringVar()
        segment_btn = Button(self.parent, textvariable=button_txt,
                             font='Raleway', bg='#CCB0D5', fg='#3c4043',
                             height=hig, width=wid, image=self.imgs[self.img_num])
        button_txt.set(txt)
        segment_btn.grid(column=y, row=x)
        self.img_num += 1

    def create_pipline(self):
        circle_height = self.height / 5
        circle_width = self.width / 5

        self.create_circles(circle_height, circle_width)
        self.create_bars(circle_height, circle_width)

    def create_circles(self, circle_height, circle_width):
        self.oval1 = self.canva.create_oval(10, 0, circle_width, circle_height,
                                            outline="white", fill="white",
                                            width=2)
        self.oval2 = self.canva.create_oval(10, circle_height + 10, circle_width, circle_height * 2,
                                            outline="white", fill="white",
                                            width=2)
        self.oval3 = self.canva.create_oval(10, (circle_height * 2 + 10), circle_width, circle_height * 3,
                                            outline="white", fill="white",
                                            width=2)
        self.oval4 = self.canva.create_oval(10, (circle_height * 3 + 10), circle_width, circle_height * 4,
                                            outline="white", fill="white",
                                            width=2)

        self.oval5 = self.canva.create_oval(10, (circle_height * 4 + 10), circle_width, circle_height * 5,
                                            outline="white", fill="white",
                                            width=2)

    def create_bars(self, circle_height, circle_width):
        #TODO complete bar
        start_x = circle_width * (1 / 3)
        end_x = circle_width * (3 / 4)
        self.canva.create_rectangle(start_x, circle_height - 20, end_x, circle_height + 30,
                                    outline="white", fill="white",
                                    width=2)

        self.canva.create_rectangle(start_x, circle_height * 2 - 20, end_x, circle_height * 2 + 30,
                                    outline="white", fill="white",
                                    width=2)

        self.canva.create_rectangle(start_x, circle_height * 3 - 20, end_x, circle_height * 3 + 30,
                                    outline="white", fill="white",
                                    width=2)

        self.canva.create_rectangle(start_x, circle_height * 4 - 20, end_x, circle_height * 4 + 30,
                                    outline="white", fill="white",
                                    width=2)
