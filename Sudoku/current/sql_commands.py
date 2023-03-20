import sqlite3


class Sql:
    def __init__(self):
        self.con = sqlite3.connect("data.db")

        self.cur = self.con.cursor()


    def commit(self):
        self.con.commit()


    def close(self):
        self.con.close()


    def create_user_table(self):
        command1 = ("CREATE TABLE user("
                    "UserID INTEGER PRIMARY KEY,"
                    "username TEXT,"
                    "email TEXT,"
                    "password TEXT)")

        self.cur.execute(command1)


    def insert_user_values(self):
        # hashed = b'$2b$12$dgwplqLS1QUYgGKL7Csdd.kJFV8vQhcBQR/uVlc7MCybSEPrpjkve'
        command2 = (f"INSERT INTO user VALUES (4, 'Theo123', 'theomc@gmail.com', 'Password1!')")
    
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

    
    def return_password(self, username):
        command = (f"SELECT password FROM user WHERE username='{username}'")
        self.cur.execute(command)

        result = self.cur.fetchall()
        # print(result[0][0])
        return result[0][0]
    

    def check_email(self, inputted_email):
        command = (f"SELECT EXISTS(SELECT 1 FROM user WHERE email='{inputted_email}')")
        self.cur.execute(command)

        result = self.cur.fetchall()
        return result[0][0]
    

    def check_username(self, username): # Check if the inputted username is already taken
        command = (f"SELECT EXISTS(SELECT 1 FROM user WHERE username='{username}')")
        self.cur.execute(command)

        result = self.cur.fetchall()
        return result[0][0]
    

    def update_password(self, email, new_password):
        command = (f"UPDATE user SET password='{new_password}' WHERE email='{email}'")
        self.cur.execute(command)

        self.commit()


    def get_user_id(self, username):
        command = (f"SELECT UserID from user WHERE username='{username}'")
        self.cur.execute(command)

        result = self.cur.fetchall()
        try:
            return result[0][0] # Return the ID if it exits. It should always return the UserID as this is only called when the person is signed in so they will always have a valid username
        except:
            return False # Else, return False
        


    def delete_user_values(self, table):
        command = (f"DELETE FROM {table} WHERE UserID = 4")

        self.cur.execute(command)

        self.commit()



# Puzzle tables

    def create_puzzle_table(self):
        command = ("CREATE TABLE puzzle("
                   "UserID INTEGER PRIMARY KEY,"
                   "PuzzleID INTEGER,"
                   "StartingBoard TEXT,"
                   "EditedBoard TEXT)")
        
        self.cur.execute(command)


    def insert_into_puzzle(self, userid, puzzleid, starting_board, edited_board):
        command = (f"Insert into puzzle values ('{userid}', '{puzzleid}', '{starting_board}', '{edited_board}')")
        self.cur.execute(command)

        self.commit()


if __name__ == "__main__":
    db = Sql()
    db.delete_user_values("puzzle")