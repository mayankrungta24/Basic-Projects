from tkinter import *

import mysql.connector as m
from tkinter import messagebox
def dk(Cust_en):
    try:
        print("del")
        db= m.connect(host="localhost", username="root", password="", database="food_ordering_app")
        cur = db.cursor()
        a1= Cust_en.get()
        dl =" Delete from Customer_Info where Cust_ID = %d;"%(int(a1))
        print(dl)
        cur.execute(dl)
        db.commit()
        messagebox.showinfo("Info","Order Deleted")
    except:
        db.rollback()
        messagebox.showerror("Error","Something not correct")



def ex(win6):
    win6.destroy()

def dele():
    print("delete order")
    win6 =Tk()
    win6.configure(background='#D5DFDF')
    win6.title("Delete Order")
    win6.geometry("300x300")

    del_label = Label(win6,text="Enter Cust. ID", bg ="#D5DFDF",font=( 14))
    del_label.grid(row=1,column=1,padx=20,pady=20)

    Cust_en=Entry(win6,width="10")
    Cust_en.grid(row=1,column=2)

    Delete_b = Button(win6,text="Delete Order", command=lambda : dk(Cust_en))
    Delete_b.grid(row=2, column=1, pady=30)

    back_bt = Button(win6,text="Back", command=lambda: ex(win6))
    back_bt.grid(row=2, column=2)
    win6.mainloop()



