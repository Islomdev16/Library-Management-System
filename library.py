from tkinter import *

class Library:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1920x1015+0+0")
        self.root.resizable(False, False)

        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=3, y=130, width=1915, height=460)

        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg="green", bd=15, relief=RIDGE, font=("times new roman", 19, "bold"), padx=2, pady=6)
        DataFrameLeft.place(x=0, y=5, width=1175, height=370)

        DataFrameLeft = LabelFrame(frame, text="Book Details", bg="powder blue", fg="green", bd=15,
                                   relief=RIDGE, font=("times new roman", 19, "bold"), padx=2, pady=6)
        DataFrameLeft.place(x=1185, y=5, width=670, height=370)


        # ======================= BUTTON FRAME SECTION ======================
        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1915, height=70)

        # ======================= INFORMATION FRAME SECTION ======================
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=600, width=1915, height=460)




if __name__ == "__main__":
    root = Tk()
    obj = Library(root)
    root.mainloop()


