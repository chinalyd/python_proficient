import tkinter
import tkinter.messagebox
def cmd():
    global n
    global buttontext
    n = n + 1
    if n == 1:
        tkinter.messagebox.askokcancel('Python tkinter', 'Cancel')
        buttontext.set('Software')
    elif n == 2:
        tkinter.messagebox.askquestion('Python tkinter question', 'Software')
        buttontext.set('AAAA')
    elif n == 3:
        tkinter.messagebox.askyesno('Python tkinter', 'No')
        buttontext.set('showerror')
    elif n == 4:
        tkinter.messagebox.showerror('Python tkinter', 'Error')
        buttontext.set('showinfo')
    elif n == 5:
        tkinter.messagebox.showinfo('python tkinter', 'Detail')
        buttontext.set('Show warning')
    else:
        n = 0
        tkinter.messagebox.showwarning('python tkinter', 'Warning')
        buttontext.set('AAAAl')
n = 0
root = tkinter.Tk()
buttontext = tkinter.StringVar()
buttontext.set('AAAAl')
button = tkinter.Button(root, textvariable = buttontext, command = cmd)
button.pack()
root.mainloop()

