#MADE BY
#TANISHKA PASBOLA 12A 31
#ANSH GOYAL 12A 7
import mysql.connector
import pandas as pd
import random
import os

passwd=str(input("ENTER DATABASE PASSWORD:")) 

dictp=["PRODUCT ID","PRODUCT NAME","TYPE","QUANTITY","BRAND","Price ex. GST","DISCOUNT(%)","GST %"]

custp=["CUST. NAME","MOBILE NUMBER","INVOICE LOC.","TIME STAMP","AMOUNT"]

mydb = mysql.connector.connect(host='localhost',user='root',password=passwd)

mycursor=mydb.cursor()

mycursor.execute("create database if not exists project")

mycursor.execute("use project")

mycursor.execute("create table  if not exists customers (cust_name varchar(50), phone_number bigint, invoice_dest varchar(50), date_time datetime , amount float)")

mycursor.execute("create table if not exists product (product_id integer primary key,product_name varchar(50),type varchar(50),quantity integer,brand varchar(50),Price_ex_GST integer,discount integer,GST integer)")


mycursor.execute("create table if not exists user_data(username varchar(30) primary key,password varchar(30) default'000')")
print("-----------------------------------------------------WELCOME TO SUPER STORE---------------------------------------------------------------------------------")
def home():
    a=int(input('''SELECT YOUR ENTRY:
1. CLIENT
2. ADMIN
3. EXIT:
'''))
    if a==1:
        client()
    elif a==2:
        admin()
    elif a==3:
        print("THANK YOU!!!!!")
    else:
        print("INVALID INPUT")
        home()
    os.system('cls')

def client():
    os.system('cls')
    b=int(input('''
1. BUY
2. PRINT INVOICE
3. HOME SCREEN:
'''))
    if b==1:
        invoice()
    elif b==2:
        printi()
    elif b==3:
        home()
    else:
        print("INVALID INPUT")
        client()
    os.system('cls')
def admin():
    print("""
                                                                                1. SIGN IN (LOGIN)
                                                                                2. SIGN UP (REGISTER)
                                                                                3. HOMESCREEN
                                                                                """)
    
    c=int(input("enter your choice:"))
    if c==2:
        print("""

                                                    =================================================================================
                                                    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!PLEASE REGISTER YOURSELF!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                                    =================================================================================
                                                    """)
        u=input("ENTER YOUR PREFERRED USERNAME!!:")
        p=input("ENTER YOUR PREFERRED PASSWORD (MINIMUM  6 CHARACTERS):")
        if len(p)< 6:
            p=input("ENTER YOUR PREFERRED PASSWORD (MINIMUM  6 CHARACTERS):")
        mycursor.execute("insert into user_data values('"+u+"','"+p+"')")
        mydb.commit()
    
    
        print("""
                                                    =================================================================================
                                                    !!!!!!!!!!!!!!!!!!!!!!!!!!!REGISTERED SUCCESSFULLY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                                    =================================================================================
                                                    """)
        x=input("enter any key to continue:")
        os.system('cls')
        admin()
    elif c==1:
        c2=False
        
        print("""
                                                        =================================================================================
                                                        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  {{SIGN IN }}  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                                        =================================================================================
                                                        """)
        un=input("ENTER THE USERNAME!!:")
        ps=input("ENTER THE PASSWORD!!:")
                
        mycursor.execute("select password from user_data where username='"+un+"'")
        row=mycursor.fetchall()
        for i in row:
            a=list(i)
            if a[0]==str(ps):
                c2=True
            else:
                continue
        if c2==True:
            admin1()
        elif c2==False:
            print("WRONG PASSWORD!!! TRY AGAIN!!")
            admin()
    elif c==3:
        home()
    os.system('cls')
def admin1():
    d=int(input('''
1. PASSWORD CHANGE
2. SALES
3. EDIT PRODUCTS
4. STOCK IN HAND
5. HOMESCREEN:
'''))
    if d==1:
        change()
    elif d==2:
        sales()
    elif d==3:
        products()
    elif d==4:
        stock()
    elif d==5:
        home()
    else:
        print("INVALID INPUT")
        admin1()


