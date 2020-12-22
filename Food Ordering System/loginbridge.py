from tkinter import *
from neworder import new_ord
from vieworder import view_order
from deleteorder import dele
from logout import logout

def qf():
    print("dewfwe")

def log(win1,sid):
    sid1 = sid
    win1.destroy()
    win3 = Tk()
    win3.configure(background='#D5DFDF')
    win3.title("options")
    win3.geometry("650x300")

    new_order = Button(text="New Order", width=15, command= lambda : new_ord(sid1))
    new_order.grid(row=1, column=1, pady=20, padx=250)

    View_order = Button(text="View Order", width=15, command=view_order)
    View_order.grid(row=2, column=1, pady=20, padx=1)

    Delete_order = Button(text="Delete Order", width=15, command=dele)
    Delete_order.grid(row=3, column=1, pady=20, padx=1)

    Logout = Button(text="Logout", width=15, command= lambda: logout(win3))
    Logout.grid(row=4, column=1, pady=20, padx=1)

    win3.mainloop()
