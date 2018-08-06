from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox
import random
import time
import datetime

root = Tk()
root.geometry("1280x700")
root.title("TRAIN TICKETING")
root.iconbitmap('TRAIN.ico')
root.configure(background='black')

#Functions
def Click(numbers):
    global operator
    operator = operator +str(numbers)
    text_input.set(operator)

def Clear():
    global operator
    operator=""
    text_input.set("")

def equal():
    global operator
    sumup =str(eval(operator))
    text_input.set(sumup)
    operator("")

def Exitt():
    qExit=tkinter.messagebox.askyesno("Quit System","Do you want to quit?")
    if qExit>0:
        root.destroy()
        return

def Travel_Cost():
    if (var9.get()=="Katra" and  var4.get()== 1):
        if(var1.get()==1):
            Tcost = float(540)
            TicketClass.set("Standard")
        elif (var2.get()== 1):
            Tcost = float(600)
            TicketClass.set("Economy")
        elif (var3.get()== 1):
            Tcost = float(750)
            TicketClass.set("First Class")
        Single = float(var12.get())
        Adult_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.03))
        Adult_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.03)))
        if (var11.get()== 1):
            Single = float(var12.get())
            Adult_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.03)*2))
            Adult_Fees = "₹", str('%.2f' % ((Tcost * Single)*2))
            TotalCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.03))*2))

        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        TicketClass.set("Standard")
        TicketClass.set("Economy")
        TicketClass.set("First Class")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("J&K")
        To_Destination.set("Katra")
        Fee_Price.set(TotalCost)
        Total.set(Adult_Fees)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)

    elif (var9.get()== "Katra" and  var5.get()== 1):
        if (var1.get() == 1):
            Tcost = float(270)
            TicketClass.set("Standard")
        elif (var2.get() == 1):
            Tcost = float(320)
            TicketClass.set("Standard")
        elif (var3.get() == 1):
            Tcost = float(320)
            TicketClass.set("Standard")
        Single = float(var12.get())
        Child_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.03))
        Child_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.03)))
        if ( var11.get()== 1):
            Single = float(var12.get())
            Child_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.03) * 2))
            Child_Fees = "₹", str('%.2f' % ((Tcost * Single) * 2))
            ChildCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.03)) * 2))

        Tax.set(Child_Tax)
        SubTotal.set(Child_Fees)
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("J&K")
        To_Destination.set("Katra")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)


    elif (var9.get()== "Amritsar" and var4.get()== 1):
        if (var1.get() == 1):
            Tcost = float(260)
            TicketClass.set("Standard")
        elif (var2.get() == 1):
            Tcost = float(495)
            TicketClass.set("Economy")
        elif (var3.get() == 1):
            Tcost = float(700)
            TicketClass.set("First Class")
        Single = float(var12.get())
        Adult_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.03))
        Adult_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.03)))
        if (var11.get() == 1):
            Single = float(var12.get())
            Adult_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.03) * 2))
            Adult_Fees = "₹", str('%.2f' % ((Tcost * Single) * 2))
            TotalCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.03)) * 2))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("J&K")
        To_Destination.set("Amritsar")
        Fee_Price.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)


    elif (var9.get()== "Amritsar" and var5.get()== 1):
        if (var1.get() == 1):
            Tcost = float(125)
            TicketClass.set("Standard")
        elif (var2.get() == 1):
            Tcost = float(300)
            TicketClass.set("Standard")
        elif (var3.get() == 1):
            Tcost = float(565)
            TicketClass.set("Standard")
        Single = float(var12.get())
        Child_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.03))
        Child_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.03)))
        if ( var11.get()== 1):
            Single = float(var12.get())
            Child_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.03) * 2))
            Child_Fees = "₹", str('%.2f' % ((Tcost * Single) * 2))
            ChildCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.03)) * 2))
        Tax.set(Child_Tax)
        SubTotal.set(Child_Fees)
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("J&K")
        To_Destination.set("Amritsar")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)


    elif (var9.get()== "Mumbai" and var4.get()== 1):
        if (var1.get() == 1):
            Tcost = float(685)
            TicketClass.set("Standard")
        elif (var2.get() == 1):
            Tcost = float(1895)
            TicketClass.set("Economy")
        elif (var3.get() == 1):
            Tcost = float(2705)
            TicketClass.set("First Class")
        Single = float(var12.get())
        Adult_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.03))
        Adult_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.03)))
        if (var11.get() == 1):
            Single = float(var12.get())
            Adult_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.03) * 2))
            Adult_Fees = "₹", str('%.2f' % ((Tcost * Single) * 2))
            TotalCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.03)) * 2))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("J&K")
        To_Destination.set("Mumbai")
        Fee_Price.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)


    elif (var9.get()== "Mumbai" and var5.get()== 1):
        if (var1.get() == 1):
            Tcost = float(490)
            TicketClass.set("Standard")
        elif (var2.get() == 1):
            Tcost = float(1595)
            TicketClass.set("Standard")
        elif (var3.get() == 1):
            Tcost = float(2205)
            TicketClass.set("Standard")
        Single = float(var12.get())
        Child_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.03))
        Child_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.03)))
        if ( var11.get()== 1):
            Single = float(var12.get())
            Child_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.03) * 2))
            Child_Fees = "₹", str('%.2f' % ((Tcost * Single) * 2))
            ChildCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.03)) * 2))
        Tax.set(Child_Tax)
        SubTotal.set(Child_Fees)
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("J&K")
        To_Destination.set("Mumbai")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)


    elif (var9.get()== "Delhi" and var4.get()== 1):
        if (var1.get() == 1):
            Tcost = float(930)
            TicketClass.set("Standard")
        elif (var2.get() == 1):
            Tcost = float(960)
            TicketClass.set("Economy")
        elif (var3.get() == 1):
            Tcost = float(1050)
            TicketClass.set("First Class")
        Single = float(var12.get())
        Adult_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.03))
        Adult_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.03)))
        if (var11.get() == 1):
            Single = float(var12.get())
            Adult_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.03) * 2))
            Adult_Fees = "₹", str('%.2f' % ((Tcost * Single) * 2))
            TotalCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.03)) * 2))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("J&K")
        To_Destination.set("Mumbai")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)


    elif (var9.get()== "Delhi" and var5.get()== 1):
        if (var1.get() == 1):
            Tcost = float(400)
            TicketClass.set("Standard")
        elif (var2.get() == 1):
            Tcost = float(430)
            TicketClass.set("Standard")
        elif (var3.get() == 1):
            Tcost = float(420)
            TicketClass.set("Standard")
        Single = float(var12.get())
        Child_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.03))
        Child_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.03)))
        if ( var11.get()== 1):
            Single = float(var12.get())
            Child_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.03) * 2))
            Child_Fees = "₹", str('%.2f' % ((Tcost * Single) * 2))
            ChildCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.03)) * 2))
        Tax.set(Child_Tax)
        SubTotal.set(Child_Fees)
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("J&K")
        To_Destination.set("Delhi")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)



    elif (var9.get()== "Ludhiana" and var4.get()== 1):
        if (var1.get() == 1):
            Tcost = float(560)
            TicketClass.set("Standard")
        elif (var2.get() == 1):
            Tcost = float(620)
            TicketClass.set("Economy")
        elif (var3.get() == 1):
            Tcost = float(700)
            TicketClass.set("First Class")
        Single = float(var12.get())
        Adult_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.03))
        Adult_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.03)))
        if (var11.get() == 1):
            Single = float(var12.get())
            Adult_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.03) * 2))
            Adult_Fees = "₹", str('%.2f' % ((Tcost * Single) * 2))
            TotalCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.03)) * 2))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("J&K")
        To_Destination.set("Ludhiana")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)


    elif (var9.get()== "Ludhiana" and var5.get()== 1):
        if (var1.get() == 1):
            Tcost = float(230)
            TicketClass.set("Standard")
        elif (var2.get() == 1):
            Tcost = float(270)
            TicketClass.set("Standard")
        elif (var3.get() == 1):
            Tcost = float(350)
            TicketClass.set("Standard")
        Single = float(var12.get())
        Child_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.03))
        Child_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.03)))
        if ( var11.get()== 1):
            Single = float(var12.get())
            Child_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.03) * 2))
            Child_Fees = "₹", str('%.2f' % ((Tcost * Single) * 2))
            ChildCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.03)) * 2))
        Tax.set(Child_Tax)
        SubTotal.set(Child_Fees)
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("J&K")
        To_Destination.set("Ludhiana")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)



    elif (var9.get()== "Jalhandar" and var4.get()== 1):
        if (var1.get() == 1):
            Tcost = float(500)
            TicketClass.set("Standard")
        elif (var2.get() == 1):
            Tcost = float(540)
            TicketClass.set("Economy")
        elif (var3.get() == 1):
            Tcost = float(600)
            TicketClass.set("First Class")
        Single = float(var12.get())
        Adult_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.03))
        Adult_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.03)))
        if (var11.get() == 1):
            Single = float(var12.get())
            Adult_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.03) * 2))
            Adult_Fees = "₹", str('%.2f' % ((Tcost * Single) * 2))
            TotalCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.03)) * 2))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("J&K")
        To_Destination.set("Jalhandar")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)


    elif (var9.get()== "Jalhandar" and var5.get()== 1):
        if (var1.get() == 1):
            Tcost = float(200)
            TicketClass.set("Standard")
        elif (var2.get() == 1):
            Tcost = float(240)
            TicketClass.set("Standard")
        elif (var3.get() == 1):
            Tcost = float(300)
            TicketClass.set("Standard")
        Single = float(var12.get())
        Child_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.03))
        Child_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.03)))
        if ( var11.get()== 1):
            Single = float(var12.get())
            Child_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.03) * 2))
            Child_Fees = "₹", str('%.2f' % ((Tcost * Single) * 2))
            ChildCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.03)) * 2))
        Tax.set(Child_Tax)
        SubTotal.set(Child_Fees)
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("J&K")
        To_Destination.set("Jalhandar")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)



    elif (var9.get()== "Bathinda" and var4.get()== 1):
        if (var1.get() == 1):
            Tcost = float(250)
            TicketClass.set("Standard")
        elif (var2.get() == 1):
            Tcost = float(300)
            TicketClass.set("Economy")
        elif (var3.get() == 1):
            Tcost = float(350)
            TicketClass.set("First Class")
        Single = float(var12.get())
        Adult_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.03))
        Adult_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.03)))
        if (var11.get() == 1):
            Single = float(var12.get())
            Adult_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.03) * 2))
            Adult_Fees = "₹", str('%.2f' % ((Tcost * Single) * 2))
            TotalCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.03)) * 2))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("J&K")
        To_Destination.set("Bathinda")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)


    elif (var9.get()== "Bathinda" and var5.get()== 1):
        if (var1.get() == 1):
            Tcost = float(100)
            TicketClass.set("Standard")
        elif (var2.get() == 1):
            Tcost = float(145)
            TicketClass.set("Standard")
        elif (var3.get() == 1):
            Tcost = float(220)
            TicketClass.set("Standard")
        Single = float(var12.get())
        Child_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.03))
        Child_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.03)))
        if ( var11.get()== 1):
            Single = float(var12.get())
            Child_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.03) * 2))
            Child_Fees = "₹", str('%.2f' % ((Tcost * Single) * 2))
            ChildCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.03)) * 2))
        Tax.set(Child_Tax)
        SubTotal.set(Child_Fees)
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("J&K")
        To_Destination.set("Bathinda")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)


