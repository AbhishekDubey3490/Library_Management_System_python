import mysql.connector as data
import os
try:
    db=data.connect(host="localhost",user="root",passwd="1234",database="library")
except:
    z=input("Enter Your Mysql Password:")
    db=data.connect(host="localhost",user="root",passwd=z)
    cursor=db.cursor()
    a="create database library"
    cursor.execute(a)
    cursor.execute("use library")
    b='''create table student(Adm_No int(4) primary key not null,
    Name char(20) not null,
    Class int(2) not null,
    Section char(15) not null,
    Mobile_No bigint(13) not null)
    '''
    cursor.execute(b)
    c='''create table book(B_id int(4) primary key not null,
    B_Name char(30) not null,
    Author char(30) not null,
    Printed int(4) not null,
    Price int not null)'''
    cursor.execute(c)
    d='''create table record(Adm_No int(4) primary key not null,
    Name char(20) not null,
    B_id int(4) not null,
    B_Name char(30) not null,
    Is_Date date not null,
    Rt_Date date not null)'''
    cursor.execute(d)
    cursor.execute("insert into student values(1000,'Abhishek Dubey',12,'Maths',9874563214)")
    cursor.execute("insert into book values(100,'Discovery of India','Pt Jawahar Lal Nehru',1946,439)")
    cursor.execute("insert into record values(1000,'Abhishek Dubey',100,'Discovery of India','2020-12-01','2020-12-10')")
