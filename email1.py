import sqlite3

class email1:
    def __init__(self):
        self.con=sqlite3.connect("./mydata.db")
        self.cur=self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS email1(id INTEGER PRIMARY KEY, fname  TEXT, lname TEXT , email  TEXT , password TEXT )")
        self.con.commit()
    def sign_up(self,fname,lname,email,password):
        self.cur.execute("INSERT INTO email1 VALUES(NULL,?,?,?,?)",(fname,lname,email,password))
        self.con.commit()
        return "insert"
   
    def sign_in(self,email,password):
         self.cur.execute("SELECT * FROM email1 WHERE email = ? and password = ? ",(email,password))
         record=self.cur.fetchall()
         return record












