import tkinter as tk
from tkinter import ttk


def get_current_value():  # 傳回目前進度值之顯示字串
    return "目前進度 : " + str(progressbar["value"]) + "%"


def start():
    if progressbar["value"] < progressbar["maximum"]:  # 小於最大值持續增量
        progressbar["value"] += 5  # 進度增量 10
        label["text"] = get_current_value()  # 顯示目前值
    else:
        label["text"] = "已完成!"


def stop():
    progressbar.stop()  # 進度條歸零
    label["text"] = get_current_value()  # 顯示目前值


win = tk.Tk()
win.title("tkinter GUI 測試")
win.geometry("300x200")

progressbar = ttk.Progressbar(win, length=280, mode="determinate")  # 確定模式
progressbar.pack()
ttk.Button(win, text="開始", command=start).pack()
ttk.Button(win, text="停止", command=stop).pack()
label = ttk.Label(win)
label.pack()
win.mainloop()
