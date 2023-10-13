from subprocess import call
from tkinter import *
import tkinter as tk
import tkinter.messagebox as tm
import sqlite3

# Creates main window
root = Tk(className=''' HOTEL MANAGEMENT SYSTEM ''')
root.geometry('1920x1080')

# Customer Entry function
def click_checkin():
    call(["python", "C:\\Users\\saura\\OneDrive\\Documents\\python project\\Hotel-Database-Management-System--main\\Python_code\\check_in.py"])

# Customer Exit function
def click_checkout():
    call(["python", "C:\\Users\\saura\\OneDrive\\Documents\\python project\\Hotel-Database-Management-System--main\\Python_code\\check_out.py"])

# Check vacancy function
def click_vacancy():
    call(["python", "C:\\Users\\saura\\OneDrive\\Documents\\python project\\Hotel-Database-Management-System--main\\Python_code\\vacancy.py"])

# Customer detail function
def click_custdetail():
    call(["python", "C:\\Users\\saura\\OneDrive\\Documents\\python project\\Hotel-Database-Management-System--main\\Python_code\\customer_detail.py"])

# All details function
def click_allcust():
    call(['python', 'C:\\Users\\saura\\OneDrive\\Documents\\python project\\Hotel-Database-Management-System--main\\Python_code\\all_details.py'])

# Employee function
def click_employee():
    call(['python', 'C:\\Users\\saura\\OneDrive\\Documents\\python project\\Hotel-Database-Management-System--main\\Python_code\\employee.py'])

# Restaurant menu function
def click_menu():
    call(['python', 'C:\\Users\\saura\\OneDrive\\Documents\\python project\\Hotel-Database-Management-System--main\\Python_code\\restaurant_menu.py'])
    
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

# Title label
title_label = Label(root, text="		    HOTEL MANAGEMENT SYSTEM  			", height=4, font=('Times New Roman', 25), bg="red",fg="white")
title_label.pack(fill=X)


# Welcome label
welcome_label = Label(root, text=" WELCOME TO HOTEL ", bg="cyan", fg="black", font=('Orbitron', 25))
welcome_label.pack(fill=X)

blankspace = Label(root, text="\n")
blankspace.pack()

# Buttons

cin_button = tk.Button(root, text="CUSTOMER ENTRY", bg='#000000', fg='white', font=('Orbitron', 20, 'bold'), width=30,
                    command=click_checkin)

cin_button.pack(pady=10) 

cot_button = Button(root, text="CUSTOMER EXIT", bg='#1a1a1a', fg='white', font=('Orbitron', 20, 'bold'), width=30,
                    command=click_checkout)
cot_button.pack(pady=10)

cd_button = Button(root, text="SEARCH CUSTOMER", bg='#404040', fg='white', font=('Orbitron', 20, 'bold'), width=30,
                    command=click_custdetail)
cd_button.pack(pady=10)

cd_button = Button(root, text="RESTAURANT MENU", bg='#404040', fg='white', font=('Orbitron', 20, 'bold'), width=30,
                    command=click_menu)
cd_button.pack(pady=10)

exit_button = Button(root, text="EXIT", bg="#ff0000", fg="white", width=30, command=root.quit,
                     font=('Orbitron', 20, 'bold'))
exit_button.pack(pady=10)
 
Ratelabel = Label(root, text="Our Rating is ", font=('Orbitron', 28, 'bold'))
Ratelabel.place(relx=0.85, rely=0.32, anchor=E)
mydb = sqlite3.connect('C:\\Users\\saura\\OneDrive\\Documents\\python project\\Hotel-Database-Management-System--main\\SQL database\\hotel_database.db')
cur = mydb.cursor()
cur.execute("SELECT AVG(Rate) AS average FROM rating")
label = Label(root)
label.pack()
result = cur.fetchall()

for i in result:
    average= float(i[0])


average=round(average,2)
label.config(text = average, font=('Orbitron', 28))
label.place(relx=0.897, rely=0.32, anchor=E)

root.mainloop()