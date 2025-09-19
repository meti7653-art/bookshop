from tkinter import *
from tkinter import messagebox
#--------------
win=Tk()
win.title("timer")
win.geometry("400x275")
win.resizable(FALSE,FALSE)
#----_____-----
lbl_time=Label(text="time :",font="arial 18 bold")
lbl_time.place(x=50 ,y=87)

lbl_timer=Label(text="  ",font="arial 18 bold",bg="black",fg="white")
lbl_timer.place(x=195 ,y=20)


ent_time=Entry(win)
ent_time.place(x=135, y=97)

time=0

def set_time():
     global time 
     
     try: 
        time= int(ent_time.get())
     
        if time <= 0:
            messagebox.showerror("error" ,"pleas enter a big number!!!")
     
     
        else:
         lbl_timer.configure(text=time)  
     except ValueError:
            messagebox.showerror("error","pleas enter just a number")    
     ent_time.delete(0,END) 

#____________
def start_timer():
     global time
     if time >  -1  :
        lbl_timer.configure(text=time)
        time -=1 
        win.after(1000,start_timer)
        btn_start.configure(state=DISABLED)
        btn_set.configure(state=DISABLED)
     else:
          messagebox.showinfo("finish","finish")
          resert_num()
         
#________
def resert_num():
    global time
    time=0
    lbl_timer.configure(text=0)
    ent_time.delete(0,END)
    btn_start.configure(state=NORMAL)
    btn_set.configure(state=NORMAL)




btn_set=Button(text=" set ",font="arial 18 bold",bg="black",fg="white",command=set_time)
btn_set.place(x=48,y=180)

btn_start=Button(text=" start ",font="arial 18 bold",bg="black",fg="white",command=start_timer)
btn_start.place(x=155,y=180)



btn_reset=Button(text=" reset ",font="arial 18 bold",bg="black",fg="white",command=resert_num)
btn_reset.place(x=280,y=180)










win.mainloop()