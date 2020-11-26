import mysql.connector
import pickle

mydb = mysql.connector.connect( host = "",
    user = "",
    passwd = "",
    database = ''
)

mycursor = mydb.cursor(buffered = True)

#create database
#mycursor.execute('create database income_tax_management')

#Function to display the menu
def Menu():
    print("*"*140)
    print("MAIN MENU".center(140))
    print("1.Insert Record/Records".center(140))
    print("2.Get Taxable Income".center(140))
    print("3.Display all Records".center(140))
    print("4.Search Record Details according to ID".center(140))
    print("5.Update Record".center(140))
    print("6.Delete Record".center(140))
    print("7.Exit".center(140))
    print("*"*140)

def Create():
    try:
        mycursor.execute('create table user_info(ID varchar(10) primary key NOT NULL,NAME varchar(20) NOT NULL,MOBILE varchar(10),EMAIL varchar(20),ADDRESS varchar(20),CITY varchar(10) NOT NULL,COUNTRY varchar(20) NOT NULL,INCOME integer(15))')
        print("Table Created")
        Insert()
    except:
        print("Table Exist")
        Insert()


def Insert():
    while True: #Loop for accepting records
        Acc=input("Enter ID: ")
        Name=input("Enter Name: ")
        Mob=input("Enter Mobile: ")
        email=input("Enter Email: ")
        Add=input("Enter Address: ")
        City=input("Enter City: ")
        Country=input("Enter Country: ")
        Inc=int(input("Enter Annual Income: "))
        Rec=[Acc,Name.upper(),Mob,email.upper(),Add.upper(),City.upper(),Country.upper(),Inc]
        Cmd="insert into user_info values(%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(Cmd,Rec)
        mydb.commit()
        ch=input("Do you want to enter more records? (Y/N): ")
        if ch=='N' or ch=='n':
            break


def Disp_All(): #Function to Display records as per ascending order of ID
    try:
        cmd="select * from user_info order by ID"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        F="%15s %15s %15s %15s %15s %15s %15s %15s"
        print(F % ("ID","NAME","MOBILE","EMAIL ADDRESS","COMPLETE ADDRESS","CITY","COUNTRY","INCOME"))
        print("="*125)
        for i in S:
            for j in i:
                print("%15s" % j, end=' ')
            print("\n")
        print("="*125)
    except:
        print("Table doesn't exist")

def DispSearchID(): #Function to Search for the Record from the database with respect to the ID
    try:
        cmd="select * from user_info"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        ch=input("Enter the ID to be searched: ")
        for i in S:
            if i[0]==ch:
                print("="*125)
                F="%15s %15s %15s %15s %15s %15s %15s %15s"
                print(F % ("ID","NAME","MOBILE","EMAIL ADDRESS","COMPLETE ADDRESS","CITY","COUNTRY","INCOME"))
                print("="*125)
                for j in i:
                    print('%15s' % j,end=' ')
                print()
                break
            else:
                print("Record Not found!")
    except:
        print("Table doesn't exist!")
        

def Update(): #Function to change the details of a customer
    try:
        cmd="select * from user_info"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        A=input("Enter the account ID whose details to be changed: ")
        for i in S:
            i=list(i)
            if i[0]==A:
                ch=input("Change Name?(Y/N): ")
                if ch=='y' or ch=='Y':
                    i[1]=input("Enter Name: ")
                    i[1]=i[1].upper()
                ch=input("Change Mobile?(Y/N): ")
                if ch=='y' or ch=='Y':
                    i[2]=input("Enter Mobile: ")
                ch=input("Change Email?(Y/N): ")
                if ch=='y' or ch=='Y':
                    i[3]=input("Enter email: ")
                    i[3]=i[3].upper()
                ch=input("Change Address?(Y/N): ")
                if ch=='y' or ch=='Y':
                    i[4]=input("Enter Address: ")
                    i[4]=i[4].upper()
                ch=input("Change city?(Y/N): ")
                if ch=='y' or ch=='Y':
                    i[5]=input("Enter City: ")
                    i[5]=i[5].upper()
                ch=input("Change Country?(Y/N): ")
                if ch=='y' or ch=='Y':
                    i[6]=input("Enter country: ")
                    i[6]=i[6].upper()
                ch=input("Change Income?(Y/N): ")
                if ch=='y' or ch=='Y':
                    i[7]=float(input("Enter Annual Income: "))

                    
                cmd="UPDATE user_info SET NAME=%s,MOBILE=%s,EMAIL=%s,ADDRESS=%s,CITY=%s,COUNTRY=%s,INCOME=%s WHERE ID=%s"
                val=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Account Updated!")
                break
            else:
                print("Record not found!!")
    except:
        print("Table doesn't exist!") 


def Delete(): #Function to delete the details of a customer
    try:
        cmd="select * from user_info"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        A=input("Enter the account ID to be deleted: ")
        for i in S:
            i=list(i)
            if i[0]==A:
                cmd="delete from user_info where ID=%s"
                val=(i[0],)
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Account Deleted!")
                break
            else:
                print("Record not found!")
    except:
        print("Table doesn't exist!")  

       
def Get_Income_Tax(): #Function to Withdraw the amount by assuring the min balance of Rs 5000
    try:
        cmd="select * from user_info"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        acc=input("Enter the ID for which taxable income to be calculated:  ")
        for i in S:
            i=list(i)
            if i[0]==acc:
               if i[7]<=250000:
                   tax = 0
                   print ("Your Annual Income is:",i[7],"\nTaxable income is: ",tax)
               elif i[7]>250000 & i[7]<=500000:
                   tax = i[7]*0.05
                   print ("Your Annual Income is:",i[7],"\nTaxable income is: ",tax)
               elif i[7]>500000 & i[7]<=750000:
                   tax= i[7]*0.10
                   print ("Your Annual Income is:",i[7],"\nTaxable income is: ",tax)
               elif i[7]>750000 & i[7]<=1000000:
                   tax = i[7]*0.15
                   print ("Your Annual Income is:",i[7],"\nTaxable income is: ",tax)
               elif i[7]>1000000 & i[7]<=1250000:
                   tax = i[7]*0.20
                   print ("Your Annual Income is:",i[7],"\nTaxable income is: ",tax)
               elif i[7]>1250000 & i[7]<=1500000:
                   tax = i[7]*0.25
                   print ("Your Annual Income is:",i[7],"\nTaxable income is: ",tax)
               else:
                   tax = i[7]*0.30
                   print ("Your Annual Income is:",i[7],"\nTaxable income is: ",tax) 
            else:
                print("Record Not found")
    except:
        print("Table Doesn't exist")


while True:
    Menu()
    ch=input("Enter your Choice: ")
    if ch=="1":
        Create()
    elif ch=="2":
        Get_Income_Tax()
    elif ch=="3":
        Disp_All()
    elif ch=="4":
        DispSearchID()
    elif ch=="5":
        Update()
    elif ch=="6":
        Delete()
    elif ch=="7":
        print("Exiting...")
        break
    else:
        print("Wrong Choice Entered!!!")

