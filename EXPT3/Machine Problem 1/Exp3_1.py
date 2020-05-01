# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:16:49 2020

@author: eugen
"""
import sqlite3
conn = sqlite3.connect('Exp3_1.db')
c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS participant
              (ParticipantNum int,
               LastName text,
               FirstName text,
               Address text,
               City text,
               State text,
               PostalCode text,
               PhoneNum text,
               DateOfBirth text)""")
          
    c.execute("""CREATE TABLE IF NOT EXISTS class
              (ClassNum int,
               ClassDescription text,
               MaxNum int,
               ClassFee num)""")

    c.execute("""CREATE TABLE IF NOT EXISTS classParticipant
              (ClassNum int,
               ParticipantNum int,
               Date text,
               ActualParticipant text)""")

def create_entry():
    c.execute("INSERT INTO participant VALUES(1,'Labuac','Eugene','B22 L10 Kalayaan Village','Pasay','N/A','1300','09052719521','09/03/99')")
    c.execute("INSERT INTO participant VALUES(2,'Gonzales','Jerald','B15 L6 Mapulang Lupa','Valenzuela','N/A','1448','09052152187','10/10/99')")
    c.execute("INSERT INTO participant VALUES(3,'Fajardo','Khaye','B15 L6 Tondo','Manila','N/A','1003','09216940154','11/06/99')")

    c.execute("INSERT INTO class VALUES(1,'Section: Einstein',24,25000.00)")   
    c.execute("INSERT INTO class VALUES(2,'Section: Faraday',28,27070.00)")   
    c.execute("INSERT INTO class VALUES(3,'Section: Mendeleev',25,26500.50)")   
    
    c.execute("INSERT INTO classParticipant VALUES(1,1,'04/29/2020','Jerald Gonzales')") 
    c.execute("INSERT INTO classParticipant VALUES(1,2,'04/29/2020','Eugene Labuac')") 
    c.execute("INSERT INTO classParticipant VALUES(1,3,'04/29/2020','Khaye Fajardo')") 

def view_class():
    c.execute("SELECT * FROM class")
    data = c.fetchall()
    for row in data:
        print(row)

def view_classParticipant():
    c.execute("SELECT * FROM classParticipant")
    data = c.fetchall()
    for row in data:
        print(row)

def view_participant():
    c.execute("SELECT * FROM participant")
    data = c.fetchall()
    for row in data:
        print(row)

     
        
create_table()
#create_entry()
conn.commit()
view_participant()
c.close()
conn.close()
