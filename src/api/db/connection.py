import psycopg2
import psycopg2.extras
import os

# connection details
DB_NAME = os.environ.get('DB_NAME', 'yacs')
DB_USER = os.environ.get('DB_USER', 'yacs')
DB_HOST = os.environ.get('DB_HOST', '0.0.0.0')
DB_PORT = os.environ.get('DB_PORT', 5432)
DB_PASS = os.environ.get('DB_PASS', 'easy_dev_pass')

class database():
    def connect(self):
        # if we cannot connect to db, then app is useless, so better crash, don't catch error here.
        self.conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT,
        )
        print('-' * 50)
        print("Database connected")
        print('-' * 50)

    def close(self):
        self.conn.close()

    def execute(self, sql, args, isSELECT=True):
        cur = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        ret = None
        try:
            if isSELECT:
                cur.execute(sql, args)
                ret = cur.fetchall()
            else:
                cur.execute(sql, args)
                ret = 0
                self.conn.commit()

        except psycopg2.Error as e:
            print(e)
            return (ret, e)

        return (ret, None)

    def get_connection(self):
        return self.conn


db = database()
db.connect()
