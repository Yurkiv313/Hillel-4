import sqlite3

from faker import Faker


class NamesManager:

    @staticmethod
    def create_table():
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        cursor.execute('''
              CREATE TABLE IF NOT EXISTS users (
              id INTEGER PRIMARY KEY,
              f_name TEXT,
              l_name TEXT,
              email TEXT,
              phone TEXT
              )
          ''')
        fake = Faker()
        for _ in range(200):
            f_name = fake.first_name()
            l_name = fake.last_name()
            email = fake.email()
            phone = fake.phone_number()
            cursor.execute('INSERT INTO users (f_name, l_name, email, phone) VALUES (?, ?, ?, ?)',
                           (f_name, l_name, email, phone))

        conn.commit()

    @staticmethod
    def unique_names():
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM users')
        count = cursor.fetchone()[0]
        if count == 0:
            NamesManager.create_table()
        else:
            query = "SELECT COUNT(DISTINCT f_name) FROM users"
            cursor.execute(query)
            result = cursor.fetchone()
            unique_names_count = result[0] if result else 0
            conn.close()
            return unique_names_count
