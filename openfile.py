import tkinter
import tkinter.filedialog
def FileOpen():
    r = tkinter.filedialog.askopenfilename(title = 'Python', filetypes=[('Python', '*.py *.pyw'), ('All files', '*')])
    print(r)
def FileSave():
    r = tkinter.filedialog.asksaveasfilename(title = 'Python', initialdir=r'E:\Python\code',initialfile='test.py')
    print(r)
root = tkinter.Tk()
button1 = tkinter.Button(root, text = 'OpenFile', command = FileOpen)
button1.pack(side='left')
button2 = tkinter.Button(root, text = 'SaveFile', command = FileSave)
button2.pack(side='left')
root.mainloop()
