from tkinter import* 
from tkinter import messagebox
from book import *
#_____________
win=Tk() 
win.resizable(FALSE,FALSE)
win.geometry("600x350")
win.configure(bg="#909090")
win.title("bookshop")
data=book()
#___________lbl and entry
lbl_namebook=Label(win,text=" title :",font="arial 16")
lbl_namebook.place(x=15,y=15)

ent_nbook=Entry(win)
ent_nbook.place(x=95,y=20)

lbl_history=Label(win,text=" history :",font="arial 16")
lbl_history.place(x=15,y=60)

ent_history=Entry(win)
ent_history.place(x=110,y=65)

lbl_writer=Label(win,text=" writer :",font="arial 16")
lbl_writer.place(x=240,y=15)

ent_write=Entry(win)
ent_write.place(x=330,y=20)

lbl_isbn=Label(win,text=" isbn :",font="arial 16")
lbl_isbn.place(x=260,y=60)

ent_isbn=Entry(win)
ent_isbn.place(x=330,y=65)

def add():
    title=ent_nbook.get()
    writer=ent_write.get()
    isbn=ent_isbn.get()
    history=ent_history.get()
    if not title or not writer or not isbn or not history :
            messagebox.showerror("no entery","enter somthing")
            return
    data.insert(title,writer,history,isbn)
    clear()
def show():
    lst.delete(0,END)    
    record=data.select()
    if record:
         for rec in record:
               lst.insert(END,rec)
    else:
         messagebox.showerror("none","lst not somthing")
def clear():
     ent_history.delete(0,END)
     ent_isbn.delete(0,END)
     ent_nbook.delete(0,END)
     ent_write.delete(0,END)
def select_records(event):
  
         index=lst.curselection()
         global select_record
         select_record=lst.get(index)
         ent_nbook.insert(0,select_record[1])
         ent_write.insert(0,select_record[2])
         ent_history.insert(0,select_record[3])
         ent_isbn.insert(0,select_record[4])

def delete2():
    index=lst.curselection()
    select_record=lst.get(index)
   
    anser=messagebox.askquestion("delete","are you sure delete this record???")
        
    if anser.lower()=='yes':
           data.delete1(select_record[0])
    else:
        messagebox.showerror("nothing","select index !!!")  
def exite():
    anser=messagebox.askquestion("exite","are you sure exite ???")
    if anser=="yes":
        win.destroy()
#_____lst and scrolbal1
scx=Scrollbar(win)
scx.place(x=410,y=120,height=200)
scy=Scrollbar(win,orient="horizontal")
scy.place(x=20,y=320,width=400)
lst=Listbox(win)
lst.place(x=15,y=120,width=400,height=200)
lst.bind("<<ListboxSELECT>>",select_records)
scx.config(command=lst.xview)
scy.config(command=lst.yview)
#_______btn
btn_insert=Button(win,text="insert",font="arial 13",command=add)
btn_insert.place(x=545,y=164 )

btn_search=Button(win,text="search",font="arial 13")
btn_search.place(x=538,y=191)

btn_delete=Button(win,text="delete",font="arial 13",command=delete2)
btn_delete.place(x=542,y=223)

btn_show=Button(win,text="show_list",font="arial 13",command=show)
btn_show.place(x=520,y=255)

btn_clear=Button(win,text="clear",font="arial 13")
btn_clear.place(x=549,y=287)
 
btn_exite=Button(win,text="    exite       ",font="arial 13",command=exite)
btn_exite.place(x=500,y=317)
lbl=Label(win,text="__________________________________",bg="#909090")
lbl.place(x=428,y=150)

win.mainloop()