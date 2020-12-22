from tkinter import *
from login import login
from nu import nu

def exit1_():
   win1.destroy()

win1=Tk()
win1.configure(background='#D5DFDF')
win1.title("Login Page")
win1.geometry("650x300")

Title = Label(text ="FOOD ORDERING SYSTEM", bg ="#D5DFDF",font=("Zapfino", 14, "bold italic"))
Title.grid(row=0,column=1,columnspan=3,sticky='e',padx=150,pady=10)




login_label = Label(text="login ID", bg ="#D5DFDF",font=(14) )
login_label.grid(row=1,column =1,padx=50,sticky='e',pady=5)
login_en = Entry(width="20")
login_en.grid(row=1,column =2,sticky='w')


password_label = Label(text="password", bg ="#D5DFDF",font=(14) )
password_label.grid(row=2,column =1,padx=50,sticky='e',pady=10)
password_en = Entry(width="20",show='*')
password_en.grid(row=2,column =2,sticky='w',pady=10)

login_ = Button(text="Login",command=lambda: login(win1,login_en,password_en))
login_.grid(row=3,column =2,sticky='w',pady=10,padx=17)

New_user_ = Button(text = "New User", command =lambda: nu(win1))
New_user_.grid(row=3,column =2)

exit=Button(text="   Exit   ",font=(14),command= exit1_)
exit.grid( row=4,column =3,pady=40)




win1.mainloop()
