import tkinter
import tkinter.colorchooser
def ChooseColor():
    r = tkinter.colorchooser.askcolor(title = 'Python')
    print(r)
root = tkinter.Tk()
button = tkinter.Button(root, text = 'Select color', command = ChooseColor)
button.pack()
root.mainloop()
