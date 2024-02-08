import tkinter as tk

class color_srv():

    def __init__(self, w_count=0, r_count=0, y_count=0, b_count=0):
        self.w_count = w_count
        self.r_count = r_count
        self.y_count = y_count
        self.b_count = b_count
        self.init_count()

    def init_count(self):
        self.window = tk.Tk()  # 建立主視窗 Frame
        # self.w_label = tk.Label(self.window, text=self.w_count, bg='#EEBB00', font=('Arial', 12), width=10, height=2)
        self.w_label = tk.Label(self.window, text=self.w_count, font=('Arial', 12), width=5, height=2)
        self.r_label = tk.Label(self.window, text=self.r_count, font=('Arial', 12), width=5, height=2)
        self.y_label = tk.Label(self.window, text=self.y_count, font=('Arial', 12), width=5, height=2)
        self.b_label = tk.Label(self.window, text=self.b_count, font=('Arial', 12), width=5, height=2)

        self.w_label.place(x=50, y=200)
        self.r_label.place(x=200, y=200)
        self.y_label.place(x=350, y=200)
        self.b_label.place(x=500, y=200)

    def white_add(self):
        self.w_count += 1
        self.w_label["text"] = self.w_count
        self.print_max_color()

    def red_add(self):
        self.r_count += 1
        self.r_label["text"] = self.r_count
        self.print_max_color()

    def yellow_add(self):
        self.y_count += 1
        self.y_label["text"] = self.y_count
        self.print_max_color()

    def blue_add(self):
        self.b_count += 1
        self.b_label["text"] = self.b_count
        self.print_max_color()

    def cle_color(self):
        # 顏色歸0
        self.w_label["text"] = 0
        self.r_label["text"] = 0
        self.y_label["text"] = 0
        self.b_label["text"] = 0
        self.w_count = 0
        self.r_count = 0
        self.y_count = 0
        self.b_count = 0

        self.w_label["font"] = ('Arial', 12)
        self.r_label["font"] = ('Arial', 12)
        self.y_label["font"] = ('Arial', 12)
        self.b_label["font"] = ('Arial', 12)

    def print_max_color(self):
        max_color = max(self.w_count, self.r_count, self.y_count, self.b_count)
        if max_color == self.w_count:
            self.w_label["font"] = ('Arial', 20)
            self.r_label["font"] = ('Arial', 12)
            self.y_label["font"] = ('Arial', 12)
            self.b_label["font"] = ('Arial', 12)
        elif max_color == self.r_count:
            self.w_label["font"] = ('Arial', 12)
            self.r_label["font"] = ('Arial', 20)
            self.y_label["font"] = ('Arial', 12)
            self.b_label["font"] = ('Arial', 12)
        elif max_color == self.y_count:
            self.w_label["font"] = ('Arial', 12)
            self.r_label["font"] = ('Arial', 12)
            self.y_label["font"] = ('Arial', 20)
            self.b_label["font"] = ('Arial', 12)
        elif max_color == self.b_count:
            self.w_label["font"] = ('Arial', 12)
            self.r_label["font"] = ('Arial', 12)
            self.y_label["font"] = ('Arial', 12)
            self.b_label["font"] = ('Arial', 20)

    def do(self):
        self.window.title('ColorCount')  # 設定視窗標題
        # 設定視窗大小為 900x500，視窗（左上角）在螢幕上的座標位置為 (450, 250)
        self.window.geometry("700x400+450+250")

        # 建立按鈕
        button_w = tk.Button(self.window,
                             # text = '黃色V',  # 顯示文字
                             # image=img_btn_yu,
                             # bg="gray",
                             bg="white",  # 底色白色
                             command=self.white_add, height=5, width=10,
                             padx=10, pady=10)  # 按下按鈕所執行的函數
        button_r = tk.Button(self.window, bg="red", command=self.red_add, height=5, width=10, padx=10, pady=10)
        button_y = tk.Button(self.window, bg="yellow", command=self.yellow_add, height=5, width=10, padx=10, pady=10)
        button_b = tk.Button(self.window, bg="blue", command=self.blue_add, height=5, width=10, padx=10, pady=10)
        button_clear = tk.Button(self.window, text='重製', bg="gray", command=self.cle_color)

        button_w.place(x=50, y=70)
        button_r.place(x=200, y=70)
        button_y.place(x=350, y=70)
        button_b.place(x=500, y=70)
        button_clear.place(x=650, y=70)

        label = tk.Label(self.window,  # 文字標示所在視窗
                         text='海底顏色輔助',  # 顯示文字
                         bg='#EEBB00',  # 背景顏色
                         font=('Arial', 12),  # 字型與大小
                         width=15, height=2)  # 文字標示尺寸
        label.pack()

        # y_label = tk.Label(self.window, text=self.y_count, bg='#EEBB00', font=('Arial', 12), width=10, height=2)

        self.y_label.place(x=350, y=200)

        # ttk.Button(self.window, text="開始", command=self.yellow_add).pack()
        # 執行主程式
        self.window.mainloop()


if __name__ == '__main__':
    app = color_srv()
    app.do()
