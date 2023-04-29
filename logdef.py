#log in page
from tkinter import *
from PIL import Image,ImageTk



class log_win:
    
    
    def __init__(self, window):
        self.window=window
        self.window.title("login")
        self.window.geometry("1600x1400")
        #self.window.configure(bg="light blue")


        self.bg=ImageTk.PhotoImage(file=r"C:/Users/Dell/OneDrive/Desktop/pyt/tkinter/background (1).png")
        lbl_bg=Label(self.window,image=self.bg,width = 1600, height = 1400).place(anchor='center', relx = 0.5, rely = 0.5)
        


        img1=Image.open(r"C:\Users\Dell\OneDrive\Desktop\pyt\tkinter\top.png")
        img1=img1.resize((500,400))
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbl1=Label(image = self.photoimage1, bg = "light blue", borderwidth = 0)
        lbl1.place(anchor='e', relx = 0.68, rely =0.1)
        


        frame=Frame(self.window, bg="white", width = 600, height = 400)
        frame.pack()
        frame.place(anchor="center", relx = 0.5, rely = 0.5)



        txt=Label(frame, text = "          good to see you again       ", font=("arial 15 bold"), fg = "black", bg = "white")
        txt.place(anchor='e', relx = 0.7, rely = 0.12)



        username=Label(frame, text = "username*", font=("arial 15 bold"), fg = "black", bg = "white")
        username.place(anchor = 'e', relx = 0.25, rely = 0.2)
        self.textuser=Entry(frame, font = ("arial 15 bold"),bg = "grey")
        self.textuser.place(anchor = 'e', relx = 0.4, rely = 0.3)


        userpass=Label(frame, text = "password*", font=("arial 15 bold"), fg = "black", bg = "white")
        userpass.place(anchor = 'e', relx = 0.25, rely = 0.4)
        self.textpass=Entry(frame, font = ("arial 15 bold"),bg = "grey")
        self.textpass.place(anchor = 'e', relx = 0.4, rely = 0.5)



        logbt = Button (frame, text = "log in",bg = "blue", fg = "white", font =("arial 15 bold"), bd=3, relief = RIDGE )
        logbt.place(anchor = "e", relx = 0.55, rely = 0.75, width = 100, height= 50)

        logbt = Button (frame, text = "forgot password?",bg = "white", fg = "red", font =("arial 10 bold underline"))
        logbt.place(anchor = "e", relx = 0.3, rely = 0.59, width = 200, height= 20)

        
        
if __name__=="__main__":
    window=Tk()
    app=log_win(window)
    window.mainloop()