def change():
    e=str(input("ENTER PREVIOUS PASSWORD TO CONTINUE:"))
    un1=input("ENTER THE USERNAME!!:")
    mycursor.execute("select password from user_data where username='"+un1+"'")
    row=mycursor.fetchall()
    for i in row:
        a=list(i)
        if a[0]==str(e):
            e1=str(input("ENTER NEW PASSWORD TO CONTINUE:"))
            mycursor.execute("update user_data \
                             set password='"+e1+"'\
                             where username='"+un1+"'")
            mydb.commit()
            print('''CHANGED SUCCESSFULLY
LOGIN AGAIN !!!!''')
            admin()
    os.system('cls')
def products():
    f=int(input('''
1. ADD PRODUCTS
2. UPDATE 
3. DELETE PRODUCTS
4. BACK
5. HOMESCREEN
'''))
    if f==1:
        addp()
    elif f==2:
        updatep()
    elif f==3:
        deletep()
    elif f==4:
        admin1()
    elif f==5:
        home()
    else:
        print('INVALID INPUT!!!')
    os.system('cls')
def addp():
    g1=input("ENTER PRODUCT ID:")
    g2=input("ENTER PRODUCT NAME:")
    g3=input("ENTER PRODUCT TYPE:")
    g4=input("ENTER QUANTITY:")
    g5=input("ENTER BRAND:")
    g6=int(input("ENTER MRP:"))
    g7=int(input("ENTER DISCOUNT:"))
    g8=int(input("ENTER GST %:"))
    g6=str(g6)
    g7=str(g7)
    g8=str(g8)
    mycursor.execute("select * from product")
    row=mycursor.fetchall()
    g10=0
    for i in row:
       if i[0]==int(g1):
            g10=1
    if g10==1:
        print("PRODUCT ID IS ALREADY USED PLEASE USE DIFFERENT ID OR UPDATE STOCK")
        g9=int(input('''1. ADD PRODUCT
2. UPDATE STOCK:
'''))
        if g9==1:
            addp()
        elif g9==2:
            updatep()
        else:
            print("INVALID INPUT!!")
            admin1()
    elif g10==0:
        mycursor.execute("insert into product values("+g1+",'"+g2+"','"+g3+"',"+g4+",'"+g5+"',"+g6+","+g7+","+g8+")")
        mydb.commit()
        print("PRODUCT ADDED")
        products()
    g11=input("WANT TO ADD MORE?(Y/N):")
    g11=g11.upper()
    if g11=="Y":
        addp()
    elif g11=="N":
        products()
    else:
        admin1()
def updatep():
    h1=input("ENTER PRODUCT ID:")
    mycursor.execute("desc product")
    h2=mycursor.fetchall()
    for i in range(1,7):
        h3=h2[i][0]
        h10=dictp[i]
        a23="WANT TO UPDATE "+h10+" ?(Y/N):"
        h4=input(a23)
        h4=h4.upper()
        if h4=="Y":
            h5=input("ENTER UPDATED VALUE:")
            h5=h5.upper()
            if h10=="quantity":
                mycursor.execute("update product \
                                set quantity=quantity +'"+h5+"' \
                                where product_id="+h1+"")
                mydb.commit()
            else:
                mycursor.execute("update product \
                                set "+h3+"='"+h5+"' \
                                where product_id="+h1+"")
                mydb.commit()
            print("UPDATED!!!")
        elif h4=="N":
            continue
    h7=input("WANT TO UPDATE MORE?(Y/N):")
    h7=h7.upper()
    if h7=="Y":
        updatep()
    elif h7=="N":
        products()
