from tkinter import *
from subprocess import call
import mysql.connector
import tkinter as tk
import sqlite3

root = Tk(className=" HOTEL MANAGEMENT SYSTEM")
root.geometry('1920x1080')

def click_vacancy():
    call(["python", "C:\\Users\\saura\\OneDrive\\Documents\\python project\\Hotel-Database-Management-System--main\\Python_code\\vacancy.py"])
def click_allcust():
    call(['python', 'C:\\Users\\saura\\OneDrive\\Documents\\python project\\Hotel-Database-Management-System--main\\Python_code\\all_details.py'])
def click_employee():
    call(['python', 'C:\\Users\\saura\\OneDrive\\Documents\\python project\\Hotel-Database-Management-System--main\\Python_code\\employee.py'])

# Menu Bar
menu_bar = Menu(root)
root.config(menu=menu_bar)
home_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Home", menu=home_menu)
home_menu.add_command(label="Vacancy", command=click_vacancy)
home_menu.add_separator()
home_menu.add_command(label="Exit", command=root.quit)

view_menu = Menu(menu_bar)
menu_bar.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Guest list", command=click_allcust)
view_menu.add_separator()
view_menu.add_command(label="Employee list", command=click_employee)

# heading
heading_label = Label(root, text="---------  ALL CUSTOMERS  ---------", font=('Orbitron', 15), bg="black", fg="white")
heading_label.pack(fill=X)

top_frame = Frame(root)
top_frame.pack()

# customer text view
text = Text(root, bd=5, bg="white", fg='blue', width=200, font=('Arial', 15))
text.place(rely=0.1)

# database
mydb = sqlite3.connect('C:\\Users\\saura\\OneDrive\\Documents\\python project\\Hotel-Database-Management-System--main\\SQL database\\hotel_database.db')
cur = mydb.cursor()
cur.execute('SELECT * from guests')
result = cur.fetchall()
title = "First Name\t\t Last Name\t\t Phone Number\t\t Email id\t\t\t    Address\t\t Room No\t\t Room Type\t\t " \
        "Days\n"
text.insert(INSERT, title)
formatting = "-------------------------------------------------------------------------------------------" \
             "-------------------------------------------------------------------------------------------" \
             "------------------------------------------------------------------------------------------\n"
text.insert(INSERT, formatting)
text.insert(INSERT, formatting)
for i in result:
    a = list(i)
    rt = ''
    if a[7] == 1:
        rt = "AC"
    else:
        rt = "Non-AC"
    s = a[0] + "\t\t" + a[1] + "\t\t" + str(a[2]) + "\t\t" + a[3] + "\t\t\t   " + a[4] + "\t\t" + str(
        a[5]) + "\t\t" + rt + "\t\t " + str(a[6]) + "\n\n"
    text.insert(INSERT, s)

root.mainloop()