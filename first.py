#trying for graphics in python
from tkinter import *
from tkinter.font import Font


def home():
    window=Tk()

    window.geometry("1366x768")#size for window
    window.configure(bg="blue")#background of window

    frame = Frame(window, bg="blue", width=200, height=200)#creating frame 
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)#placing at centre

    photo=PhotoImage(file="C:/Users/Dell/OneDrive/Desktop/pyt/tkinter/logo.png")#importing image
    label=Label(image=photo)#labelling
    label.pack()
    label.place(anchor='center', relx=0.5, rely=0.5)#placing at centre

    my_font=Font(family="cooper black",size=48)#declaring font
    txt=Label(window,text="URFINE",fg="white",bg="blue", font=my_font).place(anchor="w",relx=0.4, rely=0.8)#add text at specified position and font

    window.after(2000, window.destroy)#deatroy the current window in 3 sec
    window.mainloop()
    from logm import register #new window imported
    register()