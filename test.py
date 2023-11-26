from tkinter import *

root = Tk()
root.config(padx=20, pady=20)
frame = Frame(root)
frame.grid(row=0, column=0)

bottomframe = Frame(root)
bottomframe.grid(row=1, column=0)

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

root.mainloop()