import sqlite3
import random

print("Opened database successfully")
global new_name, new_password, new_address, new_pin, new_number,new_status
global p_name, p_address, p_pin, p_number,p_desc,p_id,p_status
global choice1
global id


def hospital_list():
    conn = sqlite3.connect('test1.db')
    c = conn.cursor()
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='HOSPITALS' ''')

    # if the count is 1, then table exists
    if c.fetchone()[0] == 1:
        print('Table exists')
    else:
        conn.execute('''CREATE TABLE HOSPITALS
        (ID INT PRIMARY KEY  NOT NULL,
        NAME  TEXT  NOT NULL,
        PASSWORD TEXT NOT NULL,
        ADDRESS TEXT  NOT NULL,
        PIN INT NOT NULL,
        NUMBER TEXT NOT NULL,
        STATUS TEXT NOT NULL);''')
        print("Table created successfully")
        conn.execute("INSERT INTO HOSPITALS (ID,NAME,PASSWORD,ADDRESS,PIN,NUMBER,STATUS) \
                VALUES (2309, 'MANIPAL','PASSWORD','Rajarajeshwari Nagar', 560061,9876543210,'YES')")
        conn.commit()
    conn.close()

hospital_list()

def patient_list():
    conn = sqlite3.connect('test1.db')
    c = conn.cursor()
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='PATIENTS' ''')

    # if the count is 1, then table exists
    if c.fetchone()[0] == 1:
        print('Table exists')
    else:
        conn.execute('''CREATE TABLE PATIENTS
        (ID INT PRIMARY KEY  NOT NULL,
        NUMBER INT NOT NULL,
        NAME  TEXT  NOT NULL,
        ADDRESS TEXT  NOT NULL,
        PIN INT NOT NULL,
        DESC TEXT NOT NULL,
        STATUS TEXT NOT NULL);''')
        print("Table created successfully")
        conn.execute("INSERT INTO PATIENTS (ID,NUMBER,NAME,ADDRESS,PIN,DESC,STATUS) \
                VALUES (2309,9876543210, 'CHARVI','Rajarajeshwari Nagar', 560061,'EMERGENCY','NOT TAKEN')")
        conn.commit()
    conn.close()


patient_list()
"""
def allocate_volunteer():
    sql_select_query4 = '''select * from VOLUNTEERS where NAME = ? and PASSWORD = ?'''
    cursor = conn.cursor()
    cursor.execute(sql_select_query4, (name,password))
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[3])
        print("PIN = ", row[4])
        print("QUANTITY = ",row[5])
        print("FOOD = ",row[6])
        print("STATUS = ",row[7])
"""

def sign_in(name,password):
    conn = sqlite3.connect('test1.db')
    cursor3 = conn.cursor()
    cursor3.execute("SELECT * FROM HOSPITALS where NAME = ? and PASSWORD = ?",(name,password))
    data = cursor3.fetchall()
    if len(data) !=0:
        sql_select_query4 = '''select * from HOSPITALS where NAME = ? and PASSWORD = ?'''
        cursor = conn.cursor()
        cursor.execute(sql_select_query4,(name,password))
        return True
    else:
        return False
        '''for row in cursor3:
            name1 = row[1]
            password1 = row[2]
        if(name == name1 and password == password1):
            allocate_volunteer()
        else:
            print("Error! Invalid username or Password")
            sign_in()'''


def registration_hospital(new_name,new_password,new_address,new_pin,new_number,new_status):
    conn = sqlite3.connect('test1.db')
    id = random.randint(1000, 9999)
    conn.execute("INSERT OR IGNORE INTO HOSPITALS (ID,NAME,PASSWORD,ADDRESS,PIN,NUMBER,STATUS)\
                VALUES(?,?,?,?,?,?,?)",
                 [id, new_name, new_password,new_address, new_pin, new_number,new_status])
    conn.commit()
    print("Registered successfully")
    conn.close()


def create_patient(p_number, p_name, p_address, p_pin,p_desc):
    conn = sqlite3.connect('test1.db')
    p_id = random.randint(1000,9999)
    p_status = 'NOT TAKEN'
    conn.execute("INSERT OR IGNORE INTO PATIENTS (ID,NUMBER,NAME,ADDRESS,PIN,DESC,STATUS)\
                    VALUES(?,?,?,?,?,?,?)",
                 [p_id,p_number, p_name, p_address, p_pin,p_desc,p_status])
    conn.commit()
    sql_select_query5 = """select * from PATIENTS where NAME = ?"""
    cursor = conn.cursor()
    cursor.execute(sql_select_query5, (p_name,))
    for row in cursor:
        print("ID = ",row[0])
        print("NUMBER = ", row[1])
        print("NAME = ", row[2])
        print("ADDRESS = ", row[3])
        print("PIN = ", row[4])
        print("DESC = ", row[5])
        print("STATUS = ",row[6])
    conn.close()


'''
choice = input("Volunteer or Patient: ")
if(choice == "Volunteer"):
    sign_in()
else:
    create_patient()
'''

