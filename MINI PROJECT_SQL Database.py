from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox as m
import pymysql
mydb=pymysql.Connect(host="localhost",user="root",password="mohan",database="signup_project")
mycursor=mydb.cursor()
def report():
        global rep
        rep=Toplevel(w)
        rep.geometry("1366x768")
        load=Image.open("6608059.jpg")
        photo=ImageTk.PhotoImage(load)
        label=Label(rep,image=photo)
        label.image=photo
        label.place(x=0,y=0)
        rep.title("REPORT")
        global sname
        global e
        global t
        global ma
        global sci
        global soc
        global cls
        teachername=e1.get()
        cls=int(e10.get())
        reg=int(e11.get())
        e=int(e15.get())
        t=int(e16.get())
        ma=int(e17.get())
        sci=int(e18.get())
        soc=int(e19.get())
        sname=e9.get()
        total=e+t+ma+sci+soc
        avg=total/5
        if e>=91 and e<=100:
                egrade="A+"
        elif e>=81 and e<91:
                egrade="A"
        elif e>=71 and e<81:
                egrade="B"
        elif e>=61 and e<71:
                egrade="C"
        elif e>=50 and e<61:
                egrade="D"
        elif e<50:
                egrade="F"
                
        if t>=91 and t<=100:
                tgrade="A+"
        elif t>=81 and t<91:
                tgrade="A"
        elif t>=71 and t<81:
                tgrade="B"
        elif t>=61 and t<71:
                tgrade="C"
        elif t>=50 and t<61:
                tgrade="D"
        elif t<50:
                tgrade="F"
                
        if ma>=91 and ma<=100:
                magrade="A+"
        elif ma>=81 and ma<91:
                magrade="A"
        elif ma>=71 and ma<81:
                magrade="B"
        elif ma>=61 and ma<71:
                magrade="C"
        elif ma>=50 and ma<61:
                magrade="D"
        elif ma<50:
                magrade="F"
                
        if sci>=91 and sci<=100:
                scigrade="A+"
        elif sci>=81 and sci<91:
                scigrade="A"
        elif sci>=71 and sci<81:
                scigrade="B"
        elif sci>=61 and sci<71:
                scigrade="C"
        elif sci>=50 and sci<61:
                scigrade="D"
        elif sci<50:
                scigrade="F"
                
        if soc>=91 and soc<=100:
               socgrade="A+"
        elif soc>=81 and soc<91:
                socgrade="A"
        elif soc>=71 and soc<81:
                socgrade="B"
        elif soc>=61 and soc<71:
                socgrade="C"
        elif soc>=50 and soc<61:
                socgrade="D"
        elif soc<50:
                socgrade="F"
                
        if egrade =='F':
                result='FAIL'
        else:
                result='PASS'
        if tgrade =='F':
                result1='FAIL'
        else:
                result1='PASS'
        if magrade =='F':
                result2='FAIL'
        else:
                result2='PASS'
        if scigrade =='F':
                result3='FAIL'
        else:
                result3='PASS'
        if socgrade =='F':
                result4='FAIL'
        else:
                result4='PASS'
                
        if result=='PASS' and result1=='PASS' and result2=='PASS' and result3=='PASS' and result4=='PASS':
                overallresult='PASS'
        else:
                overallresult='FAIL'

        frame=Frame(rep,width=1200,height=600,bg="white").place(x=50,y=40)
        f1=Frame(rep,width=1050,height=2,bg="black").place(x=60,y=220)
        f2=Frame(rep,width=1050,height=2,bg="black").place(x=60,y=260)
        f3=Frame(rep,width=1050,height=2,bg="black").place(x=60,y=305)
        f4=Frame(rep,width=1050,height=2,bg="black").place(x=60,y=345)
        f5=Frame(rep,width=1050,height=2,bg="black").place(x=60,y=385)
        f6=Frame(rep,width=1050,height=2,bg="black").place(x=60,y=425)
        f7=Frame(rep,width=1050,height=2,bg="black").place(x=60,y=470)
        f8=Frame(rep,width=2,height=250,bg="black").place(x=327,y=220)
        f9=Frame(rep,width=2,height=250,bg="black").place(x=560,y=220)
        f10=Frame(rep,width=2,height=250,bg="black").place(x=805,y=220)
        f11=Frame(rep,width=2,height=250,bg="black").place(x=958,y=220)
        f12=Frame(rep,width=2,height=250,bg="black").place(x=1110,y=220)
        f13=Frame(rep,width=2,height=250,bg="black").place(x=60,y=220)
        f14=Frame(rep,width=1000,height=2,bg="black").place(x=60,y=490)
        f15=Frame(rep,width=1000,height=2,bg="black").place(x=60,y=540)
        f16=Frame(rep,width=1000,height=2,bg="black").place(x=60,y=590)
        f17=Frame(rep,width=2,height=100,bg="black").place(x=60,y=490)
        f18=Frame(rep,width=2,height=100,bg="black").place(x=327,y=490)
        f19=Frame(rep,width=2,height=100,bg="black").place(x=560,y=490)
        f20=Frame(rep,width=2,height=100,bg="black").place(x=830,y=490)
        f21=Frame(rep,width=2,height=100,bg="black").place(x=1060,y=490)
        f22=Frame(rep,width=430,height=2,bg="black").place(x=63,y=55)
        f23=Frame(rep,width=430,height=2,bg="black").place(x=63,y=93)
        f24=Frame(rep,width=430,height=2,bg="black").place(x=63,y=133)
        f25=Frame(rep,width=430,height=2,bg="black").place(x=63,y=173)
        f26=Frame(rep,width=430,height=2,bg="black").place(x=63,y=214)
        f27=Frame(rep,width=2,height=160,bg="black").place(x=63,y=55)
        f28=Frame(rep,width=2,height=160,bg="black").place(x=320,y=55)
        f29=Frame(rep,width=2,height=160,bg="black").place(x=491,y=55)
        load=Image.open("sla1.png")
        photo=ImageTk.PhotoImage(load)
        label=Label(rep,image=photo)
        label.image=photo
        label.place(x=730,y=50)
        slaschool=Label(rep,text="SLA Matriculation School, KK Nagar, Chennai",bg="white",fg="black",font="arial 15 bold italic").place(x=650,y=140)
        
        l20=Label(rep,text="STUDENT DETAILS",bg="tomato",font="georgia 17 bold").place(x=550,y=7)
        l21=Label(rep,text="Student Name",width=17,bg="khaki",fg="black",font="arial 15 bold").place(x=80,y=60)
        l22=Label(rep,text=sname,width=10,bg="khaki",fg="black",font="arial 15 bold").place(x=350,y=60)
        l23=Label(rep,text="Class",width=17,bg="khaki",fg="black",font="arial 15 bold").place(x=80,y=100)
        l24=Label(rep,text=cls,width=10,bg="khaki",fg="black",font="arial 15 bold").place(x=350,y=100)
        rnum=Label(rep,text="Registration number",width=17,bg="khaki",fg="black",font="arial 15 bold").place(x=80,y=140)
        rnum1=Label(rep,text=reg,width=10,bg="khaki",fg="black",font="arial 15 bold").place(x=350,y=140)
        tname=Label(rep,text="Teacher name",width=17,bg="khaki",fg="black",font="arial 15 bold").place(x=80,y=180)
        tname1=Label(rep,text=teachername,width=10,bg="khaki",fg="black",font="arial 15 bold").place(x=350,y=180)
        stitle=Label(rep,text="SUBJECTS",bg="tomato",font="georgia 13 bold").place(x=125,y=230)
        ttitle=Label(rep,text="TOTAL MARKS",bg="tomato",font="georgia 13 bold").place(x=385,y=230)
        mtitle=Label(rep,text="OBTAINED MARKS",bg="tomato",font="georgia 13 bold").place(x=590,y=230)
        gtitle=Label(rep,text="GRADE",bg="tomato",font="georgia 13 bold").place(x=845,y=230)
        rtitle=Label(rep,text="RESULT",bg="tomato",font="georgia 13 bold").place(x=990,y=230)
        l29=Label(rep,text="ENGLISH",bg="khaki",width=15,fg="black",font="arial 15 bold").place(x=90,y=270)
        l31=Label(rep,text="TAMIL",bg="khaki",width=15,fg="black",font="arial 15 bold").place(x=90,y=310)
        l33=Label(rep,text="MATHS",bg="khaki",width=15,fg="black",font="arial 15 bold").place(x=90,y=350)
        l35=Label(rep,text="SCIENCE",bg="khaki",width=15,fg="black",font="arial 15 bold").place(x=90,y=390)
        l37=Label(rep,text="SOCIAL SCIENCE",width=15,bg="khaki",fg="black",font="arial 15 bold").place(x=90,y=430)
        
        l30=Label(rep,text=egrade,width=5,bg="khaki",fg="black",font="arial 15 bold").place(x=850,y=270)
        l32=Label(rep,text=tgrade,width=5,bg="khaki",fg="black",font="arial 15 bold").place(x=850,y=310)
        l34=Label(rep,text=magrade,width=5,bg="khaki",fg="black",font="arial 15 bold").place(x=850,y=350)
        l36=Label(rep,text=scigrade,width=5,bg="khaki",fg="black",font="arial 15 bold").place(x=850,y=390)
        l38=Label(rep,text=socgrade,width=5,bg="khaki",fg="black",font="arial 15 bold").place(x=850,y=430)
        
        ttotal=Label(rep,text="100",width=5,bg="khaki",fg="black",font="arial 15 bold").place(x=410,y=270)
        ttotal1=Label(rep,text="100",width=5,bg="khaki",fg="black",font="arial 15 bold").place(x=410,y=310)
        ttotal2=Label(rep,text="100",width=5,bg="khaki",fg="black",font="arial 15 bold").place(x=410,y=350)
        ttotal3=Label(rep,text="100",width=5,bg="khaki",fg="black",font="arial 15 bold").place(x=410,y=390)
        ttotal4=Label(rep,text="100",width=5,bg="khaki",fg="black",font="arial 15 bold").place(x=410,y=430)

        english=Label(rep,text=e,width=5,bg="khaki",fg="black",font="arial 15 bold").place(x=640,y=270)
        tamil=Label(rep,text=t,width=5,bg="khaki",fg="black",font="arial 15 bold").place(x=640,y=310)
        maths=Label(rep,text=ma,width=5,bg="khaki",fg="black",font="arial 15 bold").place(x=640,y=350)
        science=Label(rep,text=sci,width=5,bg="khaki",fg="black",font="arial 15 bold").place(x=640,y=390)
        social=Label(rep,text=soc,width=5,bg="khaki",fg="black",font="arial 15 bold").place(x=640,y=430)

        res=Label(rep,text=result,width=5,bg="khaki",fg="black",font="arial 15 bold").place(x=995,y=270)
        res1=Label(rep,text=result1,width=5,bg="khaki",fg="black",font="arial 15 bold").place(x=995,y=310)
        res2=Label(rep,text=result2,width=5,bg="khaki",fg="black",font="arial 15 bold").place(x=995,y=350)
        res3=Label(rep,text=result3,width=5,bg="khaki",fg="black",font="arial 15 bold").place(x=995,y=390)
        res4=Label(rep,text=result4,width=5,bg="khaki",fg="black",font="arial 15 bold").place(x=995,y=430)
        
        l25=Label(rep,text="Total",bg="palegreen",width=15,fg="black",font="arial 15 bold").place(x=90,y=500)
        overalltotal=Label(rep,text="500",width=11,bg="palegreen",fg="black",font="arial 15 bold").place(x=375,y=500)
        obtmarks=Label(rep,text="Obtained marks",bg="palegreen",width=15,fg="black",font="arial 15 bold").place(x=610,y=500)
        l26=Label(rep,text=total,bg="palegreen",width=11,fg="black",font="arial 15 bold").place(x=880,y=500)
        l27=Label(rep,text="Percentage",width=15,bg="palegreen",fg="black",font="arial 15 bold").place(x=90,y=550)
        l28=Label(rep,text=avg,bg="palegreen",width=11,fg="black",font="arial 15 bold").place(x=375,y=550)
        l39=Label(rep,text="Result",bg="palegreen",width=15,fg="black",font="arial 15 bold").place(x=610,y=550)
        l40=Label(rep,text=overallresult,bg="palegreen",width=11,fg="black",font="arial 15 bold").place(x=880,y=550)
        b7=Button(rep,text="Cancel",width=10,font="calibril 10 bold",bg="aquamarine",bd=7,command=rep.destroy).place(x=590,y=647)
        
