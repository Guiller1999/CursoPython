from tkinter import Tk, Frame

root = Tk()

root.title("Uso de Frame")
root.iconbitmap("Img\\aprobar.ico")
#root.geometry("500x450")
root.config(bg = "Black")

frame = Frame()
frame.config(width = "500", height = "450")
frame.config(bd = 35, cursor = "hand2")
frame.config(bg = "White", relief = "groove")
#frame.pack(side = "left", anchor = "s")
#frame.pack(fill = "both", expand = "True")
frame.pack()

root.mainloop()