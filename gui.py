from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import subprocess, sys

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\\assets\\frame0")

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
window = Tk()

window.geometry("840x552")
window.configure(bg = "#242424", border=None)
window.overrideredirect(True)

def openInstaller():
    subprocess.run(["install"])
    sys.exit()

def warnOnExit():
    msgbox = messagebox.askyesno("경고", "프로그램을 나갈시 시스템을 재시작해야할수도 있습니다!\n그래도 하시겠습니까?")
    if msgbox == 1:
        sys.exit()
    elif msgbox == 0:
        print("cancel.")

canvas = Canvas(
    window,
    bg = "#242424",
    height = 552,
    width = 840,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    54.0,
    124.0,
    anchor="nw",
    text="원하는 항목을 선택해주세요",
    fill="#FFFFFF",
    font=("Pretendard Variable", 25 * -1)
)

canvas.create_text(
    54.0,
    58.0,
    anchor="nw",
    text="Aero 복구",
    fill="#FFFFFF",
    font=("Pretendard Variable", 55 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: openInstaller(),
    relief="flat"
)
button_1.place(
    x=54.0,
    y=177.0,
    width=341.0,
    height=101.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: subprocess.run(["gparted"]),
    relief="flat"
)
button_2.place(
    x=54.0,
    y=289.0,
    width=341.0,
    height=96.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: warnOnExit(),
    relief="flat"
)
button_3.place(
    x=54.0,
    y=401.0,
    width=341.0,
    height=97.0
)

center(window)
window.resizable(False, False)
window.mainloop()
