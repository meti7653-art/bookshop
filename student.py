import sqlite3

class form():
    def __init__(self,db) :
         self.con=sqlite3.connect(db)
         self.cur=self.con.cursor()
         self.cur.execute(" CREATE  TABLE  IF NOT EXISTS students(fname,lname,email,password)")
         self.con.commit()
         
    def insert(self,fname,lname,email,password):
        
             self.cur.execute('INSERT INTO student VALUES (NULL,?,?,?)',
                               (fname,lname,email,password))
             self.con.commit()
             return "insert successfully"
    
db=form("E:\student.py")    