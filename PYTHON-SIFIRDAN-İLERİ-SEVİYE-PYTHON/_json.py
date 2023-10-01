#dict 
import json


# person={"name":"Ali","languages":['Pyhton','c#']}
# result=person['name'] böyle okuur ama json yaparsak okumaz ... 
# result=person['languages']
# result=person['languages'][0]
# personDict={"name":"Ali","languages":['Pyhton','c#']}
# person_jsonolacak='{"name":"Ali","languages":["Pyhton","c#"]}'

#1-import json yap 
#2-Json string to Dict 

# result=json.loads(person_string)
# result=result['name']
# print(type(result))



# with open("person.json") as f:
#     data = json.load(f)
#     print(data["name"])
#     print(data["languages"])


# print(result)

#dict to Json string 


# result=json.dumps(person_dict)
# # print(result)
# # print(type(result))
# # print(result['name'])
# with open('person.json',"w") as f :
#     json.dump(person_dict,f)
    


person_dict = {'name': 'Ali', 'languages': ['python', 'c#', 'java']}
person_string = '{"name": "Ali", "languages": ["Python", "c#"]}'

# JSON dizesini bir Python sözlüğüne çözümleme
person_dict = json.loads(person_string)
result=json.dumps(person_dict,indent=4,sort_keys=True)
print(person_dict)
print(result)
