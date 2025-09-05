from tkinter import *
from tkinter import messagebox
import random
#____________ 
win=Tk()
win.title("game_color")
win.geometry("350x300")
win.resizable(0,0)
#_________
time=30
score=0
color=["red","blue","white","black","yellow","orange","green","brown","pink"]
random.shuffle(color)
#_____
def start() :
    global time
    global score
    lbl_welcome.configure(text="")
    if time==30:
        countdown()
    next_color()    
                  
 

def countdown():
    
    global time
    global score
    if time==0:
        messagebox.showinfo("time down",f"score: {score}")
        time==30
        lbl_score.config(text=f"score : {score}")
        lbl_time.config(text=f"time : {time}")
        ent_color.delete(0,END)
        return
    if time>0:
        time-=1
        lbl_time.configure(text=f"time : {time}")
        lbl_time.after(1000,countdown)
def next_color():
    global color 
    global score
     

    if ent_color.get().lower()!=color[1].lower():
        if score >0:   
            score -=1
            ent_color.delete(0,END)
            random.shuffle(color)
        if score==0:
            ent_color.delete(0,END)
            random.shuffle(color)
    if ent_color.get().lower()==color[1].lower():
            score +=1        
            ent_color.delete(0,END)
            random.shuffle(color)
    lbl_score .configure(text=f"score:{score}")
    lbl_color.configure(text=f"{color[0]}",fg=f"{color[1]}")
       
btn_start=Button(win,text="start",command=start)
btn_start.place(x=150,y=150)
lbl_welcome=Label(win,text="welcome to game color",font="arial 15")
lbl_welcome.pack(side=TOP,pady=15)
#________lbl 
lbl_color=Label(win,text="red",font="arial 15")
lbl_color.place(x=145,y=100)
lbl_time=Label(win,text="time :",font="arial 16")
lbl_time.place(x=15,y=15)
lbl_score=Label(win,text="score :",font="arial 16")
lbl_score.place(x=15,y=50)
ent_color=Entry(win)
ent_color.place(x=110,y=170)

win.mainloop()