from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
from Hospital_Management_system_DB import HP_database_patient,HP_database_doctor,HP_database_appo,HP_database_bill


class HOSPITAL:
        def __init__(self):
            self.vijay = Tk()
            self.vijay.geometry("1920x1080")
            self.vijay.title("Hospital Management System")
            self.vijay.config(bg="grey")
            self.db = HP_database_patient("HS_data.db")
            self.doc_db = HP_database_doctor("HS_data_doctor.db")
            self.appo_db = HP_database_appo("HS_appoin.db")
            self.bill_db  = HP_database_bill("HS_bill.db")
            self.full_ui()
            # Data base File
            print("hii")
            self.vijay.mainloop()
            print("Hello")

        def full_ui(self):
            notebook = ttk.Notebook(self.vijay)
            notebook.pack(fill=BOTH, expand=True)

            self.patient_ui = Frame(notebook,bg="lightyellow")
            notebook.add(self.patient_ui,text="Patient")

            self.doctor_ui = Frame(notebook,bg="lightyellow")
            notebook.add(self.doctor_ui,text="Doctor")

            self.apponment_ui = Frame(notebook,bg="lightyellow")
            notebook.add(self.apponment_ui,text="Appoinment")

            self.billing_ui = Frame(notebook,bg="lightyellow")
            notebook.add(self.billing_ui,text="Billing")

            self.patient_full_ui(),self.doc_full_ui(),self.appoinment_full_ui(),self.billing_full_ui()

            #Patient UI Start
            #Patient UI Start
            #Patient UI Start
        def refresh(self):
              for item in self.patient_tree.get_children():
                    self.patient_tree.delete(item)
              rows = self.db.fetch()
              for row in rows:
                   id_val,fname,lname,gender,dob,phone,email,address,date = row
                   self.patient_tree.insert("","end",values=(id_val,fname,lname,gender,dob,phone,email,address,date))
                   
        def selct_item(self,event):
            selected = self.patient_tree.focus()

            values = self.patient_tree.item(selected,"values")
            if values:
                id_val,fname,lname,gender,dob,phone,email,address,date = values

                self.fname_entry.delete(0,END)
                self.lname_entry.delete(0,END)
                self.dob_entry.delete(0,END)
                self.phone_entry.delete(0,END)
                self.email_entry.delete(0,END)
                self.address_entry.delete(0,END)

                self.fname_entry.insert(0,fname)
                self.lname_entry.insert(0,lname)
                self.dob_entry.insert(0,dob)
                self.phone_entry.insert(0,phone)
                self.email_entry.insert(0,email)
                self.address_entry.insert(0,address)

                    
        def add(self):
                id_val = len(self.patient_tree.get_children()) + 1
                fname = self.fname_entry.get()
                lname = self.lname_entry.get()
                gender = self.gender.get()
                dob = self.dob_entry.get()
                phone = self.phone_entry.get()
                email = self.email_entry.get()
                address = self.address_entry.get()
                date = datetime.now().strftime("%y-%m-%d %H:%M:%S")


                self.patient_tree.insert("","end",values=(id_val,fname,lname,gender,dob,phone,email,address,date))
                self.db.add(fname,lname,gender,dob,phone,email,address,date)

                self.fname_entry.delete(0,END)
                self.lname_entry.delete(0,END)
                self.dob_entry.delete(0,END)
                self.phone_entry.delete(0,END)
                self.email_entry.delete(0,END)
                self.address_entry.delete(0,END)

        def update(self):
            selected = self.patient_tree.focus()
            if not selected:
                 messagebox.showwarning("Error","Please select First")
            
            values = self.patient_tree.item(selected,"values")
            id_val = values[0]

            fname = self.fname_entry.get()
            lname = self.lname_entry.get()
            gender = self.gender.get()
            dob = self.dob_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()
            date = datetime.now().strftime("%y-%m-%d %H:%M:%S")

            self.db.update(id_val,fname,lname,gender,dob,phone,email,address,date)
            self.refresh()

            self.fname_entry.delete(0,END)
            self.lname_entry.delete(0,END)
            self.dob_entry.delete(0,END)
            self.phone_entry.delete(0,END)
            self.email_entry.delete(0,END)
            self.address_entry.delete(0,END)


        def patient_full_ui(self):
            patien_frame = Frame(self.patient_ui)
            patien_frame.pack(fill=BOTH, expand=True)

            # === Input Fields ===
            Label(patien_frame, text="First Name", font=("Arial",15,"bold"), bg="lightblue", width=10).grid(row=0, column=0, padx=10, pady=5, sticky="w")
            self.fname_entry = Entry(patien_frame, font=("Arial",15,"bold"))
            self.fname_entry.grid(row=0, column=1)

            Label(patien_frame, text="Last Name", font=("Arial",15,"bold"), bg="lightblue", width=10).grid(row=0, column=2, padx=10, pady=5, sticky="w")
            self.lname_entry = Entry(patien_frame, font=("Arial",15,"bold"))
            self.lname_entry.grid(row=0, column=3)

            Label(patien_frame, text="Gender", font=("Arial",15,"bold"), bg="lightblue", width=10).grid(row=0, column=4, padx=10, pady=5, sticky="w")
            self.gender = ttk.Combobox(patien_frame, values=["Male","Female"], state="readonly", width=35)
            self.gender.current(0)
            self.gender.grid(row=0, column=5)

            Label(patien_frame, text="DOB (YYYY-MM-DD)", font=("Arial",15,"bold"), bg="lightblue", width=16).grid(row=0, column=6, padx=10, pady=5, sticky="w")
            self.dob_entry = Entry(patien_frame, font=("Arial",15,"bold"))
            self.dob_entry.grid(row=0, column=7)

            Label(patien_frame, text="Phone", font=("Arial",15,"bold"), bg="lightblue", width=10).grid(row=1, column=0, padx=10, pady=5, sticky="w")
            self.phone_entry = Entry(patien_frame, font=("Arial",15,"bold"))
            self.phone_entry.grid(row=1, column=1)

            Label(patien_frame, text="Email", font=("Arial",15,"bold"), bg="lightblue", width=10).grid(row=1, column=2, padx=10, pady=5, sticky="w")
            self.email_entry = Entry(patien_frame, font=("Arial",15,"bold"))
            self.email_entry.grid(row=1, column=3)

            Label(patien_frame, text="Address", font=("Arial",15,"bold"), bg="lightblue", width=10).grid(row=1, column=4, padx=10, pady=5, sticky="w")
            self.address_entry = Entry(patien_frame, font=("Arial",15,"bold"))
            self.address_entry.grid(row=1, column=5)

            Button(patien_frame, text="Add", font=("Arial",15,"bold"), width=10, bg="lightgreen", command=self.add).grid(row=1, column=6, padx=5, pady=10)
            Button(patien_frame, text="Update", font=("Arial",15,"bold"), width=10, bg="red", command=self.update).grid(row=1, column=7, pady=10)

            # === Treeview Frame ===
            tree_frame = Frame(patien_frame)
            tree_frame.grid(row=3, column=0, columnspan=8, padx=10, pady=20, sticky="nsew")

            # Make expandable
            patien_frame.grid_rowconfigure(3, weight=1)
            patien_frame.grid_columnconfigure(0, weight=1)

            tree_frame.grid_rowconfigure(0, weight=1)
            tree_frame.grid_columnconfigure(0, weight=1)

            # Scrollbars
            tree_scroll_y = Scrollbar(tree_frame, orient=VERTICAL)
            tree_scroll_y.grid(row=0, column=1, sticky="ns")

            tree_scroll_x = Scrollbar(tree_frame, orient=HORIZONTAL)
            tree_scroll_x.grid(row=1, column=0, sticky="ew")

            # === Patient Treeview ===
            columns = ("id", "First Name", "Last Name", "Gender", "DOB", "Phone", "Email", "Address", "Created")
            self.patient_tree = ttk.Treeview(
                tree_frame,
                columns=columns,
                show="headings",
                yscrollcommand=tree_scroll_y.set,
                xscrollcommand=tree_scroll_x.set
            )
            self.patient_tree.bind("<<TreeviewSelect>>", self.selct_item)
            self.patient_tree.grid(row=0, column=0, sticky="nsew")

            tree_scroll_y.config(command=self.patient_tree.yview)
            tree_scroll_x.config(command=self.patient_tree.xview)

            for col in columns:
                self.patient_tree.heading(col, text=col)
                self.patient_tree.column(col, width=120, anchor=CENTER, stretch=True)

            self.refresh()



            #Patient UI End
            #Patient UI End
            #Patient UI End
            

            #Doctor UI Start
            #Doctor UI Start
            #Doctor UI Start
        
        def refresh_doc(self):
            for item in self.tree_doc.get_children():
                  self.tree_doc.delete(item)
            rows = self.doc_db.fetch()
            for row in rows:
                 idval,doc_fname,doc_lname,doc_spec,doc_phone,doc_email = row
                 self.tree_doc.insert("","end",values=(idval,doc_fname,doc_lname,doc_spec,doc_phone,doc_email))
                 

        def doc_add(self):
            id_val = len(self.tree_doc.get_children()) + 1
            doc_fname = self.fdoc_name_entry.get()
            doc_lname = self.ldoc_name_entry.get()
            doc_spec = self.spec_entry.get()
            doc_phone = self.doc_phone_entry.get()
            doc_email = self.doc_email_entry.get()

            self.tree_doc.insert("","end",values=(id_val,doc_fname,doc_lname,doc_spec,doc_phone,doc_email))
            self.doc_db.doc_add(doc_fname,doc_lname,doc_spec,doc_phone,doc_email)

            self.fdoc_name_entry.delete(0,END)
            self.ldoc_name_entry.delete(0,END)
            self.spec_entry.delete(0,END)
            self.doc_phone_entry.delete(0,END)
            self.doc_email_entry.delete(0,END) 

        def select_doc(self,event):
             selected = self.tree_doc.focus()

             values = self.tree_doc.item(selected,"values")
            
             if values:
                id_val,doc_fname,doc_lname,doc_spec,doc_phone,doc_email = values

                self.fdoc_name_entry.delete(0,END)
                self.ldoc_name_entry.delete(0,END)
                self.spec_entry.delete(0,END)
                self.doc_phone_entry.delete(0,END)
                self.doc_email_entry.delete(0,END) 

                self.fdoc_name_entry.insert(0,doc_fname)
                self.ldoc_name_entry.insert(0,doc_lname)
                self.spec_entry.insert(0,doc_spec)
                self.doc_phone_entry.insert(0,doc_phone)
                self.doc_email_entry.insert(0,doc_email)

        def update_doc(self):
            selected = self.tree_doc.focus()
            if not selected:
                 messagebox.showwarning("Error","Please select First")
            
            values = self.patient_tree.item(selected,"values")
            id_val = values[0]
            doc_fname = self.fdoc_name_entry.get()
            doc_lname = self.ldoc_name_entry.get()
            doc_spec = self.spec_entry.get()
            doc_phone = self.doc_phone_entry.get()
            doc_email = self.doc_email_entry.get()

            self.tree_doc.insert("","end",values=(id_val,doc_fname,doc_lname,doc_spec,doc_phone,doc_email))
            self.doc_db.update(id_val,doc_fname,doc_lname,doc_spec,doc_phone,doc_email)
            self.refresh_doc()

            self.fdoc_name_entry.delete(0,END)
            self.ldoc_name_entry.delete(0,END)
            self.spec_entry.delete(0,END)
            self.doc_phone_entry.delete(0,END)
            self.doc_email_entry.delete(0,END)


        def doc_full_ui(self):
            doc_frame = Frame(self.doctor_ui)
            doc_frame.pack(fill=BOTH, expand=True)
            doc_frame.grid_propagate(False)

            Label(doc_frame,text="First Name",font=("Arial",15,"bold"),bg="lightblue",width=30).grid(row=0,column=0,padx=10,pady=5,sticky="w")
            self.fdoc_name_entry = Entry(doc_frame,font=("Arial",15,"bold"),width=20)
            self.fdoc_name_entry.grid(row=0,column=1)
            
            Label(doc_frame,text="Last Name",font=("Arial",15,"bold"),bg="lightblue").grid(row=0,column=2,padx=10,pady=5,sticky="w")
            self.ldoc_name_entry = Entry(doc_frame,font=("Arial",15,"bold"),width=20)
            self.ldoc_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky="w")
            
            Label(doc_frame,text="Specification",font=("Arial",15,"bold"),bg="lightblue").grid(row=0,column=4,padx=10,pady=5,sticky="w")
            self.spec_entry = Entry(doc_frame,font=("Arial",15,"bold"),width=20)
            self.spec_entry.grid(row=0,column=5,padx=10)
            
            Label(doc_frame,text="Phone",font=("Arial",15,"bold"),bg="lightblue",width=30).grid(row=1,column=0,padx=10,pady=5,sticky="w")
            self.doc_phone_entry = Entry(doc_frame,font=("Arial",15,"bold"),width=20)
            self.doc_phone_entry.grid(row=1,column=1,padx=10)
            
            Label(doc_frame,text="Email",font=("Arial",15,"bold"),bg="lightblue").grid(row=1,column=2,padx=10,pady=5,sticky="w")
            self.doc_email_entry = Entry(doc_frame,font=("Arial",15,"bold"),width=20)
            self.doc_email_entry.grid(row=1,column=3)

            Button(doc_frame, text="Add", font=("Arial",15,"bold"), width=10, bg="lightgreen", command=self.doc_add).grid(row=1, column=4, padx=5, pady=10)
            Button(doc_frame, text="Update", font=("Arial",15,"bold"), width=10, bg="red", command=self.update_doc).grid(row=1, column=5, pady=10)


            # === Treeview Frame ===
            tree_frame_doc = Frame(doc_frame)
            tree_frame_doc.grid(row=3, column=0, columnspan=8, padx=10, pady=20, sticky="nsew")

            # Make frame expandable
            doc_frame.grid_rowconfigure(3, weight=1)
            doc_frame.grid_columnconfigure(0, weight=1)

            # Scrollbars
            tree_scroll_y = Scrollbar(tree_frame_doc, orient=VERTICAL)
            tree_scroll_y.pack(side=RIGHT, fill=Y)

            tree_scroll_x = Scrollbar(tree_frame_doc, orient=HORIZONTAL)
            tree_scroll_x.pack(side=BOTTOM, fill=X)

            # Columns
            columns = ("id", "First Name", "Last Name", "Specification", "Phone", "Email")
            self.tree_doc = ttk.Treeview(
                tree_frame_doc, 
                columns=columns, 
                show="headings", 
                yscrollcommand=tree_scroll_y.set,
                xscrollcommand=tree_scroll_x.set
            )
            self.tree_doc.pack(fill=BOTH, expand=True)
            self.tree_doc.bind("<<TreeviewSelect>>", self.select_doc)
            self.refresh_doc()

            tree_scroll_y.config(command=self.tree_doc.yview)
            tree_scroll_x.config(command=self.tree_doc.xview)

            for col in columns:
                self.tree_doc.heading(col, text=col)
                self.tree_doc.column(col, width=120, anchor=CENTER, stretch=True)
            #Doctor UI End
            #Doctor UI End
            #Doctor UI End


            #Appoinment UI Start
            #Appoinment UI Start
            #Appoinment UI Start

        def refresh_appo(self):
             for item in self.tree_appo.get_children():
                  self.tree_appo.delete(item)
             rows = self.appo_db.fetch()
             for row in rows:
                  id_val,date,time,reason,patient,doctor = row
                  self.tree_appo.insert("","end",values=(id_val,date,time,reason,patient,doctor))

        def add_appo(self):
             id_val = len(self.tree_appo.get_children()) + 1
             date = self.date_entry.get()
             time = self.time_entry.get()
             reason = self.reason_entry.get()
             patient = self.patient.get()
             doctor = self.doctor.get()

             self.tree_appo.insert("","end",values=(id_val,date,time,reason,patient,doctor))
             self.appo_db.appo_add(date,time,reason,patient,doctor)
            
             self.date_entry.delete(0,END)
             self.time_entry.delete(0,END)
             self.reason_entry.delete(0,END)
             self.patient.delete(0,END)
             self.doctor.delete(0,END)

             messagebox.showinfo("Message",f"Appoinment {patient} Added")


        def load_patients_into_combo(self):
            names = self.db.patient_name()  
            self.patient["values"] = names
        
        def load_doctor_into_combo(self):
            doc_name = self.doc_db.doc_name()
            self.doctor["values"] = doc_name
            

        def appoinment_full_ui(self):
            appo_frame = Frame(self.apponment_ui)
            appo_frame.pack(fill=BOTH, expand=True)

            Label(appo_frame, text="Patient", font=("Arial",15,"bold"), bg="lightblue",width=18).grid(row=0,column=0)

            self.patient = ttk.Combobox(appo_frame, state="readonly", width=35)
            self.patient.grid(row=0, column=1)
            self.load_patients_into_combo()
            self.patient.current(0)

            Label(appo_frame,text="Doctor",font=("Arial",15,"bold"),bg="lightblue",width=18).grid(row=0,column=2)
            self.doctor = ttk.Combobox(appo_frame, state="readonly", width=35)
            self.doctor.grid(row=0, column=3)
            self.load_doctor_into_combo()
            self.doctor.current(0)

            Label(appo_frame,text="Reason",font=("Arial",15,"bold"),bg="lightblue",width=18).grid(row=0,column=4,padx=5)
            self.reason_entry = Entry(appo_frame,font=("Arial",15,"bold"),width=20)
            self.reason_entry.grid(row=0,column=5)

            Label(appo_frame, text="DATE (YYYY-MM-DD)", font=("Arial",15,"bold"), bg="lightblue", width=18).grid(row=1, column=0, padx=10, pady=5, sticky="w")
            self.date_entry = Entry(appo_frame, font=("Arial",15,"bold"))
            self.date_entry.grid(row=1, column=1)

            Label(appo_frame, text="TIME (HH-MM-SS)", font=("Arial",15,"bold"), bg="lightblue", width=18).grid(row=1, column=2, padx=10, pady=5, sticky="w")
            self.time_entry = Entry(appo_frame, font=("Arial",15,"bold"))
            self.time_entry.grid(row=1, column=3)

            Button(appo_frame, text="Book Appoinment", font=("Arial",15,"bold"), width=15, bg="lightgreen",command=self.add_appo).grid(row=1, column=4, padx=5, pady=10)
            

             # === Treeview Frame ===
            tree_frame_appo = Frame(appo_frame)
            tree_frame_appo.grid(row=3, column=0, columnspan=8, padx=10, pady=20, sticky="nsew")

            # Make frame expandable
            appo_frame.grid_rowconfigure(3, weight=1)
            appo_frame.grid_columnconfigure(0, weight=1)

            # Scrollbars
            tree_scroll_y = Scrollbar(tree_frame_appo, orient=VERTICAL)
            tree_scroll_y.pack(side=RIGHT, fill=Y)

            tree_scroll_x = Scrollbar(tree_frame_appo, orient=HORIZONTAL)
            tree_scroll_x.pack(side=BOTTOM, fill=X)

            # Columns
            columns = ("id","Date","Time","Reason", "Patient","Doctor")
            self.tree_appo = ttk.Treeview(
                tree_frame_appo, 
                columns=columns, 
                show="headings", 
                yscrollcommand=tree_scroll_y.set,
                xscrollcommand=tree_scroll_x.set
            )
            self.tree_appo.pack(fill=BOTH, expand=True)
            self.tree_appo.bind("<<TreeviewSelect>>", self.select_doc)
            self.refresh_appo()

            tree_scroll_y.config(command=self.tree_appo.yview)
            tree_scroll_x.config(command=self.tree_appo.xview)

            for col in columns:
                self.tree_appo.heading(col, text=col)
                self.tree_appo.column(col, width=120, anchor=CENTER, stretch=True)
        #Appoinment UI End
        #Appoinment UI End
        #Appoinment UI End

        #Billing UI Start
        #Billing UI Start
        #Billing UI Start
        def load_patient_into_combo(self):
            names = self.appo_db.patient()
            self.patient_bill["values"] = names
        
        def refresh_bill(self):
             for item in self.tree_bill.get_children():
                  self.tree_bill.delete(item)
             rows = self.bill_db.fetch()
             for row in rows:
                  id_val,patient, date, reason, amount, paid = row
                  self.tree_bill.insert("","end",values=(id_val,patient, date, reason, amount, paid))

        def bill_add(self):
             id_val = len(self.tree_bill.get_children()) + 1
             patient = self.patient_bill.get()
             date = self.date_entry_bill.get()
             reason = self.reason_entry_bill.get()
             bill_amt = self.amt_entry_bill.get()
             paid = "Paid"

             self.tree_bill.insert("","end",values=(id_val,patient, date, reason, bill_amt, paid))
             self.bill_db.insert_bill(patient,date,reason,bill_amt,paid)

             self.date_entry_bill.delete(0,END)
             self.reason_entry_bill.delete(0,END)
             self.amt_entry_bill.delete(0,END)

             messagebox.showinfo("Message",f"{patient} Paided")


        def billing_full_ui(self):
            bill_frame = Frame(self.billing_ui)
            bill_frame.pack(fill=BOTH, expand=True)

            Label(bill_frame, text="Patient", font=("Arial",15,"bold"), bg="lightblue", width=18).grid(row=0, column=0)


            # Set values to combobox
            Label(bill_frame,text="Patient",font=("Arial",15,"bold"),bg="lightblue",width=18).grid(row=0,column=2)
            self.patient_bill = ttk.Combobox(bill_frame, state="readonly", width=35)
            self.patient_bill.grid(row=0, column=1)
            self.load_patient_into_combo()
            self.patient_bill.current(0)

            Label(bill_frame, text="DATE (YYYY-MM-DD)", font=("Arial",15,"bold"), bg="lightblue", width=18).grid(row=0, column=2, padx=10, pady=5, sticky="w")
            self.date_entry_bill = Entry(bill_frame, font=("Arial",15,"bold"))
            self.date_entry_bill.grid(row=0, column=3)

            Label(bill_frame, text="Reason", font=("Arial",15,"bold"), bg="lightblue", width=18).grid(row=0, column=4, padx=10, pady=5, sticky="w")
            self.reason_entry_bill = Entry(bill_frame, font=("Arial",15,"bold"))
            self.reason_entry_bill.grid(row=0, column=5)

            Label(bill_frame, text="Amount", font=("Arial",15,"bold"), bg="lightblue", width=18).grid(row=1, column=0, padx=10, pady=5, sticky="w")
            self.amt_entry_bill = Entry(bill_frame, font=("Arial",15,"bold"))
            self.amt_entry_bill.grid(row=1, column=1)

            Button(bill_frame, text="Book Appoinment", font=("Arial",15,"bold"), width=15, bg="lightgreen",command=self.bill_add).grid(row=1, column=2, padx=5, pady=10)

            # === Treeview Frame ===
            tree_frame_bill = Frame(bill_frame)
            tree_frame_bill.grid(row=3, column=0, columnspan=8, padx=10, pady=20, sticky="nsew")

            bill_frame.grid_rowconfigure(3, weight=1)
            bill_frame.grid_columnconfigure(0, weight=1)

            tree_scroll_y = Scrollbar(tree_frame_bill, orient=VERTICAL)
            tree_scroll_y.pack(side=RIGHT, fill=Y)

            tree_scroll_x = Scrollbar(tree_frame_bill, orient=HORIZONTAL)
            tree_scroll_x.pack(side=BOTTOM, fill=X)

            columns = ("id","Patient","Date","Reason","₹Amount","Paid")
            self.tree_bill = ttk.Treeview(
                tree_frame_bill, 
                columns=columns, 
                show="headings", 
                yscrollcommand=tree_scroll_y.set,
                xscrollcommand=tree_scroll_x.set
            )
            self.tree_bill.pack(fill=BOTH, expand=True)
            self.tree_bill.bind("<<TreeviewSelect>>")
            self.refresh_bill()

            tree_scroll_y.config(command=self.tree_bill.yview)
            tree_scroll_x.config(command=self.tree_bill.xview)

            for col in columns:
                self.tree_bill.heading(col, text=col)
                self.tree_bill.column(col, width=120, anchor=CENTER, stretch=True)    
vijay = HOSPITAL() 