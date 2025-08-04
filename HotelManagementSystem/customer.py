from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import re
import random
import mysql.connector
class Customer:
    
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x580+230+220")
        #=============== Database Variable============
        self.var_ref = StringVar()
        x = random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_name = StringVar()
        self.var_father = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_idProof = StringVar()
        self.var_idNumber = StringVar()
        self.var_adress = StringVar()
        def validate_mobile(P):
            return (P.isdigit() and len(P) <= 10) or P == ""

        def validate_email(self, email):
            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if not re.match(pattern, email):
                messagebox.showerror("Invalid Email", "Enter a valid email address.")
                return False
            return True
       #------------TiTle---------------
        lbl_title = Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RAISED )
        lbl_title.place(x=0,y=0,width=1295,height=50) 
        # ____________logo__________
        image2=Image.open(r"D:\PROJECT\HotelManagementSystem\images\logohotel.png")
        img2 = image2.resize((100,40),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=0,relief=RAISED)
        lblimg.place(x=5,y=2,width=100,height=40)  
        #================Label Frame================
        labelframeleft =  LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #=============Label and Entry===============
        #customer reference
        lbl_cust_ref = Label(labelframeleft,text="Costomer Ref:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
  
        entry_ref = ttk.Entry(labelframeleft,textvariable=self.var_ref, width=29,font=("arial",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)
 
        #Customer name
        cname = Label(labelframeleft,text="Costomer Name:",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname = ttk.Entry(labelframeleft,textvariable=self.var_name,width=29,font=("arial",13,"bold"))
        txtcname.grid(row=1,column=1)

        #Father name
        fname = Label(labelframeleft,text="Father Name:",font=("arial",12,"bold"),padx=2,pady=6)
        fname.grid(row=2,column=0,sticky=W)
        txtfname = ttk.Entry(labelframeleft,textvariable=self.var_father,width=29,font=("arial",13,"bold"))
        txtfname.grid(row=2,column=1)

        #Gender combobox
        Gname = Label(labelframeleft,text="Gender:",font=("arial",12,"bold"),padx=2,pady=6)
        Gname.grid(row=3,column=0,sticky=W)
        combo_gender = ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly",cursor="hand2")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        #postcode
        pcname = Label(labelframeleft,text="PostCode:",font=("arial",12,"bold"),padx=2,pady=6)
        pcname.grid(row=4,column=0,sticky=W)
        txtpcname = ttk.Entry(labelframeleft,textvariable=self.var_post,width=29,font=("arial",13,"bold"))
        txtpcname.grid(row=4,column=1)

        #MobileNumber
        vcmd = (self.root.register(validate_mobile), '%P')

        mbname = Label(labelframeleft, text="Mobile Number:", font=("arial",12,"bold"), padx=2, pady=6)
        mbname.grid(row=5, column=0, sticky=W)

        txtmbname = ttk.Entry(labelframeleft, width=29,textvariable=self.var_mobile, font=("arial",13,"bold"),
                        validate='key', validatecommand=vcmd)
        txtmbname.grid(row=5, column=1)
        self.txtmbname = txtmbname

        #Email  
        vcmd = (self.root.register(validate_email), '%P')

        Ename = Label(labelframeleft,text="Email:",font=("arial",12,"bold"),padx=2,pady=6)
        Ename.grid(row=6,column=0,sticky=W)
        txtEname = ttk.Entry(labelframeleft,width=29,textvariable=self.var_email,font=("arial",13,"bold"),
                             validate='key', validatecommand=vcmd)
        txtEname.grid(row=6,column=1)

        #Nationality combobox
        Nname = Label(labelframeleft,text="Nationality:",font=("arial",12,"bold"),padx=2,pady=6)
        Nname.grid(row=7,column=0,sticky=W)
        combo_NA = ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly",cursor="hand2")
        countries = ("India","United States", "Canada", "United Kingdom", "Germany", "France","China", "Japan", "Australia", "Brazil")
        combo_NA["value"]=countries
        combo_NA.current(0)
        combo_NA.grid(row=7,column=1)
        
        #ID proof combobox
        IPname = Label(labelframeleft,text="ID Proof:",font=("arial",12,"bold"),padx=2,pady=6)
        IPname.grid(row=8,column=0,sticky=W)
        combo_IP = ttk.Combobox(labelframeleft,textvariable=self.var_idProof,font=("arial",12,"bold"),width=27,state="readonly",cursor="hand2")
        id_proofs = ( "Aadhaar Card","PAN Card","Voter ID","Passport", "Driver's License", "National ID Card", "Social Security Card", "Residence Permit", "Military ID", "Employee ID")
        combo_IP["value"]=id_proofs
        combo_IP.current(0)
        combo_IP.grid(row=8,column=1)

        #ID number
        IDname = Label(labelframeleft,text="ID Number:",font=("arial",12,"bold"),padx=2,pady=6)
        IDname.grid(row=9,column=0,sticky=W)
        txtIDname = ttk.Entry(labelframeleft,width=29,textvariable=self.var_idNumber,font=("arial",13,"bold"))
        txtIDname.grid(row=9,column=1)

        #Adress 
        ADname = Label(labelframeleft,text="Adress:",font=("arial",12,"bold"),padx=2,pady=6)
        ADname.grid(row=10,column=0,sticky=W)
        txtADname = ttk.Entry(labelframeleft,width=29,textvariable=self.var_adress,font=("arial",13,"bold"))
        txtADname.grid(row=10,column=1)

        #===============Button Frame (update Delete Insert Btn) ============
        btn_frame = Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)
        #Add
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10,cursor="hand2")
        btnAdd.grid(row=0,column=0,padx=1)
        #Update
        btnUpdate=Button(btn_frame,command=self.udate_data,text="Update",font=("arial",11,"bold"),bg="black",fg="gold",width=10,cursor="hand2")
        btnUpdate.grid(row=0,column=1,padx=1)
        #Delete
        btnDelete=Button(btn_frame,command=self.delete_data,text="Delete",font=("arial",11,"bold"),bg="black",fg="gold",width=10,cursor="hand2")
        btnDelete.grid(row=0,column=2,padx=1)
         #reset
        btnReset=Button(btn_frame,command=self.reset,text="Reset",font=("arial",11,"bold"),bg="black",fg="gold",width=10,cursor="hand2")
        btnReset.grid(row=0,column=3,padx=1)

        #================== Table label Frame search =======================
        Tableframe =  LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"),padx=2)
        Tableframe.place(x=435,y=50,width=860,height=490)

        lblSearch = Label(Tableframe,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearch.grid(row=0,column=0,sticky=W,padx=2,pady=5)
        
        self.var_search = StringVar()
        combo_search = ttk.Combobox(Tableframe,textvariable=self.var_search,font=("arial",12,"bold"),width=24,state="readonly",cursor="hand2")
        combo_search["value"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
        
        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Tableframe,width=24,textvariable=self.txt_search,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Tableframe,text="Search",command=self.search_data,font=("arial",11,"bold"),bg="green",fg="white",width=10,cursor="hand2")
        btnSearch.grid(row=0,column=3,padx=1)

        btnShow=Button(Tableframe,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="green",fg="white",width=10,cursor="hand2")
        btnShow.grid(row=0,column=4,padx=1)

        #================== Show Data Frame ===============
        details_frame = Frame(Tableframe,bd=2,relief=RIDGE)
        details_frame.place(x=0,y=50,width=860,height=350)

        scroll_x = ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_frame,orient=VERTICAL)
        
        self.cust_details = ttk.Treeview(details_frame,columns=("ref","name","father","gender","post","mobile",
                                                               "email","nationality","idproof","idnumber","adress" ),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details.xview)
        scroll_y.config(command=self.cust_details.yview)

        self.cust_details.heading("ref",text="Refer No")
        self.cust_details.heading("name",text="Name")
        self.cust_details.heading("father",text="Father")
        self.cust_details.heading("gender",text="Gender")
        self.cust_details.heading("post",text="PostCode")
        self.cust_details.heading("mobile",text="Mobile")
        self.cust_details.heading("email",text="Email")
        self.cust_details.heading("nationality",text="Nationality")
        self.cust_details.heading("idproof",text="ID Proof")
        self.cust_details.heading("idnumber",text="Id Number")
        self.cust_details.heading("adress",text="Adress")
       
        self.cust_details["show"]="headings"

        self.cust_details.column("name",width=100,anchor="center")
        self.cust_details.column("ref",width=100,anchor="center")
        self.cust_details.column("father",width=100,anchor="center")
        self.cust_details.column("gender",width=100,anchor="center")
        self.cust_details.column("post",width=100,anchor="center")
        self.cust_details.column("mobile",width=100,anchor="center")
        self.cust_details.column("email",width=100,anchor="center")
        self.cust_details.column("nationality",width=100,anchor="center")
        self.cust_details.column("idproof",width=100,anchor="center")
        self.cust_details.column("idnumber",width=100,anchor="center")
        self.cust_details.column("adress",width=100,anchor="center")

        self.cust_details.pack(fill=BOTH,expand=1)
        self.cust_details.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
#=========== add data ===============
    def add_data(self):
        if self.var_name.get()==""or self.var_mobile.get()=="" or self.var_father.get()=="" or self.var_email.get()=="":
           messagebox.showerror("Error"," All fields are required ",parent=self.root)

        if self.var_idNumber.get()=="" or self.var_post.get()=="" or self.var_adress.get()=="":
           messagebox.showerror("Error"," All fields are required ",parent=self.root)
        
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Anoop@123",database="management")
                mycursor = conn.cursor()
                mycursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_ref.get(),
                self.var_name.get(),
                self.var_father.get(),
                self.var_gender.get(), 
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_idProof.get(),
                self.var_idNumber.get(),
                self.var_adress.get()
                       ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been adeed Succesfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)
    
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Anoop@123",database="management")
        mycursor = conn.cursor()

        mycursor.execute("select * from customer")
        rows = mycursor.fetchall()

        if len(rows)!=0:
            self.cust_details.delete(*self.cust_details.get_children())

            for i in rows:
                self.cust_details.insert("",END,values=i)

            conn.commit()
        conn.close()
    
    def get_cursor(self,event=""):
        cursor_row = self.cust_details.focus()
        content = self.cust_details.item(cursor_row)
        row = content["values"]
        self.var_ref.set(row[0]),
        self.var_name.set(row[1]),
        self.var_father.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_idProof.set(row[8]),
        self.var_idNumber.set(row[9]),
        self.var_adress.set(row[10])

    def udate_data(self): 
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="Anoop@123",database="management")
            mycursor = conn.cursor()
            mycursor.execute("UPDATE customer SET name=%s,father=%s, gender=%s, post=%s, mobile=%s, email=%s, nationality=%s, idproof=%s, idnumber=%s, adress=%s WHERE ref=%s",(
                
                self.var_name.get(),
                self.var_father.get(),
                self.var_gender.get(), 
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_idProof.get(),
                self.var_idNumber.get(),
                self.var_adress.get(),
                self.var_ref.get()
            ))
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated succesfully ",parent=self.root)
            
    
    def delete_data(self):
        delete_data=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if delete_data>0:
            conn = mysql.connector.connect(host="localhost",username="root",password="Anoop@123",database="management")
            mycursor = conn.cursor()
            query = "delete from customer where ref=%s"
            value =(self.var_ref.get(),)
            mycursor.execute(query,value)

        else:
            if not delete_data:
                return
        
        conn.commit()
        self.fetch_data()
        conn.close()
    
    def reset(self):
        x = random.randint(1000,9999)
        self.var_ref.set(str(x)),
        self.var_name.set(""),
        self.var_father.set(""),
        # self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        # self.var_nationality.set(""),
        # self.var_idProof.set(""),
        self.var_idNumber.set(""),
        self.var_adress.set("")

    def search_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Anoop@123",database="management")
        mycursor = conn.cursor()
        mycursor.execute("select * from customer where "+str(self.var_search.get())+" LIKE '%"+str(self.txt_search.get())+"%'")

        row = mycursor.fetchall()

        if len(row)!=0:
            self.cust_details.delete(*self.cust_details.get_children())
            for i in row:
                self.cust_details.insert("",END,values=i)
            conn.commit()
        
        conn.close()

if __name__=='__main__':
    root = Tk()
    obj = Customer(root)
    root.mainloop()