import tkinter
root = tkinter.Tk()
label1 = tkinter.Label(root,
                       anchor = tkinter.E,
                       bg = 'red',
                       fg = 'blue',
                       text = 'Python',
                       width = 40,
                       height = 5)
label1.pack()
label2 = tkinter.Label(root, text = 'Python\ntkinter', justify = tkinter.LEFT, width = 40, height = 5)
label2.pack()
label3 = tkinter.Label(root, text = 'Python\ntkinter',
                      justify = tkinter.RIGHT,
                      width = 40,
                      height = 5)
label3.pack()
label4 = tkinter.Label(root, text = 'Python\ntkinter',
                        justify = tkinter.CENTER,
                        width = 40,
                        height = 5)
label4.pack()
root.mainloop()

