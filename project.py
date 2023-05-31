from tkinter import *
import mysql.connector as m
from tkinter import messagebox as msg
import matplotlib.pyplot as mat

root = Tk()
root.title("Helath Tracker")
root.geometry("600x500")
root.minsize(300, 300)
root.maxsize(1200, 900)

mydatabase1 = m.connect(host="localhost", user="***", password="******", database="project")

frame1 = Frame(root, bg="darkslategray", borderwidth=6, relief=SUNKEN)
l1 = Label(frame1, text="Health Tracker",font=("calbri",15,"bold"),fg="white",bg="darkslategray").place(x=0, relwidth=1)
frame1.place(relx=0, y=0, relheight=0.065, relwidth=1)
# To add user
def adduser():
    # create a frame
    frame3 = Frame(root, bg="darkseagreen2", borderwidth=6, relief=SUNKEN)

    # Create the entries that add text fields
    Name = Entry(frame3,font=("calbri",10),fg="black")
    Name.place(x=200, y=50, relwidth=0.5)

    Age = Entry(frame3,font=("calbri",10),fg="black")
    Age.place(x=200, y=100, relwidth=0.5)

    Gender = Entry(frame3,font=("calbri",10),fg="black")
    Gender.place(x=200, y=150, relwidth=0.5)

    Weight = Entry(frame3,font=("calbri",10),fg="black")
    Weight.place(x=200, y=200, relwidth=0.5)

    Height = Entry(frame3,font=("calbri",10),fg="black")
    Height.place(x=200, y=250, relwidth=0.5)

    # Create labels
    l1 = Label(frame3, text="Name",font=("calbri",10,"bold"),fg="black",bg="darkseagreen2").place(x=10, y=50, relwidth=0.25)
    l2 = Label(frame3, text="Age",font=("calbri",10,"bold"),fg="black",bg="darkseagreen2").place(x=10, y=100, relwidth=0.25)
    l3 = Label(frame3, text="Gender",font=("calbri",10,"bold"),fg="black",bg="darkseagreen2").place(x=10, y=150, relwidth=0.25)
    l4 = Label(frame3, text="Weight (kg)",font=("calbri",10,"bold"),fg="black",bg="darkseagreen2").place(x=10, y=200, relwidth=0.25)
    l5 = Label(frame3, text="Height",font=("calbri",10,"bold"),fg="black",bg="darkseagreen2").place(x=10, y=250, relwidth=0.25)

    # Submit user will submit all the records entered by user and place inside project database
    def submitadduser():
        cursor = mydatabase1.cursor()
        query = "insert into adduser(name,age,gender,weight,height) values(%s,%s,%s,%s,%s)"
        try:
            cursor.execute(query, [Name.get(), Age.get(), Gender.get(), Weight.get(), Height.get()])
            mydatabase1.commit()

            # It will fetch the ID from record and display it to user

            query1 = "select id from adduser where name=%s and age=%s and weight=%s"
            cursor.execute(query1, [Name.get(), Age.get(), Weight.get()])
            i = cursor.fetchone()
            msg.showinfo("Successful", f"User Successfully Added. ID is: {i}")
        except m.Error:
            msg.showerror("Missing Fields", "Enter valid fields")

    # Create Buttons
    b6 = Button(frame3, text="Submit", width=25,font=("calbri",10,"bold"),fg="black",bg="white", command=submitadduser).place(x=10, y=300, relwidth=0.9)
    b7 = Button(frame3, text="Back", width=25,font=("calbri",10,"bold"),fg="black",bg="white", command=root.destroy).place(x=10, y=350, relwidth=0.9)
    frame3.place(relx=0.38, y=50, relheight=0.8, relwidth=0.6)

