from tkinter import*
from PIL import Image,ImageTk   #pip install pillow
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class student_window:
    def __init__(self,root) :
        self.root=root
        self.root.title("TechDorm")
        self.root.geometry("1295x550+230+220")   # to size the screen



        self.var_ref=StringVar()
        x=random.randint(1,100)
        self.var_ref.set(str(x))

        self.var_stu_name=StringVar()
        self.var_father=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()











        lbl_title=Label(self.root,text="ADD STUDENT DETAILS",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)



        img2=Image.open(r"C:\Users\sdgid\OneDrive\Desktop\Python Project\iiitklogo.png")     #r is convert backslash to slash    
        img2 = img2.resize((100, 40), Image.LANCZOS) #high level image is converted to low level image using Antialias
        self.pimg2=ImageTk.PhotoImage(img2)   # resized image is stored in this variable pimg2


        lblimg=Label(self.root,image=self.pimg2,bd=4,relief=RIDGE)  #bd means border relief means style
        lblimg.place(x=5,y=2,width=100,height=40)



        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)


        lbl_student_ref=Label(labelframeleft,text="Student Ref:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_student_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("arial",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)



        sname=Label(labelframeleft,text="Student name:",font=("arial",12,"bold"),padx=2,pady=6)
        sname.grid(row=1,column=0,sticky=W)

        txtsname=ttk.Entry(labelframeleft,textvariable=self.var_stu_name,width=29,font=("arial",13,"bold"))
        txtsname.grid(row=1,column=1)


        lblfname=Label(labelframeleft,text="Father name:",font=("arial",12,"bold"),padx=2,pady=6)
        lblfname.grid(row=2,column=0,sticky=W)

        txtfname=ttk.Entry(labelframeleft,textvariable=self.var_father,width=29,font=("arial",13,"bold"))
        txtfname.grid(row=2,column=1)


        lblmname=Label(labelframeleft,text="Mother name:",font=("arial",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=3,column=0,sticky=W)

        txtmname=ttk.Entry(labelframeleft,width=29,textvariable=self.var_mother,font=("arial",13,"bold"))
        txtmname.grid(row=3,column=1)



        lblgender=Label(labelframeleft,text="Gender:",font=("arial",12,"bold"),padx=2,pady=6)
        lblgender.grid(row=4,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=('arial',12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=4,column=1)





        lblPostCode=Label(labelframeleft,text="PostCode:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=5,column=0,sticky=W)

        txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_post,width=29,font=("arial",13,"bold"))
        txtPostCode.grid(row=5,column=1)



        lblMobile=Label(labelframeleft,text="Mobile:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=6,column=0,sticky=W)

        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=("arial",13,"bold"))
        txtMobile.grid(row=6,column=1)




        lblEmail=Label(labelframeleft,text="Email:",font=("arial",12,"bold"),padx=2,pady=6)
        lblEmail.grid(row=7,column=0,sticky=W)

        txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=("arial",13,"bold"))
        txtEmail.grid(row=7,column=1)


        lblNationality=Label(labelframeleft,text="Nationality:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNationality.grid(row=8,column=0,sticky=W)
        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=('arial',12,"bold"),width=27,state="readonly")
        combo_Nationality["value"]=("Indian","Other")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=8,column=1)


        lblIdProof=Label(labelframeleft,text="Id Proof Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdProof.grid(row=9,column=0)
        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=('arial',12,"bold"),width=27,state="readonly")
        combo_id["value"]=("AadhaarCard","PANCard","Other")
        combo_id.current(0)
        combo_id.grid(row=9,column=1)



        lblIdNumber=Label(labelframeleft,text="Id Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=10,column=0,sticky=W)

        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number,width=29,font=("arial",13,"bold"))
        txtIdNumber.grid(row=10,column=1)




        lblAddress=Label(labelframeleft,font=("arial",12,"bold"),text="Address:",padx=2,pady=6)
        lblAddress.grid(row=11,column=0,sticky=W)

        txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("arial",13,"bold"))
        txtAddress.grid(row=11,column=1)



        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=420,width=412,height=40)  #400-->420

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)


        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)


        btnDelete=Button(btn_frame,text="Delete",command=self.sDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)


        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)


        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("times new roman",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=('arial',12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Mobile","Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,width=24,textvariable=self.txt_search,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)


        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnSearch.grid(row=0,column=3,padx=1)


        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnShowAll.grid(row=0,column=4,padx=1)








        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)


        self.Student_Details_Table=ttk.Treeview(details_table,column=("ref","name","father","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Student_Details_Table.xview)
        scroll_y.config(command=self.Student_Details_Table.yview)

        self.Student_Details_Table.heading("ref",text="Refer No")
        self.Student_Details_Table.heading("name",text="Name")
        self.Student_Details_Table.heading("father",text="Father Name")
        self.Student_Details_Table.heading("mother",text="Mother Name")
        self.Student_Details_Table.heading("gender",text="Gender")
        self.Student_Details_Table.heading("post",text="PostCode")
        self.Student_Details_Table.heading("mobile",text="Mobile")
        self.Student_Details_Table.heading("email",text="Email")
        self.Student_Details_Table.heading("nationality",text="Nationality")
        self.Student_Details_Table.heading("idproof",text="Id Proof")
        self.Student_Details_Table.heading("idnumber",text="Id Number")
        self.Student_Details_Table.heading("address",text="Address")


        self.Student_Details_Table['show']="headings"

        self.Student_Details_Table.column("ref",width=100)
        self.Student_Details_Table.column("name",width=100)
        self.Student_Details_Table.column("father",width=100)
        self.Student_Details_Table.column("mother",width=100)
        self.Student_Details_Table.column("gender",width=100)
        self.Student_Details_Table.column("post",width=100)
        self.Student_Details_Table.column("mobile",width=100)
        self.Student_Details_Table.column("email",width=100)
        self.Student_Details_Table.column("nationality",width=100)
        self.Student_Details_Table.column("idproof",width=100)
        self.Student_Details_Table.column("idnumber",width=100)
        self.Student_Details_Table.column("address",width=100)

        self.Student_Details_Table.pack(fill=BOTH,expand=1)
        self.Student_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()



    def add_data(self):
        if self.var_mobile.get()=="" or self.var_stu_name.get()=="" or self.var_father.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="studentmanagement")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_ref.get(),
                        self.var_stu_name.get(),
                        self.var_father.get(),
                        self.var_mother.get(),
                        self.var_gender.get(),
                        self.var_post.get(),
                        self.var_mobile.get(),
                        self.var_email.get(),
                        self.var_nationality.get(),
                        self.var_id_proof.get(),
                        self.var_id_number.get(),
                        self.var_address.get(),
                                    ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)
            
         
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="studentmanagement")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Student_Details_Table.delete(*self.Student_Details_Table.get_children())
            for i in rows:
                self.Student_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.Student_Details_Table.focus()
        content=self.Student_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_stu_name.set(row[1]),
        self.var_father.set(row[2]),
        self.var_mother.set(row[3]),
        self.var_gender.set(row[4]),
        self.var_post.set(row[5]),
        self.var_mobile.set(row[6]),
        self.var_email.set(row[7]),
        self.var_nationality.set(row[8]),
        self.var_id_proof.set(row[9]),
        self.var_id_number.set(row[10]),
        self.var_address.set(row[11])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="studentmanagement")
            my_cursor=conn.cursor()
            my_cursor.execute("update student set Name=%s,Father=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,IdNumber=%s,Address=%s where Ref=%s",(
                                                        self.var_stu_name.get(),
                                                        self.var_father.get(),
                                                        self.var_mother.get(),
                                                        self.var_gender.get(),
                                                        self.var_post.get(),
                                                        self.var_mobile.get(),
                                                        self.var_email.get(),
                                                        self.var_nationality.get(),
                                                        self.var_id_proof.get(),
                                                        self.var_id_number.get(),
                                                        self.var_address.get(),
                                                        self.var_ref.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Student details has been updated successfully",parent=self.root)


    def sDelete(self):
        sDelete=messagebox.askyesno("Student Management System","Do you want to delete this student",parent=self.root)
        if sDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="studentmanagement")
            my_cursor=conn.cursor()
            query="delete from student where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not sDelete:
                return
            
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_ref.set(""),
        self.var_stu_name.set(""),
        self.var_father.set(""),
        self.var_mother.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="studentmanagement")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from student where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.Student_Details_Table.delete(*self.Student_Details_Table.get_children())
            for i in rows:
                self.Student_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()




    


if __name__ == "__main__":
    root=Tk()
    obj=student_window(root)
    root.mainloop()