#Declaring variables

text_input=StringVar()
operator=("")
Tax =StringVar()
SubTotal =StringVar()
TotalCost=StringVar()
Total=StringVar()
date1=StringVar()
time1=StringVar()

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=StringVar()
var7=StringVar()
var8=StringVar()
var9=StringVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
Tax=StringVar()

TicketClass=StringVar()
TicketPrice=StringVar()
Child_Ticket=StringVar()
Adult_Ticket=StringVar()
From_Destination=StringVar()
To_Destination=StringVar()
Fee_Price=StringVar()
Route=StringVar()
Receipt_Ref=StringVar()

var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")
var9.set("")
var10.set("0")
var11.set("0")
var12.set("0")
Tax.set("0")
Total.set("0")
SubTotal.set("0")
TotalCost.set("0")
TicketClass.set("")
TicketPrice.set("")
Child_Ticket.set("")
Adult_Ticket.set("")
From_Destination.set("")
To_Destination.set("")
Fee_Price.set("0")
Route.set("")
Receipt_Ref.set("")

def reset():
    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("")
    var10.set("0")
    var11.set("0")
    var12.set("")
    Tax.set("0")
    Total.set("0")
    SubTotal.set("0")
    TotalCost.set("0")
    TicketClass.set("")
    TicketPrice.set("")
    Child_Ticket.set("")
    Adult_Ticket.set("")
    From_Destination.set("")
    To_Destination.set("")
    Fee_Price.set("0")
    Route.set("")
    Receipt_Ref.set("")


