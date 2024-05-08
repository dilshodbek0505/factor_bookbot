import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data


    def create_user_table(self):
        sql = """
CREATE TABLE IF NOT EXISTS customers(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
   	name TEXT NOT NULL,
	phone_number TEXT NOT NULL);
"""
        self.execute(sql=sql, commit=True)
    
    def create_book_table(self):
        sql = """
CREATE TABLE IF NOT EXISTS books(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
   	name TEXT NOT NULL,
	author TEXT NOT NULL,
    genre TEXT NOT NULL,
    translator TEXT NOT NULL,
    cover TEXT NOT NULL,
    description TEXT NOT NULL,
    price TEXT NOT NULL,
    image_id TEXT NOT NULL);
"""

        self.execute(sql=sql, commit=True)


    def add_book(self,
                 name: str,
                 author: str,
                 genre: str,
                 translator: str,
                 cover: str,
                 description: str,
                 price: str,
                 image_id: str):
        sql = """INSERT INTO books(name, author, genre, translator, cover, description, price, image_id)
        VALUES(?,?,?,?,?,?,?,?);
"""    
        self.execute(sql, parameters=(name, author, genre, translator, cover, description, price, image_id), commit=True)

    def all_books(self):
        sql = "SELECT * FROM books;"
        return self.execute(sql, fetchall=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")