# STUDENT=================================================================:
def student():
    def insert():
        cursor=db.cursor()
        cursor.execute("select max(Adm_No) from Student")
        a=cursor.fetchone()
        b=a[0]+1
        os.system("cls")
        print("\n",37*" ",77*"-","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",53*" ","* * * ! ! ! TO ENTER DATA OF NEW STUDENT ! ! ! * * *","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",37*" ",77*"-","\n")
        print("\n""ID For This Data is: ",b)
        c=input("\n""Enter Name of Student:")
        d=input("\n""Enter Class of Student:")
        e=input("\n""Enter Section of Student:")
        f=input("\n""Enter Mobile No. of Student:")
        if f.isdigit() and len(f)==10:
            h=int(f)
        else:
            print("\n",44*" ","* * ! ! Invalid Mobile Number ! ! * *")
        try:
            i="insert into student values({},'{}',{},'{}',{})".format(b,c,d,e,h)
            cursor.execute(i)
            db.commit()
            print("\n",44*" ","* * ! ! Data added successfully ! ! * *")
            print("\n",49*" ","* * ! ! Thank You ! ! * *")
            input("\n""**Press Enter To Continue.....")
        except:
            print("\n",44*" ","* * ! ! Sorry Data Not Added ! ! * *")
            input("\n""**Press Enter To Continue.....")
    def edit():
        import os
        os.system("cls")
        print("\n",37*" ",77*"-","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",55*" ","* * * ! ! ! TO EDIT DATA OF STUDENT ! ! ! * * *","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",37*" ",77*"-")
        a=""
        cursor=db.cursor()
        while a!="5":
            print("\n",55*" ","*Press 1--- To Edit Name of Student: ")
            print("\n",55*" ","*Press 2--- To Edit Class of Student: ")
            print("\n",55*" ","*Press 3--- To Edit Section of Student: ")
            print("\n",55*" ","*Press 4--- To Edit Mobile No of Student: ")
            print("\n",55*" ","*Press 5--- To Go Back")
            a=input("\n""Please Enter Your Choice: ")
            if a in ["1","2","3","4"]:
                try:
                    c=input("\n""Enter The Adm. No. Of Student: ")
                    q="select*from student where Adm_No=%s"%(c)
                    cursor.execute(q)
                    f=cursor.fetchone()
                    data=cursor.rowcount
                    if a=="1":
                        d=input("\n""Enter New Name of student: ")
                        b="update student set Name='{}' where Adm_No={}".format(d,c)
                        cursor.execute(b)
                        db.commit()
                    elif a=="2":
                        d=input("\n""Enter New Class of Student: ")
                        b="update student set Class={} where Adm_No={}".format(d,c)
                        cursor.execute(b)
                        db.commit()
                    elif a=="3":
                        d=input("\n""Enter New Section of Student: ")
                        b="update student set Section='{}' where Adm_No={}".format(d,c)
                        cursor.execute(b)
                        db.commit()
                    elif a=="4":
                        a=input("\n""Enter New Mobile No of student: ")
                        if a.isdigit() and len(a)<13 and len(a)>9:
                            d=int(a)
                            b="update student set Mobile_No={} where Adm_No={}".format(d,c)
                            cursor.execute(b)
                            db.commit()
                        else:
                            print("\n",44*" ","* * ! ! Invalid Mobile Number ! ! * *")
                    if data !=0:
                        print("\n",44*" ","! ! * * Data Edited Successfully * * ! !")
                        input("\n""**Press Enter To Continue......")
                        os.system("cls")
                except:
                    print("\n",44*" ","! ! * * Sorry! Data Not Found * * ! !")
                    print("\n",49*" ","! ! * * Please try again * *! !")
                    input("\n""**Press Enter To Continue.....")
                    os.system("cls")
            elif a=="5":
                print(44*" ","! ! * * Thank You * * ! !")
                input("\n""**Press Enter To Continue....")
                break
            elif a=="":
                print("\n",44*" ","! ! * * Sorry! You Entered No Choice * * ! !")
                print("\n",49*" ","! ! * * Please Try Again * * ! !")
                input("\n""**Press Enter To Continue....")
                os.system("cls")
            else:
                print("\n",44*" ","! ! * * Sorry! You Entered Wrong Choice * * ! !")
                print("\n",49*" ","! ! * * Please Try Again * * ! !")
                input("\n""**Press Enter To Continue....")
    def search():
        import os
        os.system("cls")
        print("\n",37*" ",77*"-","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",54*" ","* * * ! ! ! TO SEARCH DATA OF STUDENT ! ! ! * * *","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",37*" ",77*"-","\n")
        f=input("\n""Please Enter Adm_No of Student: ")
        try:
            cursor=db.cursor()
            q="select*from student where Adm_No=%s"%(f)
            cursor.execute(q)
            c=cursor.fetchone()
            print("\n""Adm_No >>",c[0])
            print("\n""Name >>",c[1])
            print("\n""Class >>",c[2])
            print("\n""Section >>",c[3])
            print("\n""Mobile No >>",c[4])
            print("\n",44*" ","* * ! ! Thank You ! ! * *")
            input("\n""**Press Enter For Main Menu.....")
        except:
            print("\n",44*" ","* * ! ! Sorry! Data Not Found ! ! * *")
            print("\n",49*" ","* * ! ! Please Try Again ! ! * *")
            input("\n""**Press Enter To Continue.....")
    def remove():
        import os
        os.system("cls")
        print("\n",37*" ",77*"-","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",54*" ","* * * ! ! ! TO REMOVE DATA OF STUDENT ! ! ! * * *","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",37*" ",77*"-","\n")
        a=input("\n""Enter the Adm_No of Student: ")
        cursor=db.cursor()
        try:
            b="delete from student where Adm_No=%s"%(a)
            cursor.execute(b)
            db.commit()
            print("\n",44*" ","! ! * * Data Deletd Successfully * * ! !")
            input("\n""**Press Enter To Continue.....")
        except:
            print("\n",44*" ","! ! * * Sorry! Data Not Found * * ! !")
            input("\n""**Press Enter To Continue.....")
    def display():
        os.system("cls")
        print("\n",37*" ",77*"-","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",52*" ","* * * ! ! ! TO GET THE LIST OF ALL STUDENT ! ! ! * * *","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",37*" ",77*"-","\n")
        cursor=db.cursor()
        cursor.execute("select *from student")
        a=cursor.fetchall()
        d=0
        for b in a:
            d=d+1
            print("\n""Record >>",d)
            print("\n""Adm_No >>",b[0])
            print("Name >>",b[1])
            print("Class >>",b[2])
            print("Section >>",b[3])
            print("Mobile No. >>",b[4])
        print("\n",44*" ","* * ! ! Thank You ! ! * *")
        input("\n""**Press Enter To Continue.....")
