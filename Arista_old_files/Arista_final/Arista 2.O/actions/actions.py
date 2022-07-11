# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# from .covid19 import Covid_19
# from .disease_symptoms import symptom_prediction
# from .hospital_booking import email_call_sms
# 1. Covid_19 class Depreated#############
class ActionCovid19Place(Action):

    def name(self) -> Text:
        return "action_place"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        place= tracker.get_slot("place")
        full_details = tracker.get_slot("full_details")
        print(f'place=={place}')
        # covid=Covid_19(str(place))

        # dispatcher.utter_message(text=covid.covid_19_details_current())
        # dispatcher.utter_message(text=covid.covid_19_details_total())
        # dispatcher.utter_message(text=covid.total_covid_19())

        #
        # if full_details.lower() in ['yes','yea','ya','why not','oh ya']:
            # dispatcher.utter_message(text=covid.kerala_total())
        dispatcher.utter_message(text=f"place is {place} and full_details is {full_details}")


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
        dispatcher.utter_message(text='hospital_booking')
        print(name,age,place)
        # dispatcher.utter_message(text=email_call_sms(name,age,hospital_name,place))

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
        dispatcher.utter_message(text='disease prediction')
        print(name1,symptoms,other_symptoms)
        # dispatcher.utter_message(text=symptom_prediction(str(name1),str(symptoms),str(other_symptoms)))

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
        print(f"height={height} and weight={weight} and name2=={name2}")

        return []


# 5. Pill remainder function

class ActionPillRemainder(Action):

    def name(self) -> Text:
        return "action_pill_remainder"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        number_of_medicine = tracker.get_slot("number_of_medicine")
        medicine_details = tracker.get_slot("medicine_details")
        print(number_of_medicine,medicine_details)

        return []

# 6. Ambulance service

class ActionAmbulanceService(Action):

    def name(self) -> Text:
        return "action_ambulance_service"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ambulance_place = tracker.get_slot("ambulance_place")
        print(f"Ambulance Place is {ambulance_place}")

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

        return []

#8. Healthy lifestyle function


class ActionHealthylifestyletips(Action):
    def name(self) -> Text:
        return "action_healthy_tips"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print('inside healthy lifestyle tips')
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
        print(f"name3={name3}  food_items=={food_items}  lifestyle ={lifestyle}")
        return []

#10  Health News teller
class ActionHealthyNews(Action):
    def name(self) -> Text:
        return "action_health_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("inside healthy news teller")
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
        contact_number=tracker.get_slot("contact_number")
        print(blood_group,contact_number,name,district,bystander_number)

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
        print(name, place,mobile)
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
        print(name, place,mobile)

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
        print(name, place,mobile)
        return []
# 13 Add Bloodbank representative details

class ActionUpdateAmbulancedriverdetails(Action):
    def name(self) -> Text:
        return "action_update_ambulance_driver"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name=tracker.get_slot("driver_name1")
        place=tracker.get_slot("driver_place1")
        mobile=tracker.get_slot("driver_mobile1")
        print(name, place,mobile)
        return []









