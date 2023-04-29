#log in page
from tkinter import *
from PIL import Image,ImageTk



class log_win:
    def __init__(self, window):
        self.window=window
        self.window.title("login")
        self.window.geometry("1600x1400")
        self.window.configure(bg="light blue")


        self.bg=ImageTk.PhotoImage(file="C:/Users/Dell/OneDrive/Desktop/pyt/tkinter/background (1).png")
        lbl_bg=Label(self.window,image=self.bg).place(x = 0, y = 0, relwidth = 1, relheight = 1)


        

        
        
if __name__=="__main__":
    window=Tk()
    app=log_win(window)
    window.mainloop()

'''pic = PhotoImage(file = 'C:/Users/Dell/OneDrive/Desktop/pyt/tkinter/top.png')
fix = Label(image = pic, bg = '#87CEEB')
fix.pack( )
fix.place(anchor = 'e', relx = 0.72, rely = 0.1)'''

'''frame = Frame(window, width = 400, height = 400)
frame.place(anchor = 'w', relx = 0.35, rely = 0.5)

txt = Label( text ="  good to see you again  ", font = "arial 15 bold", fg = "black")
txt.place(anchor ='e',  relx = 0.58, rely = 0.28)

usernamelabel = Label(window, text = "user name", font = "arial 20 ", fg="black")
usernamelabel.place(anchor = 'w', relx = 0.35, rely = 0.35)
username=StringVar( )
usernameentry = Entry(window, textvariable = username)
usernameentry.place(anchor = 'w', relx = 0.35, rely = 0.38)

passwordlabel = Label(window, text = "password" , font = "arial 20", fg="black")
passwordlabel.place(anchor = 'w', relx = 0.35, rely = 0.42)
password = StringVar( )
passwordentry = Entry(window, textvariable = password)
passwordentry.place(anchor  = 'w', relx = 0.35, rely = 0.45)

loginvalid = partial(loginvalid, username, password)
loginbutton = Button(window, text = "       log in       ",  bg = "royal blue", font = "arial 15 bold", command = loginvalid( ))
loginbutton.place(anchor = 'w', relx = 0.45, rely = 0.5)'''

#self.window.mainloop( )