# MAIN MENU FOR STUDENT================================================================================================:
    z=""
    while z!="6":
        import os
        os.system("cls")
        print("\n",37*" ",77*"-","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",33*" ","* * * ! ! ! ALL THE INFORMATIONS RELATED WITH STUDENTS ARE AVAILABLE HERE ! ! ! * * *","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",37*" ",77*"-","\n")
        print("\n",46*" ","*Press 1--- To Enter data of New Student")
        print("\n",46*" ","*Press 2--- To Edit data of Student")
        print("\n",46*" ","*Press 3--- To Remove data of Student")
        print("\n",46*" ","*Press 4--- To Search Data of Student")
        print("\n",46*" ","*Press 5--- To Get List of All Students")
        print("\n",46*" ","*Press 6--- To Go Back")
        z=input("\n""Please Enter Your Choice: ")
        if z=="1":
            insert()
        elif z=="2":
            edit()
        elif z=="3":
            remove()
        elif z=="4":
            search()
        elif z=="5":
            display()
        elif z=="6":
            print(46*" ","* * ! ! Thank You ! ! * *")
            break
        elif z=="":
            print("\n",44*" ","! ! * * Sorry! You Entered No Number * * ! !")
            print("\n",49*" ","! ! * * Please Try Again * * ! !")
            input("\n""**Press Enter To Continue....")
            os.system("cls")
            continue
        else:
            print(46*" ","! ! * *Entered Number Is Incorrect* * ! !""\n")
            print(49*" ","! ! * * Please Try Again * * ! !""\n")
            input("\n""**Press Enter To Continue.....")
            os.system("cls")
            continue
