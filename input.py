import tkinter
import tkinter.simpledialog
def InStr():
    r = tkinter.simpledialog.askstring('Python', 'String', initvalue='StringString')
    print(r)
def InInt():
    r = tkinter.simpledialog.askinteger('Python', 'Input Int:')
    print(r)
def InFlo():
    r = rkinter.simpledialog.askfloat('Python', 'Input float')
    print(r)
root = tkinter.Tk()
button1 = tkinter.Button(root, text = 'Input String', command=InStr)
button1.pack(side='left')
button2=tkinter.Button(root, text='Input Float', command=InFlo)
button2.pack(side='left')
button2 = tkinter.Button(root, text='Input Integer', command = InInt)
button2.pack(side='left')
root.mainloop()

