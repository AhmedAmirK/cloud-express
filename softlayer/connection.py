'''
@author Ahmed Hassan Koshek
'''
from pymongo import MongoClient
from pprint import pprint as pp

class connect:
    def start_connection(self):
        self.client = MongoClient("mongodb://ahmedkoshek:cloud99.@ds111124.mlab.com:11124/cloud-recovery")
        db = client.cloud-recovery
        self.col = db.users
        self.get_USERS()
        print("Connected to Databse")

    def close_connection(self):
        self.client.close()
        print("Disconnected")


    def get_USERS(self):
        self.users = self.col.find({})
        self.count = len(self.users)

    def refresh(self):
        self.get_users()

    def __init__(self):
        self.client = None
        self.col = None
        self.users = None
        self.count = None
