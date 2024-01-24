import tkinter
from tkinter import ttk
screen = tkinter.Tk()
screen.title("Register for a new account")

frame = tkinter.Frame(screen)
frame.pack()
user_info = tkinter.LabelFrame(frame, text="User Information")
user_info.grid(row=0, column=0, padx=20, pady=20)
name_label = tkinter.Label(user_info,text="First Name")
name_label.grid(row=0,column=0)
last_name = tkinter.Label(user_info,text="Last Name")
last_name.grid(row=0,column=1)

name_entry = tkinter.Entry(user_info)
last_name = tkinter.Entry(user_info)
name_entry.grid(row=1,column=0)
last_name.grid(row=1,column=1)

title = tkinter.Label(user_info,text="Title")
combobox = ttk.Combobox(user_info, values=["Mr","Ms","Mrs","Dr"])
title.grid(row=0,column=2,padx=20,pady=20)
combobox.grid(row=1,column=2)

ID = tkinter.Label(user_info,text="ID Number")
ID.grid(row=2,column=0)
ID_entry = tkinter.Entry(user_info)
ID_entry.grid(row=3,column=0,padx=20,pady=20)

age = tkinter.Label(user_info,text="Age")
spinbox = tkinter.Spinbox(user_info,from_=0, to=50)
age.grid(row=2,column=1)
spinbox.grid(row=3,column=1)

school = tkinter.Label(user_info,text="Name of School")
school.grid(row=2,column=2)
school_entry = tkinter.Entry(user_info)
school_entry.grid(row=3,column=2,padx=20,pady=20)

email = tkinter.Label(user_info,text="Valid Email")
email.grid(row=4,column=0)
email_entry = tkinter.Entry(user_info)
email_entry.grid(row=5,column=0,padx=20,pady=20)

ID = tkinter.Label(user_info,text="ID Number")
ID.grid(row=2,column=0)
ID_entry = tkinter.Entry(user_info)
ID_entry.grid(row=3,column=0,padx=20,pady=20)

password = tkinter.Label(user_info,text="Password")
password.grid(row=4,column=1)
password_entry = tkinter.Entry(user_info)
password_entry.grid(row=5,column=1,padx=20,pady=20)

confirm = tkinter.Label(user_info,text="Confirm Password")
confirm.grid(row=4,column=2)
confirm_entry = tkinter.Entry(user_info)
confirm_entry.grid(row=5,column=2,padx=20,pady=20)





screen.mainloop()