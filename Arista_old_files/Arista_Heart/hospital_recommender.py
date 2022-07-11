import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
}

def Hospital_Recommender(place):
    hospital_details=[]
    hospital_names1=[]
    def Hospitals_Fetching(details):
        url=f"https://www.google.co.in/search?q={details}"
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        try:
            hospital_names = soup.findAll("div",class_="dbg0pd")
            hospital_ratings=soup.findAll("span",class_="MvDXgc")
            hospital_locations=soup.findAll("a",class_="yYlJEf Q7PwXb VByer")
            for hospital_name_1,hospital_rating_1,hospital_location_1 in zip(hospital_names,hospital_ratings,hospital_locations):
                hospital_name,hospital_rating,hospital_location=hospital_name_1.get_text(),hospital_rating_1.get_text(),hospital_location_1['data-url']
                if hospital_name not in hospital_names1:
                    if '(' in hospital_rating and ')' in hospital_rating:
                        hospital_rating1,hospital_rating_user=list(map(float,hospital_rating.replace('(',' ').replace(')','').split(' ')))
                        hospital_details.append((hospital_name,hospital_rating1,hospital_rating_user,f"https://www.google.com/{hospital_location}"))
                        hospital_names1.append((hospital_name))
        except Exception as e:
            print(e)
            return []
    Hospitals_Fetching(f'best hospitals in {place}')
    Hospitals_Fetching(f"hospitals in {place}")
    if hospital_details==[]:
        return "Sorry cannot get the hospitals available according to the input you may try with other common places"
    # hospital_details

    hospital_details=sorted(hospital_details,key=lambda x:x[1],reverse=True)
    print(hospital_details)


Hospital_Recommender('chengannur')