#To add records
def addrecord():
    frame3 = Frame(root, bg="darkseagreen2", borderwidth=6, relief=SUNKEN)



    def addHaemoglobinWeight():
        frame5 = Frame(root, bg="darkseagreen2", borderwidth=6, relief=SUNKEN)
        l1 = Label(frame5, text="ID",font=("calbri",10,"bold"),fg="black",bg="darkseagreen2").place(x=10, y=100, relwidth=0.25)
        l2 = Label(frame5, text="Haemoglobin",font=("calbri",10,"bold"),fg="black",bg="darkseagreen2").place(x=10, y=150, relwidth=0.25)
        l3 = Label(frame5, text="Weight (kg)",font=("calbri",10,"bold"),fg="black",bg="darkseagreen2").place(x=10, y=200, relwidth=0.25)

        id = Entry(frame5)
        id.place(x=200, y=100, relwidth=0.5)
        Haemoglobin = Entry(frame5,font=("calbri",10,"bold"),fg="black",bg="white")
        Haemoglobin.place(x=200, y=150, relwidth=0.5)
        Weight = Entry(frame5,font=("calbri",10,"bold"),fg="black",bg="white")
        Weight.place(x=200, y=200, relwidth=0.5)

        #This will add haemoglobin and weight in table
        def submithaemoglobinweight():

            cursor = mydatabase1.cursor()
            query = "insert into addhaemoglobinweight(id,haemoglobin,weight) values(%s,%s,%s)"
            try:
                cursor.execute(query,[id.get(), Haemoglobin.get(), Weight.get()])

                # It will update weight and haemoglobin inside adduser table

                query1 = " update adduser set weight=%s where id=%s"
                query2 = "update adduser set haemoglobin=%s where id=%s"
                cursor.execute(query1, [Weight.get(), id.get()])
                cursor.execute(query2, [Haemoglobin.get(), id.get()])
                mydatabase1.commit()
                msg.showinfo("Successful", "Details added Successfully")
            except Exception:
                msg.showerror("Missing Fields", "Enter valid fields")

        b1 = Button(frame5, text="Submit", width=25,font=("calbri",10,"bold"),fg="black",bg="white", command=submithaemoglobinweight).place(x=10, y=300, relwidth=0.9)
        b2 = Button(frame5, text="Back", width=25,font=("calbri",10,"bold"),fg="black",bg="white", command=addrecord).place(x=10, y=350, relwidth=0.9)
        frame5.place(relx=0.38, y=50, relheight=0.8, relwidth=0.6)

    def addBPSPO2():
        frame4 = Frame(root, bg="darkseagreen2", borderwidth=6, relief=SUNKEN)

        l1 = Label(frame4, text="ID",font=("calbri",10,"bold"),fg="black",bg="darkseagreen2").place(x=10, y=100, relwidth=0.25)
        l2 = Label(frame4, text="BP",font=("calbri",10,"bold"),fg="black",bg="darkseagreen2").place(x=10, y=150, relwidth=0.25)
        l3 = Label(frame4, text="SPO2",font=("calbri",10,"bold"),fg="black",bg="darkseagreen2").place(x=10, y=200, relwidth=0.25)

        id = Entry(frame4,font=("calbri",10,"bold"),fg="black",bg="white")
        id.place(x=200, y=100, relwidth=0.5)
        BP = Entry(frame4,font=("calbri",10,"bold"),fg="black",bg="white")
        BP.place(x=200, y=150, relwidth=0.5)
        SPO2 = Entry(frame4,font=("calbri",10,"bold"),fg="black",bg="white")
        SPO2.place(x=200, y=200, relwidth=0.5)

        # It will insert BP and SPO2 inside addBPSPO2 table

        def submitBPSPO2():
            cursor = mydatabase1.cursor()
            query = "insert into addBPSPO2(id,BP,SPO2) values(%s,%s,%s)"
            try:
                cursor.execute(query,[id.get(), BP.get(), SPO2.get()])

                # It will update BP and SPO2 inside adduser table

                query1 = " update adduser set bp=%s where id=%s"
                query2 = "update adduser set spo2=%s where id=%s"
                cursor.execute(query1, [BP.get(), id.get()])
                cursor.execute(query2, [SPO2.get(), id.get()])
                mydatabase1.commit()
                msg.showinfo("Successful","Details added Successfully")
            except Exception:
                msg.showerror("Missing Fields", "Enter valid fields")
        b1 = Button(frame4, text="Submit", width=25,font=("calbri",10,"bold"),fg="black",bg="darkseagreen2", command=submitBPSPO2).place(x=10, y=300, relwidth=0.9)
        b2 = Button(frame4, text="Back", width=25,font=("calbri",10,"bold"),fg="black",bg="darkseagreen2", command=addrecord).place(x=10, y=350, relwidth=0.9)
        frame4.place(relx=0.38, y=50, relheight=0.8, relwidth=0.6)

    # create a frame

    # Create labels
    l1 = Label(frame3, text="Add Daily:-",font=("calbri",10,"bold"),fg="black",bg="darkseagreen2").place(x=10, y=30, relwidth=0.25)
    b1 = Button(frame3, text="Add BP and SPO2", width=25,font=("calbri",10,"bold"),fg="black",bg="white", command=addBPSPO2).place(x=10, y=60, relwidth=0.9)

    l2 = Label(frame3, text="Add Monthly:-",font=("calbri",10,"bold"),fg="black",bg="darkseagreen2").place(x=10, y=160, relwidth=0.25)
    b2 = Button(frame3, text="Add Haemoglobin and Weight", width=25,font=("calbri",10,"bold"),fg="black",bg="white", command=addHaemoglobinWeight).place(x=10, y=190,
                                                                                                         relwidth=0.9)

    b1 = Button(frame3, text="Submit", width=25,font=("calbri",10,"bold"),fg="black",bg="white").place(x=10, y=300, relwidth=0.9)
    b2 = Button(frame3, text="Back", width=25,font=("calbri",10,"bold"),fg="black",bg="white", command=root.destroy).place(x=10, y=350, relwidth=0.9)
    frame3.place(relx=0.38, y=50, relheight=0.8, relwidth=0.6)


