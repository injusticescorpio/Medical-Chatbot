'''
References
https://www.verywellfit.com/how-many-calories-do-i-need-each-day-2506873
https://www.medicinenet.com/how_to_calculate_calorie_deficit_for_weight_loss/article.htm
'''

from .BMI_db import BMI_Information_Store
from .Calorie_details import Calorie_Details
import sqlite3
import re
import json
import sqlite3
conn = sqlite3.connect('bmi_info.db')
from bs4 import BeautifulSoup
import requests
import os

class Calorie_Tracker:
    def __init__(self,name,fooditems,lifestyle,weight_info):
        self.name = name
        self.fooditems = fooditems
        self.lifestyle = lifestyle
        self.weight_info=weight_info
    def calories_details_extractor(self,calories_details):
        self.calories = calories_details.lower().split(' ')
        # print(self.calories)
        prev = 0
        for i in range(len(self.calories)):
            if 'calories' in self.calories[i].lower() or "cal" in self.calories[i].lower() or "cals" in self.calories[i].lower():
                prev = i - 1
                if self.calories[prev].isdigit() and prev!=-1:
                    return int(self.calories[prev])
                elif self.calories[prev].isdecimal() and prev!=-1:
                    return int(float(self.calories[prev]))
                break
        front=0
        for i in range(len(self.calories)):
            if 'calories' in self.calories[i].lower() or "cal" in self.calories[i].lower() or "cals" in self.calories[i].lower():
                front =i+1
                if re.sub('[:.$&^*/}{+_#@!)(~]+', '',self.calories[front]).isdecimal() and front!= len(self.calories) :
                    return int(re.sub('[:.$&^*/}{+_#@!)(~]+', '',self.calories[front]))
                break

    def load_low_calorie_food(self):
        data={

  "juice": {

    "Apple Juice": {
      "Calories": 110,
    "quantity": "240 ml",
    "unit": "cal"
    },
   "Carrot Juice": {
    "Calories": 96,
    "quantity": "240 ml",
    "unit": "cal"
   },
   "Coconut Water": {
    "Calories": 46,
    "quantity": "240 ml",
    "unit": "cal"
  },
    "Cranberry Juice": {
      "Calories": 110,
      "quantity": "240 ml",
      "unit": "cal"
    },
    "Cucumber Juice": {
      "Calories": 24,
      "quantity": "240 ml",
      "unit": "cal"
    },
    "Grapefruit Juice": {
      "Calories": 110,
      "quantity": "240 ml",
      "unit": "cal"
    },
    "Lemon Juice": {
      "Calories": 50,
      "quantity": "240 ml",
      "unit": "cal"
    },
    "Lime Juice": {
      "Calories": 50,
      "quantity": "240 ml",
      "unit": "cal"
    },
    "Nestea": {
      "Calories": 50,
      "quantity": "240 ml",
      "unit": "cal"
    },
    "Orange Juice": {
      "Calories": 110,
      "quantity": "240 ml",
      "unit": "cal"
    },
    "Passion Fruit Juice": {
      "Calories": 115,
      "quantity": "240 ml",
      "unit": "cal"
    },
    "Sauerkaut Juice":{
      "Calories": 34,
      "quantity": "240 ml",
      "unit": "cal"
    },
    "Tomato Juice": {
      "Calories": 41,
      "quantity": "240 ml",
      "unit": "cal"
    }

},
  "Soup":{

    "Cabbage Soup": {
      "Calories": 69,
      "quantity": "1 cup 245 grams",
      "unit": "cal"
    },
    "Beef Noodle Soup": {
      "Calories": 83,
      "quantity": "1 cup 244 grams",
      "unit": "cal"
    },
    "Beef Soup": {
      "Calories": 70,
      "quantity": "1 cup 213 grams",
      "unit": "cal"
    },
    "Carrot Ginger Soup": {
      "Calories": 95,
      "quantity": "1 cup 381 grams",
      "unit": "cal"
    },
    "Chicken Noodle Soup": {
      "Calories": 62,
      "quantity": "1 cup 248 grams",
      "unit": "cal"
    },
    "Cream of Mushroom Soup": {
      "Calories": 97,
      "quantity": "1 cup 248 grams",
      "unit": "cal"
    },
    "Cream of Potato Soup": {
      "Calories": 73,
      "quantity": "1 cup 244 grams",
      "unit": "cal"
    },
    "Cream of Onion Soup": {
      "Calories": 107,
      "quantity": "1 cup 244 grams",
      "unit": "cal"
    },
    "French Onion Soup": {
      "Calories": 56,
      "quantity": "1 cup 243 grams",
      "unit": "cal"
    },
    "Minestrone": {
      "Calories": 82,
      "quantity": "1 cup 241 grams",
      "unit": "cal"
    },
    "Mushroom Soup": {
      "Calories": 85,
      "quantity": "1 cup 244 grams",
      "unit": "cal"
    },
    "Onion Soup": {
      "Calories": 56,
      "quantity": "1 cup 243 grams",
      "unit": "cal"
    },
    "Oxtail Soup": {
      "Calories": 68,
      "quantity": "1 cup 244 grams",
      "unit": "cal"
    },
    "Pumpkin Soup": {
      "Calories": 71,
      "quantity": "1 cup 245 grams",
      "unit": "cal"
    },
    "Scotch Broth": {
      "Calories": 80,
      "quantity": "1 cup 241 grams",
      "unit": "cal"
    },
    "Tomato Soup": {
      "Calories": 74,
      "quantity": "1 cup 248 grams",
      "unit": "cal"
    },
    "Vegetable Soup": {
      "Calories": 67,
      "quantity": "1 cup 241 grams",
      "unit": "cal"
    }
  },

  "dishes-meals": {

    "Black Pudding": {
      "Calories": 101,
      "quantity": "1 pudding 40 grams",
      "unit": "cal"
    },
    "California Roll": {
      "Calories": 33,
      "quantity": "1 roll 35 grams",
      "unit": "cal"
    },
    "Collard Greens": {
      "Calories": 13,
      "quantity": "1 cup 45 grams",
      "unit": "cal"
    },
    "Deviled Eggs": {
      "Calories": 62,
      "quantity": "1/2 egg 31 grams",
      "unit": "cal"
    },
    "Dim Sum": {
      "Calories": 37,
      "quantity": "1 piece 19 grams",
      "unit": "cal"
    },
    "Fired Shrimp": {
      "Calories": 75,
      "quantity": "1 shrimp 27 grams",
      "unit": "cal"
    },
    "Roast Beef": {
      "Calories": 23,
      "quantity": "1 slice 21 grams",
      "unit": "cal"
    },
    "Samosa": {
      "Calories": 107,
      "quantity": "1 samosa 50 grams",
      "unit": "cal"
    },
    "Sausage Roll": {
      "Calories": 101,
      "quantity": "1 roll 34 grams",
      "unit": "cal"
    },
    "Sloppy Joe": {
      "Calories": 101,
      "quantity": "1/2 cup 142 grams",
      "unit": "cal"
    },
    "Yorkshire Pudding": {
      "Calories": 83,
      "quantity": "1 pudding 15 grams",
      "unit": "cal"
    }
  },
  "nuts-seeds": {

    "Acorn": {
      "Calories": 108,
      "quantity": "1 oz. 28.35 grams",
      "unit": "cal"
    },
    "Breadfruit": {
      "Calories": 53,
      "quantity": "1 oz. 28.35 grams",
      "unit": "cal"
    },
    "Ginkgo Nuts": {
      "Calories": 51,
      "quantity": "1 oz. 28.35 grams",
      "unit": "cal"
    },
    "Lima Beans": {
      "Calories": 88,
      "quantity": "1/2 cup 124 grams",
      "unit": "cal"
    },
    "Lotus Seed": {
      "Calories": 25,
      "quantity": "1 oz. 28.35 grams",
      "unit": "cal"
    },
    "Peas": {
      "Calories": 117,
      "quantity": "1 cup 145 grams",
      "unit": "cal"
    },
    "Poppy Seeds": {
      "Calories": 42,
      "quantity": "1 tbsp 8.8 grams",
      "unit": "cal"
    },
    "Radish Seeds": {
      "Calories": 16,
      "quantity": "1 cup 38 grams",
      "unit": "cal"
    },
    "Sweet Chestnut": {
      "Calories": 54,
      "quantity": "1 oz. 28.35 grams",
      "unit": "cal"
    },
    "Watermelon": {
      "Calories": 86,
      "quantity": "1 wedge 286 grams",
      "unit": "cal"
    }

  },

  "ice-cream": {

    "Chocolate Chip Ice Cream": {
      "Calories": 155,
      "quantity": "1 scope 72 grams",
      "unit": "cal"
    },
    "Chocolate Ice Cream": {
      "Calories": 156,
      "quantity": "1 scope 72 grams",
      "unit": "cal"
    },
    "Coffee Ice Cream": {
      "Calories": 170,
      "quantity": "1 scope 72 grams",
      "unit": "cal"
    },
    "Cookie Dough Ice Cream": {
      "Calories": 130,
      "quantity": "1/2 cup 65 grams",
      "unit": "cal"
    },
    "French Vanilla Ice Cream": {
      "Calories": 145,
      "quantity": "1 scope 72 grams",
      "unit": "cal"
    },
    "Ice Milk": {
      "Calories": 164,
      "quantity": "1 scope 103 grams",
      "unit": "cal"
    },
    "Magnolia": {
      "Calories": 166,
      "quantity": "1 scope 72 grams",
      "unit": "cal"
    },
    "Schwan's": {
      "Calories": 177,
      "quantity": "1 scope 72 grams",
      "unit": "cal"
    },
    "Snickers Ice Cream": {
      "Calories": 180,
      "quantity": "1 bar 50 grams",
      "unit": "cal"
    },
    "Solero": {
      "Calories": 75,
      "quantity": "1 solero 75 grams",
      "unit": "cal"
    },
    "Sundae": {
      "Calories": 155,
      "quantity": "1 scope 72 grams",
      "unit": "cal"
    },
    "Vanilla Ice Cream": {
      "Calories": 145,
      "quantity": "1 scope 72 grams",
      "unit": "cal"
    },
    "Mint Chocolate Chip Ice Cream": {
      "Calories": 172,
      "quantity": "1 scope 72 grams",
      "unit": "cal"
    }
  }

}
        self.juice = data['juice']
        self.soup = data['Soup']
        self.dishes_meals=data['dishes-meals']
        self.nuts_seeds=data['nuts-seeds']
        self.ice_cream=data['ice-cream']

        self.juice = sorted(self.juice.items(), key=lambda x: x[1]['Calories'])
        self.soup = sorted(self.soup.items(), key=lambda x: x[1]['Calories'])
        self.dishes_meals=sorted(self.dishes_meals.items(), key=lambda x: x[1]['Calories'])
        self.nuts_seeds=sorted(self.nuts_seeds.items(), key=lambda x: x[1]['Calories'])
        self.ice_cream=sorted(self.ice_cream.items(), key=lambda x: x[1]['Calories'])
        # print(f"juice=={self.juice}")
        # print(f"soup=={self.soup}")
        # print(f"dishes_meals=={self.dishes_meals}")
        # print(f"nuts_seeds=={self.nuts_seeds}")
        # print(f"ice_cream=={self.ice_cream}")
    def getting_calorie_details(self,calories,weight_info):
        print(f"calories in getting{calories} and weight_info {weight_info} and lifestyle=={self.lifestyle}")
        if 'reduce' in weight_info:
            print("entered in if")
            if self.lifestyle=='1' or self.lifestyle=='2':
                calories-=500
            elif self.lifestyle=='3' or self.lifestyle=='4':
                calories-=400
            elif self.lifestyle=='5':
                calories-=300
            print(f"calories in getting {calories}")
            return calories
        elif 'maintain' in weight_info:
            return calories
        else:
            return calories
    def calculate_total_calorie_food(self,weight):
        return int(round(float(weight)* 2.205*15.0))
    def process(self):
        self.user = BMI_Information_Store()
        self.user_details = self.user.retrieve_user_details(self.name)
        print(self.user_details)
        if self.user_details is None or self.user_details==[]:
            return "First you calculate the bmi then only use this feature :)"
        self.total_user_calories = self.calculate_total_calorie_food(self.user_details[0][-1])
        print(self.total_user_calories)
        self.calories_needed=self.getting_calorie_details(self.total_user_calories,self.weight_info)
        print(f"calorie need {self.calories_needed}")
        self.calories_reduced=self.total_user_calories-self.calories_needed
        print(f"calories reduced {self.calories_reduced}")
        if self.calories_needed is None:
            return "Invalid option provided please provide correct option"
        '''
        calories calculation steps
        '''
        self.calories_user_entered=0
        for food in self.fooditems.split(","):
            c=Calorie_Details(food)
            food_calories=self.calories_details_extractor(c.calorie_info())
            if food_calories is None:
                return f"""Sorry I don't have any idea about the {food} food item.
                Please try again :)
                """
            self.calories_user_entered+=food_calories
        # print(f"calories from user is {self.calories_user_entered}")
        # print(f"calories need :{self.calories_needed}")
        def needed_to_eat_food():
            if self.calories_user_entered<self.calories_needed:
                self.load_low_calorie_food()
                remaining_calories=self.calories_needed-self.calories_user_entered
                remaining_food_items=[]
                prev_remaining_food_items=[]
                juice1=soup1=dishes_meals1=nuts_seeds1=ice_cream1=0
                while remaining_calories>0 and (soup1<len(self.soup) or juice1<len(self.juice)):
                    if soup1<len(self.soup) and (remaining_calories-self.soup[soup1][1]['Calories'])>=0:
                        remaining_calories-=self.soup[soup1][1]['Calories']
                        remaining_food_items.append(f"{self.soup[soup1][0]} having calories {self.soup[soup1][1]['Calories']} {self.soup[soup1][1]['unit']} and quantity {self.soup[soup1][1]['quantity']}")
                        soup1+=1
                    if juice1<len(self.juice) and (remaining_calories- self.juice[juice1][1]['Calories'])>=0:
                        remaining_calories -= self.juice[juice1][1]['Calories']
                        remaining_food_items.append(f"{self.juice[juice1][0]} having calories {self.juice[juice1][1]['Calories']} {self.juice[juice1][1]['unit']} and quantity {self.juice[juice1][1]['quantity']}")
                        juice1+=1
                    if dishes_meals1<len(self.dishes_meals) and (remaining_calories-self.dishes_meals[dishes_meals1][1]['Calories'])>=0:
                        remaining_calories-=self.dishes_meals[dishes_meals1][1]['Calories']
                        remaining_food_items.append(f"{self.dishes_meals[dishes_meals1][0]} having calories {self.dishes_meals[dishes_meals1][1]['Calories']} {self.dishes_meals[dishes_meals1][1]['unit']} and quantity {self.dishes_meals[dishes_meals1][1]['quantity']}")
                        dishes_meals1+=1
                    if nuts_seeds1<len(self.nuts_seeds) and (remaining_calories-self.nuts_seeds[nuts_seeds1][1]['Calories'])>=0:
                        remaining_calories-=self.nuts_seeds[nuts_seeds1][1]['Calories']
                        remaining_food_items.append(f"{self.nuts_seeds[nuts_seeds1][0]} having calories {self.nuts_seeds[nuts_seeds1][1]['Calories']} {self.nuts_seeds[nuts_seeds1][1]['unit']} and quantity {self.nuts_seeds[nuts_seeds1][1]['quantity']}")
                        nuts_seeds1+=1
                    if ice_cream1<len(self.ice_cream) and(remaining_calories-self.ice_cream[ice_cream1][1]['Calories'])>=0:
                        remaining_calories-=self.ice_cream[ice_cream1][1]['Calories']
                        remaining_food_items.append(f"{self.ice_cream[ice_cream1][0]} having calories {self.ice_cream[ice_cream1][1]['Calories']} {self.ice_cream[ice_cream1][1]['unit']} and quantity {self.ice_cream[ice_cream1][1]['quantity']}")
                        ice_cream1+=1
                    if remaining_food_items!=prev_remaining_food_items:
                        prev_remaining_food_items=remaining_food_items[:]
                    else:
                        return [remaining_calories,remaining_food_items]
            else:
                return "You need to remove some food items which are high in calories"
        if type(needed_to_eat_food())==list:
            remaining_calories,remaining_food_items=needed_to_eat_food()
            self.calories_reduced+=remaining_calories
            return f'By following the particular lifestyle that you mentioned and following the below menu you will eventually reduce {self.calories_reduced} calories for sure\n'+'\n'.join(map(lambda x:'⦿ '+x,remaining_food_items))
        else:
            return needed_to_eat_food()





# c=Calorie_Tracker('Arjun','chicken curry',3,'reduce weight')
# # # # c.load_low_calorie_food()
# print(c.process())
