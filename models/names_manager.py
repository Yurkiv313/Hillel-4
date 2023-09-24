import sqlite3


class Names:

    def __init__(self, f_name, l_name, email, phone):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.phone = phone

    @staticmethod
    def unique_names():
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        query = "SELECT COUNT(DISTINCT f_name) FROM users"
        cursor.execute(query)
        result = cursor.fetchone()
        unique_names_count = result[0] if result else 0
        conn.close()
        return unique_names_count
