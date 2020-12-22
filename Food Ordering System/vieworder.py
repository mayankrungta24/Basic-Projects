from tkinter import *
import mysql.connector as m
from tkinter import messagebox

def cl(Cust_en,Cust_nm,Food_en,price_en,Qty_en,Total_en,Pay_en):
    print("Clear")
    Cust_en.delete(0,END)
    Cust_nm.delete(0, END)
    Food_en.delete(0, END)
    price_en.delete(0, END)
    Qty_en.delete(0, END)
    Total_en.delete(0, END)
    Pay_en.delete(0, END)

def exi(win):
    print("exit")
    win.destroy()
def view(Cust_en,Cust_nm,Food_en,price_en,Qty_en,Total_en,Pay_en):
    try:
        print("view")
        db = m.connect(host="localhost", username="root", password="", database="food_ordering_app")
        cur = db.cursor()
        a= Cust_en.get()
        sel ="select * from Customer_Info where Cust_ID = %d;"%(int(a))
        cur.execute(sel)
        ls= cur.fetchall()
        i=ls

        if i:

            Cust_nm.delete(0,END)
            Cust_nm.insert(0,i[0][2])
            Food_en.delete(0, END)
            Food_en.insert(0, i[0][3])
            price_en.delete(0, END)
            price_en.insert(0, i[0][4])
            Qty_en.delete(0, END)
            Qty_en.insert(0, i[0][5])
            Total_en.delete(0, END)
            Total_en.insert(0, i[0][6])
            Pay_en.delete(0, END)
            Pay_en.insert(0, i[0][7])
        else:
            messagebox.showerror("Error", "Customer ID not found")

        print(ls)
    except:
        messagebox.showerror("Error", "Something Wrong")
def view_order():
    print("View order")
    db = m.connect(host="localhost", username="root", password="", database="food_ordering_app")
    cur = db.cursor()
    winVO = Tk()
    winVO.configure(background='#D5DFDF')
    winVO.title("View Order")
    winVO.geometry("650x600")

    View_label = Label(winVO, text="Enter Cust. ID", bg="#D5DFDF", font=(14))
    View_label.grid(row=1, column=1, padx=70, pady=20,sticky="w")

    Cust_en = Entry(winVO, width="30")
    Cust_en.grid(row=1, column=2)

    Custnm_label = Label(winVO, text="Customer Name", bg="#D5DFDF", font=(14))
    Custnm_label.grid(row=2, column=1, pady=20)
    Cust_nm = Entry(winVO, width="30")
    Cust_nm.grid(row=2, column=2)

    Food_label = Label(winVO, text="Food", bg="#D5DFDF", font=(14))
    Food_label.grid(row=3, column=1, pady=20)
    Food_en = Entry(winVO, width="30")
    Food_en.grid(row=3, column=2)

    price_label = Label(winVO, text="Price", bg="#D5DFDF", font=(14))
    price_label.grid(row=4, column=1, pady=20)
    price_en = Entry(winVO, width="30")
    price_en.grid(row=4, column=2)

    Qty_label = Label(winVO, text="Quantity", bg="#D5DFDF", font=(14))
    Qty_label.grid(row=5, column=1, pady=20)
    Qty_en = Entry(winVO, width="30")
    Qty_en.grid(row=5, column=2)

    Total_label = Label(winVO, text="Total Amount", bg="#D5DFDF", font=(14))
    Total_label.grid(row=6, column=1, pady=20)
    Total_en = Entry(winVO, width="30")
    Total_en.grid(row=6, column=2)

    Pay_label = Label(winVO, text="Payment Method", bg="#D5DFDF", font=(14))
    Pay_label.grid(row=7, column=1, pady=20)
    Pay_en = Entry(winVO, width="30")
    Pay_en.grid(row=7, column=2)

    backbt= Button(winVO,text="View",width ="10",font=(14), command = lambda: view(Cust_en,Cust_nm,Food_en,price_en,Qty_en,Total_en,Pay_en))
    backbt.grid(row=8,column =1, pady =30)

    exbt= Button(winVO,text="Back",width ="10",font=(14), command = lambda: exi(winVO))
    exbt.grid(row=9, column=1)

    clearbt=Button(winVO,text="Clear",width ="10",font=(14), command = lambda: cl(Cust_en,Cust_nm,Food_en,price_en,Qty_en,Total_en,Pay_en))
    clearbt.grid(row=8, column=2 )


    winVO.mainloop()