#======================================STUDENT COMPLETE===================================================
#LIBRARY
def library():
    def insert():
        cursor=db.cursor()
        cursor.execute("select max(B_id) from book")
        a=cursor.fetchone()
        b=a[0]+1
        os.system("cls")
        print("\n",37*" ",77*"-","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",53*" ","* * * ! ! ! TO ENTER DATA OF NEW BOOK ! ! ! * * *","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",37*" ",77*"-","\n")
        print("\n""ID For This Book is: ",b)
        c=input("\n""Enter Name of Book:")
        d=input("\n""Enter Author of Book:")
        e=input("\n""Enter Year of Print:")
        h=input("\n""Enter Price of Book:")
        i="insert into book values({},'{}','{}','{}',{})".format(b,c,d,e,h)
        cursor.execute(i)
        db.commit()
        print("\n",44*" ","* * ! ! Data added successfully ! ! * *")
        print("\n",49*" ","* * ! ! Thank You ! ! * *")
        input("\n""**Press Enter To Continue.....")
    def edit():
        import os
        os.system("cls")
        print("\n",37*" ",77*"-","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",55*" ","* * * ! ! ! TO EDIT DATA OF BOOK ! ! ! * * *","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",37*" ",77*"-")
        a=""
        cursor=db.cursor()
        while a!="5":
            print("\n",55*" ","*Press 1--- To Edit Name of Book: ")
            print("\n",55*" ","*Press 2--- To Edit Author of Book: ")
            print("\n",55*" ","*Press 3--- To Edit Year of Print: ")
            print("\n",55*" ","*Press 4--- To Edit Price of Book: ")
            print("\n",55*" ","*Press 5--- To Go Back")
            a=input("\n""Please Enter Your Choice: ")
            if a in ["1","2","3","4"]:
                try:
                    c=input("Enter The ID of Book: ")
                    q="select*from book where B_id=%s"%(c)
                    cursor.execute(q)
                    f=cursor.fetchone()
                    data=cursor.rowcount
                    if a=="1":
                        d=input("\n""Enter New Name of Book: ")
                        b="update book set B_Name='{}' where B_id={}".format(d,c)
                        cursor.execute(b)
                        db.commit()
                    elif a=="2":
                        d=input("\n""Enter New Author Of Book ")
                        b="update book set Author='{}' where B_id={}".format(d,c)
                        cursor.execute(b)
                        db.commit()
                    elif a=="3":
                        d=input("\n""Enter New Year of Print: ")
                        b="update book set Printed='{}' where B_id={}".format(d,c)
                        cursor.execute(b)
                        db.commit()
                    elif a=="4":
                        d=input("\n""Enter New Price: ")
                        b="update book set Price='{}' where B_id={}".format(d,c)
                        cursor.execute(b)
                        db.commit()
                    if data !=0:
                        print("\n",44*" ","! ! * * Data Edited Successfully * * ! !")
                        input("\n""**Press Enter To Continue......")
                        os.system("cls")
                except:
                    print("\n",44*" ","! ! * * Sorry! Data Not Found * * ! !")
                    print("\n",49*" ","! ! * * Please try again * *! !")
                    input("\n""**Press Enter To Continue.....")
                    os.system("cls")
            elif a=="5":
                print(44*" ","! ! * * Thank You * * ! !")
                input("\n""**Press Enter To Continue....")
                break
            elif a=="":
                print("\n",44*" ","! ! * * Sorry! You Entered No Choice * * ! !")
                print("\n",49*" ","! ! * * Please Try Again * * ! !")
                input("\n""**Press Enter To Continue....")
                os.system("cls")
            else:
                print("\n",44*" ","! ! * * Sorry! You Entered Wrong Choice * * ! !")
                print("\n",49*" ","! ! * * Please Try Again * * ! !")
                input("\n""**Press Enter To Continue....")
    def search():
        import os
        os.system("cls")
        print("\n",37*" ",77*"-","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",54*" ","* * * ! ! ! TO SEARCH DATA OF BOOK ! ! ! * * *","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",37*" ",77*"-","\n")
        f=input("\n""Please Enter ID of Book: ")
        try:
            cursor=db.cursor()
            q="select*from book where B_id=%s"%(f)
            cursor.execute(q)
            c=cursor.fetchone()
            print("\n""Book Id >>",c[0])
            print("\n""Name of Book >>",c[1])
            print("\n""Author of Book >>",c[2])
            print("\n""Year of Print>>",c[3])
            print("\n""Price of book>>",c[4])
            print("\n",44*" ","* * ! ! Thank You ! ! * *")
            input("\n""**Press Enter For Main Menu.....")
        except:
            print("\n",44*" ","* * ! ! Sorry! Data Not Found ! ! * *")
            print("\n",49*" ","* * ! ! Please Try Again ! ! * *")
            input("\n""**Press Enter To Continue.....")
    def remove():
        import os
        os.system("cls")
        print("\n",37*" ",77*"-","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",54*" ","* * * ! ! ! TO REMOVE DATA OF BOOK ! ! ! * * *","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",37*" ",77*"-","\n")
        a=input("\n""Enter the ID of Book: ")
        cursor=db.cursor()
        try:
            b="delete from book where B_id=%s"%(a)
            cursor.execute(b)
            db.commit()
            print("\n",44*" ","! ! * * Data Deletd Successfully * * ! !")
            input("\n""**Press Enter To Continue.....")
        except:
            print("\n",44*" ","! ! * * Sorry! Data Not Found * * ! !")
            input("\n""**Press Enter To Continue.....")
    def display():
        os.system("cls")
        print("\n",37*" ",77*"-","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",52*" ","* * * ! ! ! TO GET THE LIST OF ALL BOOKS ! ! ! * * *","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",37*" ",77*"-","\n")
        cursor=db.cursor()
        cursor.execute("select *from book")
        a=cursor.fetchall()
        d=0
        for b in a:
            d=d+1
            print("\n""Record >>",d)
            print("\n""Book_ID >>",b[0])
            print("Name of Book >>",b[1])
            print("Name Of Author >>",b[2])
            print("Year Of Print >>",b[3])
            print("Cost Of Book >>",b[4])
        print("\n",44*" ","* * ! ! Thank You ! ! * *")
        input("\n""**Press Enter To Continue.....")        