class Final:
    def student():
        global stdnt
        stdnt=Toplevel(w)
        stdnt.geometry("1366x768")
        load=Image.open("2741721.jpg")
        photo=ImageTk.PhotoImage(load)
        label=Label(stdnt,image=photo)
        label.image=photo
        label.place(x=0,y=0)
        stdnt.title("Student details")
        global sn
        global e9
        global e15
        global e16
        global e17
        global e18
        global e19
        global e10
        global e11
        sn=StringVar()
        l8=Label(stdnt,text="STUDENT DETAILS",bg="tomato",font="georgia 17 bold").place(x=560,y=20)
        l9=Label(stdnt,text="1. Student Name",bg="black",fg="white",font="farisi 15 bold").place(x=450,y=80)
        e9=Entry(stdnt,textvariable=sn,width=40)
        e9.place(x=700,y=80)
        l10=Label(stdnt,text="2. Class",bg="black",fg="white",font="farisi 15 bold").place(x=450,y=120)
        e10=Entry(stdnt,width=40)
        e10.place(x=700,y=120)
        l11=Label(stdnt,text="3. Registration number",bg="black",fg="white",font="farisi 15 bold").place(x=450,y=160)
        e11=Entry(stdnt,width=40)
        e11.place(x=700,y=160)
        l12=Label(stdnt,text="4. Phone number",bg="black",fg="white",font="farisi 15 bold").place(x=450,y=200)
        e12=Entry(stdnt,width=40)
        e12.place(x=700,y=200)
        l13=Label(stdnt,text="5. Address",bg="black",fg="white",font="farisi 15 bold").place(x=450,y=240)
        e13=Entry(stdnt,width=40)
        e13.place(x=700,y=240)
        l14=Label(stdnt,text="STUDENT MARKS",bg="tomato",font="georgia 17 bold").place(x=560,y=270)
        l15=Label(stdnt,text="ENGLISH",bg="black",fg="white",font="farisi 15 bold").place(x=450,y=330)
        e15=Entry(stdnt,width=40)
        e15.place(x=700,y=330)
        l16=Label(stdnt,text="TAMIL",bg="black",fg="white",font="farisi 15 bold").place(x=450,y=370)
        e16=Entry(stdnt,width=40)
        e16.place(x=700,y=370)
        l17=Label(stdnt,text="MATHS",bg="black",fg="white",font="farisi 15 bold").place(x=450,y=420)
        e17=Entry(stdnt,width=40)
        e17.place(x=700,y=420)
        l18=Label(stdnt,text="SCIENCE",bg="black",fg="white",font="farisi 15 bold").place(x=450,y=470)
        e18=Entry(stdnt,width=40)
        e18.place(x=700,y=470)
        l19=Label(stdnt,text="SOCIAL SCIENCE",bg="black",fg="white",font="farisi 15 bold").place(x=450,y=520)
        e19=Entry(stdnt,width=40)
        e19.place(x=700,y=520)
        b5=Button(stdnt,text="Cancel",width=10,font="calibril 10 bold",bg="aquamarine",bd=7,command=stdnt.destroy).place(x=500,y=590)
        b6=Button(stdnt,text="Report",width=10,font="calibril 10 bold",bg="aquamarine",bd=7,command=report).place(x=700,y=590)

