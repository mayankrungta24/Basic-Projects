from tkinter import *
import mysql.connector as m
from tkinter import messagebox
from login import exit_,login
def exit_(win1):
   win1.destroy()
def ui():


   win1 = Tk()
   win1.configure(background='#D5DFDF')
   win1.title("Login Page")
   win1.geometry("650x300")

   admin = Label(text="FOOD ORDERING SYSTEM", bg="#D5DFDF", font=("Zapfino", 14, "bold italic"))
   admin.grid(row=0, column=1, columnspan=3, sticky='e', padx=150, pady=10)

   login_label = Label(text="login ID", bg="#D5DFDF", font=(14))
   login_label.grid(row=1, column=1, padx=50, sticky='e', pady=5)
   login_en = Entry(width="20")
   login_en.grid(row=1, column=2, sticky='w')

   password_label = Label(text="password", bg="#D5DFDF", font=(14))
   password_label.grid(row=2, column=1, padx=50, sticky='e', pady=10)
   password_en = Entry(width="20", show='*')
   password_en.grid(row=2, column=2, sticky='w', pady=10)

   login_ = Button(text="Login", command=lambda: login(win1,login_en, password_en))
   login_.grid(row=3, column=2, sticky='w', pady=10, padx=17)

   New_user_ = Button(text="New User", command=lambda: nu(win1))
   New_user_.grid(row=3, column=2)

   exit = Button(text="Exit", font=(14), command= lambda : exit_(win1))
   exit.grid(row=3, column=3, sticky='w')

   win1.mainloop()


def nu(win1):
    try:
        def back_():
            print("back")
            win2.destroy()
            ui()
        def addinfo_():
            try:
                print(1)
                db = m.connect(host="localhost", username="root", password="", database="food_ordering_app")
                cur = db.cursor()
                a1=Name_entry.get()
                a2=DOB_entry.get()
                a3=Mob_entry.get()
                a4=City_entry.get()
                a5 = Email_entry.get()
                a6 = ps_entry.get()


                ins = "INSERT INTO `server` ( `Name`, `DOB`, `Mobile No.`, `City`, `Email`, `Password`) VALUES ('%s','%s','%d','%s','%s','%s');" % (a1, a2, int(a3), a4, a5, a6)

                cur.execute(ins)
                db.commit()
                print("Info Added")
            except:
                db.rollback()
                messagebox.showerror("Error")

        exit_(win1)
        win2= Tk()
        win2.configure(background='#D5DFDF')
        win2.title("New User Page")
        win2.geometry("650x700")

        admin = Label(text="User Registration", bg="#D5DFDF", font=("Zapfino", 14, "bold italic"))
        admin.grid(row=0, column=1, columnspan=3, sticky='e', padx=250, pady=10)

        Name_label = Label(text="Name", bg ="#D5DFDF",font=("Zapfino", 16))
        Name_label.grid(row=2, column =1)
        Name_entry = Entry(width=30)
        Name_entry.grid(row=2, column =2, pady = 10)

        DOB_label = Label(text="DOB", bg="#D5DFDF", font=("Zapfino", 12))
        DOB_label.grid(row=3, column=1)
        DOB_entry = Entry(width=30)
        DOB_entry.grid(row=3, column=2, pady =10)

        Mob_label = Label(text="Mobile Number", bg="#D5DFDF", font=("Zapfino", 13))
        Mob_label.grid(row=4, column=1)
        Mob_entry = Entry(width=30)
        Mob_entry.grid(row=4, column=2, pady=10)

        City_label = Label(text="City", bg="#D5DFDF", font=("Zapfino", 13))
        City_label.grid(row=5, column=1)
        City_entry = Entry(width=30)
        City_entry.grid(row=5, column=2, pady=10)

        Email_label = Label(text="Email", bg="#D5DFDF", font=("Zapfino", 13))
        Email_label.grid(row=6, column=1)
        Email_entry = Entry(width=30)
        Email_entry.grid(row=6, column=2, pady=10)

        ps_label = Label(text="Password", bg="#D5DFDF", font=("Zapfino", 13))
        ps_label.grid(row=7, column=1)
        ps_entry = Entry(width=30, show ="*")
        ps_entry.grid(row=7, column=2, pady=10)

        Add_ = Button(text="Add Info", font=(14), command = addinfo_)
        Add_.grid(row=8, column=1, pady =20)

        Back_ = Button(text="Back", font=(14),command = back_)
        Back_.grid(row=8, column=2, pady=20)


        win2.mainloop()
    except:
        messagebox.showerror('Error', 'Something missing')
