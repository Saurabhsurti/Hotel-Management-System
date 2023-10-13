from tkinter import *
from subprocess import call
import mysql.connector
from tkinter import messagebox
import tkinter as tk
import sqlite3

root = Tk(className=" HOTEL MANAGEMENT SYSTEM")
root.geometry('1920x1080')

# calling functions
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

#  1.drinks
#                 2.breakfast combo
#                 3.lunch
#                 4.dinner
#                 5.Exit


#functions
total_cost=0
def op1():
    global total_cost
    total_cost+=100
    # tk.Label(root,text=f"\nYour total cost is {total_cost}\n").pack()
def op2():
    global total_cost
    total_cost+=150
    # tk.Label(root,text=f"\nYour total cost is {total_cost}\n").pack()
def op3():
    global total_cost
    total_cost+=200
    # tk.Label(root,text=f"\nYour total cost is {total_cost}\n").pack()
def op4():
    global total_cost
    total_cost+=250
    # tk.Label(root,text=f"\nYour total cost is {total_cost}\n").pack()
def op5():
    
    # tk.Label(root,text=f"\nYour total cost is {total_cost}\n\n").pack()
    op5_label = tk.Label(root, text=f"Your total cost is {total_cost}", font=('Orbitron', 15), bg="black",
                      fg="white")
    op5_label.pack(fill=X)

    black_space = tk.Label(root, text="\n\n")
    black_space.pack()

    
# heading
newWindow = tk.Toplevel(root)
heading_label = tk.Label(root, text="---------  Restaurant Menu  ---------", font=('Orbitron', 15), bg="black",
                      fg="white")
heading_label.pack(fill=X)

black_space = tk.Label(root, text="\n\n")
black_space.pack()

heading_label = tk.Label(root, text="Just click on the item to order and click on show bill to show final bill...", font=('Orbitron', 15), bg="white",
                    fg="black")
heading_label.pack(fill=X)

black_space = tk.Label(root, text="\n\n")
black_space.pack()

#Buttons
cd_button = Button(root, text="Drinks(Rs100)", bg='#404040', fg='white', font=('Orbitron', 20, 'bold'), width=30,
                    command=op1)
cd_button.pack(pady=10)
cd_button = Button(root, text="Breakfast Combo(Rs150)", bg='#404040', fg='white', font=('Orbitron', 20, 'bold'), width=30,
                    command=op2)
cd_button.pack(pady=10)
cd_button = Button(root, text="Lunch(Rs200)", bg='#404040', fg='white', font=('Orbitron', 20, 'bold'), width=30,
                    command=op3)
cd_button.pack(pady=10)
cd_button = Button(root, text="Dinner(Rs250)", bg='#404040', fg='white', font=('Orbitron', 20, 'bold'), width=30,
                    command=op4)
cd_button.pack(pady=10)

cd_button = Button(root, text="Show your bill", bg='#404040', fg='white', font=('Orbitron', 20, 'bold'), width=30,
                    command=op5)
cd_button.pack(pady=10)

exit_button = Button(root, text="Exit", bg="#ff0000", fg="white", width=30, command=root.quit,
                     font=('Orbitron', 20, 'bold'))
exit_button.pack(pady=10)
 



root.mainloop()