def deletep():
    i1=input("ENTER PRODUCT ID OF RECORD TO BE DELETED:")
    mycursor.execute("select * from product")
    row=mycursor.fetchall()
    i2=0
    for i in row:
        if i[0]==int(i1):
            i2=1
        else:
            i2=0
    if i2==1:
        print("RECORD TO BE DELETED:")
        for i in row:
            if i[0]==int(i1):
                v=list(i)
                d=dict(zip(dictp,v))
        print(d)
        mycursor.execute("delete from product where product_id='"+i1+"'")
        mydb.commit()
        print("DELETED!!!")
    elif i2==0:
        print("NO RECORD FOUND WITH PRODUCT ID", i1)
    i3=input("WANT TO DELETE MORE?(Y/N):")
    i3=i3.upper()
    if i3=="Y":
        deletep()
    if i3=="N":
        products()
def stock():
    mycursor.execute("Select * from product  ")
    data=mycursor.fetchall()
    j1=pd.DataFrame(data,columns=dictp)
    pd.set_option("display.max_rows",None,"display.max_columns",None)
    print(j1.to_string())
    j=input("PRESS ANY KEY TO CONTINUE TO ADMIN'S MENU:")
    os.system('cls')
    admin1()
def strip(a):
    x = ""
    for i in range(0,len(a)-1):
        x=x+a[i]
    return(x)
