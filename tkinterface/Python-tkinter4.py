import tkinter
from math import*

window=tkinter.Tk()
window.title("PYTHON")
window.geometry("640x480+100+100")
window.resizable(False, False)

def calc(event):
    label.config(text="결과="+str(eval(entry.get())))

entry=tkinter.Entry(window)
entry.bind("<Return>", calc)
entry.pack()

label=tkinter.Label(window)
label.pack()

window.mainloop()
