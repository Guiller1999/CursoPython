import tkinter as tk

root = tk.Tk()

textContainer = tk.Frame(root, borderwidth=1, relief="sunken", bg = "red")
text = tk.Text(textContainer, width=24, height=13, wrap="none", borderwidth=0)
textVsb = tk.Scrollbar(textContainer, orient="vertical", command=text.yview)
textHsb = tk.Scrollbar(textContainer, orient="horizontal", command=text.xview)
text.configure(yscrollcommand=textVsb.set, xscrollcommand=textHsb.set)

text.grid(row=0, column=0, sticky="nsew")
textVsb.grid(row=0, column=1, sticky="ns")
textHsb.grid(row=1, column=0, sticky="ew")

textContainer.grid_rowconfigure(0, weight=1)
textContainer.grid_columnconfigure(0, weight=1)

textContainer.pack(side="top", fill="both", expand=True)

root.mainloop()