import sqlite3

class HP_database_patient:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS data(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fname TEXT NOT NULL,
                lname TEXT NOT NULL,
                gender TEXT NOT NULL,
                dob TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT NOT NULL,
                address TEXT NOT NULL,
                date TEXT NOT NULL
            )
        """)
        self.con.commit()
    
    def fetch(self):
        self.cur.execute("SELECT * FROM data")
        return self.cur.fetchall()
    
    def patient_name(self):
        rows = self.cur.execute("SELECT fname FROM data").fetchall()
        return rows 

    def add(self, fname, lname, gender, dob, phone, email, address, date):
        add = """INSERT INTO data 
                 (fname, lname, gender, dob, phone, email, address, date)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        self.cur.execute(add, (fname, lname, gender, dob, phone, email, address, date))
        self.con.commit()
    
    def update(self,id_val,fname, lname, gender, dob, phone, email, address, date):
        update = ("""
                    UPDATE data SET fname=?,lname=?, gender=?, dob=?, phone=?, email=?, address=?, date=? WHERE id = ?
        """)
        self.cur.execute(update,(fname, lname, gender, dob, phone, email, address, date,id_val))
        self.con.commit()

class HP_database_doctor:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS doc_data(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fname_doc TEXT NOT NULL,
                lname_doc TEXT NOT NULL,
                doc_spec TEXT NOT NULL,
                doc_phone INTEGER NOT NULL,
                doc_email TEXT NOT NULL
                )

            """)
        self.con.commit()
    
    def fetch(self):
        self.cur.execute("SELECT * FROM doc_data")
        return self.cur.fetchall()

    def doc_name(self):
        row = self.cur.execute("SELECT fname_doc FROM doc_data").fetchall()
        return row
    
    def doc_add(self,doc_fname,doc_lname,doc_spec,doc_phone,doc_email):
        doc_add = """
        INSERT INTO doc_data
        (fname_doc,lname_doc,doc_spec,doc_phone,doc_email)
        VALUES(?,?,?,?,?)
        """
        self.cur.execute(doc_add,(doc_fname,doc_lname,doc_spec,doc_phone,doc_email))
        self.con.commit()

    def update(self,id_val,doc_fname,doc_lname,doc_spec,doc_phone,doc_email):
        upadate = """
        UPDATE doc_data SET fname_doc=?,lname_doc=?,doc_spec=?,doc_phone=?,doc_email=? WHERE id=?
        """
        self.cur.execute(upadate,(doc_fname,doc_lname,doc_spec,doc_phone,doc_email,id_val))
        self.con.commit()
        

class HP_database_appo:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS appo_data(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date TEXT NOT NULL,
                        time  TEXT NOT NULL,
                         reason TEXT NOT NULL,
                         patient TEXT NOT NULL,
                         doctor TEXT NOT NULL
                         )
                    """) 
        self.con.commit()
    
    def patient(self):
        name = self.cur.execute("SELECT patient FROM appo_data").fetchall()
        return name
    
    def fetch(self):
        row = self.cur.execute("SELECT * FROM appo_data").fetchall()
        return row
    
    def appo_add(self,date,time,reason,patient,doctor):
        add = """INSERT INTO appo_data
            (date,time,reason,patient,doctor)
            VALUES(?,?,?,?,?)
        """
        self.cur.execute(add,(date,time,reason,patient,doctor))
        self.con.commit()


class HP_database_bill:
    def __init__(self, db):
        import sqlite3
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS bill_data(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient TEXT NOT NULL,
                date TEXT NOT NULL,
                reason TEXT,
                amount REAL NOT NULL,
                paid TEXT
            )
        """)
        self.con.commit()

    def fetch(self):
        row = self.cur.execute("SELECT * FROM bill_data")
        return row


    def insert_bill(self, patient, date, reason, amount, paid):
        self.cur.execute(
            "INSERT INTO bill_data(patient,date,reason,amount,paid) VALUES (?,?,?,?,?)",
            (patient, date, reason, amount, paid)
        )
        self.con.commit()
