from tkinter import*
from tkinter.font import Font
from tkinter import messagebox
import mysql.connector as mysql
from PIL  import Image,ImageTk

def no_acc(win):
    win.destroy()
    from signup import sign
    sign()

def submit(win, username,password):     #function for store data in sql
    if (username=="" or password==""):
        messagebox.showwarning("invalid details","values can't be empty")
        return 
    
    con = mysql.connect(host="localhost" , user = "root",password="root", database = "urfine")
    cursor = con.cursor()
    cursor.execute("select email, password from user_info;")
    result = cursor.fetchall()
    for email , pas  in result:
        if username == email and pas == password:
            messagebox.showinfo("success!!!", "you are loged in!!")
            win.destroy()
            return
    messagebox.showerror("invalid details","no such username and password")
    
    
def login():     #function for login 
    win = Tk()     #new window
    win.geometry("1400x1400")   
    win.title("log in page")
    
    bg = PhotoImage(file=r"C:\Users\Dell\OneDrive\Desktop\pyt\tkinter\bg.png")     #background image
    lbl_bg =Label (win,image=bg, width = 1366, height = 768).place(anchor = 'center', relx = 0.5,  rely = 0.5)


    frm = Frame(win, bg = "white", width = 850, height = 450).place(anchor = "center", relx = 0.5, rely=0.65)  #white frame

    #top = PhotoImage(file = "./top.png")
    #toplbl = Label( win, width = 550, height = 200).place(anchor='center', relx = 0.5, rely = 0.2)


    top = Image.open(r"C:\Users\Dell\OneDrive\Desktop\pyt\tkinter\top.png")    #top image
    # top=top.resize((600,250))
    photoi = ImageTk.PhotoImage(top)
    lbl1=Label(image = photoi, bg = "#B3DCEE", borderwidth=0)
    #lbl1.lower()
    lbl1.place(anchor='e', relx = 0.65, rely =0.1)


    txt=Label(frm, text = "           Good to see you again!!!         ", font=("arial 25 bold"), fg = "black", bg = "white")   #text
    txt.place(anchor='center', relx = 0.49, rely = 0.4)


    username=Label(frm, text = "email*", font=("arial 15 bold"), fg = "black", bg = "white")   #usernme text
    username.place(anchor = 'center', relx = 0.458, rely = 0.5) 
    textuser=Entry(frm, font = ("arial 15 bold"),bg = "grey")  #entry field
    textuser.place(anchor = 'center', relx = 0.5, rely = 0.55)


    userpass=Label(frm, text = "password*", font=("arial 15 bold"), fg = "black", bg = "white")  #password text
    userpass.place(anchor = 'center', relx = 0.458, rely = 0.595)
    textpass=Entry(frm, font = ("arial 15 bold"),bg = "grey")    #entry field
    textpass.place(anchor = 'center', relx = 0.5, rely = 0.645)

    
    logbt = Button (frm, text = "log in",bg = "blue", fg = "white", font =("arial 15 bold"), bd=3, relief = RAISED , command = lambda:submit(win, textuser.get(),textpass.get()))  #login button
    logbt.place(anchor = "center", relx = 0.5, rely = 0.76, width = 100, height= 50)

    fgpass = Button(frm, text = "forgot password", bg = "white", fg = "firebrick",activeforeground="blue", font = ("arial 12 "), bd=0, relief = FLAT )   #forgot password button
    fgpass.place(anchor = "center", relx =0.25, rely = 0.76  )

    dntacct = Button(frm, text = "don't have an account?", bg = "white", fg = "firebrick", activeforeground="blue", font = ("arial 12"), bd = 0, relief = FLAT, command = lambda:no_acc(win))   #don't have an account
    dntacct.place(anchor="center", relx = 0.73, rely = 0.76)

    # # back = Button(frm, text = "back", bg = "blue", fg = "white",font = ("arial 15"), bd = 0, relief = RAISED)
    # back.place(anchor = "center", relx = 0.3, rely = 0.76,width=100, height=50)

    

    

    win.mainloop()
