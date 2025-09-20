from tkinter import *
from tkinter import messagebox
import sqlite3
#_________WIN_seting
win=Tk()
win.geometry("450x500")
win.resizable(0,0)
#______date
con=sqlite3.connect("./mydate.db")
cur=con.cursor()                       
cur.execute("CREATE TABLE IF NOT EXISTS registration_form(fname TEXT , lname TEXT , phone  INTEGER,gender TEXT,course TEXT ,id INTEGER PRIMARY KEY)")
con.commit()
#_____lbl
def insert2(fname,lname,phone,course,gender):
    global con
    global cur
    cur.execute("INSERT INTO registration_form(fname ,lname ,phone ,course ,gender ) VALUES (?,?,?,?,?) ",(fname,lname,gender,course,phone))
    con.commit()
    messagebox.showinfo("done","insert succfully") 
def delete(id):
    cur.execute("DELETE FROM registration_from  WHERE id=? ",(id,))
    con.commit()
def update(lname,fname,phone):
    cur.execute("UPDATE registration_from SET fname=? ,lname=? ,phone=? WHERE id =?",(fname,lname,phone))

def show2():
     lst.delete(0,END)
     record=c.show()
     
     for rec in record:
          lst.insert(END,rec)
def  select3(event):
     index=lst.curselection()
     
     data=lst.get(index)
     fname_entry.insert(0,data[1])
     lname_entry.insert(0,data[2])
     phone_entry.insert(0,data[3])
def update1():
  
    fname=fname_entry.get()
    lname=lname_entry.get()
    phone=phone_entry.get()
    
    index=lst.curselection()
    data=lst.get(index)
    student_id=data[0]
    select()
    q=messagebox.askquestion("update","are you sure updateing this recorde???")
    if q.lower() =="yes":
               
        update(student_id,fname,lname,phone)    
        show2()        
                
    else:
        clear()
def select():
    cur.execute("SELECT * FROM registration_form ")
    record=cur.fetchall()
    return record

def show():
    
    record=select()
    for i in record:
        lst.insert(END,i)
    lst.delete(0,END)
def exite():
    a=messagebox.askquestion("exite","are you sure???")
    if a =="yes":
        win.destroy()
        con.close()
def delete1():
   try: 
        index=lst.curselection()
        data=lst.get(index)
        student_id=data[0]
        anser=messagebox.askquestion("delete","are you sure delete this record???")
        if anser.lower()=='yes':
            delete(student_id)
        
        else:
            clear()
   except Exception as ex:
        return ex

def clear():
    fname_entry.delete(0,END)
    lname_entry.delete(0,END)
    phone_entry.delete(0,END)
    gender_var.set("male")
    c.set(0)
    py.set(0)
    net.set(0)

def insert1():
    fname=fname_entry.get()
    lname=lname_entry.get()
    phone=phone_entry.get()
    python=py.get()
    network=net.get()
    c_sharp=c.get()
    gender=gender_var.get()
    course=""
    if len(phone)!=2:
        messagebox.showerror("error","pleas enter  number")
        return
    if not fname or not lname or not phone:
         messagebox.showerror("error","pleas enter somthing!!!")
         return
    if python==1:
        course+="python"
    if c_sharp==1:
        course+="c#"
    if network==1:
        course+="network"
    lst.insert(END,f"{fname},{lname},{phone},{gender},{course}")
    insert2(fname,lname,phone,gender,course) 
    clear() 
lbl_fname=Label(win,text="fname :",font="arial 13")
lbl_fname.place(x=15,y=10)

lbl_lname=Label(win,text="lname :",font="arial 13")
lbl_lname.place(x=15,y=38)

lbl_phone=Label(win,text="phone :",font="arial 13")
lbl_phone.place(x=15,y=68)

#-----entery
fname_entry=Entry(win)
fname_entry.place(x=80,y=15)

lname_entry=Entry(win)
lname_entry.place(x=80,y=44)

phone_entry=Entry(win)
phone_entry.place(x=80,y=70)
#________-------lblfram
lbl_gender=LabelFrame(win,text="gender",font="arial 15",width=200,height=150)
lbl_gender.place(x=15,y=95)

gender_var=StringVar(value="male")
gender_var.set("male")

male=Radiobutton(lbl_gender,text="male",font="arial 15",variable=gender_var,value="male")
male.place(x=15,y=15)

female=Radiobutton(lbl_gender,text="female",font="arial 15",variable=gender_var,value="female")
female.place(x=15,y=50)
#__----___________----____
lbl_course=LabelFrame(win,text="course",font="arial 15",width=200,height=150)
lbl_course.place(x=15,y=250)

c=IntVar()
py=IntVar()
net=IntVar()

c_chk=Checkbutton(lbl_course,text="c#",font="arial 15 ",variable=c)
c_chk.place(x=10,y=10)

py_chk=Checkbutton(lbl_course,text="python",font="arial 15 ",variable=py)
py_chk.place(x=10,y=35)

network_chk=Checkbutton(lbl_course,text="network",font="arial 15 ",variable=net)
network_chk.place(x=10,y=65)
#__________
lst=Listbox(win)
lst.place(x=230,y=20,width=200,height=200)
lst.bind('<<ListboxSelect>>',select)
#_______btn
btn_add=Button(win,text="add",font="arial 15",command=insert1)
btn_add.place(x=250,y=230)

btn_update=Button(win,text="update",font="arial 15",command=update1)
btn_update.place(x=320,y=230)

btn_clear=Button(win,text="clear",font="arial 15",command=delete1)
btn_clear.place(x=250,y=290)

btn_show=Button(win,text="show_list",font="arial 15",command=show)
btn_show.place(x=330,y=290)

btn_exite=Button(win,text="         exite         ",font="arial 15",command=exite)
btn_exite.place(x=250,y=350)

















win.mainloop()