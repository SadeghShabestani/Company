from sqlite3 import connect


class Database:
    con = connect('company.db')
    cursor = con.cursor()

    @staticmethod
    def select():
        Database.cursor.execute('SELECT * FROM employees')
        fetch = Database.cursor.fetchall()
        return fetch

    @staticmethod
    def insert(national_code, name, family, date):
        Database.cursor.execute(
            f'INSERT INTO employees(National_code,name , family , date_birthday) VALUES ("{national_code}","{name}" , "{family}" , "{date}")')

        Database.con.commit()

        return True

    @staticmethod
    def update(code, name, family, date, where):
        Database.cursor.execute(
            f'UPDATE employees SET National_code = "{code}" , name ="{name}" , family = "{family}" , date_birthday = "{date}"WHERE name = "{where}" ')
        Database.cursor.execute('SELECT * FROM employees')
        Database.con.commit()
        fetch = Database.cursor.fetchall()
        return fetch
