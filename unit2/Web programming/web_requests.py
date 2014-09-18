import requests
#r = requests.get('https://api.github.com/events')
#print type(r)

r = requests.get('https://github.com/timeline.json')
print(r.url)
print r.text
r.json()
