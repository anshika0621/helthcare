from tkinter import*
from tkinter.font import Font
from PIL import Image, ImageTk


def Open_window(window): #function def for new window
    window.destroy()
    from loginpage import login
    login()

def O_window(): #function def for new window
    win = Tk()
    win.geometry("400x400")
    win.title("new window")
    Label(win, text = "sign page").pack()
    win.mainloop()

def register():  
    window = Tk()
    window.geometry("1600x1400")
    window.configure(bg = "blue")

    font1=Font(family = "cooper black", size = 50)
    txt = Label(window, text = "welcome!!!", bg = "blue", fg = "white", font = font1).place(anchor = 'e', relx = 0.65, rely = 0.2)#text

    logo = PhotoImage( file = "C:/Users/Dell/OneDrive/Desktop/pyt/tkinter/logo.png")#image
    label = Label(image = logo)
    label.pack()
    label.place(anchor = 'e', relx = 0.6, rely = 0.4)

    font2 = Font(family ="arial", size = 15)
    log  = Button(window, text = "    log in    ", fg = "black", bg = "white", font = font2, command = lambda:Open_window(window)) #login button
    #log.pack()
    log.place(anchor = 'w', relx = 0.48, rely = 0.6)

    sig = Button(window, text = "    sign in    ", fg = "black", bg = "white", font = font2, command = O_window)#signin button
    sig.pack()
    sig.place(anchor = 'w', relx = 0.48, rely = 0.7)

    font3 = Font(family = "algerian", size = 45, weight = "bold")
    txt1=Label(window, text= "U R F I N E", bg = "blue", fg = "white", font = font3)
    txt1.place(anchor = 'w', relx = 0.41, rely = 0.8)

    font4 = Font(family = "Times New Roman", size = 25, weight ="bold")
    txt2 = Label(window, text = "   a minute from you can save your life    ", bg = "blue", fg ="white", font = font4)
    txt2.place(anchor = 'w', relx  = 0.3, rely = 0.9)

    window.mainloop()
