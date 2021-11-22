import psycopg2

def updateReceptionist(r_id, address):
    try:
        connection = psycopg2.connect(user="postgres",
                                   password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")

        cursor = connection.cursor()

        sql_update_query = """Update receptionist set recep_address = %s where recep_id = %s"""
        cursor.execute(sql_update_query, (address,r_id))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query = """select * from receptionist where recep_id = %s"""
        cursor.execute(sql_select_query, (r_id,))
        record = cursor.fetchone()
        print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def deleteReceptionist(re_id):
    try:
        connection = psycopg2.connect(user="postgres",
                                   password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")

        cursor = connection.cursor()

        sql_delete_query = """Delete from receptionist where recep_id = %s"""
        cursor.execute(sql_delete_query, (re_id,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def updateRecord(rec_id, desc):
    try:
        connection = psycopg2.connect(user="postgres",
                                   password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")

        cursor = connection.cursor()

        sql_update_query = """Update records set record_description = %s where record_id = %s"""
        cursor.execute(sql_update_query, (desc,rec_id))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query = """select * from records where record_id = %s"""
        cursor.execute(sql_select_query, (rec_id,))
        record = cursor.fetchone()
        print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def deleteDataRecord(rec_id):
    try:
        connection = psycopg2.connect(user="postgres",
                                   password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")

        cursor = connection.cursor()

        sql_delete_query = """Delete from records where record_id = %s"""
        cursor.execute(sql_delete_query, (rec_id,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")        

def Retrieve_All_Data_Receptionist():
    try:
        connection = psycopg2.connect(user="postgres",
                                       password="4219@Pad",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="hospital")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from receptionist"

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")
        for row in mobile_records:
            print("Receptionist Id = ", row[0], )
            print("Receptionist Name = ", row[1])
            print("Receptionist email = ", row[2])
            print("Receptionist address  = ", row[3], "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def Retrieve_Data_By_Receptionist_Id(ID):
    try:
        connection = psycopg2.connect(user="postgres",
                                       password="4219@Pad",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="hospital")
        cursor = connection.cursor()
        
        postgreSQL_select_Query = "select * from receptionist where recep_id=%s"

        cursor.execute(postgreSQL_select_Query,(ID,))
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")
        for row in mobile_records:
            print("Receptionist Id = ", row[0], )
            print("Receptionist Name = ", row[1])
            print("Receptionist email = ", row[2])
            print("Receptionist address  = ", row[3], "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
def Retrieve_All_Data():
    try:
        connection = psycopg2.connect(user="postgres",
                                       password="4219@Pad",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="hospital")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from Nurse"

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")
        for row in mobile_records:
            print("Nurse Id = ", row[0], )
            print("Nurse Name = ", row[1])
            print("Nurse experience = ", row[2])
            print("Room assigned to = ", row[3])
    

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def Retrieve_record_by_id(nurseid_):
    try:
        connection = psycopg2.connect(user="postgres",
                                       password="4219@Pad",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="hospital")
        cursor = connection.cursor()
        
        postgreSQL_select_Query = "select * from Nurse where nurse_id=%s"

        cursor.execute(postgreSQL_select_Query,(nurseid_,))
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")
        for row in mobile_records:
            print("Nurse Id = ", row[0], )
            print("Nurse Name = ", row[1])
            print("Nurse experience = ", row[2])

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def Retrieve_All_Data_ofRoom():
    try:
        connection = psycopg2.connect(user="postgres",
                                       password="4219@Pad",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="hospital")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from Room"

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")
        for row in mobile_records:
            print("Room Id = ", row[0], )
            print("Nurse Id = ", row[1])
            print("Pat experience = ", row[2])
    

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def Retrieve_record_by_id_forroom(roomid_):
    try:
        connection = psycopg2.connect(user="postgres",
                                       password="4219@Pad",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="hospital")
        cursor = connection.cursor()
        
        postgreSQL_select_Query = "select * from Room where room_id=%s"

        cursor.execute(postgreSQL_select_Query,(roomid_,))
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")
        for row in mobile_records:
            print("Room Id = ", row[0], )
            print("Nurse Id = ", row[1])
            print("Pat Id = ", row[2])

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def insert_record_room(record):
    try:
        connection = psycopg2.connect(user="postgres",
                                   password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO Room (room_id,nurse_id,pat_id) VALUES (%s,%s,%s)"""
        cursor.execute(postgres_insert_query, (record))
        connection.commit()

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into receptionist table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into receptionist table", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def deleteRoom(roomid):
    try:
        connection = psycopg2.connect(user="postgres",
                                   password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")

        cursor = connection.cursor()

        sql_delete_query = """Delete from Room where room_id = %s"""
        cursor.execute(sql_delete_query, (roomid,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def insert_record(record):
    try:
        connection = psycopg2.connect(user="postgres",
                                   password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO Nurse (nurse_id,nurse_name,nurse_exp,room_id) VALUES (%s,%s,%s,%s)"""
        cursor.execute(postgres_insert_query, (record))
        connection.commit()

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into receptionist table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into receptionist table", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def deleteNurse(nurseid):
    try:
        connection = psycopg2.connect(user="postgres",
                                   password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")

        cursor = connection.cursor()

        sql_delete_query = """Delete from Nurse where nurse_id = %s"""
        cursor.execute(sql_delete_query, (nurseid,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def insert_record_Receptionist(record):
    try:
        connection = psycopg2.connect(user="postgres",
                                   password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO receptionist (recep_id,recep_name,recep_email,recep_address) VALUES (%s,%s,%s,%s)"""
        cursor.execute(postgres_insert_query, (record))
        connection.commit()

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into receptionist table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into receptionist table", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def Retrieve_All_Data_Records():
    try:
        connection = psycopg2.connect(user="postgres",
                                   password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from records"

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")
        for row in mobile_records:
            print("record Id = ", row[0], )
            print("Doctor Id = ", row[1])
            print("Patient Id = ", row[2])
            print("Record Description  = ", row[3], "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
def Retrieve_Data_By_Record_Id(Rec_Id):
    try:
        connection = psycopg2.connect(user="postgres",
                                   password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")
        cursor = connection.cursor()
        
        postgreSQL_select_Query = "select * from records where record_id=%s"

        cursor.execute(postgreSQL_select_Query,(Rec_Id,))
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")
        for row in mobile_records:
            print("record Id = ", row[0], )
            print("Doctor Id = ", row[1])
            print("Patient Id = ", row[2])
            print("Record Description  = ", row[3], "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def Retrieve_All_Data_Doctor():
    try:
        connection = psycopg2.connect(user="postgres",
                                       password="4219@Pad",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="hospital")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from doctor"

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")
        for row in mobile_records:
            print("Doctor Type = ", row[0], )
            print("Doctor Id = ", row[1])
            print("Doctor Specialization = ", row[2])
            print("Doctor Qualification  = ", row[3])
            print("Doctor Name  = ", row[4])
            print("Doctor Email  = ", row[5], "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def Retrieve_record_by_did(d_id):
    try:
        connection = psycopg2.connect(user="postgres",
                                   password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")
        cursor = connection.cursor()
        
        postgreSQL_select_Query = "select * from doctor where d_no=%s"

        cursor.execute(postgreSQL_select_Query,(d_id,))
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")
        print("Print each row and it's columns values")
        for row in mobile_records:
            print("Doctor Type = ", row[0], )
            print("Doctor Id = ", row[1])
            print("Doctor Specialization = ", row[2])
            print("Doctor Qualification  = ", row[3])
            print("Doctor Name  = ", row[4])
            print("Doctor Email  = ", row[5], "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def insert_record_Record(record):
    try:
        connection = psycopg2.connect(user="postgres",
                                   password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO records (record_id,d_id,p_id,record_description) VALUES (%s,%s,%s,%s)"""
        cursor.execute(postgres_insert_query, (record))
        connection.commit()

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into record table")
    
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into record table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def insert_record_Doctor(record):
    try:
        connection = psycopg2.connect(user="postgres",
                                   password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO doctor (d_type,d_no,d_specialization,d_education,d_name,doc_email) VALUES (%s,%s,%s,%s,%s,%s)"""
        cursor.execute(postgres_insert_query, (record))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into doctor table")
    
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into doctor table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def deleteDoctor(d_id):
    try:
        connection = psycopg2.connect(user="postgres",
                                   password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")

        cursor = connection.cursor()

        sql_delete_query = """Delete from doctor where d_no = %s"""
        cursor.execute(sql_delete_query, (d_id,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def updateDoctor(dno, edu):
    try:
        connection = psycopg2.connect(user="postgres",
                                   password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")

        cursor = connection.cursor()

        sql_update_query = """Update records set d_education = %s where dno = %s"""
        cursor.execute(sql_update_query, (edu,dno))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query = """select * from records where dno = %s"""
        cursor.execute(sql_select_query, (dno,))
        record = cursor.fetchone()
        print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def updateRoom(room_id,pid):
    try:
        connection = psycopg2.connect(user="postgres",
                                   password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")

        cursor = connection.cursor()

        sql_update_query = """Update room set pat_id = %s where room_id = %s"""
        cursor.execute(sql_update_query, (pid,room_id))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query = """select * from room where room_id = %s"""
        cursor.execute(sql_select_query, (room_id,))
        record = cursor.fetchone()
        print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def updateNurse(nurse_id,room_id):
    try:
        connection = psycopg2.connect(user="postgres",
                                   password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")

        cursor = connection.cursor()

        sql_update_query = """Update Nurse set room_id = %s where nurse_id = %s"""
        cursor.execute(sql_update_query, (room_id,nurse_id))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query = """select * from Nurse where nurse_id = %s"""
        cursor.execute(sql_select_query, (nurse_id,))
        record = cursor.fetchone()
        print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def Retrieve_All_Data_Patient():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="4219@Pad",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="hospital")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from Patient"

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")
        for row in mobile_records:
            print("Patient Id = ", row[0], )
            print("Patient Contact Number = ", row[1])
            print("Patient Name = ", row[2])
            print("Date Admitted  = ", row[3])
            print("Date Discharged  = ", row[4], "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def Retrieve_All_Data_Medicine():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="4219@Pad",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="hospital")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from medicine"

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")
        for row in mobile_records:
            print("Price = ", row[0], )
            print("Quantity = ", row[1])
            print("Doctor Id = ", row[2])
            print("Medicine Id  = ", row[3])
            print("Medicine Description  = ", row[4], "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def Retrieve_All_Data_Treatment():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="4219@Pad",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="hospital")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from Treatment"

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")
        for row in mobile_records:
            print("Treatment Id = ", row[0], )
            print("Patient Id = ", row[1])
            print("Treatment Status = ", row[2], "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
def Retrieve_All_Data_Patient_by_ID(p_id):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="4219@Pad",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="hospital")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from Patient where p_no=%s"

        cursor.execute(postgreSQL_select_Query,(p_id,))
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")
        for row in mobile_records:
            print("Patient Id = ", row[0], )
            print("Patient Contact Number = ", row[1])
            print("Patient Name = ", row[2])
            print("Date Admitted  = ", row[3])
            print("Date Discharged  = ", row[4], "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def Retrieve_All_Data_Medicine_by_ID(med_id):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="4219@Pad",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="hospital")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from medicine where med_id=%s"

        cursor.execute(postgreSQL_select_Query,(med_id,))
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")
        for row in mobile_records:
            print("Price = ", row[0], )
            print("Quantity = ", row[1])
            print("Doctor Id = ", row[2])
            print("Medicine Id  = ", row[3])
            print("Medicine Description  = ", row[4], "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def Retrieve_All_Data_Treatment_by_ID(t_id):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="4219@Pad",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="hospital")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from Treatment where t_id=%s"

        cursor.execute(postgreSQL_select_Query,(t_id,))
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")
        for row in mobile_records:
            print("Treatment Id = ", row[0], )
            print("Patient Id = ", row[1])
            print("Treatment Status = ", row[2], "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def insert_record_Patient(record):
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO Patient (p_no,p_contactno,p_name,date_admitted,date_discharged) VALUES (%s,%s,%s,%s,%s)"""
        cursor.execute(postgres_insert_query, (record))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into patient table")
    
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into patient table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def insert_record_Medicine(record):
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO medicine (price,qty,d_number,med_id,med_description) VALUES (%s,%s,%s,%s,%s)"""
        cursor.execute(postgres_insert_query, (record))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into medicine table")
    
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into medicine table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def insert_record_Treatment(record):
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO Treatment (t_id,p_id,is_treated) VALUES (%s,%s,%s)"""
        cursor.execute(postgres_insert_query, (record))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into treatment table")
    
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into treatment table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def deletePatient(p_id):
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")

        cursor = connection.cursor()

        sql_delete_query = """Delete from Patient where p_no = %s"""
        cursor.execute(sql_delete_query, (p_id,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def deleteMedicine(med_id):
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")

        cursor = connection.cursor()

        sql_delete_query = """Delete from medicine where med_id = %s"""
        cursor.execute(sql_delete_query, (med_id,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def deleteTreatment(t_id):
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")

        cursor = connection.cursor()

        sql_delete_query = """Delete from Treatment where t_id = %s"""
        cursor.execute(sql_delete_query, (t_id,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def updatePatient(pno, contactno):
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")

        cursor = connection.cursor()

        sql_update_query = """Update Patient set p_contactno = %s where p_no = %s"""
        cursor.execute(sql_update_query, (contactno,pno))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query = """select * from Patient where p_no = %s"""
        cursor.execute(sql_select_query, (pno,))
        record = cursor.fetchone()
        print(record)
        
    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
def updateMedicine(m_id, price):
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")

        cursor = connection.cursor()

        sql_update_query = """Update medicine set price = %s where med_id = %s"""
        cursor.execute(sql_update_query, (price,m_id))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query = """select * from medicine where med_id = %s"""
        cursor.execute(sql_select_query, (m_id,))
        record = cursor.fetchone()
        print(record)
        
    except (Exception, psycopg2.Error) as error:
        print("Error in Update operation", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def updateTreatment(tid, status):
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="4219@Pad",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hospital")

        cursor = connection.cursor()

        sql_update_query = """Update Treatment set is_treated = %s where t_id = %s"""
        cursor.execute(sql_update_query, (status,tid))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query = """select * from Treatment where t_id = %s"""
        cursor.execute(sql_select_query, (tid,))
        record = cursor.fetchone()
        print(record)
        
    except (Exception, psycopg2.Error) as error:
        print("Error in Update operation", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

print("Hospital Management System")
print("Which Department you want to access:")
print("1. Doctor")
print("2. Patient")
print("3. Medicine")
print("4. Nurse")
print("5. Rooms")
print("6. Treatment")
print("7. Records")
print("8. Receptionist")
ch = int(input('Enter your choice:'))
if ch==1:
    print("Doctor Section!!")
    print("Select what operation you want to do in the Doctors Section:")
    print("1. Retrieve data")
    print("2. Insert data")
    print("3. Delete data")
    print("4. Update data")
    ch7 = int(input('Enter your choice:'))
    if ch7 == 1:
        print("Retrieve Section!")
        print("\t1.Retrieve All Information Related to Doctor")
        print("\t2.Retrieve Information by provididng d_no")
        print("Enter choice(1 or 2):")
        h=int(input())
        if h==1:
            Retrieve_All_Data_Doctor()
        elif h==2:
            print("Enter the d_no")
            d_no=int(input())
            Retrieve_record_by_did(d_no)
        else:
            print("wrong choice")

		
    elif ch7 == 2:
        values = input("enter details: ")
        data = values.split(",")
        record = tuple(data)
        print(record)
        insert_record_Doctor(record)
    elif ch7 == 3:
        print("Delete Section!")
        print("Enter the d_no to delete a record")
        d_no=int(input())
        deleteDoctor(d_no)
    elif ch7 == 4:
        d_id = int(input('enter id of doctor for updation:'))
        edu = input('enter new education:')
        updateReceptionist(d_id, edu)

elif ch==2:
    print("Patient Section!!")
    print("Select what operation you want to do in the Patient's Section:")
    print("1. Retrieve data")
    print("2. Insert data")
    print("3. Delete data")
    print("4. Update data")
    ch7 = int(input('Enter your choice:'))
    if ch7 == 1:
        print("Retrieve Section!")
        print("\t1.Retrieve All Information Related to Patient")
        print("\t2.Retrieve Information by provididng p_no")
        print("Enter choice(1 or 2):")
        h=int(input())
        if h==1:
            Retrieve_All_Data_Patient()
        elif h==2:
            print("Enter the p_no")
            p_no=int(input())
            Retrieve_All_Data_Patient_by_ID(p_no)
        else:
            print("wrong choice")
    elif ch7 == 2:
        print("Insert Section!")
        values = input("Enter details(p_no,p_contactno,p_name,date_admitted,date_discharged): ")
        data = values.split(",")
        record = tuple(data)
        print(record)
        insert_record_Patient(record)
    elif ch7 == 3:
        p_no = int(input("Enter p_no to be deleted:"))
        deletePatient(p_no)
    elif ch7 == 4:
        print("Update Section!")
        p_no = int(input('Enter p_no of record for updation: ')) 
        p_contactno = input('Enter new contactno:')
        updatePatient(p_no, p_contactno)
    else:
        print("Wrong Choice")

elif ch==3:
    print("Medicine Section!!")
    print("Select what operation you want to do in the Medicine Section:")
    print("1. Retrieve data")
    print("2. Insert data")
    print("3. Delete data")
    print("4. Update data")
    ch7 = int(input('Enter your choice:'))
    if ch7 == 1:
        print("Retrieve Section!")
        print("\t1.Retrieve All Information Related to Medicine")
        print("\t2.Retrieve Information by provididng med_id")
        print("Enter choice(1 or 2):")
        h=int(input())
        if h==1:
            Retrieve_All_Data_Medicine()
        elif h==2:
            print("Enter the med_id")
            med_id=int(input())
            Retrieve_All_Data_Medicine_by_ID(med_id)
        else:
            print("wrong choice")
    elif ch7 == 2:
        print("Insert Section!")
        values = input("Enter details(price,qty,d_number,med_id,med_description): ")
        data = values.split(",")
        record = tuple(data)
        print(record)
        insert_record_Medicine(record)
    elif ch7 == 3:
        print("Delete Section!")
        med_id = int(input("Enter med_id to be deleted:"))
        deleteMedicine(med_id)
    elif ch7 == 4:
        print("Update Section!")
        print("Enter the med_id ")
        med_id=input()
        price=input("Enter updated price:")
        updateMedicine(med_id, price)
    else:
        print("Wrong Choice")
elif ch==4:
    print("Nurse Section!!")
    print("Select what operation you want to do in the Nurse Section:")
    print("1. Retrieve data")
    print("2. Insert data")
    print("3. Delete data")
    print("4. Update data")
    ch7 = int(input('Enter your choice:'))
    if ch7 == 1:
        print("\t1.Retrieve All Information Related to Nurse")
        print("\t2.Retrieve Information by provididng Nurse_id")
        print("Enter choice(1 or 2):")
        h=int(input())
        if h==1:
            Retrieve_All_Data()
        elif h==2:
            print("Enter the nurseid:")
            nurseid_=int(input())
            Retrieve_record_by_id(nurseid_)
        else:
            print()

    elif ch7 == 2:
        print("Insert Section!")
        print("Enter the details nurse_id,nurse_name,nurse_exp,room_id")
        values = input("enter details: ")
        data = values.split(",")
        record = tuple(data)
        print(record)
        insert_record(record)
		
    elif ch7 == 3:
        print("Delete Section!")
        print("Enter the nurseid to delete a record")
        nurseid=int(input())
        deleteNurse(nurseid)
		
    elif ch7 == 4:
        print("Update Section!")
        print("Enter the nurseid ")
        nurseid=int(input())
        room_id = input("enter room id:")
        updateNurse(nurseid,room_id)
		
    else:
        print("Wrong Choice")
	
elif ch==5:
    print("Rooms Section!!")
    print("Select what operation you want to do in the Rooms Section:")
    print("1. Retrieve data")
    print("2. Insert data")
    print("3. Delete data")
    print("4. Update data")
    ch7 = int(input('Enter your choice:'))
    if ch7 == 1:
        print("Retrieve Section!")
        print("\t1.Retrieve All Information Related to Rooms")
        print("\t2.Retrieve Information by provididng Room_id")
        print("Enter choice(1 or 2):")
        h=int(input())
        if h == 1:
            Retrieve_All_Data_ofRoom()
            print(1)
        elif h==2:
            print("Enter the roomid:")
            roomid_=int(input())
            Retrieve_record_by_id_forroom(roomid_)
        else:
            print("wrong choice")
    		 
		
    elif ch7 == 2:
        print("Enter the details")
        values = input("enter details: ")
        data = values.split(",")
        record = tuple(data)
        print(record)
        insert_record_room(record)
		
    elif ch7 == 3:
        print("Enter the roomid to delete a record")
        roomid=int(input())
        deleteRoom(roomid)
    elif ch7 == 4:
        print("Enter the roomid ")
        roomid=input()
        pid = input("enter patient id:")
        updateRoom(roomid,pid)
    else:
        print("Wrong Choice")
elif ch==6:
    print("Treatment Section!!")
    print("Select what operation you want to do in the Medicine Section:")
    print("1. Retrieve data")
    print("2. Insert data")
    print("3. Delete data")
    print("4. Update data")
    ch7 = int(input('Enter your choice:'))
    if ch7 == 1:
        print("Retrieve Section!")
        print("\t1.Retrieve All Information Related to Treatment")
        print("\t2.Retrieve Information by provididng t_id")
        print("Enter choice(1 or 2):")
        h=int(input())
        if h==1:
            Retrieve_All_Data_Treatment()
        elif h==2:
            print("Enter the t_id")
            t_id=int(input())
            Retrieve_All_Data_Treatment_by_ID(t_id)
        else:
            print("wrong choice")
    elif ch7 == 2:
        values = input("Enter details(t_id,p_id,is_treated): ")
        data = values.split(",")
        record = tuple(data)
        print(record)
        insert_record_Treatment(record)
    elif ch7 == 3:
        print("Delete Section!")
        t_id = int(input("Enter t_id to be deleted:"))
        deleteTreatment(t_id)
    elif ch7 == 4:
        print("Update Section!")
        print("Enter the t_id ")
        t_id = input()
        is_treated=input("Enter updated status:")
        updateTreatment(t_id, is_treated)
    else:
        print("Wrong Choice")
elif ch==7:
    print("Select what operation you want to do in the Records Section:")
    print("1. Retrieve data")
    print("2. Insert data")
    print("3. Delete data")
    print("4. Update data")
    choice = int(input('Enter your choice:'))
    if choice == 1:
        if choice == 1:
            print("\t1.Retrieve All Information Related to Records")
            print("\t2.Retrieve Information by provididng Records_id")
            print("Enter choice(1 or 2):")
            h=int(input())
            if h == 1:
                Retrieve_All_Data_Records()
            elif h==2:
                print("Enter the roomid:")
                rec_id=int(input())
                Retrieve_Data_By_Record_Id(rec_id)
            else:
                print("wrong choice")
    elif choice == 2:
        values = input("enter details: ")
        data = values.split(",")
        record = tuple(data)
        insert_record_Record(record)

    elif choice == 3:
        id1 = int(input("Enter id to be deleted:"))
        deleteDataRecord(id1)
    elif choice == 4:
        r_id = int(input('enter id of record for updation = '))
        desc = input('enter new description =')
        updateRecord(r_id, desc)
    else:
        print("Wrong Choice")
elif ch==8:
    print("Select what operation you want to do in the Receptionist Section:")
    print("1. Retrieve data")
    print("2. Insert data")
    print("3. Delete data")
    print("4. Update data")
    choice = int(input('Enter your choice:'))
    if choice == 1:
        if choice == 1:
            print("Retrieve Section!")
            print("\t1.Retrieve All Information Related to Receptionist")
            print("\t2.Retrieve Information by provididng Receptionist_id")
            print("Enter choice(1 or 2):")
            h=int(input())
            if h == 1:
                Retrieve_All_Data_Receptionist()
            elif h==2:
                print("Enter the roomid:")
                rec_id=int(input())
                Retrieve_Data_By_Receptionist_Id(rec_id)
            else:
                print("wrong choice")
    elif choice == 2:
        values = input("enter details: ")
        data = values.split(",")
        record = tuple(data)
        insert_record_Receptionist(record)
    elif choice == 3:
        id1 = int(input("Enter id to be deleted:"))
        deleteReceptionist(id1)
    elif choice == 4:
        r_id = int(input('enter id of receptionist for updation:'))
        addr = input('enter new address:')
        updateReceptionist(r_id, addr)
    else:
        print("Wrong Choice")
else:
    print("wrong choice")
