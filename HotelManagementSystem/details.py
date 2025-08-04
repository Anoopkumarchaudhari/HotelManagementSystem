from tkinter import *
from PIL import Image,ImageTk,ImageEnhance #pip install pillow
from tkinter import ttk,messagebox
import re
import random
import mysql.connector
from time import strftime
from datetime import datetime

class Details:
    
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x580+230+220")
       #------------TiTle---------------

#=========== Variables =============
        self.var_floor = StringVar()
        self.var_roomno = StringVar()
        self.var_roomType = StringVar()
       
        lbl_title = Label(self.root,text="ROOM INFO  DEPARTMENT ",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RAISED )
        lbl_title.place(x=0,y=0,width=1295,height=50) 
# ____________logo__________
        image2=Image.open(r"D:\PROJECT\HotelManagementSystem\images\logohotel.png")
        img2 = image2.resize((100,40),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root,image=self.photoimg2,bd=0,relief=RAISED)
        lblimg.place(x=5,y=2,width=100,height=40)  

#================Label Frame================
        labelframeleft =  LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=55,width=520,height=250)

        labelframebuttom =  LabelFrame(self.root,bd=2,relief=RIDGE,text="Fare Or Charges",font=("times new roman",12,"bold"),bg="black",fg="gold",padx=2)
        labelframebuttom.place(x=5,y=305,width=520,height=250)

#============== Label Frame image ==============
       # Background label inside labelframebuttom
        bg_image = Image.open(r"D:\PROJECT\HotelManagementSystem\images\meal2.jpg") 
        bg_image = bg_image.resize((520, 250))
        enhancer = ImageEnhance.Brightness(bg_image) 
        dark_img = enhancer.enhance(0.4) 
        photo = ImageTk.PhotoImage(bg_image)
        
        bg_label = Label(labelframebuttom, image=photo)
        bg_label.image = photo  
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Background label inside labelframeleft
        bg_image = Image.open(r"D:\PROJECT\HotelManagementSystem\images\mealroom.jpg") 
        bg_image = bg_image.resize((520, 250))
        enhancer = ImageEnhance.Brightness(bg_image) 
        dark_img = enhancer.enhance(0.4) 
        photo = ImageTk.PhotoImage(bg_image)
        
        bg_label = Label(labelframeleft, image=photo)
        bg_label.image = photo  
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        #=============Label and Entry in leftFrame===============
        #Floor
        lbl_floor = Label(labelframeleft,text="Floor :-  ",font=("arial",12,"bold"),padx=2,pady=3)
        lbl_floor.grid(row=0,column=0,sticky=W,padx=20,pady=10)
        entry_floor = ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=("arial",13,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W,padx=3,pady=6)
        #Room No
        lbl_room  = Label(labelframeleft,text="Room :- ",font=("arial",12,"bold"),padx=2,pady=3)
        lbl_room.grid(row=1,column=0,sticky=W,padx=20,pady=5)
        entry_room = ttk.Entry(labelframeleft,textvariable=self.var_roomno,width=20,font=("arial",13,"bold"))
        entry_room.grid(row=1,column=1,sticky=W,padx=2,pady=5)

        #Room Type
        lbl_check_out = Label(labelframeleft,text="Room Type:- ",font=("arial",12,"bold"),padx=2,pady=3)
        lbl_check_out.grid(row=2,column=0,sticky=W,padx=20,pady=5)

        combo_roomType = ttk.Combobox(labelframeleft,textvariable=self.var_roomType,font=("arial",12,"bold"),width=27,state='readonly')
        combo_roomType['value'] = ("Single","Double","Luxury","Duplex")
        combo_roomType.current(0)
        combo_roomType.grid(row=2,column=1)
