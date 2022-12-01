import json

# define a list of multiple dictionaries
data = '''
[
  { "id" : "001",
    "Attribute" : "2",
    "Name" : "Chuck"
  } ,
  { "id" : "009",
    "Attribute" : "7",
    "Name" : "Sally"
  }
]'''

#use JSON parser to return list
info = json.loads(data)
print(f'User count: {len(info)}\n')

#iterate through each list element (ie. visit each contained dictionary)
for item in info:
    for key in item:  # returns list --- item.keys():
        print(f"{key}:  {item[key]}")
    print()
        
    # print('Name', item['name'])
    # print('Id', item['id'])
    # print('Attribute', item['x'])

