from tkinter import *
from tkinter import messagebox
from student import *
#_______setting_WIN
win=Tk()
win.resizable(0,0)
win.geometry("350x400")
win.title("information")
c=student()

#_______lbl
lbl_fname=Label(win,text="fname :",font="arial 15")
lbl_fname.place(x=15,y=10)

lbl_lname=Label(win,text="lname :",font="arial 15")
lbl_lname.place(x=15,y=40)

lbl_idnumber=Label(win,text="id number :",font="arial 15")
lbl_idnumber.place(x=15,y=70)

#___________ent
ent_fname=Entry(win)
ent_fname.place(x=100,y=14)

ent_lname=Entry(win)
ent_lname.place(x=100,y=45)

ent_idnumber=Entry(win)
ent_idnumber.place(x=130,y=74)

#_________listbox
sc1=Scrollbar(win)
sc1.place(x=315,y=120,height=220)

sc2=Scrollbar(win,orient="horizontal")
sc2.place(x=120,y=340,width=210)


lst=Listbox(win)
lst.place(x=120,y=120,height=220,width=200)
sc1.config(command=lst.yview)
lst.place(x=120,y=120,height=220,width=200)
sc1.config(command=lst.yview)
sc2.config(command=lst.xview)
#__________def



def add():
    fname=ent_fname.get()
    lname=ent_lname.get()    
    idnumber=ent_idnumber.get()
    if fname=="" or lname=="" or idnumber=="" :   
         messagebox.showerror("error","pleas inter somthing")
         clear1()    
    elif not idnumber.isdigit() or len(idnumber)!=11:
         messagebox.showerror("error","pleas check your idnumber!!!")
         clear1()
    elif  fname=="  " or  lname==" " or idnumber==" "   :
             messagebox.showerror("error","pleas check your idnumber!!!")
             clear1()
    
    
    else:
       messagebox.showinfo( "insert",f"{c.insert(fname,lname,idnumber)}")
       clear1()    
def clear1():
     ent_fname.delete(0,END)    
     ent_lname.delete(0,END)    
     ent_idnumber.delete(0,END)    
def clear():
     lst.delete(0,END)

def show2():
     lst.delete(0,END)
     record=c.show()
     
     for rec in record:
          lst.insert(END,rec)
def delete1():
   try: 
        index=lst.curselection()
        data=lst.get(index)
        student_id=data[0]
        anser=messagebox.askquestion("delete","are you sure delete this record???")
        if anser.lower()=='yes':
           c.delete(student_id)
        
        else:
            clear()
   except Exception as ex:
        return ex
def  select():
     index=lst.curselection()
     global data
     data=lst.get(index)
     ent_fname.insert(0,data[1])
     ent_lname.insert(0,data[2])
     ent_idnumber.insert(0,data[3])
def update1():
  
        fname=ent_fname.get()
        lname=ent_lname.get()
        idnumber=ent_idnumber.get()
    
        index=lst.curselection()
        data=lst.get(index)
        student_id=data[0]
        select()
        q=messagebox.askquestion("update","are you sure updateing this recorde???")
        if q.lower() =="yes":
               
                c.update(student_id,fname,lname,idnumber)    
                show2()        
                
        else:
            clear1()
    
def exite():
     if messagebox.askokcancel("quit","are you sure want to quit??"):
         win.destroy()
 
#______________btn
btn_add=Button(win,text="ADD",font="arial 13",command=add)
btn_add.place(x=50,y=140)

btn_show=Button(win,text="show ",font="arial 13",command=show2)
btn_show.place(x=50,y=180)

btn_clear=Button(win,text="clear",font="arial 13",command=clear)
btn_clear.place(x=50,y=220)

btn_delete=Button(win,text="delete",font="arial 13",command=delete1)
btn_delete.place(x=50,y=260)

btn_update=Button(win,text="update",font="arial 13",command=update1)
btn_update.place(x=50,y=300)

btn_exite=Button(win,text="                        exite                    ",font="arial 13",command=exite)
btn_exite.place(x=65,y=360)

win.mainloop()