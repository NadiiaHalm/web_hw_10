from pymongo import MongoClient


def get_mongodb():
    client = MongoClient('mongodb+srv://nadiadanilova1301:Jbt7g26q2lWDxlKE@cluster0.ww1p23e.mongodb.net/')
    db = client.quotes_app
    return db
