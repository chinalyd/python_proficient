import tkinter
root = tkinter.Tk()
r = tkinter.StringVar()
r.set('1')
radio = tkinter.Radiobutton(root,
                     variable = r,
                     value = '1',
                     text = 'radiobutton1')
radio.pack()
radio  = tkinter.Radiobutton(root,
                     variable = r,
                     value = '2',
                     text = 'radiobutton2')
radio.pack()
radio = tkinter.Radiobutton(root,
                     variable = r,
                     value = '3',
                     text = 'radiobutton3')
radio.pack()
c = tkinter.IntVar()
c.set(1)
check = tkinter.Checkbutton(root,
                     text = 'checkbutton',
                     variable = c,
                     onvalue  = 1,
                     offvalue = 3)
check.pack()
root.mainloop()
print(r.get())
print(c.get())

