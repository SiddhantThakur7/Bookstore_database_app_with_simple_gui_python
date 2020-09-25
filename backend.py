import sqlite3

class DB:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.con.commit()

    def insert(self,title, author, year, isbn):
        self.cur.execute("INSERT  INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.con.commit()


    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def searchr(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        self.con.commit()
        return rows

    def delete_one(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.con.commit()

    def delete_all(self):
        self.cur.execute("DELETE FROM book")
        self.con.commit()

    def updater(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.con.commit()

    def __del__(self):
        self.con.close()


'''insert("The Sea", "John Tablet", 1918, 913123132)
insert("The moon", "John smooth", 1929, 91876577)
print(view())
delete_all()
print(view())
connect()
insert("a", "b", 1, 2)
insert("t", "sid", 22, 6)
print(view())
updater(1, 'aa', 'bb', 11, 22)
print(view())
print(searchr(author='sid'))'''