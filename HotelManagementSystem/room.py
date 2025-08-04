from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import re
import random
import mysql.connector
from time import strftime
from datetime import datetime
from tkcalendar import DateEntry
from details import Details

class Room:
    
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x580+230+220")

        # ============ Variables ===============
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_days = StringVar()
        self.var_tax = StringVar()
        self.var_actualTotal = StringVar()
        self.var_total = StringVar()

       #------------TiTle---------------
        lbl_title = Label(self.root,text="ROOM BOOKING DETAILS ",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RAISED )
        lbl_title.place(x=0,y=0,width=1295,height=50) 
        # ____________logo__________
        image2=Image.open(r"D:\PROJECT\HotelManagementSystem\images\logohotel.png")
        img2 = image2.resize((100,40),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root,image=self.photoimg2,bd=0,relief=RAISED)
        lblimg.place(x=5,y=2,width=100,height=40)  

       #================Label Frame================
        labelframeleft =  LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #=============Label and Entry===============
        #customer contact
        lbl_cust_contact = Label(labelframeleft,text="Costomer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        entry_contact = ttk.Entry(labelframeleft, textvariable=self.var_contact,width=20,font=("arial",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

         # button fetch data
        btnFetchData = Button(labelframeleft,command=self.fetch_contact,font=("arial",8,"bold"),bg='black',fg='gold',text="Fetch Data",width=8)
        btnFetchData.place(x=347,y=4)

        # Check_in Date
        lbl_check_in= Label(labelframeleft,text="Check-in Date:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_check_in.grid(row=1,column=0,sticky=W)
        entry_check_in = DateEntry(labelframeleft,textvariable=self.var_checkin, width=25,font=("arial",13,"bold"),date_pattern="dd/mm/yyyy")
        entry_check_in.grid(row=1,column=1)

        #chech_out Date
        lbl_check_out = Label(labelframeleft,text="Check-out Date:",font=("arial",12,"bold"),padx=2,pady=3)
        lbl_check_out.grid(row=2,column=0,sticky=W)
        entry_check_out = DateEntry(labelframeleft,textvariable=self.var_checkout, width=25,font=("arial",13,"bold"),date_pattern='dd/mm/yyyy')
        entry_check_out.grid(row=2,column=1)

        # Room Type
        lbl_check_out = Label(labelframeleft, text="Room Type:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_check_out.grid(row=3, column=0, sticky=W)

        combo_roomType = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype, font=("arial", 12, "bold"), width=25, state='readonly')
        combo_roomType.grid(row=3, column=1)

        # Fetch distinct room types
        conn = mysql.connector.connect(host="localhost", username="root", password="Anoop@123", database="management")
        mycursor = conn.cursor()
        mycursor.execute("SELECT DISTINCT roomtype FROM details")
        roomtypes = [row[0] for row in mycursor.fetchall()]
        combo_roomType['values'] = roomtypes
        conn.close()

        # Available Room Label
        lbl_avlRoom = Label(labelframeleft, font=("arial", 12, "bold"), text="Available room:", padx=2, pady=6)
        lbl_avlRoom.grid(row=4, column=0, sticky=W)

        combo_avlRoom = ttk.Combobox(labelframeleft, textvariable=self.var_roomavailable, font=("arial", 12, "bold"), width=25, state='readonly')
        combo_avlRoom.grid(row=4, column=1)

        # Function to update available rooms based on room type
        def update_available_rooms(event=None):
            selected_type = self.var_roomtype.get()
            conn = mysql.connector.connect(host="localhost", username="root", password="Anoop@123", database="management")
            mycursor = conn.cursor()
            query = "SELECT roomno FROM details WHERE roomtype = %s"
            mycursor.execute(query, (selected_type,))
            available_rooms = [row[0] for row in mycursor.fetchall()]
            combo_avlRoom['values'] = available_rooms
            if available_rooms:
                combo_avlRoom.current(0)
            conn.close()

        # Bind room type selection event
        combo_roomType.bind("<<ComboboxSelected>>", update_available_rooms)

        
        #Meal
        lbl_meal = Label(labelframeleft,font=("arial",12,"bold"),text="Meal:",padx=2,pady=6)
        lbl_meal.grid(row=5,column=0,sticky=W)

        combo_meal = ttk.Combobox(labelframeleft,textvariable=self.var_meal,font=("arial",12,"bold"),width=25,state='readonly')
        combo_meal['value'] = ("BreakFast","Lunch","Dinner")
        combo_meal.current(0)
        combo_meal.grid(row=5,column=1)

        #Number of days
        lbl_days = Label(labelframeleft,font=("arial",12,"bold"),text="No of Days:",padx=2,pady=6)
        lbl_days.grid(row=6,column=0,sticky=W)

        entry_days = ttk.Entry(labelframeleft,textvariable=self.var_days,font=("arial",12,"bold"),width=25)
        entry_days.grid(row=6,column=1)

        #paid tax
        lbl_tax = Label(labelframeleft,font=("arial",12,"bold"),text="Paid Tax:",padx=2,pady=6)
        lbl_tax.grid(row=7,column=0,sticky=W)

        entry_tax=ttk.Entry(labelframeleft,textvariable=self.var_tax,font=("arial",12,"bold"),width=25)
        entry_tax.grid(row=7,column=1)

        #SUb Total
        lbl_subTotal = Label(labelframeleft,font=("arial",12,"bold"),text="Sub Total:",padx=2,pady=6)
        lbl_subTotal.grid(row=8,column=0,sticky=W)

        entry_subTotal = ttk.Entry(labelframeleft,textvariable=self.var_actualTotal,font=("arial",12,"bold"),width=25)
        entry_subTotal.grid(row=8,column=1)

        # Total Cost
        lbl_TotalCost = Label(labelframeleft,font=("arial",12,"bold"),text="Total Cost:",padx=2,pady=6)
        lbl_TotalCost.grid(row=9,column=0,sticky=W)

        entry_TotalCost = ttk.Entry(labelframeleft,textvariable=self.var_total,font=("arial",12,"bold"),width=25)
        entry_TotalCost.grid(row=9,column=1)

        #==========BILL Button==========
        btnBill = Button(labelframeleft,text="Bill",command=self.total,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

        btnprint = Button(labelframeleft,text="🖨Print",font=("arial",12,"bold"),bg="black",fg="white",width=10)
        btnprint.grid(row=10,column=1,padx=1)

        #=============== Buttons ===================
        btn_frame = Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)
        #Add
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10,cursor="hand2")
        btnAdd.grid(row=0,column=0,padx=1)
        #Update
        btnUpdate=Button(btn_frame,text="Update",command=self.update_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10,cursor="hand2")
        btnUpdate.grid(row=0,column=1,padx=1)
        #Delete
        btnDelete=Button(btn_frame,text="Delete",command=self.delete_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10,cursor="hand2")
        btnDelete.grid(row=0,column=2,padx=1)
         #reset
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10,cursor="hand2")
        btnReset.grid(row=0,column=3,padx=1)

        #============= Right side Image =================
        image3=Image.open(r"D:\PROJECT\HotelManagementSystem\images\bed.jpg")
        img3 = image3.resize((520,200),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root,image=self.photoimg3,bd=0,relief=RAISED)
        lblimg.place(x=760,y=55,width=520,height=200)

        #================== Table label Frame search =======================
        Tableframe =  LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"),padx=2)
        Tableframe.place(x=435,y=280,width=860,height=260)

        lblSearch = Label(Tableframe,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearch.grid(row=0,column=0,sticky=W,padx=2,pady=5)
        
        self.var_search = StringVar()
        combo_search = ttk.Combobox(Tableframe,textvariable=self.var_search,font=("arial",12,"bold"),width=24,state="readonly",cursor="hand2")
        combo_search["value"]=("Contact","roomavailable")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
        
        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Tableframe,width=24,textvariable=self.txt_search,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Tableframe,text="Search",command=self.search_data,font=("arial",11,"bold"),bg="green",fg="white",width=10,cursor="hand2")
        btnSearch.grid(row=0,column=3,padx=1)

        btnShow=Button(Tableframe,text="Show All",font=("arial",11,"bold"),command=self.fetch_data,bg="green",fg="white",width=10,cursor="hand2")
        btnShow.grid(row=0,column=4,padx=1)

        #================== Scroll Show Data Frame ===============
        details_frame = Frame(Tableframe,bd=2,relief=RIDGE)
        details_frame.place(x=0,y=50,width=860,height=180)

        scroll_x = ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_frame,orient=VERTICAL)
        
        self.room_details = ttk.Treeview(details_frame,columns=("contact","checkin","checkout","roomtype","roomavailable","meal","days" ),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_details.xview)
        scroll_y.config(command=self.room_details.yview)

        self.room_details.heading("contact",text="Contact")
        self.room_details.heading("checkin",text="Check-In")
        self.room_details.heading("checkout",text="Check-out")
        self.room_details.heading("roomtype",text="Room type")
        self.room_details.heading("roomavailable",text="Room No")
        self.room_details.heading("meal",text="Meal")
        self.room_details.heading("days",text="No_Of_Days")
        
     
       
        self.room_details["show"]="headings"

        self.room_details.column("contact",width=100,anchor="center")
        self.room_details.column("checkin",width=100,anchor="center")
        self.room_details.column("checkout",width=100,anchor="center")
        self.room_details.column("roomtype",width=100,anchor="center")
        self.room_details.column("meal",width=100,anchor="center")
        self.room_details.column("roomavailable",width=100,anchor="center")
        self.room_details.column("days",width=100,anchor="center")
       

        self.room_details.pack(fill=BOTH,expand=1)
        self.room_details.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

