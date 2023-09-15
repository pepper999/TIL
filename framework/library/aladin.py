import requests

API_KEY = 'ttbhun014141212002'
params = {
    'ttbkey': API_KEY,
    'QueryType': 'ItemNewAll',
    'MaxResults': 10,
    'start': 1,
    'SearchTarget': 'Book',
    'output': 'js',
    'Version': '20131101'
}
URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'

response = requests.get(URL, params=params)
data = response.json()
for item in data['item']:
    print(item['isbn'])
    print(item['title'])
    print(item['pubDate'])