# -*- coding: utf-8 -*-
"""
Created on Fri May  1 12:25:38 2020

@author: eugen
"""


import sqlite3
conn = sqlite3.connect('Exp3_3.db')
c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS ADVENTURE_TRIP
              (TRIP_ID int,
               TRIP_NAME char,
               START_LOCATION char,
               STATE char,
               DISTANCE int,
               MAX_GRP_SIZE int,
               TYPE char,
               SEASON char)""")
              
def create_entry():
    c.execute("INSERT INTO ADVENTURE_TRIP VALUES(45, 'Jay Peak', 'Jay', 'VT', 8, 8, 'Hiking','Summer')")
    
def view_table():
    c.execute("SELECT * FROM ADVENTURE_TRIP")
    data = c.fetchall()
    for row in data:
        print(row)
        
def delete_table():
    c.execute("DROP TABLE IF EXISTS ADVENTURE_TRIP")

create_table()
create_entry()
delete_table()
conn.commit()
view_table()
c.close()
conn.close()
