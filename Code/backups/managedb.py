import os
import sqlite3
from datetime import datetime
from tkinter import messagebox

from pymongo import MongoClient
client = MongoClient("mongodb+srv://shivdeep:Shubhangi>@chatterji.so23d.mongodb.net/test?retryWrites=true&w=majority")
db=client.get_database('logs')
records=db.chatterji

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, 'database', 'logs.db'))
TABLE_NAME = "CHATTERJI_LOGS"

class ManageDB:
    def __init__(self):
        if not os.path.exists(DB_PATH):
            self.create_database()
        self.conn = sqlite3.connect(DB_PATH)
        self.c = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def create_database(self):
        directory = os.path.split(DB_PATH)[0]
        os.mkdir(directory)
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""CREATE TABLE %s (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                entry_date TEXT NOT NULL,
                user TEXT NOT NULL)""" % TABLE_NAME)
        conn.commit()

    def save_data(self, data):
        entry_date = datetime.now().strftime("%d/%m/%y %I:%M:%S %p")
        user = str(data['user'])
        if not os.path.exists(DB_PATH):
            self.create_database()

        self.c.execute(
            """INSERT INTO %s (entry_date, user)
            VALUES (?, ?)
            """ % TABLE_NAME,
            (
                entry_date,
                user,
            )
        )
        self.conn.commit()

    def view_records(self):
        records = self.c.execute(
            "SELECT entry_date, user FROM %s ORDER BY id desc" % TABLE_NAME)

        for entry in records:
            entry = list(map(str, entry))
            row = (
                    entry[0],
                    entry[1]
                )
            v=("Timestamp: "+entry[0]+"\nUser: "+entry[1])
            messagebox.showinfo("Logging In", v)
            break