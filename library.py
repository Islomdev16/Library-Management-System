from tkinter import *
from tkinter import ttk

class Library:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1920x930+0+0")
        self.root.resizable(False, False)

        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=3, y=130, width=1915, height=439)

        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg="green", bd=15, relief=RIDGE, font=("times new roman", 19, "bold"), padx=2, pady=6)
        DataFrameLeft.place(x=15, y=10, width=1080, height=388)

        lblMember = Label(DataFrameLeft, bg="powder blue", text="       Member Type   ", font=("arial", 15, "bold"), padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, font=("arial", 16, "bold"), width=21, state="readonly")
        comMember["value"] = ("Admin Staff", "Student", "Lecturer")
        comMember.current(0)
        comMember.grid(row=0, column=1, sticky=W)

        lblPRN_NO = Label(DataFrameLeft, bg="powder blue", text="       PRN NO :", font=("arial", 15, "bold"), padx=2)
        lblPRN_NO.grid(row=1, column=0, sticky=W)
        txtTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtTitle.grid(row=1, column=1, sticky=W)

        lblTitle = Label(DataFrameLeft, bg="powder blue", text="       ID No :  ", font=("arial", 15, "bold"), padx=2, pady=6)
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtTitle.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, bg="powder blue", text="       First Name :  ", font=("arial", 15, "bold"), padx=2, pady=6)
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, bg="powder blue", text="       Last Name :  ", font=("arial", 15, "bold"), padx=2, pady=6)
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtLastName.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, bg="powder blue", text="       Address1 :  ", font=("arial", 15, "bold"), padx=2, pady=6)
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtAddress1.grid(row=5, column=1)

        lblAddress2 = Label(DataFrameLeft, bg="powder blue", text="       Address2 :  ", font=("arial", 15, "bold"), padx=2, pady=6)
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtAddress2.grid(row=6, column=1)

        lblPostCode = Label(DataFrameLeft, bg="powder blue", text="       Post Code :  ", font=("arial", 15, "bold"), padx=2, pady=6)
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtPostCode.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, bg="powder blue", text="       Mobile Number :  ", font=("arial", 15, "bold"), padx=2, pady=6)
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtMobile.grid(row=8, column=1)

        lblBookId = Label(DataFrameLeft, font=("arial", 15, "bold"), text="                   Book ID :    ", padx=2, bg="powder blue")
        lblBookId.grid(row=0, column=2, sticky=W)
        txtBookId = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=26)
        txtBookId.grid(row=0, column=3)




        DataFrameLeft = LabelFrame(frame, text="Book Details", bg="powder blue", fg="green", bd=15,
                                   relief=RIDGE, font=("times new roman", 19, "bold"), padx=2, pady=6)
        DataFrameLeft.place(x=1185, y=10, width=670, height=388)


        # ======================= BUTTON FRAME SECTION ======================
        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=571, width=1920, height=85)

        # ======================= INFORMATION FRAME SECTION ======================
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=657, width=1920, height=272)




if __name__ == "__main__":
    root = Tk()
    obj = Library(root)
    root.mainloop()


