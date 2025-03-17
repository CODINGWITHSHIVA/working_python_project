from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector  

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System") 
        self.root.geometry("1540x800+0+0")

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.BloodPressure=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEfect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.patientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="Hospital Management System",fg="brown",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        # ==================Data farame=====================================

        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataframeLeft=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,
                                                font=("times new roman",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=10,pady=30,padx=20,relief=RIDGE,
                                                font=("times new roman",12,"bold"),text="Prescription")
        DataframeRight.place(x=990,y=5,width=460,height=350)

        # ============================buttons frames==========================

        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)

        # ===========================Details frame=============================

        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)

        # ========================DataframeLeft=======================================

        lblNameTablet=Label(DataframeLeft,text="Name of Tablet",font=("times new roman",12,"bold"),padx=2,pady=6,fg="green")
        lblNameTablet.grid(row=0,column=0,sticky=W)


        comNametablet=ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,state="readonly",
                                                        font=("times new roman",12,"bold"), width=35)
        comNametablet["values"]=("Nice","Corona Vacacine","Acetaminophen","Adderall","Amlodiphine","Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)

        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Referance No:",padx=2,fg="green")
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.ref,width=35,fg="red")
        txtref.grid(row=1,column=1)

        lblDosse=Label(DataframeLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4,fg="green")
        lblDosse.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)

        lblNoOftablets=Label(DataframeLeft,font=("arial",12,"bold"),text="No of tablets::",padx=2,pady=6,fg="green")
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.NumberofTablets,width=35)
        txtNoOftablets.grid(row=3,column=1)

        lblLot=Label(DataframeLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6,fg="green")
        lblLot.grid(row=4,column=0,sticky=W)
        lblLot=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Lot,width=35)
        lblLot.grid(row=4,column=1)

        lblissueDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Issue Date",padx=2,pady=6,fg="green")
        lblissueDate.grid(row=5,column=0,sticky=W)
        lblissueDate=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Issuedate,width=35)
        lblissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Exp Date",padx=2,pady=6,fg="green")
        lblExpDate.grid(row=6,column=0,sticky=W)
        lblExpDate=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.ExpDate,width=35)
        lblExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Daily Dose",padx=2,pady=6,fg="green")
        lblDailyDose.grid(row=7,column=0,sticky=W)
        lblDailyDose=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.DailyDose,width=35)
        lblDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataframeLeft,font=("arial",12,"bold"),text="Side Effect",padx=2,pady=6,fg="green")
        lblSideEffect.grid(row=8,column=0,sticky=W)
        lblSideEffect=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.sideEfect,width=35)
        lblSideEffect.grid(row=8,column=1)

        lblFurtherinfo=Label(DataframeLeft,font=("arial",12,"bold"),text="FurtherInformation",padx=2,pady=6,fg="green")
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        lblFurtherinfo=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.FurtherInformation,width=35)
        lblFurtherinfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataframeLeft,font=("arial",12,"bold"),text="Blood Pressure",padx=2,pady=6,fg="green")
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        lblBloodPressure=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.BloodPressure,width=35)
        lblBloodPressure.grid(row=1,column=3)

        lblstorage=Label(DataframeLeft,font=("arial",12,"bold"),text="storage",padx=2,pady=6,fg="green")
        lblstorage.grid(row=2,column=2,sticky=W)
        lblstorage =Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.StorageAdvice,width=35)
        lblstorage.grid(row=2,column=3)

        lblMedicine=Label(DataframeLeft,font=("arial",12,"bold"),text="Medicine",padx=2,pady=6,fg="green")
        lblMedicine.grid(row=3,column=2,sticky=W)
        lblMedicine =Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.HowToUseMedication,width=35)
        lblMedicine.grid(row=3,column=3)

        lblPatientId=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Id",padx=2,pady=6,fg="green")
        lblPatientId.grid(row=4,column=2,sticky=W)
        lblPatientId =Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.PatientId,width=35)
        lblPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(DataframeLeft,font=("arial",12,"bold"),text="NHS Numbere",padx=2,pady=6,fg="green")
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        lbllNhsNumber=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.nhsNumber,width=35)
        lbllNhsNumber.grid(row=5,column=3)

        lblPatientname=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Name",padx=2,pady=6,fg="green")
        lblPatientname.grid(row=6,column=2,sticky=W)
        lblPatientname =Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.patientName,width=35)
        lblPatientname.grid(row=6,column=3)

        lblDateOfbirth=Label(DataframeLeft,font=("arial",12,"bold"),text="Date of birth",padx=2,pady=6,fg="green")
        lblDateOfbirth.grid(row=7,column=2,sticky=W)
        lblDateOfbirth =Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.DateOfBirth,width=35)
        lblDateOfbirth.grid(row=7,column=3)

        lblpateintAddress=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Address",padx=2,pady=6,fg="green")
        lblpateintAddress.grid(row=8,column=2,sticky=W)
        lblpateintAddress =Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.PatientAddress,width=35)
        lblpateintAddress.grid(row=8,column=3)

        # ==============================DataFrameRight================================================================
        self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)



        # ==========================================Buttons=============================================================
        btnPrescription=Button(Buttonframe,command=self.iPrectioption,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(Buttonframe,text="Prescription Data",bg="green",fg="white",font=("arial",12,"bold"),
                                   width=23,padx=2,pady=6,command=self.iPrescriptionDate)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,command=self.update,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,command=self.idelete,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,command=self.clear,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,command=self.iExit,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnExit.grid(row=0,column=5)




        # ==============================================Table==============================================================
        # ===============================================Scrollbar===========================================================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftablet","ref","dose","nooftablets","lot","issuedate",
                                    "expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablet",text="Name Of Tablet")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")
        

        self.hospital_table["show"]="headings"
        self.hospital_table.pack(fill=BOTH,expand=1)



        self.hospital_table.column("nameoftablet",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
       
        self.fatch_data()


        # ===========================Functinality Declration====================================
    def iPrescriptionDate(self):
        if self.Nameoftablets.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="Shushi",
                    password="Tilhar@12",
                    database="mydata"
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO hospital VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.Nameoftablets.get(),
                        self.ref.get(),
                        self.Dose.get(),
                        self.NumberofTablets.get(),
                        self.Lot.get(),
                        self.Issuedate.get(),
                        self.ExpDate.get(),
                        self.DailyDose.get(),
                        self.StorageAdvice.get(),
                        self.nhsNumber.get(),
                        self.patientName.get(),
                        self.DateOfBirth.get(),
                        self.PatientAddress.get(),
                        
                    )
                )
                conn.commit()
                self.fatch_data()
                conn.close()
                messagebox.showinfo("Success", "Data saved successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error saving data: {str(e)}")
    
    
    def update(self):
        ref_value = self.ref.get()  # Get the value from the reference field

        if not ref_value:  # If ref_value is empty
            messagebox.showerror("Error", "Please enter a valid Reference Number")
            return  # Exit the function without performing the update
    
        try:
            conn = mysql.connector.connect(host="localhost", username="Shushi", password="Tilhar@12", database="mydata")
            my_cursor = conn.cursor()
        
            my_cursor.execute("UPDATE hospital SET Nameoftablet=%s, dose=%s, NumbersofTablets=%s, lot=%s, issuedate=%s, expdate=%s, dailydose=%s, storage=%s, nhsnumber=%s, patientName=%s, DOB=%s, patientaddress=%s WHERE `Reference No`=%s", (
                self.Nameoftablets.get(),          
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.Issuedate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                self.nhsNumber.get(),
                self.patientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get(),        
                ref_value,  # Use the valid reference number here
            ))
        
            conn.commit()
            conn.close()
        
            messagebox.showinfo("Success", "Data updated successfully")
            self.fatch_data()  # Fetch updated data
        
        except Exception as e:
            messagebox.showerror("Error", f"Error updating data: {str(e)}")


    
    
    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="Shushi",password="Tilhar@12",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)

            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])          
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.patientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])      




    def iPrectioption(self):
        self.txtPrescription.insert(END,"name of tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Reference No:\t\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"number of tablets:\t\t\t"+self.NumberofTablets.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.Issuedate.get()+"\n")
        self.txtPrescription.insert(END,"Exp:\t\t\t"+self.ExpDate.get()+"\n")
        self.txtPrescription.insert(END,"daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t"+self.sideEfect.get()+"\n")
        self.txtPrescription.insert(END,"Further Information:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert(END,"Storage:\t\t\t"+self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END,"BloodPressure:\t\t\t"+self.BloodPressure.get()+"\n")
        self.txtPrescription.insert(END,"PatientId:\t\t\t"+self.PatientId.get()+"\n")
        self.txtPrescription.insert(END,"NHSNumber:\t\t\t"+self.nhsNumber.get()+"\n")
        self.txtPrescription.insert(END,"patientName:\t\t\t"+self.patientName.get()+"\n")
        self.txtPrescription.insert(END,"DateOfBirth:\t\t\t"+self.DateOfBirth.get()+"\n")
        self.txtPrescription.insert(END,"PatientAddress:\t\t\t"+self.PatientAddress.get()+"\n")

    def idelete(self):
        if not self.ref.get():
            messagebox.showerror("Error", "Reference number is required to delete a patient record.")
            return

        try:
            conn = mysql.connector.connect(host="localhost", username="Shushi", password="Tilhar@12", database="mydata")
            my_cursor = conn.cursor()
        
            query = "DELETE FROM hospital WHERE `Reference No`=%s"
            value = (self.ref.get(),)
            print("Executing query:", query % value)  # Debugging log
            
            my_cursor.execute(query, value)
            conn.commit()
        
            if my_cursor.rowcount == 0:
                messagebox.showwarning("Not Found", "No record found with the given Reference No.")
            else:
                self.fatch_data()
                messagebox.showinfo("Delete", "Patient has been deleted successfully")
        
            conn.close()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"An error occurred: {e}")



    def clear(self):
        self.Nameoftablets.set("")       
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.StorageAdvice.set("")
        self.nhsNumber.set("")
        self.patientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)      
    

    def iExit(self):
        iExit=messagebox.askyesno("Hospital management system","Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return









                

# Main execution
root = Tk()
ob = Hospital(root)
root.mainloop()