def invoice():
    c2222=random.randint(1,100)
    c2222=str(c2222)
    
    from datetime import datetime
    time=datetime.now()
    tim=str(time)
    tim = strip(strip(strip(strip(strip(strip(strip(tim)))))))
    tim=str(tim)
    name3="SUPER STORE"
    namep=""
    mycursor.execute("Select * from product where quantity>0")
    z4=mycursor.fetchall()
    apd=[]
    app=[]
    apgst=[]
    apname=[]
    for k in z4:
        apd.append(int(k[6]))
        app.append(int(k[5]))
        apgst.append(int(k[7]))
        apname.append(k[1])
    for i in name3:
        namep+=i
        namep+=" "
    ly=[]
    ny=[]
    apid=[]
    apq=[]
    a=1
    print("AVAILABLE PRODUCTS:")
    mycursor.execute("Select product_id,product_name,quantity from product where quantity>0")
    z1=mycursor.fetchall()
    for j in z1:
        apid.append(j[0])
        z=int(j[2])
        apq.append(z)
    z2=pd.DataFrame(z1,columns=["PRODUCT ID","PRODUCT NAME","QUANTITY AVAILABLE"])
    pd.set_option("display.max_rows",None,"display.max_columns",None)
    result=z2.empty
    if result==True:
        print("NO PRODUCTS PRESENT AT THIS MOMENT")
        fff=input("ENTER ANY KEY TO CONTINUE:")
        home()
    print(z2.to_string())
    while a>=1:
        print("Enter Product code:")
        p=int(input())
        if p not in apid:
            print("No Such Product Found!" + " Please Try Again")
            p1=input("Y TO CONTINUE :")
            p1=p1.upper()
            if p1=="Y":
                continue
            else:
                break
        ly.append(int(p))
        ny.append([])
        print("Quantity:")
        q=int(input())
        q1=apid.index(p)
        if q>int(apq[q1]):
            q=int(apq[q1])
            print("ONLY",int(apq[q1]),"AVAILABLE")
        for i in z4:
            if p==i[0]:
                ny[a-1].append(a)
                ny[a-1].append(q)
                ny[a-1].append(i[1])
                ny[a-1].append(i[5])
                ny[a-1].append(i[6])
                ny[a-1].append(i[7])
        y=input("ENTER 1 to stop or press any key to continue:")
        a=a+1
        if y=="1":
            #d=5
            break
    name=input("ENTER NAME:")
    mobile=input("ENTER MOBILE NUMBER :")
    name1=name+c2222+".txt"
    c=open(name1,"a")
    c.close()
    maxi = 12
    x = open(name1,"a+")
    l = " " + "S.no" + " "*2+ "Product Name" + " "*(maxi-10) + "Price" + " "*4 +"Discount"+" "*3+"GST(%)" + " "*2 +"Quantity" + "  "+ "Total"+" "
    f=len(l)
    z=int((f-len(namep))/2)
    v=int((f-len("INVOICE"))/2)
    w=int((f-len(tim))/2)
    j=" "*z
    x.write(j)
    x.write(namep+"\n")
    x.write (" "*v + "INVOICE" + "\n"*2)
    x.write(" "*w + tim + "\n")
    x.write("\n"*3)
    x.write("NAME   :"+ name +"\n")
    x.write("MOBILE NUMBER  :"+ mobile +"\n")
    x.write((" " + "S.no" + " "*2+ "Product Name" + " "*(maxi-10) + "Price" + " "*4 + "GST(%)" + " "*2 +"Discount"+" "*3+"Quantity" + "  "+ "Total"+" ")+"\n"+"\n")
    t=0
    disc=0
    for i in range(len(ly)):
        id=ly[i]
        quan=ny[i][1]
        sno=ny[i][0]
        pname=ny[i][2]
        price=ny[i][3]
        gst=ny[i][5]
        dis=ny[i][4]
        mycursor.execute("UPDATE  product  \
                          set quantity=quantity -"+str(quan)+" \
                          where product_id="+str(id)+"")
        mydb.commit()
        cost=(price*int(quan)+((price*gst*int(quan))/100))
        price1=cost-int((dis*cost)/100)
        x.write((" " + str(sno) + ")." + " "*(4-len(str(sno))) + pname + " "*(maxi +2-len(name)) + str(price) + " "*(10-len(str(price))) + str(gst) + " "* (10-len(str(gst))) +str(dis)+" "*(9-len(str(dis)))+str(quan) + " "* (10 - len(str(quan))) + str(price1) + "\n"))
        disc+=price1
    #dis=disc*d*0.01
    x.write("\n")
    total=disc
    dis=str(dis)
    total=str(total)
    #x.write(" "*f+ "Discount:" + " " + dis + "\n")
    x.write(" "*f+ "Net Payable:" + " " + total + "\n")
    x.write ("*. This is a Computer Generated Invoice and does not require Signature."+"\n")
    x.write("*. Return/Replacement is not allowed under any circumstances."+"\n")
    x.write("\n"+"Thanks for shopping with us"+"\n"*3)
    x.close()
    print("Net Payable : ",total)
    print("Press Any Key to continue!")
    if total==0.00:
        home()
    else:
        x21=input()
        os.system('cls')
        x22=input("ENTER P TO PRINT INVOICE OR ANY KEY TO CONTINUE:")
        print("\n"*4)
        x22=x22.upper()
        mycursor.execute("insert into customers values('"+name+"','"+mobile+"','"+name1+"','"+tim+"','"+total+"')")
        mydb.commit()
        if x22=="P":
            x23=open(name1)
            x24=x23.readlines()
            for i in x24:
                print(i)
            print("Press Any Key to continue!")
            x21=input()
            home()
        elif x22!="P":
            home()
def printi():
    a=input("CUSTOMER NAME:")
    #b=input("MOBILE NUMBER:")   
    mycursor.execute("select invoice_dest from customers where cust_name='"+a+"' order by date_time desc")
    ab=mycursor.fetchall()
    ab1=ab[0][0]
    file=open(ab1)
    file1=file.readlines()
    for i in file1:
        print(i)
    ff=input("ANY KEY TO CONTINUE :")
    os.system('cls')
    home()
def sales():
    mycursor.execute("select * from customers")
    data1=mycursor.fetchall()
    j11=pd.DataFrame(data1,columns=custp)
    pd.set_option("display.max_rows",None,"display.max_columns",None)
    print(j11.to_string())
    x233=input("PRESS ANY KEY TO CONTINUEEE:")
    os.system('cls')
    admin1()
if __name__ == '__main__':
    home()
#MADE BY ANSH GOYAL 12A AND TANISHKA PASBOLA 12A