#Date and Time
date1.set(time.strftime("%d/%m/%y"))
time1.set(time.strftime('%H:%M:%S'))

#Top box
Top =Frame(root,width=1280,height=100,bd=7,relief='raise')
a=Label(Top,text="Train Ticketing System",font=("times",36,"bold"))
a.pack()
Top.pack(side=TOP,fill=X)

#3 boxes
f1=Frame(root,height=600,width=750,bd=8,relief='raise')
f1a=Frame(f1)
topFrame1=Frame(f1a,width=250,height=300,bd=8,relief='raise')
topFrame1.pack(side=LEFT,fill=BOTH)
b=Label(topFrame1,text="Class",font=("times",24,"bold"))
b.pack()
sp1=Checkbutton(topFrame1,text="Standard",font=("time",20,"italic"),variable=var1,onvalue=1,offvalue=0)
sp2=Checkbutton(topFrame1,text="Economy",font=("time",20,"italic"),variable=var2,onvalue=1,offvalue=0)
sp3=Checkbutton(topFrame1,text="First Class",font=("time",20,"italic"),variable=var3,onvalue=1,offvalue=0)
sp1.pack()
sp2.pack()
sp3.pack()

topFrame2=Frame(f1a,width=250,height=300,bd=8,relief='raise')
topFrame2.pack(side=LEFT,fill=BOTH)
frm=Frame(topFrame2,width=250,relief='raise')
c=Label(frm,text="Destination selector",font=("time",30,"bold"))
c.pack()
frm.pack(side=TOP)
frm1=Frame(topFrame2,width=250,relief='raise')
d=Label(frm1,text="Destination",font=("time",24,"bold"))
d.grid(row=0,column=0,sticky=W)
combo=ttk.Combobox(frm1,textvariable=var9,state='readonly')
combo['value']=['','Katra','Mumbai','Bathinda','Delhi','Ludhiana','Jalhandar','Amritsar','J&K']
combo.grid(row=0,column=1,sticky=W)
c1=Checkbutton(frm1,text="Adult",font=("time",20,"italic"),variable=var4,onvalue=1,offvalue=0)
c1.grid(row=1,column=0,sticky=W)
c2=Checkbutton(frm1,text="Child",font=("time",20,"italic"),variable=var5,onvalue=1,offvalue=0)
c2.grid(row=2,column=0,sticky=W)
frm1.pack(side=BOTTOM)

