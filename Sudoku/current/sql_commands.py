import sqlite3


class Sql:
    def __init__(self):
        self.con = sqlite3.connect("data.db")

        self.cur = self.con.cursor()


    def commit(self):
        self.con.commit()


    def close(self):
        self.con.close()


    def create_tables(self):
        command1 = ("CREATE TABLE user("
                    "UserID INTEGER PRIMARY KEY,"
                    "username TEXT,"
                    "email TEXT,"
                    "password TEXT)")

        self.cur.execute(command1)


    def insert_values(self):
        # hashed = b'$2b$12$dgwplqLS1QUYgGKL7Csdd.kJFV8vQhcBQR/uVlc7MCybSEPrpjkve'
        command2 = (f"INSERT INTO user VALUES (1, 'Theo', 'theo@gmail.com', 'Password1!')")
    
        self.cur.execute(command2)
        
        self.commit()


    def add_user(self, username, email, password):
        command = ("SELECT * FROM user ORDER BY UserID DESC LIMIT 1") # Fetch the latest item to see the newest user ID
        
        self.cur.execute(command)
        results = self.cur.fetchall()
        latest_user_id = results[0][0]


        command2 = (f"INSERT INTO user VALUES ({latest_user_id+1}, '{username}', '{email}', '{password}')")
        self.cur.execute(command2)

        self.commit()

    
    def check_username(self, username): # Check if the inputted username is already taken
        command = (f"SELECT password FROM user WHERE username='{username}'")
        self.cur.execute(command)

        result = self.cur.fetchall()
        return result[0][0]

    
    def return_password(self, username):
        command = (f"SELECT password FROM user WHERE username='{username}'")
        self.cur.execute(command)

        result = self.cur.fetchall()
        # print(result[0][0])
        return result[0][0]


    def delete_values(self):
        command = ("DELETE FROM user WHERE UserID = 0")

        self.cur.execute(command)

        self.commit()




if __name__ == "__main__":
    db = Sql()
    db.delete_values()