def get_patients(v_name):
    conn = sqlite3.connect('test1.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM HOSPITALS where NAME = ? ", (v_name,))

    for row in cursor:
        id = row[0]
    cursor2 = conn.cursor()
    cursor2.execute("SELECT * FROM PATIENTS where ID  = ?", (id,))
    data1 = cursor2.fetchall()
    l = []
    for names in data1:
        l.append(names)
    return l


def deallocate(v_name):
    conn = sqlite3.connect('test1.db')
    sql_update_query = """Update HOSPITALS set STATUS = 'UNAVAILABLE' where NAME =? """
    cursor4 = conn.cursor()
    cursor4.execute(sql_update_query, (v_name,))
    conn.commit()
    conn.close()

def allocate_order(v_name):
    conn = sqlite3.connect('test1.db')
    global v_pin, v_id, p_no

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM HOSPITALS WHERE name = ?", (v_name,))
    #cursor.execute("""select * from VOLUNTEERS where NAME = ?""", (v_name))
    for row in cursor:
        v_id = row[0]
        v_pin = row[4]
    print(v_id)
    print(v_pin)
    cursor1 = conn.cursor()
    cursor1.execute("SELECT * FROM PATIENTS WHERE PIN = ? AND STATUS = ?", (v_pin,'NOT TAKEN'))
    data = cursor1.fetchall()
    if len(data) != 0:
        sql_select_query2 = """select * from PATIENTS where PIN = ? and STATUS = ?"""
        cursor2 = conn.cursor()
        cursor2.execute(sql_select_query2, (v_pin, 'NOT TAKEN'))
        for row in cursor2:
            p_no = row[1]
        sql_update_query1 = """Update PATIENTS set ID = ? where NUMBER = ?"""
        data1 = (v_id, p_no)
        cursor5 = conn.cursor()
        cursor5.execute(sql_update_query1, data1)
        conn.commit()
        sql_update_query = """Update HOSPITALS set STATUS = 'UNAVAILABLE' where ID = ?"""
        cursor4 = conn.cursor()
        cursor4.execute(sql_update_query, (v_id,))
        conn.commit()
        sql_select_query3 = """select * from PATIENTS where PIN = ? and STATUS = ?"""
        cursor3 = conn.cursor()
        cursor3.execute(sql_select_query3, (v_pin,'NOT TAKEN'))
        for row in cursor3:
                   print("ID = ",row[0])
                   print("NUMBER = ", row[1])
                   print("NAME = ", row[2])
                   print("ADDRESS = ", row[3])
                   print("PIN = ", row[4])
                   print("DESC = ", row[5])
                   print("STATUS = ",row[6])
        sql_update_query2 = """Update PATIENTS set STATUS = 'TAKEN' where NUMBER = ?"""
        cursor6 = conn.cursor()
        cursor6.execute(sql_update_query2, (p_no,))
        conn.commit()
        return data
    else:
        cursor1 = conn.cursor()
        cursor1.execute("SELECT * FROM PATIENTS WHERE PIN = ?AND STATUS = ?",
                        (v_pin-1,'NOT TAKEN'))
        data = cursor1.fetchall()
        if(len(data)!=0):
            sql_select_query2 = """select * from PATIENTS where PIN = ? and STATUS = ?"""
            cursor2 = conn.cursor()
            cursor2.execute(sql_select_query2, (v_pin-1,'NOT TAKEN'))
            for row in cursor2:
                p_no = row[1]
            sql_update_query1 = """Update PATIENTS set ID = ? where NUMBER = ?"""
            data1 = (v_id, p_no)
            cursor5 = conn.cursor()
            cursor5.execute(sql_update_query1, data1)
            conn.commit()
            sql_update_query = """Update HOSPITALS set STATUS = 'UNAVAILABLE' where ID = ?"""
            cursor4 = conn.cursor()
            cursor4.execute(sql_update_query, (v_id,))
            conn.commit()
            sql_select_query3 = """select * from PATIENTS where PIN = ? and STATUS = ?"""
            cursor3 = conn.cursor()
            cursor3.execute(sql_select_query3, (v_pin-1,'NOT TAKEN'))

            for row in cursor3:
                   print("ID = ",row[0])
                   print("NUMBER = ", row[1])
                   print("NAME = ", row[2])
                   print("ADDRESS = ", row[3])
                   print("PIN = ", row[4])
                   print("DESC = ", row[5])
                   print("STATUS = ",row[6])
            sql_update_query2 = """Update PATIENTS set STATUS = 'TAKEN' where NUMBER = ?"""
            cursor6 = conn.cursor()
            cursor6.execute(sql_update_query2, (p_no,))
            conn.commit()
            return data
        else:
            cursor1 = conn.cursor()
            cursor1.execute("SELECT * FROM PATIENTS WHERE PIN = ? AND STATUS = ?",
                            (v_pin + 1,'NOT TAKEN'))
            data = cursor1.fetchall()
            if(len(data)!=0):
                sql_select_query2 = """select * from PATIENTS where PIN = ?  and STATUS = ?"""
                cursor2 = conn.cursor()
                cursor2.execute(sql_select_query2, (v_pin + 1,'NOT TAKEN'))
                for row in cursor2:
                    p_no = row[7]
                sql_update_query1 = """Update PATIENTS set ID = ? where NUMBER = ?"""
                data1 = (v_id, p_no)
                cursor5 = conn.cursor()
                cursor5.execute(sql_update_query1, data1)
                conn.commit()
                sql_update_query = """Update HOSPITALS set STATUS = 'UNAVAILABLE' where ID = ?"""
                cursor4 = conn.cursor()
                cursor4.execute(sql_update_query, (v_id,))
                conn.commit()
                sql_select_query3 = """select * from PATIENTS where PIN = ? and STATUS = ?"""
                cursor3 = conn.cursor()
                cursor3.execute(sql_select_query3, (v_pin + 1,'NOT TAKEN'))
                for row in cursor3:
                   print("ID = ",row[0])
                   print("NUMBER = ", row[1])
                   print("NAME = ", row[2])
                   print("ADDRESS = ", row[3])
                   print("PIN = ", row[4])
                   print("DESC = ", row[5])
                   print("STATUS = ",row[6])
                sql_update_query2 = """Update PATIENTS set STATUS = 'TAKEN' where NUMBER = ?"""
                cursor6 = conn.cursor()
                cursor6.execute(sql_update_query2, (p_no,))
                conn.commit()
                return data
    conn.close()