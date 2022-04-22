import json
import requests

""" ********** Reading JSON Data from API & converting it to Python Dictionary ********** """

url = 'https://api.publicapis.org/entries'
req = requests.get(url)
text = req.text
print (type(text)) 

# json.loads - It will create a Python Dictionary
parsed_dict = json.loads(text)
print (type(parsed_dict))
print ((parsed_dict['entries'][2]))

""" ********** Normal JSON String. Converting back to Python Dict ********** """

normal_json_str = '{"id":101,"parent_id":null, "name":"XYZ", "is_owner":true}'
print(normal_json_str)
print(type(normal_json_str))

# json.loads - It will create a Python Dictionary
parsed_dict = json.loads(normal_json_str)

print(parsed_dict)
print(type(parsed_dict))

""" ********** Reading JSON Data from file & converting it to Python Dictionary ********** """

with open('sampledata.json') as f:
    data = json.load(f)
    print (type(data))
    print ((data['entries'][2]))
    
""" ********** Converting Python List to JSON Data & printing it. Output is string ********** """

my_dict = { 'Aphabets' : { 'A':{'Fruit':'Apple','Object':'Aeroplane'},'B':{'Fruit':'Banana','Object':'Ball'}} , 
             'Numbers'  : {  0:'Zero', 1:'One'} 
           } 
           
print(type(my_dict))
# Just Print Json data
print(json.dumps(my_dict, indent=4))

""" ********** Converting Python List to JSON Data & saving it as file ********** """

my_dict = { 'Aphabets' : { 'A':{'Fruit':'Apple','Object':'Aeroplane'},'B':{'Fruit':'Banana','Object':'Ball'}} , 
             'Numbers'  : {  0:'Zero', 1:'One'} 
           } 
           
print(type(my_dict))
# Export the JSON in file
json.dump(my_dict, open ('export.json', 'w'), indent=4)

print(json.dumps(my_dict, indent=4))