topFrame3=Frame(f1a,width=250,height=300,bd=8,relief='raise')
topFrame3.pack(side=LEFT,fill=BOTH)
frm2=Frame(topFrame3)
e=Label(frm2,text="Ticket Type",font=("times",24,"bold"))
e.pack()
frm2.pack(side=TOP)

frm3=Frame(topFrame3)
ch1=Checkbutton(frm3,text="Single",font=("time",20,"italic"),variable=var10,onvalue=1,offvalue=0,command=Button)
ch1.grid(row=0,column=0)
ch2=Checkbutton(frm3,text="Return",font=("time",20,"italic"),variable=var11,onvalue=1,offvalue=0,command=Button)
ch2.grid(row=1,column=0)
frm3.pack(side=TOP)

frm4=Frame(topFrame3)
f=Label(frm4,text="Pas. No.",font=("times",22,"italic"))
f.grid(row=2,column=0,sticky=W)
ent3=Entry(frm4,textvariable=var12)
ent3.grid(row=2,column=1,sticky=W)
frm4.pack(side=TOP,fill=Y)

f1a.pack(side=TOP,fill=X)

#below 3 boxes
f2a=Frame(f1,width=750,height=300,bd=8,relief='raise')

bottomLeft=Frame(f2a,width=400,height=300,bd=8,relief='raise')
bottomLeft.pack(side=LEFT,fill=BOTH)

