import sqlite3

class student:
    def __init__(self) :
        self.con=sqlite3.connect("./mydata.db")
        self.cur=self.con.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS students(Id INTEGER PRIMARY KEY, fname TEXT,lname TEXT,idnumber INTEGER)""")
        self.con.commit()
        
    def insert(self,fname,lname,idnumber):
        try:
             self.cur.execute('INSERT INTO students VALUES (NULL,?,?,?)',
                               (fname,lname,idnumber))
             self.con.commit()
             return "insert succfuly"
        except Exception as ex:
             return ex
    def show(self):
          self.cur.execute("SELECT * FROM students")
          records=self.cur.fetchall()
        
          return records
    
    
    def update(self,Id,fname,lname,idnumber):
          self.cur.execute('UPDATE students SET fname = ? , lname = ? , idnumber = ?  WHERE  Id = ? ',(fname,lname,idnumber,Id))
          self.con.commit()
          return "update done"
    def delete(self,Id):
         self.cur.execute("DELETE FROM students WHERE Id =?",(Id,))
         self.con.commit()