# To show the records
def showrecord():

    # Create a frame

    frame6 = Frame(root, bg="darkseagreen2", borderwidth=6, relief=SUNKEN)

    # Creating a label and Entry ie text field for ID

    l1 = Label(frame6, text="Enter ID",font=("calbri",10,"bold"),fg="black",bg="darkseagreen2").place(x=10, y=100, relwidth=0.25)
    id = Entry(frame6,font=("calbri",10,"bold"),fg="black",bg="white")
    id.place(x=200, y=100, relwidth=0.5)

    # Creating a function to fetch record from database

    def submitshowrecord():

        # Checking Length and type and the entered ID is less than zero or not

        if len(id.get()) == 0  or int(id.get()) <= 0 and type(id.get()) != IntVar:
            msg.showerror("Invalid ID", "Enter A valid ID ")
        else:
            cursor = mydatabase1.cursor()
            query = f"select Name,Age,Gender,Height,Weight,Haemoglobin,BP,SPO2 from adduser where id={id.get()}"
            cursor.execute(query)
            l = cursor.fetchall()
            frame7 = Frame(root, bg="darkseagreen2", borderwidth=6, relief=SUNKEN)

            # Creating Lables of Name, Age,Gender,Height,Weight,Haemoglobin,BP,SPO2

            l1 = Label(frame7, text="Name",font=("calbri",10,"bold"),fg="black",bg="darkseagreen2")
            l1.grid(row=0, column=0,padx=10, pady=10)
            l2 = Label(frame7, text="Age",font=("calbri",10,"bold"),fg="black",bg="darkseagreen2")
            l2.grid(row=0, column=1,padx=10, pady=10)
            l3 = Label(frame7, text="Gender",font=("calbri",10,"bold"),fg="black",bg="darkseagreen2")
            l3.grid(row=0, column=2,padx=10,pady=10)
            l4 = Label(frame7, text="Height",font=("calbri",10,"bold"),fg="black",bg="darkseagreen2")
            l4.grid(row=0,column=3,padx=10,pady=10)
            l5 = Label(frame7, text="Weight",font=("calbri",10,"bold"),fg="black",bg="darkseagreen2")
            l5.grid(row=0,column=4,padx=10,pady=10)
            l6 = Label(frame7, text="Haemoglobin",font=("calbri",10,"bold"),fg="black",bg="darkseagreen2")
            l6.grid(row=0,column=5,padx=10,pady=10)
            l7 = Label(frame7, text="BP",font=("calbri",10,"bold"),fg="black",bg="darkseagreen2")
            l7.grid(row=0, column=6,padx=10, pady=10)
            l8 = Label(frame7, text="SPO2",font=("calbri",10,"bold"),fg="black",bg="darkseagreen2")
            l8.grid(row=0, column=7,padx=10, pady=10)

            # Showing records one by one

            for i in l:
                l1 = Label(frame7, text=i[0],font=("calbri",10,"bold"),fg="black",bg="darkseagreen2")
                l1.grid(row=2,column=0,padx=10,pady=10)
                l2 = Label(frame7, text=i[1],font=("calbri",10,"bold"),fg="black",bg="darkseagreen2")
                l2.grid(row=2,column=1,padx=10,pady=10)
                l3 = Label(frame7, text=i[2],font=("calbri",10,"bold"),fg="black",bg="darkseagreen2")
                l3.grid(row=2,column=2,padx=10,pady=10)
                l4 = Label(frame7, text=i[3],font=("calbri",10,"bold"),fg="black",bg="darkseagreen2")
                l4.grid(row=2,column=3,padx=10,pady=10)
                l5 = Label(frame7, text=i[4],font=("calbri",10,"bold"),fg="black",bg="darkseagreen2")
                l5.grid(row=2,column=4,padx=10,pady=10)
                l6 = Label(frame7, text=i[5],font=("calbri",10,"bold"),fg="black",bg="darkseagreen2")
                l6.grid(row=2,column=5,padx=10,pady=10)
                l7 = Label(frame7, text=i[6],font=("calbri",10,"bold"),fg="black",bg="darkseagreen2")
                l7.grid(row=2,column=6,padx=10,pady=10)
                l8 = Label(frame7, text=i[7],font=("calbri",10,"bold"),fg="black",bg="darkseagreen2")
                l8.grid(row=2,column=7,padx=10,pady=10)
                b2 = Button(frame6, text="Back", width=25,font=("calbri",10,"bold"),fg="black",bg="white", command=showrecord)
                b2.place(x=10, y=350, relwidth=0.9)
                frame7.place(relx=0.38, y=250, relheight=0.56, relwidth=0.6)

    b1 = Button(frame6, text="Submit", width=25,font=("calbri",10,"bold"),fg="black",bg="white", command=submitshowrecord)
    b1.place(x=10, y=300, relwidth=0.9)
    b2 = Button(frame6, text="Back", width=25,font=("calbri",10,"bold"),fg="black",bg="white", command=root.destroy)
    b2.place(x=10, y=350, relwidth=0.9)
    frame6.place(relx=0.38, y=50, relheight=0.8, relwidth=0.6)

