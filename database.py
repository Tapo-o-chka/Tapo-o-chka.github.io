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
                functionality TEXT,
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
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS functionality (
                id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT
            )
        ''')
        self.conn.commit()

    def add_order(self, isava, client, type, date, place, warehouse):
        self.cursor.execute('''
            INSERT INTO orders (isava, client, type, date, place, warehouse)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (isava, client, type, date, place, warehouse))
        self.conn.commit()

    def approve_order(self, id):
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

    def decline_order(self, id):
        self.cursor.execute('''
            UPDATE orders
            SET isava = 0
            WHERE id = ?
                AND isava = 1
        ''', (id,))
        self.conn.commit()

    def register_warehouse(self, login, password, email):
        self.cursor.execute('''
            INSERT INTO warehouse (email)
            VALUES (?)
        ''', (email,))
        warehouse_id = self.cursor.lastrowid
        self.cursor.execute('''
            INSERT INTO accounts (login, password, functionality, warehouse)
            VALUES (?, ?, ?, ?)
        ''', (login, password, "3", warehouse_id))
        self.conn.commit()
    def register_user(self, login, password, functionality ,warehouse_id):
        self.cursor.execute('''
            INSERT INTO accounts (login, password, functionality, warehouse)
            VALUES (?, ?, ?, ?)
        ''', (login, password, functionality, warehouse_id))
        self.conn.commit()

    def login(self, login, password):
        self.cursor.execute('''
            SELECT id, warehouse
            FROM accounts
            WHERE login = ?
                AND password = ?
        ''', (login, password))
        return self.cursor.fetchone()

    def get_orders(self, order_type, isava, warehouse):
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
            self.cursor.execute(query, (isava, warehouse))
        else:
            return None

        results = []
        for row in self.cursor.fetchall():
            results.append([row[0],row[2],row[3],row[4],row[5]])
        return results
    def get_functionality(self, id_str=None):
        if id_str:
            ids = id_str.split(',')
            placeholders = ','.join(['?'] * len(ids))
            query = f'SELECT id, name, description FROM functionality WHERE id IN ({placeholders})'
            self.cursor.execute(query, ids)
        else:
            self.cursor.execute('SELECT id, name, description FROM functionality')
        results = []
        for row in self.cursor.fetchall():
            results.append({'id': row[0], 'name': row[1], 'description': row[2]})
        return results
    def lazy_get_functionality(self, user_login):
        self.cursor.execute('SELECT functionality FROM accounts WHERE login = ?', (user_login,))
        id_str = self.cursor.fetchone()[0]

        if id_str:
            ids = id_str.split(',')
            placeholders = ','.join(['?'] * len(ids))
            query = f'SELECT id, name FROM functionality WHERE id IN ({placeholders})'
            self.cursor.execute(query, ids)
        else:
            self.cursor.execute('SELECT id, name FROM functionality')
        results = []
        for row in self.cursor.fetchall():
            results.append({'id': row[0], 'name': row[1]})
        return results

    def edit_functionality(self, functionality, login):
        results = []
        for functional in functionality:
            self.cursor.execute('SELECT id FROM functionality WHERE name = ?', (functional,))
            results.append(self.cursor.fetchone())
        functionality = ''
        for result in results:
            functionality += f'{result[0]},'
        else:
            functionality = functionality[:-1]
        self.cursor.execute('''
            UPDATE accounts
            SET functionality = ?
            WHERE login = ?
        ''', (functionality, login))
        self.conn.commit()
        return functionality

    def add_functionality(self, name, description):
        self.cursor.execute('''
            INSERT INTO functionality (name, description)
            VALUES (?, ?)
        ''', (name, description))
        self.conn.commit()
    def get_warehouse_acounts(self,warehouse_id):
        self.cursor.execute('SELECT functionality FROM accounts WHERE warehouse = ?', (warehouse_id,))
        funcs = [self.get_functionality(func[0]) for func in self.cursor.fetchall()]
        self.cursor.execute('SELECT login, password FROM accounts WHERE warehouse = ?', (warehouse_id,))
        login_password = [acc for acc in self.cursor.fetchall()]
        accounts = [[login_password[i][0],login_password[i][1],funcs[i]] for i in range(len(funcs))]
        return accounts
db = Database('base.db')
db.edit_functionality(['lorem'],'NeTapka')