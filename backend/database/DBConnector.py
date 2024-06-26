import sqlite3
import os

DB_DIR = os.path.dirname(os.path.realpath(__file__))
DB_PATH = os.path.join(DB_DIR, 'banco.db')

#This is not thread safe, as this will not be paralleled processed for now this is fine
class SingletonMeta(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance
        return self._instances[self]

class DBConnect(metaclass=SingletonMeta):
    def __init__(self):
        self.value = None
        self.con = sqlite3.connect(DB_PATH, check_same_thread=False)

    def __del__(self):
        self.con.close()

    def runQuery(self, query, parameters = []):
        cursor = self.con.cursor()
        cursor.execute(query, parameters)
        result = cursor.fetchall()
        cursor.close()

        return result
