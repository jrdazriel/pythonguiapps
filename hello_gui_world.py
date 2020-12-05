#Window Basics
import tkinter

#Define window
root = tkinter.Tk()
root.title('Window Basics')
root.iconbitmap('')
root.geometry('720x480')
root.resizable(1,1)
root.config(bg='blue')

#second window
top = tkinter.Toplevel()
top.title('Window 2')
top.config(bg='#00c2cb')
top.geometry('480x480')

#Run root window main loop
root.mainloop()