#MAIN MENU FOR  BOOK=================================================================================:
    z=""
    while z!="6":
        import os
        os.system("cls")
        print("\n",37*" ",77*"-","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",33*" ","* * * ! ! ! ALL THE INFORMATIONS RELATED WITH BOOKS ARE AVAILABLE HERE ! ! ! * * *","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",37*" ",77*"-","\n")
        print("\n",46*" ","*Press 1--- To Enter data of New Book")
        print("\n",46*" ","*Press 2--- To Edit data of Book")
        print("\n",46*" ","*Press 3--- To Remove data of Book")
        print("\n",46*" ","*Press 4--- To Search Data of Book")
        print("\n",46*" ","*Press 5--- To Display List of Book")
        print("\n",46*" ","*Press 6--- To Go Back")
        z=input("\n""Please Enter Your Choice: ")
        if z=="1":
            insert()
        elif z=="2":
            edit()
        elif z=="3":
            remove()
        elif z=="4":
            search()
        elif z=="5":
            display()
        elif z=="6":
            print(46*" ","* * ! ! Thank You ! ! * *")
            break
        elif z=="":
            print("\n",44*" ","! ! * * Sorry! You Entered No Number * * ! !")
            print("\n",49*" ","! ! * * Please Try Again * * ! !")
            input("\n""**Press Enter To Continue....")
            os.system("cls")
            continue
        else:
            print(46*" ","! ! * *Entered Number Is Incorrect* * ! !""\n")
            print(49*" ","! ! * * Please Try Again * * ! !""\n")
            input("\n""**Press Enter To Continue.....")
            os.system("cls")
            continue