#======= Add data   ========
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
           messagebox.showerror("Error"," All fields are required ",parent=self.root)
        
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Anoop@123",database="management")
                mycursor = conn.cursor()
                mycursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                self.var_contact.get(),
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_days.get()
               
                       ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)
# =============Fetch Data ======================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Anoop@123",database="management")
        mycursor = conn.cursor()

        mycursor.execute("select * from room")
        rows = mycursor.fetchall()

        if len(rows)!=0:
            self.room_details.delete(*self.room_details.get_children())

            for i in rows:
                self.room_details.insert("",END,values=i)

            conn.commit()
        conn.close()



#=========== Get Cursor ==============
    def get_cursor(self,event=""):
        cursor_row = self.room_details.focus()
        content = self.room_details.item(cursor_row)
        row = content["values"]
        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_days.set(row[6])


#=========== Update ==================
    def update_data(self): 
      try:
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="Anoop@123",database="management")
            mycursor = conn.cursor()
            mycursor.execute("UPDATE room SET check_in=%s, check_out=%s, roomtype=%s,roomavailable=%s, meal=%s, days=%s WHERE contact=%s",(
                
               
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_days.get(),
                self.var_contact.get()
            ))
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated succesfully ",parent=self.root)
      except:
          messagebox.showerror("Error","-- Duplicate room -- ",parent=self.root)
