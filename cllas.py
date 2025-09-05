from tkinter import*
import student
win=Tk()
win.title('login form')
win.geometry('400x500')
db=student("D:\cllas.py")


fname=Label(win,text='fname:',font='arial 14')
fname.place(x=30,y=50)

lname=Label(win,text='lname:',font='arial 14')
lname.place(x=30,y=100)

email=Label(win,text='*Email:',font='arial 14')
email.place(x=30,y=150)

password=Label(win,text='* Password:',font='arial 14')
password.place(x=30,y=200)

ent_fname=Entry(win)
ent_fname.place(x=100,y=50)

ent_lname=Entry(win)
ent_lname.place(x=100,y=100)

ent_email=Entry(win)
ent_email.place(x=100,y=150)

ent_password=Entry(win)
ent_password.place(x=150,y=200)
 
def signup():
    fname=ent_fname.get()
    lname=ent_lname.get()
    email=ent_email.get()
    password=ent_password.get()
    











btn_signup=Button(win,text="sign up",font="arial 18") 
btn_signup.place(x=50,y=280)
 
btn_signin=Button(win,text="sign in",font="arial 18") 
btn_signin.place(x=190,y=280)






win.mainloop()