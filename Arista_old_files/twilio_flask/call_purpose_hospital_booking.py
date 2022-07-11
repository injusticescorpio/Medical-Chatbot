from hospital_booking_db import Hospital_Booking
import sqlite3
conn=sqlite3.connect('hospital.db')
curr=conn.cursor()
# table=Hospital_Booking()
# table.create_table()
while True:
    items=curr.execute("SELECT * FROM hospital_booking").fetchall()
    if items!=[]:
        print(items)
    curr.execute('''
    DELETE FROM hospital_booking
    ''')




