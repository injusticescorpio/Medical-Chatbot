from .ambulance_service_db import Ambulance_Service
from faker import Faker
fake = Faker('en-IN')

user=Ambulance_Service()
user.create_table()
def fake_details_generating():
    user.insert_details('Arjun','+919074774118','Chengannur,Kerala')

    location=['Mannar,Kerala','Kollam,Kerala','Kottayam,Kerala','Kochi,Kerala','Chengannur,Kerala','Palakkad,Kerala','Kannur,Kerala','Chennai,Tamil nadu','Adoor,Kerala','Thrissur,Kerala','Alappuzha,Kerala','Munnar,Kerala','Vagamon,Kerala','Thiruvananthapuram,Kerala','Ernakulam,Kerala','Pathanamthitta,Kerala','Changanassery,Kerala','Kallissery,kerala']
    for _ in range(len(location)):
        user.insert_details(fake.first_name_male(),fake.phone_number(),location[_])

print(user.fetch())
    # print(user.fetch()[-1][0])
if user.fetch()==[] or len(user.fetch())<10:
    print("fake details created")
    fake_details_generating()


def add_ambulance_driver_details(name,mobile,place):
    name_from_db=[i[1] for i in user.fetch()]
    print(name_from_db)
    if name.title() not in name_from_db:
        user.insert_details(name.title(), mobile, place.title())
        return f"{name} your user id created with id number {user.fetch()[-1][0]} save this id for further usage"
    else:
        return "User already exists with same name"

def update_ambulance_driver_details(name,mobile,place,id):
    user.update_details(name.title(),mobile,place.title(),id)
    return f"user successfully updated"
