import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS mosques(
        ID INTEGER PRIMARY KEY,
        NAME TEXT,
        Type TEXT,
        Address TEXT,
        Coordinates TEXT,
        Imam_Name TEXT)''')
        self.conn.commit()

    def display(self):
        self.cur.execute('SELECT * FROM mosques')
        rows = self.cur.fetchall()
        return rows

    def search(self, name):
        self.cur.execute('SELECT * FROM mosques WHERE NAME LIKE "%' + name + '%"')
        rows = self.cur.fetchall()
        return rows

    def insert(self, name, type, address, coordinates, imam_name):
        self.cur.execute('INSERT INTO mosques VALUES (NULL,? , ?, ?, ?, ?)', (name, type, address, coordinates, imam_name))
        self.conn.commit()

    def delete(self, id):
        self.cur.execute('DELETE FROM mosques WHERE ID=?', (id,))
        self.conn.commit()

    def update(self, id, name, type, address, coordinates, imam_name):
        self.cur.execute('UPDATE mosques SET NAME=?, Type=?, Address=?, Coordinates=?, Imam_Name=? WHERE ID=?', (name, type, address, coordinates, imam_name, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
