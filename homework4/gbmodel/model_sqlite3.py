# gbmodel/model_sqlite3.py

import sqlite3
from .model import AbstractModel

class SQLiteModel(AbstractModel):
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        # Create tables if they don't exist
        with self.conn as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS entries (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                description TEXT,
                                street_address TEXT,
                                type_of_service TEXT,
                                phone_number TEXT,
                                hours_of_operation TEXT,
                                reviews TEXT
                            );''')

    def select(self):
        # Retrieves all entries from the database
        with self.conn as conn:
            cursor = conn.execute('SELECT * FROM entries;')
            entries = cursor.fetchall()
            # Convert row data to dictionary format
            columns = [description[0] for description in cursor.description]
            return [dict(zip(columns, row)) for row in entries]

    def insert(self, name, description, street_address, type_of_service, phone_number, hours_of_operation, reviews):
        # Inserts a new entry into the database
        with self.conn as conn:
            conn.execute('''INSERT INTO entries (name, description, street_address, type_of_service,
                                                 phone_number, hours_of_operation, reviews)
                            VALUES (?, ?, ?, ?, ?, ?, ?);''', 
                            (name, description, street_address, type_of_service, phone_number, hours_of_operation, reviews))
            conn.commit()

# Instantiate the SQLiteModel to create the database and tables if they do not exist
model = SQLiteModel('entries.db')
