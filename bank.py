import sqlite3

class bank: 
    def __init__(self) :
        self.con=sqlite3.connect("./mydata.db")
        self.cur=self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS bank (id INTEGER PRIMARY KEY , fname TEXT ,lname TEXT , phone INTEGER ,address TEXT)")
        self.con.commit()
    def insert_1(self,fname,lname,phone,address):
       try:
            self.cur.execute("INSERT INTO bank VALUES (NULL,?,?,?,?)",(fname,lname,phone,address))
            self.con.commit()
            return "insert good"
       except Exception as ex:
                return ex
    def select(self):
         self.cur.execute("SELECT * FROM bank ORDER BY id ASC ")
         record=self.cur.fetchall()
         return record
    def delete(self,id):
         self.cur.execute("DELETE FROM bank WHERE id = ?",(id,))
         self.con.commit()
    def update(self,id,fname,lname,address,phone):
         self.cur.execute("UPDATE bank SET fname = ? , lname = ? , address = ? , phone= ? WHERE id =? ",(fname,lname,address,phone,id))
         self.con.commit()

    def search(self,fname):
         self.cur.execute("SELECT * FROM bank WHERE id =? or fname = ? or lname = ? or phone = ? or address = ?",(fname,fname,fname,fname,fname))
         records=self.cur.fetchall()
         return records
