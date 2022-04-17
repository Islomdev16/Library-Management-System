from tkinter import *
from tkinter import ttk
import mysql.connector

class Library:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1920x930+0+0")
        self.root.resizable(False, False)

        # ========================= Variables Section ==========================================
        self.number_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook = StringVar()
        self.lateratefine_var = StringVar()
        self.dateoverdue = StringVar()
        self.finalprice = StringVar()

        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=3, y=130, width=1915, height=439)

        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg="green", bd=15, relief=RIDGE, font=("times new roman", 19, "bold"), padx=2, pady=6)
        DataFrameLeft.place(x=15, y=10, width=1080, height=394)

        lblMember = Label(DataFrameLeft, bg="powder blue", text="     Member Type   ", font=("arial", 15, "bold"), padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, font=("arial", 16, "bold"), width=21, state="readonly")
        comMember["value"] = ("Admin Staff", "Student", "Lecturer")
        comMember.current(0)
        comMember.grid(row=0, column=1, sticky=W)

        lblPRN_NO = Label(DataFrameLeft, bg="powder blue", text="     PRN NO :", font=("arial", 15, "bold"), padx=2)
        lblPRN_NO.grid(row=1, column=0, sticky=W)
        txtTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtTitle.grid(row=1, column=1, sticky=W)

        lblTitle = Label(DataFrameLeft, bg="powder blue", text="     ID No :  ", font=("arial", 15, "bold"), padx=2, pady=6)
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtTitle.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, bg="powder blue", text="     First Name :  ", font=("arial", 15, "bold"), padx=2, pady=6)
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, bg="powder blue", text="     Last Name :  ", font=("arial", 15, "bold"), padx=2, pady=6)
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtLastName.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, bg="powder blue", text="     Address1 :  ", font=("arial", 15, "bold"), padx=2, pady=6)
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtAddress1.grid(row=5, column=1)

        lblAddress2 = Label(DataFrameLeft, bg="powder blue", text="     Address2 :  ", font=("arial", 15, "bold"), padx=2, pady=6)
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtAddress2.grid(row=6, column=1)

        lblPostCode = Label(DataFrameLeft, bg="powder blue", text="     Post Code :  ", font=("arial", 15, "bold"), padx=2, pady=6)
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtPostCode.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, bg="powder blue", text="     Mobile Number :  ", font=("arial", 15, "bold"), padx=2, pady=6)
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtMobile.grid(row=8, column=1)

        lblBookId = Label(DataFrameLeft, font=("arial", 15, "bold"), text="               Book ID :    ", padx=2, bg="powder blue")
        lblBookId.grid(row=0, column=2, sticky=W)
        txtBookId = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtBookId.grid(row=0, column=3)

        lblBookTitle = Label(DataFrameLeft, font=("arial", 15, "bold"), text="               Book Title :    ", padx=2, pady=6, bg="powder blue")
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtBookTitle.grid(row=1, column=3)

        lblAuthor = Label(DataFrameLeft, font=("arial", 15, "bold"), text="               Author Name :    ", padx=2, pady=6, bg="powder blue")
        lblAuthor.grid(row=2, column=2, sticky=W)
        txtAuthor = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtAuthor.grid(row=2, column=3)

        lblDateBorrowed = Label(DataFrameLeft, font=("arial", 15, "bold"), text="               Date Borrowed :    ", padx=2, pady=6, bg="powder blue")
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtDateBorrowed.grid(row=3, column=3)

        lblDateDue = Label(DataFrameLeft, font=("arial", 15, "bold"), text="               Date Due :    ", padx=2, pady=6, bg="powder blue")
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtDateDue.grid(row=4, column=3)

        lblDaysOnBook = Label(DataFrameLeft, font=("arial", 15, "bold"), text="               Days On Book :   ", padx=2, pady=6, bg="powder blue")
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtDaysOnBook.grid(row=5, column=3)

        lblLateReturnFine = Label(DataFrameLeft, font=("arial", 15, "bold"), text="               Late Return Fine :   ", padx=2, pady=6, bg="powder blue")
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtLateReturnFine.grid(row=6, column=3)

        lblDateOverdate = Label(DataFrameLeft, font=("arial", 15, "bold"), text="               Date Over Due :   ", padx=2, pady=6, bg="powder blue")
        lblDateOverdate.grid(row=7, column=2, sticky=W)
        txtDateOverdate = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtDateOverdate.grid(row=7, column=3)

        lblActualPrice = Label(DataFrameLeft, font=("arial", 15, "bold"), text="               Actual Price :  ", padx=2, pady=6, bg="powder blue")
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtActualPrice.grid(row=8, column=3)

        # ========================= DataFrame Right Section =======================================

        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue", fg="green", bd=15,
                                   relief=RIDGE, font=("arial", 19, "bold"), padx=2, pady=6)
        DataFrameRight.place(x=1150, y=10, width=685, height=394)

        self.txtBox = Text(DataFrameRight, font=("arial", 19, "bold"), width=23, height=17, padx=1, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")

        listBooks = ["In Search of Lost Time ", "Ulysses", "Don Quixote", "One Hundred Years of Solitude", "The Great Gatsby", "Moby Dick",
                     "War and Peace", "Hamlet", "The Odyssey", "Madame Bovary", "The Divine Comedy", "Lolita", "The Brothers Karamazov",
                     "Crime and Punishment", "Wuthering Heights", "The Catcher in the Rye", "Pride and Prejudice", "The Adventures of Huckleberry Finn", "Alice's Adventures in Wonderland", "The Iliad", "To the Lighthouse",
                     "Heart of Darkness", "The Sound and the Fury", "Great Expectations", "The Grapes of Wrath", "Invisible Man "]

        listBox = Listbox(DataFrameRight, font=("arial", 15, "bold"), width=26, height=20)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END, item)

        # ======================= BUTTON FRAME SECTION ======================
        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=571, width=1920, height=85)

        btnAddDate = Button(Framebutton, text="Add Data", font=("arial", 15, "bold"), width=23, bg="blue", fg="white")
        btnAddDate.grid(row=0, column=0, ipady=6, ipadx=6, padx=7, pady=5)

        btnShowData = Button(Framebutton, text="Show Data", font=("arial", 15, "bold"), width=23, bg="blue", fg="white")
        btnShowData.grid(row=0, column=1, ipady=6, ipadx=6, padx=7, pady=5)

        btnUpdate = Button(Framebutton, text="Update", font=("arial", 15, "bold"), width=23, bg="blue", fg="white")
        btnUpdate.grid(row=0, column=2, ipady=6, ipadx=6, padx=7, pady=5)

        btnDelete = Button(Framebutton, text="Delete", font=("arial", 15, "bold"), width=23, bg="blue", fg="white")
        btnDelete.grid(row=0, column=3, ipady=6, ipadx=6, padx=7, pady=5)

        btnReset = Button(Framebutton, text="Reset", font=("arial", 15, "bold"), width=23, bg="blue", fg="white")
        btnReset.grid(row=0, column=4, ipady=6, ipadx=6, padx=7, pady=5)

        btnExit = Button(Framebutton, text="Exit", font=("arial", 15, "bold"), width=23, bg="blue", fg="white")
        btnExit.grid(row=0, column=5, ipady=6, ipadx=6, padx=7, pady=5)

        # ======================= INFORMATION FRAME SECTION ======================
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=657, width=1920, height=272)

        Table_frame = Frame(FrameDetails, bd=6, relief=RIDGE, bg="powder blue")
        Table_frame.place(x=0, y=5, width=1859, height=220)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)
        self.library_table = ttk.Treeview(Table_frame, columns=("membertype", "prnno", "title", "firstname", "lastname", "address1",
                                                                "address2", "postId", "mobile", "bookId", "booktitle", "author", "dateBorrowed",
                                                                "datedue", "days", "LateReturnFine", "DateoverDue", "Finalprice"), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("prnno", text="PRN No.")
        self.library_table.heading("title", text="Title")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address1", text="Address1")
        self.library_table.heading("address2", text="Address2")
        self.library_table.heading("postId", text="Post ID")
        self.library_table.heading("mobile", text="Mobile Number")
        self.library_table.heading("bookId", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("dateBorrowed", text="Date Of Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="DaysOnBook")
        self.library_table.heading("LateReturnFine", text="LateReturnFine")
        self.library_table.heading("DateoverDue", text="DateOverDue")
        self.library_table.heading("Finalprice", text="Final Price")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

if __name__ == "__main__":
    root = Tk()
    obj = Library(root)
    root.mainloop()