#=========== Delete ===========================
    def delete_data(self):
        delete_data=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if delete_data>0:
            conn = mysql.connector.connect(host="localhost",username="root",password="Anoop@123",database="management")
            mycursor = conn.cursor()
            query = "delete from room where roomavailable=%s"
            value =(self.var_roomavailable.get(),)
            mycursor.execute(query,value)

        else:
            if not delete_data:
                return
        
        conn.commit()
        self.fetch_data()
        conn.close()
#============ reset ================
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        # self.var_roomtype.set(""),
        # self.var_roomavailable.set(""),
        # self.var_meal.set(""),
        self.var_days.set("")
        self.var_actualTotal.set("")
        self.var_tax.set("")
        self.var_total.set("")
#=========== fetch contact ============================
    def fetch_contact(self):
          if self.var_contact.get()=="":
               messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)

          else:
            conn = mysql.connector.connect(host="localhost",username="root",password="Anoop@123",database="management")
            mycursor = conn.cursor()

            query = ("select name from customer where mobile=%s")
            value=(self.var_contact.get(),)
            mycursor.execute(query,value)
            row = mycursor.fetchone()
            if row==None:
                messagebox.showerror("Eroor","This number is not found",parent = self.root)
            else:
                conn.commit()
                conn.close()

                showDataFrame = LabelFrame(self.root,text="Customer",bd=4,relief=RIDGE,padx=2)
                showDataFrame.place(x=450, y=55,width=300,height=200)
                #Name
                labelName = Label(showDataFrame,text="Name : ",font=("arial",12,"bold"))
                labelName.place(x=0,y=0)

                lbl = Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)
               #Gender
                conn = mysql.connector.connect(host="localhost",username="root",password="Anoop@123",database="management")
                mycursor = conn.cursor()

                query = ("select gender from customer where mobile=%s")
                value=(self.var_contact.get(),)
                mycursor.execute(query,value)
                row = mycursor.fetchone()

                labelGender = Label(showDataFrame,text="Gender : ",font=("arial",12,"bold"))
                labelGender.place(x=0,y=30)

                lbl2 = Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)  
                
                #Email
                query = ("select email from customer where mobile=%s")
                value=(self.var_contact.get(),)
                mycursor.execute(query,value)
                row = mycursor.fetchone()

                labelEmail = Label(showDataFrame,text="Email : ",font=("arial",12,"bold"))
                labelEmail.place(x=0,y=60)

                lbl3 = Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)

                # Nationality
                query = ("select nationality from customer where mobile=%s")
                value=(self.var_contact.get(),)
                mycursor.execute(query,value)
                row = mycursor.fetchone()

                labelEmail = Label(showDataFrame,text="Nationality : ",font=("arial",12,"bold"))
                labelEmail.place(x=0,y=90)

                lbl3 = Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=90)

                # Adress
                query = ("select adress from customer where mobile=%s")
                value=(self.var_contact.get(),)
                mycursor.execute(query,value)
                row = mycursor.fetchone()

                labelEmail = Label(showDataFrame,text="Address : ",font=("arial",12,"bold"))
                labelEmail.place(x=0,y=120)

                lbl3 = Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=120)

                

