from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import mysql.connector as mysql
from PIL  import Image,ImageTk
from loginpage import login


def back(new):
    new.destroy()
    from loginpage import login
    login()

def signin(new, fname, lname, email, password, phone):     #function for store data in sql
    if (fname=="" or lname=="" or email=="" or phone=="" or password==""):
        messagebox.showwarning("invalid details","values can't be empty")
        return 
    
    if not(fname.isalpha() and lname.isalpha()):
        messagebox.showwarning("invalid details","name can't have special character and digits")
        return

    if len(phone)!=10 or not phone.isdigit():
        messagebox.showwarning("invalid details","enter valid phone number")
        return
    
    if email.count("@") != 1 or(not (0 < email.count(".")<=2)):
        print(0 < email.count(".")<=2)
        messagebox.showwarning("invalid details","invalid email")
        return

    temp1 = email[:email.index("@")].isalnum()
    temp2 = email[email.index("@")+1:].split(".")
    print(temp1)
    print(temp2)
    valid_mail = temp2[0] in ["gmail", "yahoo", "outlook","gehu"]
    if email.count(".")==1:
        valid_domain = temp2[-1] =="com"
    else:
        valid_domain = temp2[-1] == "in" and temp2[-2] == "ac"
    if not temp1 or not valid_mail or not valid_domain:
        messagebox.showwarning("invalid details","invalid email")
        return


    con = mysql.connect(host="localhost" , user = "root",password="root", database = "urfine")
    cursor = con.cursor()
    cursor.execute("select email from user_info")
    result = cursor.fetchall()
    for i in result :
        if i == email :
            messagebox.showerror("invalid details","account already exists")
            return
        
    cursor.execute(f"insert into user_info values('{fname}','{lname}','{email}','{password}',{phone});")
    
    con.commit()
    messagebox.showinfo("success!!!", "your account is created successfully !!")



def sign():
    new = Tk()
    new.geometry("1366x768")
    new.title("sign up page")


    bg = PhotoImage(file = "./back.png")
    lbl2 = Label(new, image = bg, width= 1366, height=768).place(anchor="center", relx = 0.5, rely = 0.5)


    txt = Label(new, text="   sign up    ", font = ("arial 25 bold"), fg = "black", bg = "white").place(relx = 0.6, rely = 0.15)

    # name = StringVar()
    # name.set("name")

    fname = Entry(new, font = ("arial 15"),bg = "white", fg = "black")
    fname.insert(0,"first name")
    fname.place(relx = 0.48, rely = 0.25)


    lname = Entry(new, font = ("arial 15"), bg = "white", fg = "black")
    lname.insert(0,"last name")
    lname.place(relx = 0.7, rely = 0.25)


    email = Entry(new, font = ("arial 15"), bg = "white", fg = "black")
    email.insert(0,"email")
    email.place(width = 500, relx = 0.48, rely = 0.35)


    password = Entry(new, font=("arial 15"), fg = "black", bg = "white")
    password.insert(0,"password")
    password.place(width = 500, relx = 0.48, rely = 0.45)


    phone = Entry(new, font = ("arial 15"), fg = "black", bg = "white")
    phone.insert(0,"phone number")
    phone.place(width = 500, relx = 0.48, rely = 0.55)


    btt = Button(new, text = "sign in",bg = "blue", fg = "white", font =("arial 15 bold"), bd=3, relief = RAISED, command=lambda:signin(new, fname.get(), lname.get(), email.get(), password.get(), phone.get()) )  #sign in button
    btt.place(anchor = "center", relx = 0.65, rely = 0.76, width = 100, height= 50)

    haveacc = Button(new, text = "already have an account , login", bg = "white", fg ="firebrick", activeforeground="blue", bd = 0, relief = FLAT, command = lambda:back(new))
    haveacc.place(anchor = "center", relx = 0.82, rely = 0.8)
    new.mainloop()


