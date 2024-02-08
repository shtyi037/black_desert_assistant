from service.color_count import color_srv
import tkinter as tk
from tkinter import ttk

def create_page(notebook, text):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=text)
    return frame

#
# # 创建第一个分页
# page1 = create_page(notebook, "页1")
# label1 = ttk.Label(page1, text="这是第一页的内容")
# label1.pack(padx=10, pady=10)
#
# # 创建第二个分页
# page2 = create_page(notebook, "页2")
# label2 = ttk.Label(page2, text="这是第二页的内容")
# label2.pack(padx=10, pady=10)
#


def do_service():
    root = tk.Tk()
    app = color_srv(root)
    app.do()