h=Label(bottomLeft,text="State Tax",width=8,bd=16,font=("times",32,"bold"),anchor=W)
h.grid(row=3,column=2,sticky=W)
ent3=Entry(bottomLeft,bd=8,font=("times",18,"bold"),textvariable=Tax)
ent3.grid(row=3,column=3,sticky=W)

i=Label(bottomLeft,text="Sub Total",bd=16,width=8,font=("times",32,"bold"),anchor=W)
i.grid(row=4,column=2,sticky=W)
ent4=Entry(bottomLeft,bd=8,font=("times",18,"bold"),textvariable=SubTotal)
ent4.grid(row=4,column=3,sticky=W)
j=Label(bottomLeft,text="Total Cost",bd=16,width=8,font=("times",32,"bold"),anchor=W)
j.grid(row=5,column=2,sticky=W)
ent5=Entry(bottomLeft,bd=8,font=("times",18,"bold"),textvariable=Fee_Price)
ent5.grid(row=5,column=3,sticky=W)

spc1=Label(bottomLeft,text="    \n    \n  ",width=6,font=("times",28,"bold"))
spc1.grid(row=6,column=2,sticky=W)
spc2=Label(bottomLeft,text="     \n    \n  ",width=6,font=("times",28,"bold"))
spc2.grid(row=6,columnspan=4)

bottomRight=Frame(f2a,width=350,height=300,bd=8,relief='raise')
bottomRight.pack(side=LEFT,fill=X)

txtDisplay=Entry(bottomRight,font=("times",20,"bold"),textvariable=text_input,bd=11,width=18,bg="powder blue",relief="sunken")
txtDisplay.grid(columnspan=4)
btn7=Button(bottomRight,padx=8,pady=16,bd=8,width=4,fg="black",font=("times",10,"bold"),text="7",command=lambda:Click(7))
btn7.grid(row=2,column=0)
btn8=Button(bottomRight,padx=8,pady=16,bd=8,width=4,fg="black",font=("times",10,"bold"),text="8",command=lambda:Click(8))
btn8.grid(row=2,column=1)
btn9=Button(bottomRight,padx=8,pady=16,width=4,bd=8,fg="black",font=("times",10,"bold"),text="9",command=lambda:Click(9))
btn9.grid(row=2,column=2)
btnadd=Button(bottomRight,padx=8,pady=16,width=4,bd=8,fg="black",font=("times",10,"bold"),text="+",command=lambda:Click("+"))
btnadd.grid(row=2,column=3)

