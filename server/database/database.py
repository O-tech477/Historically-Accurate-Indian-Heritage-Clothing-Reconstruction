import sqlite3
import os

class Database():
    def __init__(self):

        print("Opening database:", os.path.abspath("promptDatabase.db"))

        self.conn = sqlite3.connect("database/promptDatabase.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS prompts (id VARCHAR PRIMARY KEY, prompt VARCHAR);")

        self.conn.commit()

    def getPrompt(self, garment_type: str):
        self.cur = self.conn.cursor()
        print("THE TYPE RECEIVED HERE IS:", garment_type)
        self.cur.execute(f"SELECT prompt FROM prompts WHERE id='{garment_type}'")


        results = self.cur.fetchone()

        return results[0]

    def closeDB(self):
        self.conn.close()