def logverify():
    global e
    global f
    e=e6.get()
    f=e7.get()
    query="select * from user_details"
    mycursor.execute(query)
    for i in mycursor:
            if i[1]==e and i[3]==f:
                    print("if executing..")
                    print(i[1],i[3])
                    Final.student()
            elif i[1]!=e and i[3]!=f:
                    m.showerror("warning","incorrect username/password")
                    print("else is executing..")
                    print(i[1],i[3])
                    
def login():
    global log
    log=Toplevel(w)
    log.geometry("1366x768")
    load=Image.open("2741721.jpg")
    photo=ImageTk.PhotoImage(load)
    label=Label(log,image=photo)
    label.image=photo
    label.place(x=0,y=0)
    global a
    global b
    global c
    global d
    global luid
    global lup
    global e6
    global e7
    a=e1.get()
    b=e2.get()
    c=e4.get()
    d=e5.get()
    query="insert into user_details values(%s,%s,%s,%s)"
    values=[a,b,c,d]
    mycursor.execute(query,values)
    mydb.commit()
    luid=StringVar()
    lup=StringVar()
    lo=Label(log,text="LOGIN",bg="tomato",font="georgia 30 bold").place(x=600,y=100)
    l6=Label(log,text="Staff ID",bg="black",fg="white",font="farisi 15 bold").place(x=500,y=200)
    e6=Entry(log,textvariable=luid,width=30)
    e6.place(x=700,y=200)
    l7=Label(log,text="Password",bg="black",fg="white",font="farisi 15 bold").place(x=500,y=250)
    e7=Entry(log,textvariable=lup,show="*",width=30)
    e7.place(x=700,y=250)
    b3=Button(log,text="cancel",width=10,font="calibril 10 bold",bg="aquamarine",bd=7,command=log.destroy).place(x=530,y=400)
    b4=Button(log,text="Login",width=10,font="calibril 10 bold",bg="aquamarine",bd=7,command=logverify).place(x=740,y=400)