#================================================LIBRARY COMPLETE ================================
#RECORD
def record():
    def insert():
        from datetime import date
        today=date.today()
        os.system("cls")
        cursor=db.cursor()
        print("\n",37*" ",77*"-","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",53*" ","* * * ! ! ! TO ENTER NEW RECORD ! ! ! * * *","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",37*" ",77*"-","\n")
        a=input("\n""Please Enter Adm_No of Student: ")
        b=input("\n""Enter Name of Student:")
        c=input("\n""Enter the ID of Book: ")
        d=input("\n""Enter Name of Book:")
        e=str(today)
        t=int(e[-2:])+7
        f=e[:-2]+str(t)
        cursor.execute("select B_id,Adm_No from book,student")
        q=cursor.fetchall()
        try:
            if a.isdigit() and c.isdigit():
                x=int(a)
                z=int(c)
                if (z,x) in q:
                    h="insert into record values('{}','{}','{}','{}','{}','{}')".format(a,b,c,d,today,f)
                    cursor.execute(h)
                    db.commit()
                    print("\n",45*" ","* * ! ! Book Issued For 7 Days ! ! * *")
                    print("\n",41*" ","* * ! ! Returning Date Is",f,"! ! * *")
                    print("\n",44*" ","* * ! ! Data added successfully ! ! * *")
                    print("\n",49*" ","* * ! ! Thank You ! ! * *")
                    input("\n""**Press Enter To Continue.....")
                else:
                    print("\n",44*" ","* * ! ! Data Not Entered Correctly ! ! * *")
                    print("\n",30*" ","* * ! ! Either Book Not Available Or Entered Id Is Not Member ! ! * *")
                    input("\n""**Press Enter To Continue.....")
            else:
                print("\n",44*" ","* * ! ! Check Adm No and Book ID Then Enter Record Again ! ! * *")
                print("\n",49*" ","* * ! ! Thank You ! ! * *")
                input("\n""**Press Enter To Continue.....")
        except:
            print("\n",44*" ","* * ! ! Data Not Entered Correctly ! ! * *")
            print("\n",49*" ","* * ! ! Thank You ! ! * *")
            input("\n""**Press Enter To Continue.....")
    def edit():
        import os
        os.system("cls")
        print("\n",37*" ",77*"-","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",55*" ","* * * ! ! ! TO EDIT RECORD ! ! ! * * *","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",37*" ",77*"-")
        a=""
        cursor=db.cursor()
        while a!="7":
            print("\n",55*" ","*Press 1--- To Edit ID of Student: ")
            print("\n",55*" ","*Press 2--- To Edit Name of Student: ")
            print("\n",55*" ","*Press 3--- To Edit ID of Book: ")
            print("\n",55*" ","*Press 4--- To Edit Name of Book: ")
            print("\n",55*" ","*Press 5--- To Edit Issuing Date: ")
            print("\n",55*" ","*Press 6--- To Edit Return Date: ")
            print("\n",55*" ","*Press 7--- To Go Back")
            a=input("\n""Please Enter Your Choice: ")
            if a in ["1","2","3","4","5","6"]:
                try:
                    c=input("\n""Please Enter Adm_No of Student: ")
                    q="select*from record where Adm_No=%s"%(c)
                    cursor.execute(q)
                    f=cursor.fetchone()
                    data=cursor.rowcount
                    if a=="1":
                        d=input("\n""Enter New ID of Student: ")
                        b="update record set Adm_No={} where Adm_No={}".format(d,c)
                        cursor.execute(b)
                        db.commit()
                    elif a=="2":
                        d=input("\n""Enter New Name OF Student: ")
                        b="update record set Name='{}' where Adm_No={}".format(d,c)
                        cursor.execute(b)
                        db.commit()
                    elif a=="3":
                        d=input("\n""Enter New ID of Book: ")
                        b="update record set B_id='{}' where Adm_No={}".format(d,c)
                        cursor.execute(b)
                        db.commit()
                    elif a=="4":
                        d=input("\n""Enter New Name of Book: ")
                        b="update record set B_Name='{}' where Adm_No={}".format(d,c)
                        cursor.execute(b)
                        db.commit()
                    elif a=="5":
                        d=input("\n""Enter New Issuing Date: ")
                        b="update record set Is_Date='{}' where Adm_No={}".format(d,c)
                        cursor.execute(b)
                        db.commit()
                    elif a=="6":
                        d=input("\n""Enter New Returning Date: ")
                        b="update record set Rt_Date='{}' where Adm_No={}".format(d,c)
                        cursor.execute(b)
                        db.commit()
                    if data !=0:
                        print("\n",44*" ","! ! * * Data Edited Successfully * * ! !")
                        input("\n""**Press Enter To Continue......")
                        os.system("cls")
                except:
                    print("\n",44*" ","! ! * * Sorry! Data Not Found * * ! !")
                    print("\n",49*" ","! ! * * Please try again * *! !")
                    input("\n""**Press Enter To Continue.....")
                    os.system("cls")
            elif a=="7":
                print(44*" ","! ! * * Thank You * * ! !")
                input("\n""**Press Enter To Continue....")
                break
            elif a=="":
                print("\n",44*" ","! ! * * Sorry! You Entered No Choice * * ! !")
                print("\n",49*" ","! ! * * Please Try Again * * ! !")
                input("\n""**Press Enter To Continue....")
                os.system("cls")
            else:
                print("\n",44*" ","! ! * * Sorry! You Entered Wrong Choice * * ! !")
                print("\n",49*" ","! ! * * Please Try Again * * ! !")
                input("\n""**Press Enter To Continue....")
    def search():
        import os
        os.system("cls")
        print("\n",37*" ",77*"-","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",54*" ","* * * ! ! ! TO SEARCH RECORD ! ! ! * * *","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",37*" ",77*"-","\n")
        f=input("\n""Please Enter ID of Book or Adm No of Student: ")
        try:
            cursor=db.cursor()
            q="select*from record where B_id=%s or Adm_No=%s"%(f,f)
            cursor.execute(q)
            c=cursor.fetchone()
            print("\n""Adm No >>",c[0])
            print("\n""Name of Student >>",c[1])
            print("\n""Book ID >>",c[2])
            print("\n""Name of Book >>",c[3])
            print("\n""Issunig Date >>",c[4])
            print("\n""Returning Date >>",c[5])
            print("\n",44*" ","* * ! ! Thank You ! ! * *")
            input("\n""**Press Enter For Main Menu.....")
        except:
            print("\n",44*" ","* * ! ! Sorry! Data Not Found ! ! * *")
            print("\n",49*" ","* * ! ! Please Try Again ! ! * *")
            input("\n""**Press Enter To Continue.....")
    def remove():
        import os
        os.system("cls")
        print("\n",37*" ",77*"-","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",54*" ","* * * ! ! ! TO REMOVE RECORD ! ! ! * * *","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",37*" ",77*"-","\n")
        a=input("\n""Enter the ID of Book or Adm No of Student: ")
        cursor=db.cursor()
        try:
            b="delete from record where B_id=%s or Adm_No=%s"%(a,a)
            cursor.execute(b)
            db.commit()
            print("\n",44*" ","! ! * * Data Deletd Successfully * * ! !")
            input("\n""**Press Enter To Continue.....")
        except:
            print("\n",44*" ","! ! * * Sorry! Data Not Found * * ! !")
            input("\n""**Press Enter To Continue.....")
    def display():
        os.system("cls")
        print("\n",37*" ",77*"-","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",52*" ","* * * ! ! ! TO GET THE LIST OF ALL RECORD ! ! ! * * *","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",37*" ",77*"-","\n")
        cursor=db.cursor()
        cursor.execute("select *from record")
        a=cursor.fetchall()
        d=0
        for b in a:
            d=d+1
            print("\n""Record >>",d)
            print("\n""Adm_No >>",b[0])
            print("Name of Students>>",b[1])
            print("Book ID >>",b[2])
            print("Name of Book >>",b[3])
            print("Issuing Date >>",b[4])
            print("Return Date>>",b[5])
        print("\n",44*" ","* * ! ! Thank You ! ! * *")
        input("\n""**Press Enter To Continue.....")
