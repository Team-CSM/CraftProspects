from tkinter import *
root = Tk()

def make_label(master, x, y, h, w, *args, **kwargs):
    f = Frame(master, height=h, width=w)
    f.pack_propagate(0) # don't shrink
    f.place(x=x, y=y)
    label = Label(f, *args, **kwargs)
    label.pack(fill=BOTH, expand=1)
    return label

make_label(root, 10, 10, 10, 40, text='xxx', background='red')
make_label(root, 30, 40, 10, 30, text='xxx', background='blue')

root.mainloop()