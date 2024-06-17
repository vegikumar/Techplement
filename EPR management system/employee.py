from tkinter import*
from tkinter import messagebox,ttk
import pymysql
import time
import os
import tempfile
class EmployeeSystem:
  def __init__(self,root):
    self.root=root
    self.root.title("Employee Pay Roll System")
    self.root.geometry("1370x700+0+0")
    self.root.config(bg="white")
    title=Label(self.root,text="Employee Pay Roll System",font=("times new roman",30),bg="#262626",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
    btn_emp=Button(self.root,text="All Employee's",command=self.employees,font=("times new roman",15),bg="gray",fg="white").place(x=1100,y=10,height=35)
#.................all_variables..................#
    self.var_empcode=StringVar()
    self.var_designation=StringVar()
    self.var_name=StringVar()
    self.var_experience=StringVar()
    self.var_gender=StringVar()
    self.var_email=StringVar()
    self.var_dob=StringVar()
    self.var_doj=StringVar()
    self.var_age=StringVar()
    self.var_aadhar=StringVar()
    self.var_contact=StringVar()
    





#start.................Frame1..................#
    Frame1=Frame(self.root,bd=5,relief=RIDGE,bg="white")
    Frame1.place(x=10,y=70,width=750,height=620)
    title1=Label(Frame1,text="Employee Detail",font=("times new roman",20),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        # start................... R0....................#
    lb_code=Label(Frame1,text="Employee Code",font=("times new roman",20 ),bg="white",fg="black").place(x=5,y=70)
    self.txt_code=Entry(Frame1,font=("times new roman",20),textvariable=self.var_empcode,bg="lightyellow",fg="black")
    self.txt_code.place(x=210,y=70,width=200)
    btn_search=Button(Frame1,text="Search",font=("times new roman",20 ),command=self.search,bg="grey",fg="black").place(x=490,y=70,height=35)

    #end ..................... R0....................#

     # start................... R1....................#
    lb_designation=Label(Frame1,text="Designation",font=("times new roman",20),bg="white",fg="black").place(x=10,y=140)
    txt_designation=Entry(Frame1,font=("times new roman",20),textvariable=self.var_designation,bg="lightyellow",fg="blue").place(x=170,y=140,width=200)
    lb_dob=Label(Frame1,text="D.O.B.",font=("times new roman",20),bg="white",fg="black").place(x=390,y=140)
    txt_dob=Entry(Frame1,font=("times new roman",20),textvariable=self.var_dob,bg="lightyellow",fg="blue").place(x=480,y=140,width=200)
            #end ..................... R1....................#

            # start................... R2....................#
    lb_name=Label(Frame1,text="Name",font=("times new roman",20),bg="white",fg="black").place(x=30,y=190)
    txt_name=Entry(Frame1,font=("times new roman",20),textvariable=self.var_name,bg="lightyellow",fg="blue").place(x=170,y=190,width=200)
    lb_doj=Label(Frame1,text="D.O.J.",font=("times new roman",20),bg="white",fg="black").place(x=390,y=190)
    txt_doj=Entry(Frame1,font=("times new roman",20),textvariable=self.var_doj,bg="lightyellow",fg="blue").place(x=480,y=190,width=200)
            #end ..................... R2....................#
    # start................... R3....................#
    lb_exp=Label(Frame1,text="Experience",font=("times new roman",20),bg="white",fg="black").place(x=10,y=240)
    txt_exp=Entry(Frame1,font=("times new roman",20),textvariable=self.var_experience,bg="lightyellow",fg="blue").place(x=170,y=240,width=70)
    lb_age=Label(Frame1,text="Age",font=("times new roman",20),bg="white",fg="black").place(x=390,y=240)
    txt_age=Entry(Frame1,font=("times new roman",20),textvariable=self.var_age,bg="lightyellow",fg="blue").place(x=480,y=240,width=70)
            #end ..................... R3....................#
     # start................... R4....................#
    lb_gender=Label(Frame1,text="Gender",font=("times new roman",20),bg="white",fg="black").place(x=30,y=290)
    txt_gender=Entry(Frame1,font=("times new roman",20),textvariable=self.var_gender,bg="lightyellow",fg="blue").place(x=170,y=290,width=70)
    # clicked = StringVar()
    # clicked.set("Male")  # default value
    # txt_gender = OptionMenu(Frame1, clicked, "Male", "Female")
    # txt_gender.place(x=170, y=290, width=130,height=40)
    # txt_gender.config(font=("times new roman", 15),bg="lightyellow")#-----------------------------------------textvariable=self.var_gender-----------------------------------------------------------------------------------------------------------#
    # txt_gender.config(width=10, height=2)  # Adjust width and height as needed

    # txt_name.pack()

    #txt_name=Entry(Frame1,font=("times new roman",20),bg="lightyellow",fg="blue").place(x=170,y=290,width=120)
    lb_aadhar_no=Label(Frame1,text="Aadhar No.",font=("times new roman",20),bg="white",fg="black").place(x=390,y=290)
    txt_aahar_no=Entry(Frame1,font=("times new roman",20),textvariable=self.var_aadhar,bg="lightyellow",fg="blue").place(x=530,y=290,width=200)
            #end ..................... R4....................#
     # start................... R5....................#
    lb_email=Label(Frame1,text="Email",font=("times new roman",20),bg="white",fg="black").place(x=30,y=340)
    txt_email=Entry(Frame1,font=("times new roman",20),textvariable=self.var_email,bg="lightyellow",fg="blue").place(x=170,y=340,width=200)
    lb_contact=Label(Frame1,text="Contact No.",font=("times new roman",20),bg="white",fg="black").place(x=390,y=340)
    txt_contact=Entry(Frame1,font=("times new roman",20),textvariable=self.var_contact,bg="lightyellow",fg="blue").place(x=530,y=340,width=200)
            #end ..................... R5....................#
     # start................... R5....................#
    lb_address=Label(Frame1,text="Address",font=("times new roman",20),bg="white",fg="black").place(x=30,y=390)
    self.txt_address = Entry(Frame1, font=("times new roman", 18),bg="lightyellow", fg="blue")
    self.txt_address.place(x=170,y=390,width=500,height=200)

            #end ..................... R2....................#
    

    #end ..................Frame1..................#

#.................all_variables..................#
    self.var_month=StringVar()
    self.var_basicsalary=StringVar()
    self.var_totaldays=StringVar()
    self.var_medical=StringVar()
    self.var_convence=StringVar()
    self.var_year=StringVar()
    self.var_absent=StringVar()
    self.var_pf=StringVar()
    self.var_netsalary=StringVar()


    #start............Frame2...............#
    Frame2=Frame(self.root,bd=5,relief=RIDGE,bg="white")
    Frame2.place(x=770,y=70,width=580,height=374)
     # start................... R1....................#
    lb_month=Label(Frame2,text="Month",font=("times new roman",20),bg="white",fg="black").place(x=10,y=10)
    txt_month=Entry(Frame2,font=("times new roman",20),textvariable=self.var_month,bg="lightyellow",fg="blue").place(x=170,y=10,width=110)
    lb_year=Label(Frame2,text="Year",font=("times new roman",20),bg="white",fg="black").place(x=360,y=10)
    txt_year=Entry(Frame2,font=("times new roman",20),textvariable=self.var_year,bg="lightyellow",fg="blue").place(x=450,y=10,width=80)
    
            #end ..................... R1....................#

            # start................... R2....................#
    lb_basic_salary=Label(Frame2,text="Basic Salary",font=("times new roman",20),bg="white",fg="black").place(x=10,y=70)
    txt_basic_salary=Entry(Frame2,font=("times new roman",20),textvariable=self.var_basicsalary,bg="lightyellow",fg="blue").place(x=170,y=70,width=150)
            #end ..................... R2....................#
    # start................... R3....................#
    lb_total_days=Label(Frame2,text="Total Days",font=("times new roman",20),bg="white",fg="black").place(x=10,y=120)
    txt_total_days=Entry(Frame2,font=("times new roman",20),textvariable=self.var_totaldays,bg="lightyellow",fg="blue").place(x=170,y=120,width=70)
    lb_absent=Label(Frame2,text="Absent",font=("times new roman",20),bg="white",fg="black").place(x=350,y=120)
    txt_absent=Entry(Frame2,font=("times new roman",20),textvariable=self.var_absent,bg="lightyellow",fg="blue").place(x=450,y=120,width=70)
    #         #end ..................... R3....................#
    # start................... R4....................#
    lb_Medical=Label(Frame2,text="Medical",font=("times new roman",20),bg="white",fg="black").place(x=10,y=170)
    txt_Medical=Entry(Frame2,font=("times new roman",20),textvariable=self.var_medical,bg="lightyellow",fg="blue").place(x=170,y=170,width=70)
    lb_pf=Label(Frame2,text="P.F.",font=("times new roman",20),bg="white",fg="black").place(x=360,y=170)
    txt_pf=Entry(Frame2,font=("times new roman",20),textvariable=self.var_pf,bg="lightyellow",fg="blue").place(x=450,y=170,width=90)
    #end..............................R4...............#
     # start................... R5....................#
    lb_convence=Label(Frame2,text="Convence",font=("times new roman",20),bg="white",fg="black").place(x=10,y=220)
    txt_convence=Entry(Frame2,font=("times new roman",20),textvariable=self.var_convence,bg="lightyellow",fg="blue").place(x=170,y=220,width=100)
    lb_net_salary=Label(Frame2,text="Net Salary",font=("times new roman",20),bg="white",fg="black").place(x=310,y=220)
    txt_net_salary=Entry(Frame2,font=("times new roman",20),textvariable=self.var_netsalary,bg="lightyellow",fg="blue",state="disabled").place(x=450,y=220,width=100)
    #end..............................R5...............#

    #start...............R6.................#
      
    self.btn_save=Button(Frame2,text="Save",font=("times new roman",20),command=self.add,bg="green",fg="black")
    self.btn_save.place(x=20,y=300,height=35)
    btn_calculate=Button(Frame2,text="calculate",command=self.calculate,font=("times new roman",20),bg="orange",fg="black").place(x=220,y=300,height=35)
    btn_clear=Button(Frame2,text="Clear",font=("times new roman",20 ),command=self.clear,bg="red",fg="black").place(x=470,y=300,height=35)
  
    self.btn_update=Button(Frame2,text="update",font=("times new roman",20 ),state=DISABLED,command=self.update,bg="blue",fg="black")
    self.btn_update.place(x=110,y=300,height=35)
    self.btn_delete=Button(Frame2,text="delete",command=self.delete,state=DISABLED,font=("times new roman",20),bg="grey",fg="black")
    self.btn_delete.place(x=360,y=300,height=35)
    


    #end..................R6................#
    Frame3=Frame(self.root,bd=5,relief=RIDGE,bg="white")
    Frame3.place(x=770,y=440,width=580,height=250)
    #.............start cal_Frame....................#
    self.var_txt=StringVar()
    self.var_operator=''
    def btn_click(num):
      self.var_operator=self.var_operator+str(num)
      self.var_txt.set(self.var_operator)
    def result():
      res=str(eval(self.var_operator))
      self.var_txt.set(res)
      self.var_operator=''
    def clear_cal():
      self.var_txt.set('')
      self.var_operator=''
    cal_Frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
    cal_Frame.place(x=0,y=0,width=300,height=241)
    txt_result=Entry(cal_Frame,bg='lightyellow',textvariable=self.var_txt ,font=("times new roman",20,"bold"),justify=RIGHT)
    txt_result.place(x=0,y=0,relwidth=1,height=40)
    btn_7=Button(cal_Frame,text='7',command=lambda:btn_click(7),font=("times new roman",15,"bold")).place(x=0,y=40,w=70,h=50)
    btn_8=Button(cal_Frame,text='8',command=lambda:btn_click(8),font=("times new roman",15,"bold")).place(x=75,y=42,w=70,h=50)
    btn_9=Button(cal_Frame,text='9',command=lambda:btn_click(9),font=("times new roman",15,"bold")).place(x=150,y=42,w=70,h=50)
    btn_divide=Button(cal_Frame,text='/',command=lambda:btn_click("/"),font=("times new roman",15,"bold")).place(x=225,y=42,w=70,h=50)
    btn_4=Button(cal_Frame,text='4',command=lambda:btn_click(4),font=("times new roman",15,"bold")).place(x=0,y=95,w=70,h=50)
    btn_5=Button(cal_Frame,text='5',command=lambda:btn_click(5),font=("times new roman",15,"bold")).place(x=75,y=95,w=70,h=50)
    btn_6=Button(cal_Frame,text='6',command=lambda:btn_click(6),font=("times new rom an",15,"bold")).place(x=150,y=95,w=70,h=50)
    btn_multiply=Button(cal_Frame,text='*',command=lambda:btn_click("*"),font=("times new roman",15,"bold")).place(x=225,y=95,w=70,h=50)
    btn_1=Button(cal_Frame,text='1',command=lambda:btn_click(1),font=("times new roman",15,"bold")).place(x=0,y=150,w=70,h=50)
    btn_2=Button(cal_Frame,text='2',command=lambda:btn_click(2),font=("times new roman",15,"bold")).place(x=75,y=150,w=70,h=50)
    btn_3=Button(cal_Frame,text='3',command=lambda:btn_click(3),font=("times new roman",15,"bold")).place(x=150,y=150,w=70,h=50)
    btn_minus=Button(cal_Frame,text='-',command=lambda:btn_click("-"),font=("times new roman",15,"bold")).place(x=225,y=150,w=70,h=50)
    txt_result.place(x=0,y=0,relwidth=1,height=40)
    btn_0=Button(cal_Frame,text='0',command=lambda:btn_click(0),font=("times new roman",15,"bold")).place(x=0,y=200,w=70,h=50)
    btn_dot=Button(cal_Frame,text='C',command=clear_cal ,font=("times new roman",15,"bold")).place(x=75,y=200,w=70,h=50)
    btn_plus=Button(cal_Frame,text='+',command=lambda:btn_click("+"),font=("times new roman",15,"bold")).place(x=150,y=200,w=70,h=50)
    btn_equal=Button(cal_Frame,text='=',command=result ,font=("times new roman",15,"bold")).place(x=225,y=200,w=70,h=50)
    #.............end cal_Frame....................#


    #.............start salary_Frame....................#
    self.sample=f'''Company Name, XYZ\nAddress: Xyz, Floor4
    -------------------------
    Employee ID\t:  1024
    Salary of\t:  dec
    Generated on\t: 20
    -------------------------
    Total days\t: 31
    Total Present\t: 20
    Total Absent\t: 2
    Convence\t:  Rs.1000
    Medical\t:  Rs.2000
    PF\t:  Rs.1500
    Basic Salary\t:  Rs.354743
    Net Salary\t: Rs.258669
    -------------------------
    This is computer generated 
    silp, not required any
    signature
    '''
    sal_Frame=Frame(Frame3,bg="white" ,bd=2, relief=RIDGE)
    sal_Frame.place(x=300,y=2,width=270,height=235)
    title_sal=Label(sal_Frame,text="Salary Receipt",font=("times new roman",20),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

    sal_Frame1=Frame(sal_Frame,bg="white" ,bd=2, relief=RIDGE)
    sal_Frame1.place(x=0,y=30,relwidth=1,height=180)

    scroll_y=Scrollbar(sal_Frame1,orient=VERTICAL)
    scroll_y.pack(fill=Y,side=RIGHT)

    self.txt_salary_receipt=Text(sal_Frame1,font=("times new roman",15),bg='lightyellow',yscrollcommand=scroll_y.set)
    self.txt_salary_receipt.pack(fill=BOTH,expand=1)
    scroll_y.config(command=self.txt_salary_receipt.yview)
    self.txt_salary_receipt.insert(END,self.sample)



    self.btn_print=Button(sal_Frame,text="Print",font=("times new roman",20 ),state=DISABLED,command=self.print,bg="orange",fg="black")
    self.btn_print.place(x=195,y=210,height=25,width=70)
  
  def show(self):
     try:
          con=pymysql.connect(host='localhost', user='root', db='eps')
          cur=con.cursor()
          cur.execute("select * from empsalary")
          rows=cur.fetchall()
          self.employee_tree.delete(*self.employee_tree.get_children())
          for row in rows:
             self.employee_tree.insert('',END,values=row)
          con.close()
     except Exception as ex:
          messagebox.showerror("Error", f'Error due to: {str(ex)}')


  def calculate(self):
      if self.var_month.get()=='' or self.var_basicsalary.get()=='' or self.var_totaldays.get()=='' or self.var_medical.get()=='' or self.var_convence.get()=='' or self.var_year.get()=='' or self.var_absent.get()=='' or self.var_pf.get()=='' or self.var_netsalary.get():
        messagebox.showerror('Error','All fields are required')
      else:
        per_day=int(self.var_basicsalary.get())/int(self.var_totaldays.get())
        work_day=int(self.var_totaldays.get())-int(self.var_absent.get())
        sal_=per_day*work_day
        deduct=int(self.var_medical.get())+int(self.var_pf.get())
        addition=int(self.var_convence.get())
        net_sal=sal_-deduct+addition
        self.var_netsalary.set(str(round(net_sal,2)))
  


        #....................Receipt....................#
        new_sample=f'''Company Name, XYZ\nAddress: Xyz, Floor4
    -------------------------
    Employee ID\t:  {self.var_empcode.get()}
    Salary of\t:  {self.var_month.get()}-{self.var_year.get()}
    Generated on\t: {str(time.strftime("%d-%M-%Y"))}
    -------------------------
    Total days\t: {self.var_totaldays.get()}
    Total Present\t: {int(self.var_totaldays.get())-int(self.var_absent.get())}
    Total Absent\t: {self.var_absent.get()}
    Convence\t:  Rs.{self.var_convence.get()}
    Medical\t:  Rs.{self.var_medical.get()}
    PF\t:  Rs.{self.var_pf.get()}
    Basic Salary\t:  Rs.{self.var_basicsalary.get()}
    Net Salary\t: Rs.{self.var_netsalary.get()}
    -------------------------
    This is computer generated 
    silp, not required any
    signature
    '''
        self.txt_salary_receipt.delete('1.0',END)
        self.txt_salary_receipt.insert(END,new_sample)


  def clear(self):
     self.var_empcode.set(''),
     self.var_designation.set(''),
     self.var_name.set(''),
     self.var_experience.set(''),
     self.var_gender.set(''),
     self.var_email.set(''),
     self.var_dob.set(''),
     self.var_doj.set(''),
     self.var_ase.set(''),
     self.var_aadhar.set(''),
     self.var_contact.set(''),
     self.var_month.set(''),
     self.var_basicsalary.set(''),
     self.var_totaldays.set(''),
     self.var_medical.set(''),
     self.var_convence.set(''),
     self.var_year.set(''),
     self.var_absent.set(''),
     self.var_pf.set(''),
     self.var_netsalary.set(''), 
     self.txt_address.set('1.0',END)
     self.txt_code.config(state=NORMAL)
     self.btn_save.config(state=NORMAL)
     self.btn_update.config(state=DISABLED)
     self.btn_delete.config(state=DISABLED)
     self.btn_print.config(state=DISABLED)

  def search(self):
    try:
          con=pymysql.connect(host='localhost', user='root', db='eps')
          cur=con.cursor()
          cur.execute("select * from empsalary where empcode=%s",(self.var_empcode.get()))
          row=cur.fetchone()
          if row!=None:
            messagebox.showerror("Error","Invalid Employee ID, Please Try with anothe ID",parent=self.root)
          else:
            self.var_empcode.set(row[0])
            self.var_designation.set(row[1])
            self.var_name.set(row[2])
            self.var_experience.set(row[3])
            self.var_gender.set(row[4])
            self.var_email.set(row[5])
            self.var_dob.set(row[6])
            self.var_doj.set(row[7])
            self.var_age.set(row[8])
            self.var_aadhar.set(row[9])
            self.var_contact.set(row[10])
            self.var_month.set(row[11])
            self.var_basicsalary.set(row[12])
            self.var_totaldays.set(row[13])
            self.var_medical.set(row[14])
            self.var_convence.set(row[15])
            self.var_year.set(row[16])
            self.var_absent.set(row[17])
            self.var_pf.set(row[18])
            self.var_netsalary.set(row[19])
            self.txt_address.delete('1.0',END)
            self.txt_address.insert(END,row[20])
            self.btn_save.config(state=DISABLED)
            self.btn_update.config(state=NORMAL)
            self.btn_delete.config(state=NORMAL)
            self.txt_code.config(state="readonly")
            self.btn_print.config(state=NORMAL)
    except Exception as ex:
          messagebox.showerror("Error", f'Error due to: {str(ex)}')


  def delete(self):
    try:
          con=pymysql.connect(host='localhost', user='root', db='eps')
          cur=con.cursor()
          cur.execute("select * from empsalary where empcode=%s",(self.var_empcode.get()))
          row=cur.fetchone()
          if row!=None:
            messagebox.showerror("Error","Invalid Employee ID, Please Try with anothe ID",parent=self.root)
          else:
            op=messagebox.askyesno("Confirm","Do you really want to delete?")
            if op==True:
               cur.execute("delete from empsalarywhere empcode=%s",(self.var_empcode.get()))
               con.commit()
               con.close()
               messagebox.showinfo("Delete","Employee record deleted successfully",parent=self.root)
               self.clear()
    except Exception as ex:
          messagebox.showerror("Error", f'Error due to: {str(ex)}')
  

  def update(self):
    if self.var_empcode.get()=='' or self.var_netsalary.get()=='' or self.var_name.get()=='':
       messagebox.showerror("Error","Employee details are required")
    else:
      try:
          con=pymysql.connect(host='localhost', user='root', db='eps')
          cur=con.cursor()
          cur.execute("select * from empsalary where empcode=%s",(self.var_empcode.get()))
          row=cur.fetchone()
          if row==None:
            messagebox.showerror("Error","This Employee ID is invalid, Try with valid Employee ID",parent=self.root)
          else:
            cur.execute("UPDATE `empsalary` SET `designation`=%s,`name`=%s,`experience`=%s,`gender`=%s,`email`=%s,`dob`=%s,`doj`=%s,`age`=%s,`aadhar`=%s,`contact`=%s,`month`=%s,`basicsalary`=%s,`totaldays`=%s,`medical`=%s,`convence`=%s,`year`=%s,`absent`=%s,`pf`=%s,`netsalary`=%s,`address`=%s WHERE `empcode`=%s)",
    (
        self.var_designation.get(),
        self.var_name.get(),
        self.var_experience.get(),
        self.var_gender.get(),
        self.var_email.get(),
        self.var_dob.get(),
        self.var_doj.get(),
        self.var_age.get(),
        self.var_aadhar.get(),
        self.var_contact.get(),
        self.var_month.get(),
        self.var_basicsalary.get(),
        self.var_totaldays.get(),
        self.var_medical.get(),
        self.var_convence.get(),
        self.var_year.get(),
        self.var_absent.get(),
        self.var_pf.get(),
        self.var_netsalary.get(),
        self.txt_address.get('1.0',END),
        self.var_empcode.get()
        # self.var_empcode.get() + ".txt"
    )
)


            con.commit()
            con.close()
            messagebox.showinfo("Success","Record updated successfully")
      except Exception as ex:
          messagebox.showerror("Error", f'Error due to: {str(ex)}')


  def add(self):
    if self.var_empcode.get()=='' or self.var_netsalary.get()=='' or self.var_name.get()=='':
       messagebox.showerror("Error","Employee details are required")
    else:
      try:
          con=pymysql.connect(host='localhost', user='root', db='eps')
          cur=con.cursor()
          cur.execute("select * from empsalary where empcode=%s",(self.var_empcode.get()))
          row=cur.fetchall()
          if row!=None:
            messagebox.showerror("Error","This Employee ID is alredy exists, Try with anothe ID",parent=self.root)
          else:
            cur.execute("INSERT INTO empsalary VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
    (
        self.var_empcode.get(),
        self.var_designation.get(),
        self.var_name.get(),
        self.var_experience.get(),
        self.var_gender.get(),
        self.var_email.get(),
        self.var_dob.get(),
        self.var_doj.get(),
        self.var_age.get(),
        self.var_aadhar.get(),
        self.var_contact.get(),
        self.var_month.get(),
        self.var_basicsalary.get(),
        self.var_totaldays.get(),
        self.var_medical.get(),
        self.var_convence.get(),
        self.var_year.get(),
        self.var_absent.get(),
        self.var_pf.get(),
        self.var_netsalary.get(),
        self.txt_address.get('1.0',END),
        # self.var_empcode.get() + ".txt"
    )
)


            con.commit()
            con.close()
            messagebox.showinfo("Success","Record added successfully")
            self.btn_print.config(state=NORMAL)
      except Exception as ex:
          messagebox.showerror("Error", f'Error due to: {str(ex)}')

  def employees(self):
    self.root2 = Toplevel(self.root)
    self.root2.title("Employee Pay Roll Management System")
    self.root2.geometry("900x500+100+60")
    self.root2.config(bg="white")
    
    title = Label(self.root2, text="All Employee Details", font=("times new roman", 30), bg="#262626", fg="white", anchor="w", padx=10)
    title.pack(side=TOP, fill=X)
    
    self.root2.focus_force()
    scrolly = Scrollbar(self.root2, orient=VERTICAL)
    scrollx = Scrollbar(self.root2, orient=HORIZONTAL)
    scrolly.pack(side=RIGHT, fill=Y)
    scrollx.pack(side=BOTTOM, fill=X)
    
    self.employee_tree = ttk.Treeview(self.root2, columns=('empcode', 'designation', 'name', 'experience', 'gender', 'email', 'dob', 'doj', 'age', 'aadhar', 'contact', 'month', 'basicsalary', 'totaldays', 'medical', 'convence', 'year', 'absent', 'pf', 'netsalary', 'address'), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
    
    self.employee_tree.heading('empcode', text='EID')
    self.employee_tree.heading('designation', text='Designation')
    self.employee_tree.heading('name', text='Name')
    self.employee_tree.heading('experience', text='Experience')
    self.employee_tree.heading('gender', text='Gender')
    self.employee_tree.heading('email', text='Email')
    self.employee_tree.heading('dob', text='DOB')
    self.employee_tree.heading('doj', text='DOJ')
    self.employee_tree.heading('age', text='Age')
    self.employee_tree.heading('aadhar', text='Aadhar')
    self.employee_tree.heading('contact', text='Contact')
    self.employee_tree.heading('month', text='Month')
    self.employee_tree.heading('basicsalary', text='Basic Salary')
    self.employee_tree.heading('totaldays', text='Total Days')
    self.employee_tree.heading('medical', text='Medical')
    self.employee_tree.heading('convence', text='Conveyance')
    self.employee_tree.heading('year', text='Year')
    self.employee_tree.heading('absent', text='Absent')
    self.employee_tree.heading('pf', text='PF')
    self.employee_tree.heading('netsalary', text='Net Salary')
    self.employee_tree.heading('address', text='Address')
    
    self.employee_tree['show'] = 'headings'

    self.employee_tree.column('empcode', width=100)
    self.employee_tree.column('designation', width=100)
    self.employee_tree.column('name', width=100)
    self.employee_tree.column('experience', width=100)
    self.employee_tree.column('gender', width=100)
    self.employee_tree.column('email', width=100)
    self.employee_tree.column('dob', width=100)
    self.employee_tree.column('doj', width=100)
    self.employee_tree.column('age', width=100)
    self.employee_tree.column('aadhar', width=100)
    self.employee_tree.column('contact', width=100)
    self.employee_tree.column('month', width=100)
    self.employee_tree.column('basicsalary', width=100)
    self.employee_tree.column('totaldays', width=100)
    self.employee_tree.column('medical', width=100)
    self.employee_tree.column('convence', width=100)
    self.employee_tree.column('year', width=100)
    self.employee_tree.column('absent', width=100)
    self.employee_tree.column('pf', width=100)
    self.employee_tree.column('netsalary', width=100)
    self.employee_tree.column('address', width=200)

    self.employee_tree.pack(fill=BOTH, expand=True)

    self.show()
    self.employee_tree.pack(fill=BOTH, expand=1)
    scrollx.config(command=self.employee_tree.xview)
    scrolly.config(command=self.employee_tree.yview)
    self.show()
    self.root2.mainloop()
  def print(self):
     if self.var_empcode.get():       
        file_=tempfile.mktemp(".txt")
        open(file_,'w').write(self.txt_salary_receipt.get('1.0',END))
        os.startfile(file_,'print')
# Assuming the rest of your class definition follows...

root = Tk()
obj = EmployeeSystem(root)
root.mainloop()

