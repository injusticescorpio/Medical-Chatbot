from demo1 import Hospital_Booking
d=Hospital_Booking()
d.create_table()
print("started")
while True:
    while d.fetch()==[]:
        pass
    print(d.fetch())
    d.remove_all_details()