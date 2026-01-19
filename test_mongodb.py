import os
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
def test_mongodb():
    client = MongoClient(MONGO_DB_URL)
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

if __name__=='__main__':
    test_mongodb()