from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.geometry("1280x700")
root.title("Book Your Bus")
root.configure(background='black')

#Top frame
Top =Frame(root,width=1280,height=100,bd=8,relief='raise')
a=Label(Top,text="Book Your Bus ",font=("times",36,"bold"))
a.pack()
Top.pack(side=TOP,fill=X)

#Left Bottom frame
Left_Frame=Frame(root,height=600,width=450,bd=8,relief='raise')
Left_Frame.pack(side=LEFT,fill=Y)
Left_Frame3=Frame(Left_Frame,height=300,width=450,bd=8)
Left_Frame3.pack(side=TOP,fill=X)
Left_Frame1=Frame(Left_Frame,height=300,width=450,bd=8)
Left_Frame1.pack(side=TOP,fill=X)
Left_Frame2=Frame(Left_Frame,height=300,width=450,bd=8)
Left_Frame2.pack(side=TOP,fill=X)


b=Label(Left_Frame3,text="Search Your Bus",width=14,font=("time",30,"bold"),justify="center")
b.pack()

c=Label(Left_Frame1,text="From:",width=12,font=("time",30,"bold"))
c.grid(row=0,column=0,sticky=W)
combo1=ttk.Combobox(Left_Frame1,width=30,state='readonly')
combo1['value']=['','Katra','Mumbai','Bathinda','Delhi','Ludhiana','Jalhandar','Amritsar','J&K']
combo1.grid(row=0,column=1,sticky=W)

d=Label(Left_Frame1,text="To:",width=12,font=("time",30,"bold"))
d.grid(row=1,column=0,sticky=W)
combo2=ttk.Combobox(Left_Frame1,width=30,state='readonly')
combo2['value']=['','Katra','Mumbai','Bathinda','Delhi','Ludhiana','Jalhandar','Amritsar','J&K']
combo2.grid(row=1,column=1,sticky=W)

e=Label(Left_Frame2,text="Date:",width=12,font=("time",30,"bold"))
e.grid(row=0,column=0,sticky=W)
combo3=ttk.Combobox(Left_Frame2,width=8,state='readonly')
combo3['value']=['','1','2','3','4','5','6','7','8','9','10','11','12','13','14',
                '15','16','17','18','19','20','21','22','23','24','25','26','27',
                '28','29','30','31']
combo3.grid(row=0,column=1,sticky=W)

combo4=ttk.Combobox(Left_Frame2,width=8,state='readonly')
combo4['value']=['','1','2','3','4','5','6','7','8','9','10','11','12']
combo4.grid(row=0,column=2,sticky=W)

combo5=ttk.Combobox(Left_Frame2,width=8,state='readonly')
combo5['value']=['','2018','2019','2020','2021','2022','2023','2025']
combo5.grid(row=0,column=3,sticky=W)

btnSearch=Button(Left_Frame2,text="Search",width=7,bd=6,fg="black",
                 font=("times",15,"bold"))
btnSearch.grid(row=1,column=3)


#Right Bottom frame
Right_Frame=Frame(root,height=600,width=780,bd=8,relief='raise')
Right_Frame.pack(side=LEFT,fill=Y)
Right_Frame1=Frame(Right_Frame)
Right_Frame1.pack(side=TOP,fill=Y)
Right_Frame2=Frame(Right_Frame)
Right_Frame2.pack(side=TOP,fill=Y)

aa=Label(Right_Frame1,text="Bus Avaliability",width=44,font=("time",28,"bold"))
aa.pack()

lb1a=Label(Right_Frame2,font=("times",14,"bold"),text="Bus Name",bd=10,width=11,relief="raise")
lb1a.grid(row=0,column=0)

lb2a=Label(Right_Frame2,font=("times",14,"bold"),text="Type",bd=10,width=11,relief="raise")
lb2a.grid(row=0,column=1)

lb3a=Label(Right_Frame2,font=("times",14,"bold"),text="Depart",bd=10,width=11,relief="raise")
lb3a.grid(row=0,column=2)

lb4a=Label(Right_Frame2,font=("times",14,"bold"),text="Arive",bd=10,width=11,relief="raise")
lb4a.grid(row=0,column=3)

lb5a=Label(Right_Frame2,font=("times",14,"bold"),text="Available",bd=10,width=11,relief="raise")
lb5a.grid(row=0,column=4)

lbA=Label(Right_Frame2,font=("times",14,"bold"),bd=10,width=64,height=5,relief="sunken")
lbA.grid(row=1,column=0,columnspan=5)
lbB=Label(Right_Frame2,font=("times",14,"bold"),bd=10,width=64,height=5,relief="sunken")
lbB.grid(row=2,column=0,columnspan=5)
lbC=Label(Right_Frame2,font=("times",14,"bold"),bd=10,width=64,height=5,relief="sunken")
lbC.grid(row=3,column=0,columnspan=5)

root.mainloop()