btn4=Button(bottomRight,padx=8,pady=16,width=4,bd=8,fg="black",font=("times",10,"bold"),text="4",command=lambda:Click(4))
btn4.grid(row=3,column=0)
btn5=Button(bottomRight,padx=8,pady=16,width=4,bd=8,fg="black",font=("times",10,"bold"),text="5",command=lambda:Click(5))
btn5.grid(row=3,column=1)
btn6=Button(bottomRight,padx=8,pady=16,width=4,bd=8,fg="black",font=("times",10,"bold"),text="6",command=lambda:Click(6))
btn6.grid(row=3,column=2)
btnsub=Button(bottomRight,padx=8,pady=16,width=4,bd=8,fg="black",font=("times",10,"bold"),text="-",command=lambda:Click("+"))
btnsub.grid(row=3,column=3)

btn1=Button(bottomRight,padx=8,pady=16,width=4,bd=8,fg="black",font=("times",10,"bold"),text="1",command=lambda:Click(1))
btn1.grid(row=4,column=0)
btn2=Button(bottomRight,padx=8,pady=16,width=4,bd=8,fg="black",font=("times",10,"bold"),text="2",command=lambda:Click(2))
btn2.grid(row=4,column=1)
btn3=Button(bottomRight,padx=8,pady=16,width=4,bd=8,fg="black",font=("times",10,"bold"),text="3",command=lambda:Click(3))
btn3.grid(row=4,column=2)
btnmul=Button(bottomRight,padx=8,pady=16,width=4,bd=8,fg="black",font=("times",10,"bold"),text="*",command=lambda:Click("*"))
btnmul.grid(row=4,column=3)

btn0=Button(bottomRight,padx=8,pady=16,width=4,bd=8,fg="black",font=("times",10,"bold"),text="0",command=lambda:Click(0))
btn0.grid(row=5,column=0)
btnC=Button(bottomRight,padx=8,pady=16,width=4,bd=8,fg="black",font=("times",10,"bold"),text="C",command=Clear)
btnC.grid(row=5,column=1)
btneq=Button(bottomRight,padx=8,pady=16,width=4,bd=8,fg="black",font=("times",10,"bold"),text="=",command=equal)
btneq.grid(row=5,column=2)
btndiv=Button(bottomRight,padx=8,pady=16,width=4,bd=8,fg="black",font=("times",10,"bold"),text="/",command=lambda:Click("/"))
btndiv.grid(row=5,column=3)

f2a.pack(side=TOP,fill=Y)
f1.pack(side=LEFT,fill=Y)

#right side box
rf=Frame(root,width=530,height=600,bd=8,relief='raise')
topRight=Frame(rf,width=530,height=100,bd=8,relief='raise')
topRight.pack(side=TOP,fill=X)
g=Label(topRight,text="Travelling Ticketing \nSystem",font=("times",30,"bold"))
g.pack()
topRight1=Frame(rf,width=530,height=500,bd=8,relief='raise')
topRight1.pack(side=RIGHT)

f1=Frame(topRight1)

lb1=Label(f1,font=("times",14,"bold"),text="Class",bd=10,width=7,relief="sunken")
lb1.grid(row=0,column=1)
lb11=Label(f1,font=("times",14,"bold"),bd=10,width=7,relief="sunken",textvariable=TicketClass)
lb11.grid(row=1,column=1)
lb2=Label(f1,font=("times",14,"bold"),text="Ticket",bd=10,width=7,relief="sunken")
lb2.grid(row=0,column=2)
lb22=Label(f1,font=("times",14,"bold"),bd=10,width=7,relief="sunken",textvariable=SubTotal)
lb22.grid(row=1,column=2)
lb3=Label(f1,font=("times",14,"bold"),text="Adult",bd=10,width=7,relief="sunken")
lb3.grid(row=0,column=3)
lb33=Label(f1,font=("times",14,"bold"),bd=10,width=7,relief="sunken",textvariable=Adult_Ticket)
lb33.grid(row=1,column=3)
lb4=Label(f1,font=("times",14,"bold"),text="Child",bd=10,width=7,relief="sunken")
lb4.grid(row=0,column=4)
lb44=Label(f1,font=("times",14,"bold"),bd=10,width=7,relief="sunken",textvariable=Child_Ticket)
lb44.grid(row=1,column=4)

