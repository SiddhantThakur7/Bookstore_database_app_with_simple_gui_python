from tkinter import *
import backend

'''
A book-store data base app
stores information of several books:
1) Title
2) Author
3) Year
4) ISBN 

functionality:
1) view record
2) Search a record
3) Add a new record
4) update a record
5) Delete a Record
6) close a record

'''
def get_selected_row(event):
    global target_book
    try:
        index = list1.curselection()[0]
        target_book = list1.get(index)

        e1.delete(0, END)
        e1.insert(END, target_book[1])
        e2.delete(0, END)
        e2.insert(END, target_book[2])
        e3.delete(0, END)
        e3.insert(END, target_book[3])
        e4.delete(0, END)
        e4.insert(END, target_book[4])
    except(IndexError):
        pass



def view_command():
    list1.delete(0, END)
    for record in backend.view():
        list1.insert(END, record)

def search_command():
    list1.delete(0, END)
    for ele in backend.searchr(t_inp1.get(), t_inp2.get(), t_inp3.get(), t_inp4.get()):
        list1.insert(END, ele)

def addr_command():
    backend.insert(t_inp1.get(), t_inp2.get(), t_inp3.get(), t_inp4.get())
    list1.delete(0, END)
    view_command()

def delete_command():
    backend.delete_one(target_book[0])
    list1.delete(0, END)
    view_command()

def update_command():
    backend.updater(target_book[0] ,t_inp1.get(), t_inp2.get(), t_inp3.get(), t_inp4.get())
    list1.delete(0, END)
    view_command()



window=Tk()

window.wm_title("Book Store DataBase App")

l1 = Label(window, text = "Title->")
l1.grid(row=0, column=0)
t_inp1 = StringVar()
e1 = Entry(window, textvariable=t_inp1)
e1.grid(row = 0, column = 1)


l2 = Label(window, text = "Author->")
l2.grid(row=0, column=2)
t_inp2 = StringVar()
e2 = Entry(window, textvariable=t_inp2)
e2.grid(row = 0, column = 3)


l3 = Label(window, text = "Year->")
l3.grid(row=1, column=0)
t_inp3 = StringVar()
e3 = Entry(window, textvariable=t_inp3)
e3.grid(row = 1, column = 1)


l4 = Label(window, text = "ISBN->")
l4.grid(row=1, column=2)
t_inp4 = StringVar()
e4 = Entry(window, textvariable=t_inp4)
e4.grid(row = 1, column = 3)

list1 = Listbox(window, height=8, width=36)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

sc = Scrollbar(window)
sc.grid(row =2,column=2,rowspan = 6)

view_command()

list1.configure(yscrollcommand=sc.set)
sc.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View-All", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search-Records", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add-Record", width=12, command=addr_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update-Record", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete-Record", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()