# Create a function which shows graph
def addgraph():
    # Creating frame which had ID lable which take input from user
    frame8 = Frame(root, bg="darkseagreen2", borderwidth=6, relief=SUNKEN)
    l1 = Label(frame8, text="ID",font=("calbri",10,"bold"),fg="black",bg="darkseagreen2").grid(row=1, column=0,padx=10, pady=10)
    id = Entry(frame8,font=("calbri",10,"bold"),fg="black",bg="white")
    id.place(x=200, y=10, relwidth=0.5)

    # This function show graph of haemoglobin

    def haemoglobingraph():

        # Query to fetch data from table

        query1=f"select haemoglobin from addhaemoglobinweight where id={id.get()}"
        cursor=mydatabase1.cursor()

        # If user enter wrong details and user left the field blank it raise exception

        try:
            cursor.execute(query1)
            i=cursor.fetchall()
            mat.plot(i)
            mat.show()
        except Exception:
            msg.showerror("Missing Fields", "Enter valid ID")

    # This function show graph of BP

    def bpgraph():

        #Query to fetch BP from table

        query1 = f"select bp from addbpspo2 where id={id.get()}"
        cursor = mydatabase1.cursor()
        try:
            cursor.execute(query1)
            i = cursor.fetchall()
            mat.plot(i)
            mat.show()
        except Exception:
            msg.showerror("Missing Fields", "Enter valid ID")

    # This function show graph of SPO2

    def spo2graph():
        # Query to fetch SPO2 from table

        query1 = f"select spo2 from addbpspo2 where id={id.get()}"
        cursor = mydatabase1.cursor()

        # If user enter ID value in negative or zero it raise exception
        try:
            cursor.execute(query1)
            i = cursor.fetchall()
            mat.plot(i)
            mat.show()
        except Exception:
            msg.showerror("Missing Fields", "Enter valid ID")


    b1 = Button(frame8, text="Haemoglobin", width=25,font=("calbri",10,"bold"),fg="black",bg="white", command=haemoglobingraph).grid(row=3, column=0,padx=10, pady=10)
    b2 = Button(frame8, text="BP", width=25,font=("calbri",10,"bold"),fg="black",bg="white", command=bpgraph).grid(row=4, column=0,padx=10, pady=10)
    b1 = Button(frame8, text="SPO2", width=25,font=("calbri",10,"bold"),fg="black",bg="white", command=spo2graph).grid(row=5, column=0,padx=10, pady=10)
    frame8.place(relx=0.38, y=50, relheight=0.8, relwidth=0.6)


frame2 = Frame(root, bg="darkslategray", borderwidth=6, relief=SUNKEN)
b1 = Button(frame2, text="Add User", width=25,font=("calbri",11,"bold"),fg="black",bg="white", command=adduser).place(x=10, y=50, relwidth=0.9)
b2 = Button(frame2, text="Add Record", width=25,font=("calbri",11,"bold"),fg="black",bg="white", command=addrecord).place(x=10, y=100, relwidth=0.9)
b3 = Button(frame2, text="Show Record", width=25,font=("calbri",11,"bold"),fg="black",bg="white", command=showrecord).place(x=10, y=150, relwidth=0.9)
b4 = Button(frame2, text="Graph", width=25,font=("calbri",11,"bold"),fg="black",bg="white", command=addgraph).place(x=10, y=200, relwidth=0.9)
frame2.place(relx=0, y=50, relheight=0.8, relwidth=0.37)

root.mainloop()
