# import json 

# print(json.__file__)


import requests
import json

result=requests.get("https://jsonplaceholder.typicode.com/todos")
result=json.loads(result.text)
# print(result) #<Response [200]>
# print(type(result)) yazdıramayız çünkü json formatta 
# print(result[0])

for i in result :
    if i['userId']==1:
        print(i['title'])
    
    
print(type(result))