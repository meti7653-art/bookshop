from tkinter import *
from tkinter import messagebox
from email1 import *
#________________
win=Tk()
win.geometry("300x350")
win.title("eamil")
data=email1()
#___________

def insret():
    fname=ent_fname.get()
    lname=ent_lname.get()
    email=ent_email.get()
    password=ent_password.get()
    if email==FALSE or password==email:
         messagebox.showerror("fill","enter password or email") 
         return
    if len(password)!=6:
         messagebox.showerror("error","The number of characters must be 6")     
         return
    else: 
        messagebox.showinfo("done",f"{fname}+{lname}\t very welcome to my project ")
        data.sign_up(fname,lname,email,password) 
        clear() 
def clear():
     ent_email.delete(0,END)
     ent_password.delete(0,END)
     ent_fname.delete(0,END)
     ent_lname.delete(0,END)
def sign_in1():
    email=ent_email.get()
    password=ent_password.get()
    record=data.sign_in(email,password)

    if not email or not password:
         messagebox.showerror("fill!!!","enter password or email") 
         return
    if record :
    
        messagebox.showinfo(f"welcome {record[0]}/{record[1]}",f"{record[0]}/{record[1]}you are vrey welcome to our project ")
        return  
              
    else: 
         messagebox.showwarning("not account","you shoud first sing_up")




#___________

lbl_fname=Label(win,text="fname :",font="arial 15")
lbl_fname.place(x=15,y=10)
lbl_lname=Label(win,text="lname :",font="arial 15")
lbl_lname.place(x=15,y=40)
lbl_email=Label(win,text="*email :",font="arial 15")
lbl_email.place(x=15,y=70)
lbl_password=Label(win,text="*password :",font="arial 15")
lbl_password.place(x=15,y=100)
#________
ent_fname=Entry(win)
ent_fname.place(x=90,y=16)
ent_lname=Entry(win)
ent_lname.place(x=90,y=46)
ent_email=Entry(win)
ent_email.place(x=90,y=76)
ent_password=Entry(win)
ent_password.place(x=130,y=106)
#___________
btn_sign_up=Button(win,text="sign_up",font="arial 15",command=insret)
btn_sign_up.place(x=40,y=180)
btn_sign_in=Button(win,text="sign_in",font="arial 15",command=sign_in1)
btn_sign_in.place(x=180,y=180)

win.mainloop()