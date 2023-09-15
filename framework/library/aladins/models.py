from django.db import models
import requests

# Create your models here.
class Aladin(models.Model):
    isbn = models.CharField(max_length=10)
    title = models.TextField()
    pub_date = models.DateField()

    @classmethod
    def insert_data(cls):
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
            params = {
                'isbn' : item['isbn'],
                'title' : item['title'],
                'pub_date' : item['pubDate']
            }
            book = cls(**params)
            book.save()