from datetime import datetime
from tkinter import messagebox
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
        self.collection = self.db['chatterji']

    def __del__(self):
        self.client.close()

    def save_data(self, data):
        entry_date = datetime.now().strftime("%d/%m/%y %I:%M:%S %p")
        user = str(data['user'])
        data = {
            "user": user,
            "entry_date": entry_date
        }
        self.collection.insert_one(data)

    def view_records(self):
        records = list(self.collection.find())
        data=(records.pop())
        v=("Timestamp: "+data['entry_date']+"\nUser: "+data['user'])
        messagebox.showinfo("Logging In", v)