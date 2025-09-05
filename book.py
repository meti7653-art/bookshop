import sqlite3 

class book:
    def __init__(self) :
        self.con= sqlite3.connect("./mydate.db")
        self.cur=self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book( id INTEGER PRIMARY KEY ,title  TEXT , writer  TEXT, history  INTEGER , isbn  INTEGER )")
        self.con.commit()       
    def insert(self,title,history,isbn,writer):
        self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,writer,history,isbn)) 
        self.con.commit()
        return "inser good"
    def select(self):
        self.cur.execute("SELECT * FROM book ")
        records=self.cur.fetchall()
        return records
    def search(self,title):
        self.cur.execute("SELECT * FROM book WHERE ID = ? or title = ? or isbn = ? or writer =? ",(title,title,title,title,title))
        record=self.cur.fetchall()
        return record
    def delete1(self,id):
        self.cur.execute("DELETE FROM book WHERE id = ?",(id,))
        self.con.commit()