#============== Entry in Buttom Frame ===============
        #Prices of mael and  Room
   
        mealPrice = {"Tea":80,"BreakFast":200,"Lunch":300,"Dinner":500}
        roomPrice = {"Single":300,"Double":400,"Duplex":500,"Lauxury":900}
        j = 1
        breakFast = Label(labelframebuttom, text="--Meal Prices--", font=("arial", 12, "bold"), fg="gold", bg="#000000")
        breakFast.grid(row=0,column=0 ,sticky=W,pady=(5,2),padx=10)
        for key,values in mealPrice.items():
            breakFast = Label(labelframebuttom,text=f"{key} :- Rs.{values}.0 /-",font=("arial",12),fg="yellow",bg="black",pady=3,padx=3)
            breakFast.grid(row=j,column=0 ,sticky=W,pady=3,padx=10)
            j = j+1 

        j = 1
        breakFast = Label(labelframebuttom,text=f"--Room Prices--",font=("arial",12,"bold"),bg="black",fg="gold")
        breakFast.grid(row=0,column=2 ,sticky=E)
        for key,values in roomPrice.items():
            breakFast = Label(labelframebuttom,text=f"{key} :- Rs.{values}.0 /-",font=("arial",12),bg="black",fg="yellow",pady=1)
            breakFast.grid(row=j,column=2 ,sticky=E,pady=3,padx=10)
            j = j+1 
        #=============== Buttons ===================
        btn_frame = Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=30,y=170,width=412,height=40)
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

        #================== Table label Frame search =======================
        Tableframe =  LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times new roman",12,"bold"),padx=2)
        Tableframe.place(x=535,y=55,width=750,height=510)

        lblSearch = Label(Tableframe,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearch.grid(row=0,column=0,sticky=W,padx=5,pady=5)
        
        self.var_search = StringVar()
        combo_search = ttk.Combobox(Tableframe,textvariable=self.var_search,font=("arial",12,"bold"),width=21,state="readonly",cursor="hand2")
        combo_search["value"]=("floor","roomno","roomtype")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
        
        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Tableframe,width=24,textvariable=self.txt_search,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Tableframe,text="Search",font=("arial",11,"bold"),command=self.search_data,bg="green",fg="white",width=10,cursor="hand2")
        btnSearch.grid(row=0,column=3,padx=1)

        btnShow=Button(Tableframe,text="Show All",font=("arial",11,"bold"),command=self.fetch_data,bg="green",fg="white",width=10,cursor="hand2")
        btnShow.grid(row=0,column=4,padx=1)
       #========= Details frame ==============
        details_frame = Frame(Tableframe,bd=2,relief=RIDGE)
        details_frame.place(x=5,y=50,width=740,height=510)
        scroll_x = ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_frame,orient=VERTICAL)
        
        style = ttk.Style()
        style.theme_use("clam")  

        # Main Treeview styling
        style.configure("Treeview",
            background="#1c1c1c",      # Dark gray background
            foreground="white",        # White text
            rowheight=25,
            fieldbackground="#1c1c1c",
            font=("arial", 11)
        )

        # Heading styling
        style.configure("Treeview.Heading",
            background="#000000",      # Header background
            foreground="#FFD700",      # Gold text
            font=("arial", 12, "bold")
        )

        # Selected row styling
        style.map("Treeview",
            background=[("selected", "#44475a")],
            foreground=[("selected", "white")]
        )

        self.room_details = ttk.Treeview(details_frame,columns=("floor","roomno","roomtype" ),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_details.xview)
        scroll_y.config(command=self.room_details.yview)

        self.room_details.heading("floor",text="Floor")
        self.room_details.heading("roomno",text="Room No")
        self.room_details.heading("roomtype",text="Room Type")
       
        self.room_details["show"]="headings"

        self.room_details.column("floor",width=100,anchor="center")
        self.room_details.column("roomno",width=100,anchor="center")
        self.room_details.column("roomtype",width=100,anchor="center")

        self.room_details.pack(fill=BOTH,expand=1)
        self.room_details.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()
        
#======= Add data   ========
    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomType.get()=="":
           messagebox.showerror("Error"," All fields are required ",parent=self.root)
        
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Anoop@123",database="management")
                mycursor = conn.cursor()
                mycursor.execute("insert into details values(%s,%s,%s)",(
                self.var_floor.get(),
                self.var_roomno.get(),
                self.var_roomType.get()
            
               
                       ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

# =============Fetch Data ======================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Anoop@123",database="management")
        mycursor = conn.cursor()

        mycursor.execute("select * from details")
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
        self.var_floor.set(row[0]),
        self.var_roomno.set(row[1]),
        self.var_roomType.set(row[2])
#=========== Update ==================
    def update_data(self): 
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter Floor number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="Anoop@123",database="management")
            mycursor = conn.cursor()
            mycursor.execute("UPDATE details SET floor=%s, roomtype=%s WHERE roomno=%s",(
                
                self.var_floor.get(),
                self.var_roomType.get(),
                self.var_roomno.get(),
            ))
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated succesfully ",parent=self.root)  
#=========== Delete ===========================
    def delete_data(self):
        delete_data=messagebox.askyesno("Hotel Management System","Do you want to delete this Room Details .",parent=self.root)
        if delete_data>0:
            conn = mysql.connector.connect(host="localhost",username="root",password="Anoop@123",database="management")
            mycursor = conn.cursor()
            query = "delete from details where roomno=%s"
            value =(self.var_roomno.get(),)
            mycursor.execute(query,value)

        else:
            if not delete_data:
                return
        
        conn.commit()
        self.fetch_data()
        conn.close()  
    def reset(self):
        self.var_roomno.set("")
        self.var_floor.set("")
        self.var_roomType.set("") 

#=============== Search ==================
    def search_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Anoop@123",database="management")
        mycursor = conn.cursor()
        mycursor.execute("select * from details where "+str(self.var_search.get())+" LIKE '%"+str(self.txt_search.get())+"%'")

        row = mycursor.fetchall()

        if len(row)!=0:
            self.room_details.delete(*self.room_details.get_children())
            for i in row:
                self.room_details.insert("",END,values=i)
            conn.commit()
        
        conn.close()
if __name__ == "__main__":
    root  = Tk() 
    obj = Details(root)  
    root.mainloop()