
import mysql.connector as m
from tkinter import messagebox
from loginbridge import log

def login(win1,login_en,password_en):
    try:

        db = m.connect(host="localhost", username="root", password="", database="food_ordering_app")
        cur = db.cursor()
        sel = " Select Email,Password,Server_ID from server"
        cur.execute(sel)
        ls=cur.fetchall()
        print(ls)
        id = login_en.get()
        ps = password_en.get()
        flag = 0
        fl=0
        sid=0
        for i in ls:
            if (id == i[0] and ps == i[1] ):
                flag=1
                sid=i[2]
                print("match found ", flag)
                log(win1,sid)
                break
        if flag == 0:
            print(flag)
            for i in ls:
                if id == i[0]:
                    fl=1
                    messagebox.showerror('Error', 'ID and password do not match')
                    break

            if fl ==0:
                messagebox.showerror('Error', 'ID not found')

    except:
        messagebox.showerror('Error', 'Something missing')

def exit_(win1):
   win1.destroy()



