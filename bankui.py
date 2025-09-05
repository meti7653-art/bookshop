from tkinter import *
from tkinter import messagebox
import random
from bank import *
#_____________win
win=Tk()
win.geometry("550x400")
win.resizable(FALSE,FALSE)
data=bank()
#_________DEF
def color():
   cod_hex="0123456789ABCDEF"
   cod_color="#"
   for i in range(6):
        cod_color+=random.choice(cod_hex)      
   win.configure(bg=cod_color)      
   lbl_fname.configure(bg=cod_color)
   lbl_lname.configure(bg=cod_color)
   lbl_address.configure(bg=cod_color)
   lbl_phone.configure(bg=cod_color)
   btn_insert.configure(bg=cod_color)
   btn_update.configure(bg=cod_color)
   btn_remove.configure(bg=cod_color)
   btn_search.configure(bg=cod_color)
   btn_chang.configure(bg=cod_color)
   btn_clear.configure(bg=cod_color)
   btn_exite.configure(bg=cod_color)
   btn_show.configure(bg=cod_color)
def clear():
    ent_address.delete(0,END)
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_phone.delete(0,END)
    ent_fname.focus_get()
def insert_data():
     fname=ent_fname.get().strip().capitalize()
     lname=ent_lname.get().strip()
     phone=ent_phone.get().strip()
     address=ent_address.get().strip().capitalize()
     if not fname or not lname or not address :
            messagebox.showerror("error","pleas inter somthing")
    
     if not phone.isdigit() or len(phone) !=11:
          messagebox.showerror("phone error","pleas check your phone")
          ent_phone.delete(0,END)
          return
     data.insert_1(fname,lname,address,phone)
     clear()
     return " insert succfuly"

def show():
     lst.delete(0,END)
     record=data.select()
     record.sort(key=lambda x : x[0])
     for rec in record:
          lst.insert(END,rec)
 
def select_records(event):
         clear()
         index=lst.curselection()
         global select_record
         select_record=lst.get(index)
         ent_fname.insert(0,select_record[1])
         ent_lname.insert(0,select_record[2])
         ent_address.insert(0,select_record[3])
         ent_phone.insert(0,select_record[4])
   
def update():
    fname=ent_fname.get()
    lname=ent_lname.get()
    address=ent_address.get()
    phone=ent_phone.get()
    if not fname or not lname or not address or not phone:
         messagebox.showerror("error","pleas select index!!!")
         return
    index=lst.curselection()
    select_record=lst.get(index)

    data.update(select_record[0],fname,lname,address,phone)
    messagebox.showinfo("end","finish  upate")
    show()
    clear()
def delete1():
     try:
          index=lst.curselection()
          select_record=lst.get(index)
    
          if not index:
               messagebox.showerror("not index","select index")
               return
          q=messagebox.askquestion("delete","are you sure delet this record???")
          if q=="yes":
              data.delete(select_record[0])
              clear()
     except Exception as ex:
          return ex
def search2():
     lst.delete(END,0)    
     search=ent_search.get()
     record=data.search(ent_search.get())
     if record:
          for rec in record:
              lst.insert(END,rec)
     else:
          messagebox.showinfo("none",f"not finde    {search}")
def clear2():
    lst.delete(0,END)
def exite():
     anser= messagebox.askquestion("exite","are you sure exite???")
     if anser=="yes":
          win.destroy()
          messagebox.showinfo("done","done programr")
      
#________lbl     
lbl_fname=Label(win,text=" fname :",font="arial 15")   
lbl_fname.place(x=10,y=15)

lbl_lname=Label(win,text=" lname :",font="arial 15")   
lbl_lname.place(x=10,y=70)

lbl_address=Label(win,text=" address :",font="arial 15")   
lbl_address.place(x=250,y=15)

lbl_phone=Label(win,text=" phone :",font="arial 15")   
lbl_phone.place(x=250,y=70)
#____________lst
sc=Scrollbar(win,orient=VERTICAL)
sc.place(x=415,y=220,height=180)

lst=Listbox(win)
lst.grid_propagate(False)
lst.place(x=35,y=220,width=380,height=170)
lst.bind('<<ListboxSelect>>',select_records)
sc.config(command=lst.xview)
#_________ent
ent_fname=Entry(win,font="arial 8")
ent_fname.place(x=98,y=21)

ent_lname=Entry(win,font="arial 8")
ent_lname.place(x=98,y=79)

ent_address=Entry(win,font="arial 8")
ent_address.place(x=350,y=21)

ent_phone=Entry(win,font="arial 8")
ent_phone.place(x=345,y=79)

ent_search=Entry(win,font="arial 8")
ent_search.place(x=97,y=174)
#____________btn

btn_insert=Button(win,text="insert",font="arial 12",command=insert_data)
btn_insert.place(x=20,y=120)

btn_update=Button(win,text="update",font="arial 12",command=update)
btn_update.place(x=90,y=120)

btn_remove=Button(win,text="remove",font="arial 12",command=delete1)
btn_remove.place(x=170,y=120)

btn_clear=Button(win,text="clear",font="arial 12",command=clear2)
btn_clear.place(x=250,y=120)

btn_show=Button(win,text="show_list",font="arial 12",command=show)
btn_show.place(x=310,y=120)

btn_exite=Button(win,text="exite",font="arial 12",command=exite)
btn_exite.place(x=410,y=120)

btn_search=Button(win,text="search",font="arial 12",command=search2)
btn_search.place(x=20,y=168)

btn_chang=Button(win,text="chang_color",font="arial 12",command=color)
btn_chang.place(x=260,y=168)



















win.mainloop()