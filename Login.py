from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

frame = Frame(root,width=350,height=350,bg="White")
frame.place(x=480,y=70)
heading=Label(frame,text="Login",fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
heading.place(x=100,y=5)

def enter(e):
    user.delete(0,"end")
def leave(e):
    name=user.get()
    if name=="":
        user.insert(0,"User Email: ")
        
user = Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11,))
user.place(x=30,y=80)
user.insert(0,"User Email: ")
user.bind("<FocusIn>", enter)
user.bind("<FocusOut>",leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

###########___________________________________________________
def enter(e):
    san.delete(0,"end")
def leave(e):
    name=san.get()
    if name=="":
        san.insert(0,"Password: ")


san= Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11,))
san.place(x=30,y=150)
san.insert(0,"Password: ")
san.bind("<FocusIn>",enter)
san.bind("<FocusOut>",leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)

###############################################################
######Button(frame,width=39,pady=7,text="Sign in",bg="#57a1f8",fg="white",border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg="black",bg="white",font=("Microsoft YaHei UI Light",9,))
label.place(x=75,y=270)

register = Button(frame,width=6,text="Register",border=0,bg="White",cursor="hand2",fg="#57a1f8")
register.place(x=215,y=270)



root.mainloop()