import tkinter

window=tkinter.Tk()
window.title("PYTHON")
window.geometry("640x400+100+100")
window.resizable(True, True)

image=tkinter.PhotoImage(file="kakao.png")

label=tkinter.Label(window, image=image)
label.pack()

window.mainloop()
