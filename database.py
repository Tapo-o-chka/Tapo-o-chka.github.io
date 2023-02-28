import sqlite3
class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def create_tables(self): 
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY,
                login TEXT,
                password TEXT,
                role INTEGER,
                warehouse INTEGER,
                FOREIGN KEY (warehouse) REFERENCES warehouse(id)
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                isava INTEGER,
                client TEXT,
                type TEXT,
                date DATE,
                place TEXT,
                warehouse INTEGER,
                FOREIGN KEY (warehouse) REFERENCES warehouse(id)
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS warehouse (
                id INTEGER PRIMARY KEY,
                email TEXT
            )
        ''')
        self.conn.commit()

    def add_order(self, isava, client, type, date, place, warehouse): #da
        self.cursor.execute('''
            INSERT INTO orders (isava, client, type, date, place, warehouse)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (isava, client, type, date, place, warehouse))
        self.conn.commit()

    def approve_order(self, id): #da
        self.cursor.execute('''
            UPDATE orders
            SET isava = CASE
                WHEN isava = 0 THEN 1
                WHEN isava = 1 THEN 2
                ELSE isava
            END
            WHERE id = ?
        ''', (id,))
        self.conn.commit()

    def decline_order(self, id): #da
        print(self.cursor.execute('''
            UPDATE orders
            SET isava = 0
            WHERE id = ?
                AND isava = 1
        ''', (id,)))
        self.conn.commit()

    def register_warehouse(self, login, password, email): #da
        self.cursor.execute('''
            INSERT INTO warehouse (email)
            VALUES (?)
        ''', (email,))
        warehouse_id = self.cursor.lastrowid
        self.cursor.execute('''
            INSERT INTO accounts (login, password, role, warehouse)
            VALUES (?, ?, 0, ?)
        ''', (login, password, warehouse_id))
        self.conn.commit()
    def login(self, login, password): #id, role, warehouse
        self.cursor.execute('''
            SELECT id, role, warehouse
            FROM accounts
            WHERE login = ?
                AND password = ?
        ''', (login, password))
        return self.cursor.fetchone()
    def get_orders(self, order_type, isava,warehouse): #da ВОЗВРАЩАЕТ СЛОВАРЬ
        if order_type == 'incoming' or order_type == 'outcoming':
            query = '''
                SELECT id, isava, client, type, date, place, warehouse
                FROM orders
                WHERE type = ? AND isava = ? AND warehouse = ?
            '''
            self.cursor.execute(query, (order_type, isava, warehouse))
        elif order_type == 'all':
            query = '''
                SELECT id, isava, client, type, date, place, warehouse
                FROM orders
                WHERE isava = ? AND warehouse = ?
            '''
            self.cursor.execute(query, (isava,warehouse))
        else:
            return None

        results = []
        for row in self.cursor.fetchall():
            results.append([row[0],row[2],row[3],row[4],row[5]])
        return results
