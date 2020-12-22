from tkinter import *

import mysql.connector as m
from tkinter import messagebox
def ex(win5):
    win5.destroy()

def placeorder(sid1,custnm_en,food,Qty,total_en,payment,fooditem,price_en):

    try:

        db = m.connect(host="localhost", username="root", password="", database="food_ordering_app")
        cur = db.cursor()
        a1= custnm_en.get()
        a2= food.get()
        a3 = price_en.get()
        a4=  Qty.get()
        a5 = total_en.get()
        a6= payment.get()

        ins = "INSERT INTO `Customer_info` ( `Server_ID`, `Customer_Name`, `Food`, `Price`, `Quantity`, `Total_Payment`,`Payment_Method`) VALUES ('%d','%s','%s','%d','%d','%d','%s');" % (sid1, a1, a2, int(a3), int(a4), int(a5), a6)
        print(ins)
        cur.execute(ins)
        db.commit()
    except:
        db.rollback()
        messagebox.showerror("Error", "Something went wrong1, Try Again")
        print("error")
    try:
        db = m.connect(host="localhost", username="root", password="", database="food_ordering_app")
        cur = db.cursor()
        sel ="Select Cust_ID from Customer_info"
        print("sel working")
        cur.execute(sel)

        ls= cur.fetchall()
        a7=0
        for i in ls:
           a7=i[0]
        messagebox.showinfo("Congrats","Order Placed, Customer ID: " + str(a7))
    except:
        messagebox.showerror("Error","Something went wrong2, Try Again")
        print("error")


def clear(custnm_en,food,Qty,total_en,payment):
    print("clear")
    custnm_en.delete(0,END)
    food.set("Choose food item")
    Qty.delete(0,END)
    Qty.insert(0,0)
    total_en.delete(0,END)
    payment.delete(0,END)
    payment.insert(0,"Cash")

def calc(fooditem,food,Qty,total_en,price_en):
    ls = [300, 100, 60, 120, 70, 100, 250, 30, 40, 20]
    a2=food.get()
    temp = fooditem.index(a2)
    price = ls[temp]
    price_en.delete(0,END)
    price_en.insert(0,price)
    a3=int(Qty.get())
    total = str(a3 * price)
    total_en.delete(0,END)
    total_en.insert(0,total)



def new_ord(sid):
    sid1=sid
    fooditem =["Pizza ----------------------------- 300","Burger --------------------------- 100",
               "Momos ----------------------------- 60","Falafel nugget -------------------- 120",
               "Wraps ------------------------------70","Ricebowl -------------------------- 100",
               "Biryani ----------------------------250","Paratha -------------------------- 30",
               "Chocolate fatasy ------------------ 40","Coldrinks ------------------------- 20"]
    print("New Order")
    win5=Tk()
    win5.configure(background='#D5DFDF')
    win5.title("New Order")
    win5.geometry("650x600")

    custnm_label = Label(win5,text ="Customer Name ",bg ="#D5DFDF",font=(14))
    custnm_label.grid(row=1,column =1, padx=30,pady=30)

    custnm_en =Entry(win5,width = "30")
    custnm_en.grid(row =1, column = 2)

    item_label = Label(win5, text ="Food Item ", bg="#D5DFDF", font=(14))
    item_label.grid(row=2, column=1)

    food = StringVar(win5)
    food.set("Choose food item")
    drop = OptionMenu(win5,food,*fooditem)
    drop.configure(width="28")
    drop.grid(row=2,column=2,pady=10)

    price_label = Label(win5, text="Price ", bg="#D5DFDF", font=(14))
    price_label.grid(row=3, column=1, padx=30, pady=20)
    price_en = Entry(win5, width="30")

    price_en.grid(row=3, column=2)

    Qty_label = Label(win5, text="Quantity ", bg="#D5DFDF", font=(14))
    Qty_label.grid(row=4, column=1, padx=30, pady=20)

    Qty = Spinbox(win5,width = "28", from_ =0, to= 1000)
    Qty.grid(row = 4, column = 2)

    total = Label(win5,text = "Total Amount",bg="#D5DFDF", font=(14))
    total.grid(row= 5, column =1,pady=10)
    total_en = Entry(win5, width="30")
    total_en.grid(row = 5, column = 2,pady=20)

    payment_label = Label(win5, text ="Payment Method",bg="#D5DFDF", font=(14) )
    payment_label.grid(row =6, column = 1, pady = 20)
    payment = Spinbox(win5, width="28", values=("Cash","UPI","Debit Card","Credit Card"))
    payment.grid(row=6, column = 2)

    place = Button(win5, text="PLACE ORDER", font=(14), command = lambda: placeorder(sid1,custnm_en,food,Qty,total_en,payment,fooditem,price_en))
    place.grid(row=7, column=1, pady=20)
    cle = Button(win5, text="Clear All", font=(14),command =lambda:  clear(custnm_en,food,Qty,total_en,payment))
    cle.grid(row=7, column=2, pady=20, sticky = "w")

    calc_bt = Button(win5,text=" Calculate", font =(14), command = lambda: calc(fooditem,food,Qty,total_en,price_en))
    calc_bt.grid(row = 7, column = 3)
    buttex=Button(win5,text="     Exit     ",font=(14),command = lambda: ex(win5))
    buttex.grid(row=8,column= 3,pady=20,padx=50, sticky = "e")
    win5.mainloop()

