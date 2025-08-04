from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from customer import Customer
from room import Room
from details import Details

class HotelManagementSystem:

    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")


        # _________first Image______
        image1=Image.open(r"D:\PROJECT\HotelManagementSystem\images\hotel1.png")
        img1 = image1.resize((1550,140),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root,image=self.photoimg1,bd=4,relief=RAISED)
        lblimg.place(x=0,y=0,width=1550,height=140)
        
        # ____________logo__________
        image2=Image.open(r"D:\PROJECT\HotelManagementSystem\images\logohotel.png")
        img2 = image2.resize((230,140),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=4,relief=RAISED)
        lblimg.place(x=0,y=0,width=230,height=140)
       
       #------------TiTle---------------
        lbl_title = Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RAISED )
        lbl_title.place(x=0,y=140,width=1550,height=50)

       #--------------main Frame----------
        mainframe = Frame(self.root,bd=4,relief=RAISED)
        mainframe.place(x=0,y=190,width=1550,height=620)
       #------------menu label-----------
        lbl_title = Label(mainframe,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RAISED )
        lbl_title.place(x=0,y=0,width=230)
       #---------button frame-------------
        btnframe = Frame(mainframe,bd=4,relief=RAISED)
        btnframe.place(x=0,y=35,width=228,height=190) 

        cust_btn = Button(btnframe,width=22,text="CUSTOMER",command=self.cust_detail,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2") 
        cust_btn.grid(row=0,column=0,pady=1)
        room_btn = Button(btnframe,width=22,text="ROOM",command=self.room_detail,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2") 
        room_btn.grid(row=1,column=0,pady=1)
        detail_btn = Button(btnframe,width=22,text="DETAILS",command=self.details,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2") 
        detail_btn.grid(row=2,column=0,pady=1)
        report_btn = Button(btnframe,width=22,text="REPORT",font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2") 
        report_btn.grid(row=3,column=0,pady=1)
        logout_btn = Button(btnframe,width=22,text="LOGOUT",font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2") 
        logout_btn.grid(row=4,column=0,pady=1)

        #--------------right side imge-------------
        image3=Image.open(r"D:\PROJECT\HotelManagementSystem\images\slide3.jpg")
        img3 = image3.resize((1310,590),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(mainframe,image=self.photoimg3,bd=4,relief=RAISED)
        lblimg.place(x=225,y=0,width=1310,height=590)

        #------------menu down image----------       
        image4=Image.open(r"D:\PROJECT\HotelManagementSystem\images\myh.jpg")
        img4 = image4.resize((230,210),Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg = Label(mainframe,image=self.photoimg4,bd=4,relief=RAISED)
        lblimg.place(x=0,y=225,width=230,height=210) 

        image5=Image.open(r"D:\PROJECT\HotelManagementSystem\images\khana.jpg")
        img5 = image5.resize((230,190),Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg = Label(mainframe,image=self.photoimg5,bd=4,relief=RAISED)
        lblimg.place(x=0,y=420,width=230,height=190)
 
    def cust_detail(self):
        self.new_window = Toplevel(self.root) 
        self.app = Customer(self.new_window)

    def room_detail(self):
        self.new_window = Toplevel(self.root) 
        self.app = Room(self.new_window)
    
    def details(self):
        self.new_window = Toplevel(self.root) 
        self.app = Details(self.new_window)
    
    

if __name__=="__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()