#=============== Search ==================
    def search_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Anoop@123",database="management")
        mycursor = conn.cursor()
        mycursor.execute("select * from room where "+str(self.var_search.get())+" LIKE '%"+str(self.txt_search.get())+"%'")

        row = mycursor.fetchall()

        if len(row)!=0:
            self.room_details.delete(*self.room_details.get_children())
            for i in row:
                self.room_details.insert("",END,values=i)
            conn.commit()
        
        conn.close()
#=============bill====================

    def total(self):
        prices ={"Single":float(300),"Double":float(400),"Luxury":float(900),"Duplex":float(500),
             "BreakFast":float(200),"Lunch":float(300),"Dinner":float(500)}
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate,"%d/%m/%Y")
        outDate = datetime.strptime(outDate,"%d/%m/%Y")
        self.var_days.set((outDate-inDate).days)
        if int(self.var_days.get())<0:
            messagebox.showerror("Error","--- Wrong Input in check-in or check-out dates ---",parent=self.root)
            return 0
        meal_price = prices[self.var_meal.get()]
        room_price = prices[self.var_roomtype.get()]

        days = float(self.var_days.get())

        actual = float((meal_price+room_price)*days)

        actual_total = "Rs."+str("%.2f"%((actual)))
        tax = "Rs."+str("%.2f"%((actual)*0.18))

        total = float(actual + actual *0.18)
        total = "Rs."+str("%.2f"%(total))

        self.var_tax.set(tax)
        self.var_actualTotal.set(actual_total)
        self.var_total.set(total)






if __name__ == "__main__":
    root  = Tk() 
    obj = Room(root)  
    root.mainloop()
