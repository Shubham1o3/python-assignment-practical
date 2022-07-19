from tkinter import *
from datetime import datetime
screen =Tk()
screen.geometry("500x500")

var_e1 = StringVar()
var_e2 = StringVar()
var_e3 = StringVar()
var_e4 = StringVar()
var_r1=StringVar()
var_r2=StringVar()
var_r3=StringVar()
var_r4=StringVar()
var_r5=StringVar()

current_dattime=datetime.now()
print("current date is : ",current_dattime)


current_date=str(current_dattime)

with open("data.txt","a") as f:
    f.write("todaydate : "+current_date)
def mufun():
    fullname = var_e1.get()
    age = var_e2.get()
    gender = var_e3.get()
    vaccination_dose = var_e4.get()
    var_r1.set(fullname)
    var_r2.set(age)
    var_r3.set(gender)
    var_r4.set(vaccination_dose)

    f=open("vaccinationdata.txt","a")
    
    f.write("\nfullname: "+var_r1.get())
    f.write("\nage : "+var_r2.get())
    f.write("\ngender : "+var_r3.get())
    f.write("\nvaccination_dose"+var_r4.get())
    f.write("\n-------->>>>><<<<<-------")

lbl=Label(screen,text="Enter full name :")
lbl.place(x=10,y=10)

lbl=Label(screen,text=" Age :")
lbl.place(x=10,y=50)

lbl=Label(screen,text=" gender :")
lbl.place(x=10,y=100)

lbl=Label(screen,text=" Vaccination dose : ")
lbl.place(x=10,y=150)



e1 = Entry(screen,width=20,textvariable=var_e1)
e1.place(x=120,y=10)

e2 = Entry(screen,width=20,textvariable=var_e2)
e2.place(x=120,y=50)

e3 =Entry(screen,width=20,textvariable=var_e3)
e3.place(x=120,y=100)

e4 = Entry(screen,width=20,textvariable=var_e4)
e4.place(x=120,y=150)

btn = Button(screen,text="submit",command=mufun)
btn.place(x=120,y=200)

lbl_result =Label(screen,text="Result Here",textvariable=var_r1)
lbl_result.place(x=170,y=250)

lbl_result =Label(screen,text="Result Here",textvariable=var_r2)
lbl_result.place(x=170,y=300)

lbl_result =Label(screen,text="Result Here",textvariable=var_r3)
lbl_result.place(x=170,y=350)

lbl_result =Label(screen,text="Result Here",textvariable=var_r4)
lbl_result.place(x=170,y=400)

screen.mainloop()