#MAIN MENU FOR RECORD==================================================================
    z=""
    while z!="6":
        import os
        os.system("cls")
        print("\n",37*" ",77*"-","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",49*" ","* * * ! ! ! ALL THE RECORDS ARE AVAILABLE HERE ! ! ! * * *","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",37*" ",77*"-","\n")
        print("\n",46*" ","*Press 1--- To Enter New Record")
        print("\n",46*" ","*Press 2--- To Edit Record")
        print("\n",46*" ","*Press 3--- To Remove Record")
        print("\n",46*" ","*Press 4--- To SearchRecord")
        print("\n",46*" ","*Press 5--- To Get List Of All Record")
        print("\n",46*" ","*Press 6--- To Go Back")
        z=input("\n""Please Enter Your Choice: ")
        if z=="1":
            insert()
        elif z=="2":
            edit()
        elif z=="3":
            remove()
        elif z=="4":
            search()
        elif z=="5":
            display()
        elif z=="6":
            print(46*" ","* * ! ! Thank You ! ! * *")
            break
        elif z=="":
            print("\n",44*" ","! ! * * Sorry! You Entered No Number * * ! !")
            print("\n",49*" ","! ! * * Please Try Again * * ! !")
            input("\n""**Press Enter To Continue....")
            os.system("cls")
            continue
        else:
            print(46*" ","! ! * *Entered Number Is Incorrect* * ! !""\n")
            print(49*" ","! ! * * Please Try Again * * ! !""\n")
            input("\n""**Press Enter To Continue.....")
            os.system("cls")
            continue
# MAIN MENU FOR WHOLE PROGRAM======================================================================================:
import os
import time
os.system("cls")
a=""
while a!="4":
    import os
    os.system("cls")
    print("\n",37*" ",77*"-","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",63*" ","* * * ! ! ! WELCOME ! ! ! * * *","\n""\n",62*" ",14*"-",3*"*",14*"-","\n""\n",37*" ",77*"-","\n")
    print("\n",46*" ","*Press 1---For Getting Information Related With Students")
    print("\n",46*" ","*Press 2---For Getting Information Related With Books")
    print("\n",46*" ","*Press 3---For Getting  Records of Library")
    print("\n",46*" ","*Press 4---CLOSE")
    a=input("Please Enter Your Choice: ")
    if a=="1":
        student()
    elif a=="2":
        library()
    elif a=="3":
        record()
    elif a=="4":
        print("\n""\n",63*" ","* * ! ! Thank You ! ! * *")
        print("\n",63*" ","* * ! ! Visit Again ! ! * *")
        print("\n""\n""\n",37*" ",77*"-","\n",55*" ","* * * * * CREATED BY ABHISHEK DUBEY * * * * *","\n",37*" ",77*"-")
        time.sleep(3)
        quit()
    elif a=="":
        print("\n",44*" ","* * ! ! Sorry! You Have Entered No Choice.....")
        print("\n",45*" ","* * ! ! Please Try Again ! ! * *")
        input("\n""**Press To Continue......")
        os.system("cls")
        continue
    else:
        print("\n",44*" ","* * ! ! Sorry! You Have Entered Wrong Choice.....")
        input("\n""**Press To Continue......")
        os.system("cls")
        continue
