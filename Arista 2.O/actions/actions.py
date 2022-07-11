# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from .covid19.covid import Covid_19
from .Medical_news_teller.medical_news_teller import Medicine_News_Teller
from .Hospital_Booking.hospital_booking_db import Hospital_Booking
from .Disease_Prediction_from_symptoms.Disease_prediction_symptoms import Disease_Prediction_Symptom
from .BMI_Calorie_Tracker.Calorie_details import Calorie_Details
from .BMI_Calorie_Tracker.Calorie_Tracker import Calorie_Tracker
from .BMI_Calorie_Tracker.BMI_db import BMI_Information_Store
from .BMI_Calorie_Tracker.bmi_exercise_tracker import BMI
from .Ambulance_service.add_ambulance_users import add_ambulance_driver_details
from .Ambulance_service.add_ambulance_users import  update_ambulance_driver_details
from .Ambulance_service.ambulance_service import Ambulance_Service_Info
from .Healthy_life_style_tips.healthy_tips import healthy_tips_suggest
from .Blood_Bank.add_blood_bank_user import add_representative_details,update_representative_details
from .Blood_Bank.blood_bank_main import Blood_Bank_details
from .Pill_remainder_advanced.pill_remainder_db import Patient
from .Hospital_Recommender.hospital_recommender import Hospital_Recommender
# 1. Covid_19 class Depreated#############
class ActionCovid19Place(Action):

    def name(self) -> Text:
        return "action_place"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        place= tracker.get_slot("place")
        print(f'place=={place}')
        covid_details=Covid_19(place.capitalize())
        try:
            covid_result=covid_details.covid_19_details_current()
            dispatcher.utter_message(text=f"The Covid_19 details of {place} so far is :\n{covid_result}")
        except:
            dispatcher.utter_message(text="Unable to process your request due to server issue")
        return []
# 2. Hospital Booking class
class ActionHospitalBooking(Action):

    def name(self) -> Text:
        return "action_hospital"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name=tracker.get_slot("name")
        age =tracker.get_slot("age")
        hospital_name=tracker.get_slot("hospital_name")
        place=tracker.get_slot("place1")
        print(name,age,place)
        userdata = Hospital_Booking()
        userdata.create_table()
        userdata.insert_details(name, age,hospital_name, place)
        dispatcher.utter_message(text="Forwarded your details to the respective hopsital hospital and I'll let you know via sms or phone call if they are available or not give me some time for that")

        return []
# 3. Disease Symptom class
class ActionDiseasePrediction(Action):

    def name(self) -> Text:
        return "action_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name1=tracker.get_slot("name1")
        symptoms=tracker.get_slot("symptoms")
        other_symptoms=tracker.get_slot("any_other_symptoms")
        print(name1,symptoms,other_symptoms)
        disease_details = Disease_Prediction_Symptom(name1,symptoms,other_symptoms)
        dispatcher.utter_message(text=f'Oke {name1} I think you are suffering from {disease_details.disease_prediction()}')
        dispatcher.utter_message(text=disease_details.disease_description())
        dispatcher.utter_message(text=disease_details.disease_precaution())
        dispatcher.utter_message(text=f"Take rest {name1} See u Bye")
        return []

# 4. BMI calculator function

class ActionBMI(Action):

    def name(self) -> Text:
        return "action_bmi_calculator"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name2=tracker.get_slot("name2")
        height =tracker.get_slot("height")
        weight =tracker.get_slot("weight")
        bmi_user = BMI(name2, weight, height)
        dispatcher.utter_message(text=bmi_user.bmi_calculation())
        weight_category,weight_description=bmi_user.weight_category()
        dispatcher.utter_message(text=f"Your weight belongs to {weight_category} category and {weight_description}")
        dispatcher.utter_message(text=bmi_user.store_details())
        return []


# 5. Pill remainder function

class ActionPillRemainder(Action):

    def name(self) -> Text:
        return "action_pill_remainder"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        number_of_medicine = tracker.get_slot("number_of_medicine")
        name=tracker.get_slot("name_user")
        email=tracker.get_slot("email_user")
        contact=tracker.get_slot("contact_user")
        medicine_details = tracker.get_slot("medicine_details")
        db = Patient()
        db.create_table()
        try:
            db.insert_details(number_of_medicine, name, contact,email,medicine_details)
            dispatcher.utter_message(text='Pill remainder set successfully and I\'ll let you know when to take pills  ')
        except:
            dispatcher.utter_message(text=f"there's some problem while setting the pill remainder make sure that you can only set the pill remainder once at a time")




        return []

# 6. Ambulance service

class ActionAmbulanceService(Action):

    def name(self) -> Text:
        return "action_ambulance_service"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        patient_name=tracker.get_slot("patient_name")
        contact=tracker.get_slot("contact")
        ambulance_place = tracker.get_slot("ambulance_place")
        dispatcher.utter_message(text=Ambulance_Service_Info(patient_name,contact,ambulance_place))
        return []

#7.  Hospital Recommender function