space1=Label(f1,font=("times",14,"bold"),width=34,relief="sunken")
space1.grid(row=2,column=1,columnspan=4)

lb5=Label(f1,font=("times",14,"bold"),text="Form",bd=10,width=7,relief="sunken")
lb5.grid(row=3,column=2)
lb55=Label(f1,font=("times",14,"bold"),bd=10,width=7,relief="sunken",textvariable=From_Destination)
lb55.grid(row=3,column=3)
lb6=Label(f1,font=("times",14,"bold"),text="To",bd=10,width=7,relief="sunken")
lb6.grid(row=4,column=2)
lb66=Label(f1,font=("times",14,"bold"),bd=10,width=7,relief="sunken",textvariable=To_Destination)
lb66.grid(row=4,column=3)
lb7=Label(f1,font=("times",14,"bold"),text="Price",bd=10,width=7,relief="sunken")
lb7.grid(row=5,column=2)
lb77=Label(f1,font=("times",14,"bold"),bd=10,width=7,relief="sunken",textvariable=Fee_Price)
lb77.grid(row=5,column=3)

space2=Label(f1,font=("times",14,"bold"),width=34,relief="sunken")
space2.grid(row=6,column=1,columnspan=4)

lb8=Label(f1,font=("times",14,"bold"),text="Ref No.",bd=10,width=7,relief="sunken")
lb8.grid(row=7,column=1)
lb88=Label(f1,font=("times",14,"bold"),bd=10,width=7,relief="sunken",textvariable=Receipt_Ref)
lb88.grid(row=8,column=1)
lb9=Label(f1,font=("times",14,"bold"),text="Time",bd=10,width=7,relief="sunken")
lb9.grid(row=7,column=2)
lb99=Label(f1,font=("times",14,"bold"),textvariable=time1,bd=10,width=7,relief="sunken")
lb99.grid(row=8,column=2)
lb10=Label(f1,font=("times",14,"bold"),text="Date",bd=10,width=7,relief="sunken")
lb10.grid(row=7,column=3)

lb100=Label(f1,font=("times",14,"bold"),textvariable=date1,bd=10,width=7,relief="sunken")
lb100.grid(row=8,column=3)
lb12=Label(f1,font=("times",14,"bold"),text="Route",bd=10,width=7,relief="sunken")
lb12.grid(row=7,column=4)
lb122=Label(f1,font=("times",14,"bold"),bd=10,width=7,relief="sunken",textvariable=Route)
lb122.grid(row=8,column=4)

space3=Label(f1,font=("times",14,"bold"),width=34,relief="sunken")
space3.grid(row=9,column=1,columnspan=4)

btnTotal=Button(f1,text="Total",padx=2,pady=2,width=7,bd=6,fg="black",font=("times",13,"bold"),command=Travel_Cost)
btnTotal.grid(row=10,column=1)
btnClear=Button(f1,text="Clear",padx=2,pady=2,width=7,bd=6,fg="black",font=("times",13,"bold"),command=reset)
btnClear.grid(row=10,column=2)
btnReset=Button(f1,text="Reset",padx=2,pady=2,width=7,bd=6,fg="black",font=("times",13,"bold"),command=reset)
btnReset.grid(row=10,column=3)
btnExit=Button(f1,text="Exit",padx=2,pady=2,width=7,bd=6,fg="black",font=("times",13,"bold"),command=Exitt)
btnExit.grid(row=10,column=4)

f1.pack(side=TOP)
rf.pack(side=RIGHT,fill=Y)
root.mainloop()