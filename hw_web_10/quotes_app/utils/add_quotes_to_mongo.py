import json
from bson.objectid import ObjectId

from pymongo import MongoClient


client = MongoClient('mongodb+srv://nadiadanilova1301:Jbt7g26q2lWDxlKE@cluster0.ww1p23e.mongodb.net/')

db = client.quotes_app

with open('quotes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
        })
        