# -*- coding: utf-8 -*-
'''
Experiment 3
SoftDesLab
'''
import sqlite3



conn = sqlite3.connect('experiment3practice6.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS Renter(FirstName TEXT, MiddleInitial TEXT, LastName TEXT, City TEXT, State TEXT, PostalCode INT, TelephoneNo INT, EmailAdress TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS Property(CondoLocationNo INT, CondoLocationName TEXT, Address TEXT, City TEXT, State TEXT, PostalCode INT, CondoUnitNo INT, SquareFootage INT, BedroomNo INT, BathroomNo INT, MaximumNoOfPerson INT, WeeklyRate REAL)")
    c.execute("CREATE TABLE IF NOT EXISTS RentalAgreement(RenterNo INT, FirstName TEXT, MiddleInitial Text, LastName TEXT, Adress TEXT, City TEXT, State TEXT, PostalCode INT, TelephoneNo INT, StartDateOfRental TEXT, EndDateOfRental TEXT, WeeklyRate REAL)")

'''
def data_entry():
    c.execute("INSERT INTO Renter VALUES('Jerald', 'SD','Gonzales', 'M. Francisco Street Lingunan', 'Valenzuela', 1446, 3520632, 'jsgonzales@yehoo.com')")
    c.execute("INSERT INTO Property VALUES(1011, 'Mabuhay', 'M. Francisco Street Lingunan', 'Valenzuela', 'NCR', 1446, 10, 1200, 1, 1, 2, 5000)")   
    c.execute("INSERT INTO RentalAgreement VALUES(1714, 'Jerald', 'SD', 'Gonzales', 'M.Francisco Street Lingunan', 'Valenzuela', 'NCR', 1446, 3520632, '11/06/2019', '11/07/2020', 5000)")
    
    c.execute("INSERT INTO Renter VALUES('Eugene', 'A','Labuac', 'L. Dulalia Street Canumay', 'Paranaque', 1332, 3670544, 'ealabuac@yehoo.com')")
    c.execute("INSERT INTO Property VALUES(1911, 'Makisig', 'L. Dulalia Street Canumay', 'Paranaque', 'NCR', 1332, 21, 1500, 2, 1, 23, 7000)")   
    c.execute("INSERT INTO RentalAgreement VALUES(1811, 'Eugene', 'A', 'Labuac', 'L.Dulalia Street Canumay', 'Paranaque', 'NCR', 1332, 3670544, '2/17/2018', '2/18/2020', 7000)")
    
    
    c.execute("INSERT INTO Renter VALUES('Khaye', 'C','Fajardo', 'R. Masayahin Street PasodeBlas', 'Tondo', 1881, 3620221, 'kcfajardo@yehoo.com')")
    c.execute("INSERT INTO Property VALUES(1109, 'Narra', 'R. Masayahin Street PasodeBlas', 'Tondo', 'NCR', 1771, 09, 1800, 3, 2, 5, 10000)")   
    c.execute("INSERT INTO RentalAgreement VALUES(1611, 'Khaye', 'C', 'Fajardo', 'R.Masayahin Street PasodeBlas', 'Tondo', 'NCR', 1881, 3620221, '6/11/2019', '6/12/2020', 10000)")
    conn.commit()
    c.close()
    conn.close()
'''

def read_from_db_Renter():
    c.execute('SELECT * FROM Renter')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)
        
def read_from_db_Property():
    c.execute('SELECT * FROM Property')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)
        
def read_from_db_RentalAgreement():
    c.execute('SELECT * FROM RentalAgreement')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)
        


create_table()
#data_entry()
read_from_db_Renter()
read_from_db_Property()
read_from_db_RentalAgreement()
c.close
conn.close
