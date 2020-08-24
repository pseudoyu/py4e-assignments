import json
import urllib.request, urllib.parse, urllib.error


data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

address = input('Enter location: ')
print('Retrieving', address)
uh = urllib.request.urlopen(address)

data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
print('Count: ', len(info))

sum = 0
for item in info['comments']:
    sum = sum + item['count']

print('Sum: ', sum)
