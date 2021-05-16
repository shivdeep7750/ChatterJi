
from datetime import datetime
import certifi

from pymongo import MongoClient
class ManageDB:
    def __init__(self):
        uri = "mongodb+srv://chatterji.so23d.mongodb.net/test?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
        self.client = MongoClient(uri,
                             tls=True,
                             tlsCertificateKeyFile='..\Code\X509-cert-3181802484110607799.pem',
                             tlsCAFile=certifi.where())
        self.db = self.client['logs']
        self.collection = self.db['rooms']

    def __del__(self):
        self.client.close()

    def save_data(self, data):
        entry_date = datetime.now().strftime("%d/%m/%y %I:%M:%S %p")
        room = str(data['room'])
        user = str(data['creator'])
        data = {
            "room": room,
            "entry_date": entry_date,
            "creator": user
        }
        self.collection.insert_one(data)

    def view_records(self):
        records = list(self.collection.find())
        v=[]
        for data in records:
            v.append([data['room'],data['creator']])
        return v