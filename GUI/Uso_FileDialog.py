from tkinter import Tk, filedialog, Button

def openfile():

    file = filedialog.askopenfilename(
                title = "Open file", 
                initialdir = "C://", 
                filetype = (("Excel file", "*.xlsx"), ("Text file", "*.txt"), ("All file", "*.*"))
            )

    print(file)


root = Tk()
btn_open = Button(text = "Abrir", bg = "dark blue", fg = "White", command = openfile)
btn_open.config(relief = "flat", font = ("Century Schoolbook", 14, "italic"))

btn_open.pack(anchor = "center", pady = 20)

root.title("Uso de FileDialog")
root.config(bg = "White")
root.geometry("300x350")
root.mainloop()