class ActionHospitalRecommender(Action):

    def name(self) -> Text:
        return "action_hospital_recommender"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        hospital_place = tracker.get_slot("hospital_place")
        print(f"Hospital Recommender Place is {hospital_place}")
        hospital_details=Hospital_Recommender(hospital_place)
        dispatcher.utter_message(text=f"These are list of hospitals I know\n")
        counter=0
        for details in hospital_details:
            dispatcher.utter_message(text=f"{counter}. {details[0]} having rating of {details[1]} out of {int(details[2])} users\n Directions: {details[-1]}")
            counter+=1
        return []

#8. Healthy lifestyle function


class ActionHealthylifestyletips(Action):
    def name(self) -> Text:
        return "action_healthy_tips"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=f"here is a tip that will be help you to stay healthy and fit\n{healthy_tips_suggest()}")
        return []

#9. Calorie Tracker

class ActionCalorieTracker(Action):
    def name(self) -> Text:
        return "action_calorie_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name3=tracker.get_slot("name3")
        food_items=tracker.get_slot("food_items")
        lifestyle =tracker.get_slot("lifestyle")
        weight_info =tracker.get_slot("weight_info")
        print(name3,food_items,lifestyle,weight_info)
        calorie_tracker = Calorie_Tracker(name3,food_items,lifestyle,weight_info)
        dispatcher.utter_message(text=calorie_tracker.process())
        return []

#10  Health News teller
class ActionHealthyNews(Action):
    def name(self) -> Text:
        return "action_health_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            news=Medicine_News_Teller()
            health_news=news.details()
            dispatcher.utter_message(text=f"Daily News related to health are as follows:\n{health_news}")
        except:
            dispatcher.utter_message(text='Sorry unable to process your request try after some time')
        return []
#11 Calorie Info

class ActionCalorieInformation(Action):
    def name(self) -> Text:
        return "action_calorie_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        food_info=tracker.get_slot("food_info")
        print(f"food_info =={food_info}")
        calories_tracker = Calorie_Details(food_info)
        dispatcher.utter_message(text=f"calorie information are as follows:\n{calories_tracker.calorie_info()}")
        dispatcher.utter_message(text=calories_tracker.nutrition_info())
        return []

#12 Bloodbank

class ActionBloodBank(Action):
    def name(self) -> Text:
        return "action_blood_bank"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("in blood bank details")
        blood_group=tracker.get_slot("blood_group")
        name=tracker.get_slot("name_of_person")
        no_of_units=tracker.get_slot("no_of_units")
        case =tracker.get_slot("case")
        required_date =tracker.get_slot("required_date")
        admitted_hospital=tracker.get_slot("admitted_hospital")
        bleeding_place =tracker.get_slot("bleeding_place")
        bleeding_time =tracker.get_slot("bleeding_time")
        district =tracker.get_slot("district")
        contact_number =tracker.get_slot("contact_number")
        bystander_number =tracker.get_slot("bystander_number")
        # print(blood_group,contact_number,name,district,bystander_number)
        dispatcher.utter_message(text=Blood_Bank_details(blood_group,name,no_of_units,case,required_date,admitted_hospital,bleeding_place,bleeding_time,district,contact_number,bystander_number))

        return []


# 13 Add Bloodbank representative details

class ActionAddBloodBankdetails(Action):
    def name(self) -> Text:
        return "action_add_blood_bank_repersentative"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name=tracker.get_slot("representative_name")
        place=tracker.get_slot("representative_place")
        mobile=tracker.get_slot("representative_mobile")
        dispatcher.utter_message(text=add_representative_details(name,mobile,place))
        return []


# 14 Update Bloodbank representative details

class ActionUpdateBloodBankdetails(Action):
    def name(self) -> Text:
        return "action_update_blood_bank_repersentative"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name=tracker.get_slot("representative_name1")
        place=tracker.get_slot("representative_place1")
        mobile=tracker.get_slot("representative_mobile1")
        representative_id=tracker.get_slot("representative_id")
        print(name, place,mobile)
        dispatcher.utter_message(text=update_representative_details(name,mobile,place,representative_id))

        return []

# 15 Add Ambulance driver details

class ActionAddAmbulanceDriverdetails(Action):
    def name(self) -> Text:
        return "action_add_ambulance_driver"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name=tracker.get_slot("driver_name")
        place=tracker.get_slot("driver_place")
        mobile=tracker.get_slot("driver_mobile")
        dispatcher.utter_message(text=add_ambulance_driver_details(name,mobile,place))
        return []
# 13 update Ambulance driver details

class ActionUpdateAmbulancedriverdetails(Action):
    def name(self) -> Text:
        return "action_update_ambulance_driver"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name=tracker.get_slot("driver_name1")
        place=tracker.get_slot("driver_place1")
        mobile=tracker.get_slot("driver_mobile1")
        id=tracker.get_slot("driver_id")
        dispatcher.utter_message(text=update_ambulance_driver_details(name,mobile,place, id))
        return []









