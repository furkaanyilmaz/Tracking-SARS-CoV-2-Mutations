from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from tkcalendar import*
import datetime
import pymysql
from PIL import ImageTk
from tkinter import messagebox

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1366x700+0+0")
        self.root.resizable(False,False)
        self.loginform()
    def loginform(self):
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=0,y=0,height=700,width=1366)
        self.img=ImageTk.PhotoImage(file="REGISTR.jpg")
        img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)
        frame_input=Frame(self.root,bg="white")
        frame_input.place(x=320,y=130,height=450,width=350)
        label1=Label(frame_input,text="Login here",font=("impact",32,"bold"),fg="cadetblue",bg="white")
        label1.place(x=75,y=20)
        label2 = Label(frame_input, text="Username(Email-id)", font=("Goudy old style", 20, "bold"),fg='cadetblue', bg='white')
        label2.place(x=30, y=95)
        self.email_txt = Entry(frame_input, font=("times new roman", 15, "bold"),bg='lightgray')
        self.email_txt.place(x=30, y=145, width=270, height=35)
        label3 = Label(frame_input, text="Password", font=("Goudy old style", 20, "bold"),fg='cadetblue', bg='white')
        label3.place(x=30, y=195)
        self.password = Entry(frame_input, font=("times new roman", 15, "bold"),bg='lightgray')
        self.password.place(x=30, y=245, width=270, height=35)
        btn1 = Button(frame_input, text="forgot password?", cursor='hand2',font=('calibri', 10), bg='white', fg='black', bd=0)
        btn1.place(x=125, y=305)
        btn2 = Button(frame_input, text="Login", command=self.login, cursor="hand2",font=("times new roman", 15), fg="white", bg="cadetblue",bd=0, width=15, height=1)
        btn2.place(x=90, y=340)
        btn3 = Button(frame_input, command=self.Register, text="Not Registered?register", cursor="hand2", font=("calibri", 10), bg='white', fg="black", bd=0)
        btn3.place(x=110, y=390)

    def login(self):

        if self.email_txt.get() == "" or self.password.get() == "":

            messagebox.showerror("Error", "All fields are required", parent=self.root)

        else:

            try:

                sqlCon = pymysql.connect(host="localhost", user="root", password="furkan,0698", database="library")
                cur = sqlCon.cursor()
                cur.execute('select * from register where emailid=%s and password=%s',(self.email_txt.get(), self.password.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror('Error', 'Invalid Username And Password', parent=self.root)
                    self.loginclear()
                    self.email_txt.focus()
                else:
                    self.appscreen()
                    sqlCon.close()

            except Exception as es:

                messagebox.showerror('Error', f'Error Due to : {str(es)}', parent=self.root)

    def Register(self):

        Frame_login1 = Frame(self.root, bg="white")

        Frame_login1.place(x=0, y=0, height=700, width=1366)

        self.img = ImageTk.PhotoImage(file="REGISTR.jpg")

        img = Label(Frame_login1, image=self.img).place(x=0, y=0, width=1366, height=700)

        frame_input2 = Frame(self.root, bg='white')

        frame_input2.place(x=320, y=130, height=450, width=630)

        label1 = Label(frame_input2, text="Register Here", font=('impact', 32, 'bold'),fg="black", bg='white')
        label1.place(x=45, y=20)
        label2 = Label(frame_input2, text="Username", font=("Goudy old style", 20, "bold"),fg='orangered', bg='white')
        label2.place(x=30, y=95)
        self.entry = Entry(frame_input2, font=("times new roman", 15, "bold"),bg='lightgray')
        self.entry.place(x=30, y=145, width=270, height=35)
        label3 = Label(frame_input2, text="Password", font=("Goudy old style", 20, "bold"),fg='orangered', bg='white')
        label3.place(x=30, y=195)
        self.entry2 = Entry(frame_input2, font=("times new roman", 15, "bold"),bg='lightgray')
        self.entry2.place(x=30, y=245, width=270, height=35)
        label4 = Label(frame_input2, text="Email-id", font=("Goudy old style", 20, "bold"),fg='orangered', bg='white')
        label4.place(x=330, y=95)
        self.entry3 = Entry(frame_input2, font=("times new roman", 15, "bold"),bg='lightgray')
        self.entry3.place(x=330, y=145, width=270, height=35)
        label5 = Label(frame_input2, text="Confirm Password",font=("Goudy old style", 20, "bold"), fg='orangered', bg='white')
        label5.place(x=330, y=195)
        self.entry4 = Entry(frame_input2, font=("times new roman", 15, "bold"),bg='lightgray')
        self.entry4.place(x=330, y=245, width=270, height=35)
        btn2 = Button(frame_input2, command=self.register, text="Register", cursor="hand2", font=("times new roman", 15), fg="white",bg="orangered", bd=0, width=15, height=1)
        btn2.place(x=90, y=340)
        btn3 = Button(frame_input2, command=self.loginform,text="Already Registered?Login", cursor="hand2",font=("calibri", 10), bg='white', fg="black", bd=0)
        btn3.place(x=110, y=390)

    def register(self):

        if self.entry.get() == "" or self.entry2.get() == "" or self.entry3.get() == "" or self.entry4.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        elif self.entry2.get() != self.entry4.get():
            messagebox.showerror("Error", "Password and Confirm Password Should Be Same", parent=self.root)
        else:
            try:
                sqlCon = pymysql.connect(host="localhost", user="root", password="furkan,0698", database="library")
                cur = sqlCon.cursor()
                cur.execute("select * from register where emailid=%s", self.entry3.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User already Exist,Please try with another Email", parent=self.root)
                    self.regclear()
                    self.entry.focus()
                else:
                    cur.execute("insert into register values(%s,%s,%s,%s)", (self.entry.get(), self.entry3.get(),self.entry2.get(),self.entry4.get()))
                    sqlCon.commit()
                    sqlCon.close()
                    messagebox.showinfo("Success", "Register Succesfull", parent=self.root)
                    self.regclear()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)

    def appscreen(self):

        Frame_login = Frame(self.root, bg="pink")

        Frame_login.place(x=0, y=0, height=700, width=1366)

        label1 = Label(Frame_login, text="Hi! Welcome To Lıbrary Management System", font=('times new roman', 32, 'bold'),fg="black", bg='white')
        label1.place(x=375, y=100)
        label2 = Label(Frame_login, text="Please Click the button to open Library Management System", font=('times new roman', 32, 'bold'),fg="black", bg='white')
        label2.place(x=200, y=220)
        btn3 = Button(Frame_login, text="Click", command=self.loginform, cursor="hand2", font=("times new roman", 15),fg="white", bg="orangered", bd=0, width=15, height=1)
        btn3.place(x=10, y=10)
        btn2 = Button(Frame_login, text="Logout", command=root.destroy(), cursor="hand2",font=("times new roman", 15), fg="white", bg="orangered",bd=0, width=15, height=1)
        btn2.place(x=1000, y=10)

    def regclear(self):

        self.entry.delete(0, END)

        self.entry2.delete(0, END)

        self.entry3.delete(0, END)

        self.entry4.delete(0, END)

    def loginclear(self):

        self.email_txt.delete(0, END)

        self.password.delete(0, END)

root = Tk()

ob = Login(root)

root.mainloop()

class Library:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1360x750+0+0")
        self.root.configure(bg="pink")
        MType=StringVar()
        Member=StringVar()
        Title=StringVar()
        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()
        Address2=StringVar()
        PostCode=StringVar()
        MobileNo=StringVar()
        BookISBN=StringVar()
        BookTitle=StringVar()
        BookType=StringVar()
        Author=StringVar()
        DateBorrowed=StringVar()
        DateDue=StringVar()
        SellingPrice=StringVar()
        LateReturnFine=StringVar()
        DateOverDue=StringVar()
        DaysOnLoan=StringVar()
        MainFrame=Frame(self.root,bd=10,bg="pink")
        MainFrame.grid()
        TitleFrame=Frame(MainFrame,bd=10,width=1350,padx=60,relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle=Label(TitleFrame,width=38,font=("arial",40,"bold"),text="Library Management System")
        self.lblTitle.grid()

        ButtonFrame = Frame(MainFrame, bd=10, width=1350, height=50, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        DataFrame = Frame(MainFrame, bd=10, width=1300, height=400, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)
        DataFrameLEFTCover=LabelFrame(DataFrame,bd=10,width=800,height=300,relief=RIDGE,bg="white",font=("arial",12,"bold"),text="Library Membership Info:",)
        DataFrameLEFTCover.pack(side=LEFT,padx=10)
        DataFrameLEFT=Frame(DataFrameLEFTCover,bd=10,width=800,height=300,padx=13,pady=2,relief=RIDGE)
        DataFrameLEFT.pack(side=TOP)
        DataFrameLEFTb=LabelFrame(DataFrameLEFTCover,bd=10,width=800,height=100,pady=4,padx=10,relief=RIDGE,font=("arial",12,"bold"),text="Library Membership Info:",)
        DataFrameLEFTb.pack(side=TOP)
        DataFrameRIGHT=LabelFrame(DataFrame,bd=10,width=450,height=300,padx=10,relief=RIDGE,bg="pink",font=("arial",12,"bold"),text="Book Details:",)
        DataFrameRIGHT.pack(side=RIGHT)

        def iExit():
            iExit=tkinter.messagebox.askyesno("Library Management System","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        def iReset():
            MType.set("")
            Member.set("")
            Title.set("")
            Firstname.set("")
            Surname.set("")
            Address .set("")
            Address2.set("")
            PostCode.set("")
            MobileNo .set("")
            BookISBN .set("")
            BookTitle .set("")
            BookType .set("")
            Author .set("")
            DateBorrowed .set("")
            DateDue.set("")
            SellingPrice.set("")
            LateReturnFine.set("")
            DateOverDue.set("")
            DaysOnLoan.set("")
        def addData():
            if Member.get()=="" or Firstname.get()==""or Surname.get()=="":
                tkinter.messagebox.showerror("Library Management System", "Enter correct members details")
            else:
                sqlCon=pymysql.connect(host="localhost",user="root",password="furkan,0698",database="library")
                cur=sqlCon.cursor()
                cur.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                Member.get(),
                Firstname.get(),
                Surname.get(),
                Address.get(),
                DateBorrowed.get(),
                DateDue.get(),
                DateOverDue.get(),
                Author.get(),
                BookISBN.get(),
                BookTitle.get(),
                ))

                sqlCon.commit()
                DisplayData()
                sqlCon.close()
                DateDue.set(cal.get_date())
                DateOverDue.set("Yes")
                tkinter.messagebox.showinfo("Library Management System", "Record Entered Succesfully")

        def DisplayData():
            sqlCon = pymysql.connect(host="localhost", user="root", password="furkan,0698", database="library")
            cur = sqlCon.cursor()
            cur.execute("select * from library")
            result=cur.fetchall()
            if len(result)!=0:
                self.library_records.delete(*self.library_records.get_children())
                for row in result:
                    self.library_records.insert("","end",values=row)
                    sqlCon.commit()
                sqlCon.close()

        def DeleteDB():
            sqlCon = pymysql.connect(host="localhost", user="root", password="furkan,0698", database="library")
            cur = sqlCon.cursor()
            cur.execute("delete from library where member=%s",Member.get())
            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Library Management System", "Record Succesfully Deleted")

        def SelectedBook(evt):
            booklist.curselection()
            values=str(booklist.get(booklist.curselection()))
            w=values
            if(w=="İki Şehrin Hikayesi"):
                BookISBN.set("ISBN 867849378993")
                BookTitle.set("İki Şehrin Hikayesi")
                Author.set("Charles Dickens")
                LateReturnFine.set("2.50 tl")
                SellingPrice.set("12.99 tl")
                DaysOnLoan.set(14)
                d1=datetime.date.today()
                d2=datetime.timedelta(days=14)
                d3=(d1+d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "Yüzüklerin Efendisi"):
                BookISBN.set("ISBN 125875898")
                BookTitle.set("Yüzüklerin Efendisi")
                Author.set("J.R.R. Tolkien")
                LateReturnFine.set("2.50 tl")
                SellingPrice.set("12.99 tl")
                DaysOnLoan.set(10)
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=10)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "Hobbit"):
                BookISBN.set("ISBN 125875896")
                BookTitle.set("Hobbit")
                Author.set("J.R.R. Tolkien")
                LateReturnFine.set("2.50 tl")
                SellingPrice.set("12.99 tl")
                DaysOnLoan.set(7)
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=7)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "Küçük Prens"):
                BookISBN.set("ISBN 987656545")
                BookTitle.set("Küçük Prens")
                Author.set("Antoine de Saint")
                LateReturnFine.set("2.50 tl")
                SellingPrice.set("12.99 tl")
                DaysOnLoan.set(10)
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=10)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "Harry Potter ve Felsefe Taşı"):
                BookISBN.set("ISBN 635522225")
                BookTitle.set("Harry Potter ve Felsefe Taşı")
                Author.set("J.K. Rowling")
                LateReturnFine.set("2.50 tl")
                SellingPrice.set("12.99 tl")
                DaysOnLoan.set(14)
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=14)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "On Küçük Zenci"):
                BookISBN.set("ISBN 873575898")
                BookTitle.set("On Küçük Zenci")
                Author.set("Agatha Christie")
                LateReturnFine.set("2.50 tl")
                SellingPrice.set("12.99 tl")
                DaysOnLoan.set(14)
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=14)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "Kızıl Köşkün Rüyası"):
                BookISBN.set("ISBN 525875898")
                BookTitle.set("Kızıl Köşkün Rüyası")
                Author.set("Cao Xueqin")
                LateReturnFine.set("2.50 tl")
                SellingPrice.set("12.99 tl")
                DaysOnLoan.set(14)
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=14)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "Ayişe"):
                BookISBN.set("ISBN 129975898")
                BookTitle.set("Yüzüklerin Efendisi")
                Author.set("Henry Rider Haggard")
                LateReturnFine.set("2.50 tl")
                SellingPrice.set("12.99 tl")
                DaysOnLoan.set(14)
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=14)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "Aslan,Cadı ve Dolap"):
                BookISBN.set("ISBN 824135898")
                BookTitle.set("Aslan,Cadı ve Dolap")
                Author.set("Clive Staples Lewis")
                LateReturnFine.set("2.50 tl")
                SellingPrice.set("12.99 tl")
                DaysOnLoan.set(14)
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=14)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "Da Vinci Şifresi"):
                BookISBN.set("ISBN 333875898")
                BookTitle.set("Da Vinci Şifresi")
                Author.set("Dan Brown")
                LateReturnFine.set("2.50 tl")
                SellingPrice.set("12.99 tl")
                DaysOnLoan.set(7)
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=7)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "Düşün ve Zengin Ol"):
                BookISBN.set("ISBN 125111232")
                BookTitle.set("Düşün ve Zengin Ol")
                Author.set("Napoleon Hill")
                LateReturnFine.set("2.50 tl")
                SellingPrice.set("12.99 tl")
                DaysOnLoan.set(14)
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=14)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif (w == "Çavdar Tarlasında Çocuklar"):
                BookISBN.set("ISBN 125875898")
                BookTitle.set("Çavdar Tarlasında Çocuklar")
                Author.set("J.D.Salınger")
                LateReturnFine.set("2.50 tl")
                SellingPrice.set("12.99 tl")
                DaysOnLoan.set(14)
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=14)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
            elif (w == "Simyacı"):
                BookISBN.set("ISBN 167875123")
                BookTitle.set("Simyacı")
                Author.set("Paulo Coelho")
                LateReturnFine.set("2.50 tl")
                SellingPrice.set("12.99 tl")
                DaysOnLoan.set(20)
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=20)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")




        self.lblMemberType = Label(DataFrameLEFT, font=("arial", 12, "bold"),text="MemberType", padx=2,pady=2)
        self.lblMemberType.grid(row=0, column=0, sticky=W)
        self.cboMemberType=ttk.Combobox(DataFrameLEFT,textvariable=MType,state="readonly",font=("arial", 12, "bold"),width=34)
        self.cboMemberType["value"]=("","Student","Lecturer","Admin Staff")
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0,column=1)

        self.lblBookISBN = Label(DataFrameLEFT, font=("arial", 12, "bold"),text="Book ID", padx=2,pady=2)
        self.lblBookISBN.grid(row=0, column=2, sticky=W)
        self.txtBookISBN=Entry(DataFrameLEFT,font=("arial", 12, "bold"),textvariable=BookISBN,width=31)
        self.txtBookISBN.grid(row=0,column=3)

        self.lblMemberRef = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Member Ref No:", padx=2, pady=2)
        self.lblMemberRef.grid(row=1, column=0, sticky=W)
        self.txtMemberRef = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=Member, width=36)
        self.txtMemberRef.grid(row=1, column=1)

        self.lblBookTitle = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Book Title:", padx=2, pady=2)
        self.lblBookTitle.grid(row=1, column=2, sticky=W)
        self.txtBookTitle = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=BookTitle, width=31)
        self.txtBookTitle.grid(row=1, column=3)

        self.lblTitle = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Title:", padx=2, pady=2)
        self.lblTitle.grid(row=2, column=0, sticky=W)

        self.cboTitle = ttk.Combobox(DataFrameLEFT, textvariable=Title, state="readonly",font=("arial", 12, "bold"), width=34)
        self.cboTitle["value"]=("","Mr.","Miss.","Mrs.","Dr.","Capt.","Ms.")
        self.cboTitle.current(0)
        self.cboTitle.grid(row=2,column=1)

        self.lblAuthor = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Author", padx=2, pady=2)
        self.lblAuthor.grid(row=2, column=2, sticky=W)
        self.txtAuthor = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=Author, width=31)
        self.txtAuthor.grid(row=2, column=3)

        self.lblFirstname = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Firstname", padx=2, pady=2)
        self.lblFirstname.grid(row=3, column=0, sticky=W)
        self.txtFirstname = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=Firstname, width=36)
        self.txtFirstname.grid(row=3, column=1)

        self.lblDataBorrowed = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Date Borrowed", padx=2, pady=2)
        self.lblDataBorrowed.grid(row=3, column=2, sticky=W)
        self.txtDataBorrowed = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=DateBorrowed, width=31)
        self.txtDataBorrowed.grid(row=3, column=3)

        self.lblSurname = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Surname", padx=2, pady=6)
        self.lblSurname.grid(row=4, column=0, sticky=W)
        self.txtSurname = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=Surname, width=36)
        self.txtSurname.grid(row=4, column=1)

        self.lblDateDue = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Date Due", padx=2, pady=2)
        self.lblDateDue.grid(row=4, column=2, sticky=W)
        self.txtDateDue = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=DateDue, width=31)
        self.txtDateDue.grid(row=4, column=3)

        self.lblAdress1 = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Address1:", padx=2, pady=2)
        self.lblAdress1.grid(row=5, column=0, sticky=W)
        self.txtAdress1 = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=Address, width=36)
        self.txtAdress1.grid(row=5, column=1)

        self.lblDaysOnLoan = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Days on Loan:", padx=2, pady=2)
        self.lblDaysOnLoan.grid(row=5, column=2, sticky=W)
        self.txtDaysOnLoan = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=DaysOnLoan, width=31)
        self.txtDaysOnLoan.grid(row=5, column=3)

        self.lblAddress2 = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Address 2:", padx=2, pady=2)
        self.lblAddress2.grid(row=6, column=0, sticky=W)
        self.txtAdress2= Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=Address2, width=36)
        self.txtAdress2.grid(row=6, column=1)

        self.lblLateReturnFine = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Late Return Fine", padx=2, pady=6)
        self.lblLateReturnFine.grid(row=6, column=2, sticky=W)
        self.txtLateReturnFine = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=LateReturnFine, width=31)
        self.txtLateReturnFine.grid(row=6, column=3)

        self.lblPostCode = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Post Code:", padx=2, pady=2)
        self.lblPostCode.grid(row=7, column=0, sticky=W)
        self.txtPostCode = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=PostCode, width=36)
        self.txtPostCode.grid(row=7, column=1)

        self.lblSurname = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Date Over Due:", padx=2, pady=2)
        self.lblSurname.grid(row=7, column=2, sticky=W)
        self.txtSurname = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=DateOverDue, width=31)
        self.txtSurname.grid(row=7, column=3)

        self.lblMobileNo = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Mobile No:", padx=2, pady=2)
        self.lblMobileNo.grid(row=8, column=0, sticky=W)
        self.txtMobileNo = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=MobileNo, width=36)
        self.txtMobileNo.grid(row=8, column=1)

        self.lblSellingPrice = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Selling Price:", padx=2, pady=2)
        self.lblSellingPrice.grid(row=8, column=2, sticky=W)
        self.txtSellingPrice = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=SellingPrice, width=31)
        self.txtSellingPrice.grid(row=8, column=3)

        cal=Calendar(DataFrameRIGHT,selectmode="day",year=2021,month=10,day=18,date_pattern="yyyy-mm-dd",font=("arial", 12, "bold"),padx=10)
        cal.grid(row=0,column=0,pady=10)

        scrollbar=Scrollbar(DataFrameRIGHT,orient=VERTICAL)
        scrollbar.grid(row=1,column=1,sticky="ns")
        ListOfBooks=["İki Şehrin Hikayesi","Yüzüklerin Efendisi","Hobbit","Küçük Prens","Harry Potter ve Felsefe Taşı","On Küçük Zenci","Kızıl Köşkün Rüyası","Ayişe","Aslan, Cadı ve Dolap","Da Vinci Şifresi","Düşün ve Zengin Ol","Çavdar Tarlasında Çocuklar","Simyacı"]

        booklist=Listbox(DataFrameRIGHT,width=40,height=12,font=("times",11,"bold"),yscrollcommand=scrollbar.set)
        booklist.bind('<<ListboxSelect>>',SelectedBook)
        booklist.grid(row=1,column=0,padx=3)
        scrollbar.config(command=booklist.yview)
        for items in ListOfBooks:
            booklist.insert(END,items)

        scroll_x=Scrollbar(DataFrameLEFTb,orient=HORIZONTAL)
        scroll_y=Scrollbar(DataFrameLEFTb,orient=VERTICAL)
        self.library_records=ttk.Treeview(DataFrameLEFTb,height=5,columns=("member","firstname","surname","address","dateborrowed","datedue","dayoverdue","author","bookisbn","booktitle"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        self.library_records.heading("member",text="Member")
        self.library_records.heading("firstname", text="Firstname")
        self.library_records.heading("surname", text="Surname")
        self.library_records.heading("address", text="Address")
        self.library_records.heading("dateborrowed", text="Date Borrowed")
        self.library_records.heading("datedue", text="Date Due")
        self.library_records.heading("dayoverdue", text="Days Over Due")
        self.library_records.heading("author", text="Author")
        self.library_records.heading("bookisbn", text="Book ISBN")
        self.library_records.heading("booktitle", text="Book Title")
        self.library_records["show"]="headings"
        self.library_records.column("member",width=70)
        self.library_records.column("firstname", width=100)
        self.library_records.column("surname", width=100)
        self.library_records.column("address", width=100)
        self.library_records.column("dateborrowed", width=70)
        self.library_records.column("datedue", width=70)
        self.library_records.column("dayoverdue", width=100)
        self.library_records.column("author", width=100)
        self.library_records.column("bookisbn", width=70)
        self.library_records.column("booktitle", width=70)

        self.library_records.pack(fill=BOTH,expand=1)
        self.library_records.bind("<ButtonRelease-1>")
        self.btnDisplayData=Button(ButtonFrame,text="Display Data",font=("arial",19,"bold"),padx=4,width=16,bd=4,bg="pink",command=addData)
        self.btnDisplayData.grid(row=0,column=0,padx=3)
        self.btnDelete = Button(ButtonFrame, text="Delete", font=("arial", 19, "bold"), padx=4, width=16,bd=4, bg="pink",command=DeleteDB)
        self.btnDelete.grid(row=0, column=1, padx=3)
        self.btnReset = Button(ButtonFrame, text="Reset", font=("arial", 19, "bold"), padx=4, width=16,bd=4, bg="pink",command=iReset)
        self.btnReset.grid(row=0, column=2, padx=3)
        self.btnExit = Button(ButtonFrame, text="Exit", font=("arial", 19, "bold"), padx=4, width=16,bd=4, bg="pink",command=iExit)
        self.btnExit.grid(row=0, column=3, padx=3)


if __name__ == '__main__':
    root=Tk()
    application=Library(root)
    root.mainloop()