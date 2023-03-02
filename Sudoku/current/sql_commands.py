import sqlite3


class Sql:
    def __init__(self):
        self.con = sqlite3.connect("data.db")

        self.cur = self.con.cursor()


    def commit_close(self):
        self.con.commit()
        self.con.close()


    def create_tables(self):
        command1 = ("CREATE TABLE user("
                    "UserID INTEGER PRIMARY KEY,"
                    "username TEXT,"
                    "email TEXT,"
                    "password TEXT)")

        self.cur.execute(command1)


    def insert_values(self):
        command2 = ("INSERT INTO user VALUES (2, 'Nathan', 'nathan@gmail.com', 'Nathan123!')")

        self.cur.execute(command2)
        
        self.commit_close()



    def delete_values(self):
        command = ("DELETE FROM user WHERE UserID = 2")

        self.cur.execute(command)

        self.commit_close()

db = Sql()
db.insert_values()