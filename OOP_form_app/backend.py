import sqlite3
def connect():
    con = sqlite3.connect("Books.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    con.commit()
    con.close()

def insert(title, author, year, isbn):
    con = sqlite3.connect("Books.db")
    cur = con.cursor()
    cur.execute("INSERT  INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("Books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    con.close()
    return rows

def searchr(title="", author="", year="", isbn=""):
    con = sqlite3.connect("Books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows

def delete_one(id):
    con = sqlite3.connect("Books.db")
    cur = con.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    con.commit()
    con.close()

def delete_all():
    con = sqlite3.connect("Books.db")
    cur = con.cursor()
    cur.execute("DELETE FROM book")
    con.commit()
    con.close()

def updater(id, title, author, year, isbn):
    con = sqlite3.connect("Books.db")
    cur = con.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    con.commit()
    con.close()
connect()

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