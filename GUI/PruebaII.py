from tkinter import Tk, Frame, Text, Scrollbar
import tkinter

root = Tk()
frame = Frame(root)
txt = Text(frame, wrap = tkinter.NONE)
scrolly = Scrollbar(frame, orient = "vertical", command = txt.yview)
scrollx = Scrollbar(frame, orient = "horizontal", command = txt.xview)

txt.config(yscrollcommand = scrolly.set, xscrollcommand = scrollx.set)
scrolly.pack(side = "right", fill = "y")
scrollx.pack(side = "bottom", fill = "x")
txt.pack(side = "left", fill = "both", expand = True)

frame.pack(fill = "both", expand = True)
root.mainloop()