global w
global e1
global e2
global e4
global e5
w=Tk()
w.geometry("1366x768")
load=Image.open("2741721.jpg")
photo=ImageTk.PhotoImage(load)
label=Label(w,image=photo)
label.image=photo
label.place(x=0,y=0)
w.title("Signup")
name=StringVar()
staffid=StringVar()
mailid=StringVar()
password=StringVar()
l=Label(w,text="SIGN UP",bg="tomato",font="georgia 30 bold").place(x=600,y=20)
l1=Label(w,text="Name",bg="black",fg="white",font="farisi 15 bold").place(x=500,y=100)
e1=Entry(w,textvariable=name,width=30)
e1.place(x=750,y=100)
l2=Label(w,text="staff_id",bg="black",fg="white",font="farisi 15 bold").place(x=500,y=140)
e2=Entry(w,textvariable=staffid,width=30)
e2.place(x=750,y=140)
l3=Label(w,text="Mobile number",bg="black",fg="white",font="farisi 15 bold").place(x=500,y=180)
e3=Entry(w,width=30).place(x=750,y=180)
l4=Label(w,text="Email_id",bg="black",fg="white",font="farisi 15 bold").place(x=500,y=220)
e4=Entry(w,textvariable=mailid,width=30)
e4.place(x=750,y=220)
l5=Label(w,text="Password",bg="black",fg="white",font="farisi 15 bold").place(x=500,y=260)
e5=Entry(w,textvariable=password,show="*",width=30)
e5.place(x=750,y=260)
b2=Button(w,text="Signup",width=10,font="calibril 10 bold",bg="aquamarine",bd=7,command=login).place(x=750,y=400)
b1=Button(w,text="cancel",width=10,font="calibril 10 bold",bg="aquamarine",bd=7,command=w.destroy).place(x=530,y=400)
w.mainloop()
