from tkinter import *
from tkinter import messagebox
import os

def register_window():
    global register
    register = Toplevel(window)
    register.minsize(height=300,width=250)
    register.maxsize(height=300,width=250)
    register.title("Register")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register, text="Please input your details",font="times 14 bold",bg="light blue").pack()
    Label(register, text="").pack()
    username_label = Label(register, text="Username")
    username_label.pack()
    username_entry = Entry(register, textvariable=username,bd=3,font="times 14")
    username_entry.pack()
    password_label = Label(register, text="Password")
    password_label.pack()
    password_entry = Entry(register, textvariable=password, show='*',bd=3,font="times 14")
    password_entry.pack()
    Label(register, text="").pack()
    Button(register, text="Submit", width=10, height=1, bg="maroon",fg="white", command=register_user).pack()

def login():
    global login_screen
    login_screen = Toplevel(window)
    login_screen.title("Login")
    login_screen.minsize(height=300,width=250)
    login_screen.maxsize(height=300, width=250)
    Label(login_screen, text="Please enter the details",font="times 14 bold",bg="light blue").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, bg="maroon",fg="white",command=login_verify).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register, text="Registration Success", fg="green", font=("calibri", 11)).pack()



def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


def delete_login_success():
    login_success_screen.destroy()
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
def delete_user_not_found_screen():
    user_not_found_screen.destroy()


window = Tk()
window.minsize(height=300,width=250)
window.maxsize(height=300,width=250)
window.title("Account Login")
Label(text="Account Login", width="300", height="2", bg="light blue",font=("Calibri", 13,"bold")).pack()
Label(text="").pack()
Button(text="Login", height="2", width="30",bg="maroon",fg="white", command=login,bd=5).pack()
Label(text="").pack()
Button(text="Register", height="2", width="30",bg="maroon",fg="white", command=register_window,bd=5).pack()
Label(text="").pack()
Label(text="If don't have an account,\nplease do register", width="300", height="2",bg="light blue",font=("Calibri", 13,"bold")).pack()

window.mainloop()

