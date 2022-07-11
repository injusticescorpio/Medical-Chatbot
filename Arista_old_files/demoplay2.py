import json

with open('D:\S8 Project\Arista_Heart\lowcalorie.json') as json_file:
    data = json.load(json_file)
    json_file.close()
juice=data['juice']
soup=data['Soup']
juice=sorted(juice.items(),key=lambda x:x[1]['Calories'])
soup=sorted(soup.items(),key=lambda x:x[1]['Calories'])
print(juice[0])
