from tkinter import*
from tkinter.font import Font
from tkinter import messagebox
import mysql.connector as mysql
from PIL  import Image,ImageTk


def submit(username,password):
    con = mysql.connect(host="localhost" , user = "root",password="root", database = "urfine")
    cursor = con.cursor()
    cursor.execute(f"insert into temp values('{username}',{password});")
    # result = cursor.fetchall()
    con.commit()
    messagebox.showinfo("success!!!", "you are loged in!!")

def login():
    win = Tk()
    win.geometry("1400x1400")
    win.title("log in page")
    #win.configure(bg = "light blue")

    bg = PhotoImage(file="./bg.png")
    lbl_bg =Label (win,image=bg, width = 1366, height = 768).place(anchor = 'center', relx = 0.5,  rely = 0.5)


    frm = Frame(win, bg = "white", width = 890, height = 450).place(anchor = "center", relx = 0.5, rely=0.6)

    #top = PhotoImage(file = "./top.png")
    #toplbl = Label( win, width = 550, height = 200).place(anchor='center', relx = 0.5, rely = 0.2)


    top = Image.open(r"C:\Users\Dell\OneDrive\Desktop\pyt\tkinter\top.png")
    # top=top.resize((600,300))
    photoi = ImageTk.PhotoImage(top)
    lbl1=Label(image = photoi, bg = "#B3DCEE", borderwidth=0)
    #lbl1.lower()
    lbl1.place(anchor='e', relx = 0.65, rely =0.1)
    txt=Label(frm, text = "          good to see you again       ", font=("arial 25 bold"), fg = "black", bg = "white")
    txt.place(anchor='center', relx = 0.49, rely = 0.4)


    username=Label(frm, text = "username*", font=("arial 15 bold"), fg = "black", bg = "white")
    username.place(anchor = 'center', relx = 0.458, rely = 0.5)
    textuser=Entry(frm, font = ("arial 15 bold"),bg = "grey")
    textuser.place(anchor = 'center', relx = 0.5, rely = 0.55)


    userpass=Label(frm, text = "password*", font=("arial 15 bold"), fg = "black", bg = "white")
    userpass.place(anchor = 'center', relx = 0.458, rely = 0.595)
    textpass=Entry(frm, font = ("arial 15 bold"),bg = "grey")
    textpass.place(anchor = 'center', relx = 0.5, rely = 0.645)

    
    logbt = Button (frm, text = "log in",bg = "blue", fg = "white", font =("arial 15 bold"), bd=3, relief = RAISED , command = lambda:submit(textuser.get(),textpass.get()))
    logbt.place(anchor = "center", relx = 0.5, rely = 0.76, width = 100, height= 50)

    fgpass = Button(frm, text = "forgot password", bg = "white", fg = "firebrick",activeforeground="blue", font = ("arial 12 "), bd=0, relief = FLAT )
    fgpass.place(anchor = "center", relx =0.458, rely = 0.681  )

    


    

    win.mainloop()

login()