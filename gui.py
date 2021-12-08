from tkinter import *
import tkinter.ttk
import sys

def addMedicine(submenuframe):
    form = Frame(submenuframe)
    form.pack(side=BOTTOM)
    input1 = Text(form, width=20, height=10)
    input1.pack()


# call this funtion to draw in right frame
def MedicineMenu():
    submenuframe = Frame(window, height=400, width=650)
    submenuframe.place( x=165, y=0)
    heading = Label(submenuframe,width="54", text="Medicine Menu",font='Helvetica 14 bold', bg="#590000", foreground="white")
    heading.pack(side=TOP)

    b1 = Button(submenuframe,height=2, width=21, text="Add new madicine", fg="red", command=lambda: addMedicine(submenuframe))
    b1.pack(side=LEFT, ipady=5)
    b2 = Button(submenuframe,height=2, width=21, text="Search Medicine", fg="red" )
    b2.pack(side=LEFT, ipady=5)
    b2 = Button(submenuframe,height=2, width=21, text="Update Medicine", fg="red" )
    b2.pack(side=LEFT, ipady=5)
    b2 = Button(submenuframe,height=2, width=21, text="Medicine be\npurchased", fg="red" )
    b2.pack(side=LEFT, ipady=5)
    addMedicine(submenuframe)
# call this funtion to draw in right frame
def CustomerMenu():
    submenuframe = Frame(window, height=400, width=650)
    submenuframe.place( x=165, y=0)
    heading = Label(submenuframe,width="54", text="Customer Menu",font='Helvetica 14 bold', bg="#590000", foreground="white")
    heading.pack(side=TOP)

    b1 = Button(submenuframe,height=2, width=28, text="Search Customer", fg="red" )
    b1.pack(side=LEFT, ipady=5)
    b2 = Button(submenuframe,height=2, width=28, text="New Customer", fg="red" )
    b2.pack(side=LEFT, ipady=5)
    b2 = Button(submenuframe,height=2, width=28, text="Update Customer Info", fg="red" )
    b2.pack(side=LEFT, ipady=5)

# call this funtion to draw in right frame
def SupplierMenu():
    submenuframe = Frame(window, height=400, width=650)
    submenuframe.place( x=165, y=0)
    heading = Label(submenuframe,width="54", text="Supplier Menu",font='Helvetica 14 bold', bg="#590000", foreground="white")
    heading.pack(side=TOP)

    b1 = Button(submenuframe,height=2, width=28, text="Search Supplier", fg="red" )
    b1.pack(side=LEFT, ipady=5)
    b2 = Button(submenuframe,height=2, width=28, text="New Supplier", fg="red" )
    b2.pack(side=LEFT, ipady=5)
    b2 = Button(submenuframe,height=2, width=28, text="Update Supplier Info", fg="red" )
    b2.pack(side=LEFT, ipady=5)

# call this funtion to draw in right frame
def MedicineMenu():
    submenuframe = Frame(window, height=400, width=650)
    submenuframe.place( x=165, y=0)
    heading = Label(submenuframe,width="54", text="Medicine Menu",font='Helvetica 14 bold', bg="#590000", foreground="white")
    heading.pack(side=TOP)

    b1 = Button(submenuframe,height=2, width=21, text="Add new madicine", fg="red" )
    b1.pack(side=LEFT, ipady=5)
    b2 = Button(submenuframe,height=2, width=21, text="Search Medicine", fg="red" )
    b2.pack(side=LEFT, ipady=5)
    b2 = Button(submenuframe,height=2, width=21, text="Update Medicine", fg="red" )
    b2.pack(side=LEFT, ipady=5)
    b2 = Button(submenuframe,height=2, width=21, text="Medicines to be\npurchased", fg="red" )
    b2.pack(side=LEFT, ipady=5)
    
# call this funtion to draw in right frame
def ReportMenu():
    submenuframe = Frame(window, height=400, width=650)
    submenuframe.place( x=165, y=0)
    heading = Label(submenuframe,width="54", text="Report Menu",font='Helvetica 14 bold', bg="#590000", foreground="white")
    heading.pack(side=TOP)

    b1 = Button(submenuframe,height=2, width=17, text="Day Sales", fg="red" )
    b1.pack(side=LEFT, ipady=5)
    b2 = Button(submenuframe,height=2, width=17, text="Months Sales", fg="red" )
    b2.pack(side=LEFT, ipady=5)
    b2 = Button(submenuframe,height=2, width=17, text="Day Purchase", fg="red" )
    b2.pack(side=LEFT, ipady=5)
    b2 = Button(submenuframe,height=2, width=17, text="Month Purchase", fg="red" )
    b2.pack(side=LEFT, ipady=5)
    b2 = Button(submenuframe,height=2, width=17, text="Profit Report", fg="red" )
    b2.pack(side=LEFT, ipady=5)

# call this funtion to draw in right frame
def InvoiceMenu():
    submenuframe = Frame(window, height=400, width=650)
    submenuframe.place( x=165, y=0)
    heading = Label(submenuframe,width="54", text="Invoice Menu",font='Helvetica 14 bold', bg="#590000", foreground="white")
    heading.pack(side=TOP)

    b1 = Button(submenuframe,height=2, width=44, text="Supplier Invoice", fg="red" )
    b1.pack(side=LEFT, ipady=5)
    b2 = Button(submenuframe,height=2, width=44, text="Customer Invoice", fg="red" )
    b2.pack(side=LEFT, ipady=5)
    


#Main Menu
window = Tk()
window.geometry('815x400')
window.maxsize(815,400)
window.minsize(815,400)

window.title("Pharmacy Management Software")

main_menu = Frame(window, width=21, height=400)
main_menu.place(x=0, y=0)


separator = tkinter.ttk.Separator(window, orient='vertical')
separator.place(relx=0.2, rely=0, relwidth=0.2, relheight=1)



btn1 = Button(main_menu,height=2, width=21, text="Medicine Menu",fg="red", command=MedicineMenu)
btn1.pack(side=TOP )
btn2 = Button(main_menu,height=2, width=21, text="Customer Menu",fg="red", command=CustomerMenu)
btn2.pack(side=TOP)
btn3 = Button(main_menu,height=2, width=21, text="Supplier Menu",fg="red", command=SupplierMenu)
btn3.pack(side=TOP)
btn4 = Button(main_menu,height=2, width=21, text="Report Menu",fg="red", command=ReportMenu)
btn4.pack(side=TOP)
btn5 = Button(main_menu,height=2, width=21, text="Invoicing Menu",fg="red", command=InvoiceMenu)
btn5.pack(side=TOP)



MedicineMenu()

window.mainloop()
