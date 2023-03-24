import sqlite3
import json


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



# Save table

    def create_save_table(self):
        command = ("CREATE TABLE save("
                   "SaveID INTEGER PRIMARY KEY,"
                   "UserID INTEGER,"
                   "PuzzleID INTEGER,"
                   "editedBoard TEXT)")
        
        self.cur.execute(command)


    def check_save_id(self, inputted_saveid):
        command = (f"SELECT EXISTS(SELECT 1 FROM save WHERE SaveID='{inputted_saveid}')")
        self.cur.execute(command)

        result = self.cur.fetchall()
        return result[0][0]
    

    def insert_into_save(self, saveid, userid, puzzleid, editedBoard):
        command = (f"INSERT INTO save VALUES ({saveid}, {userid}, {puzzleid+1}, '{editedBoard}')")

        self.cur.execute(command)

        self.commit()

    
    def get_puzzle_id(self, saveid):
        command = (f"SELECT PuzzleID FROM save WHERE SaveID={saveid}")
        self.cur.execute(command)

        result = self.cur.fetchall()

        return result[0][0]
    

    def get_edited_board(self, userid, saveid):
        command = (f"SELECT editedBoard FROM user, save WHERE user.UserID = save.UserID AND user.UserID={userid} AND save.SaveID={saveid}")
        self.cur.execute(command)

        result = self.cur.fetchall()

        return result[0][0]


# Puzzle tables

    def create_puzzle_table(self):
        command = ("CREATE TABLE puzzle("
                   "PuzzleID INTEGER PRIMARY KEY,"
                   "startingBoard TEXT,"
                   "difficulty TEXT)")
        
        self.cur.execute(command)

    
    def get_latest_puzzleid(self):
        command = ("SELECT * FROM puzzle ORDER BY PuzzleID DESC LIMIT 1") # Fetch the latest item to see the newest user ID
        
        self.cur.execute(command)
        results = self.cur.fetchall()
        latest_puzzle_id = results[0][0]
        return latest_puzzle_id


    def insert_into_puzzle(self, puzzle_id, starting_board, difficulty):
        command2 = (f"INSERT INTO puzzle VALUES ('{puzzle_id+1}', '{starting_board}', '{difficulty}')")
        self.cur.execute(command2)

        self.commit()


    def get_starting_board(self, puzzleid):
        command = (f"SELECT startingBoard FROM puzzle WHERE PuzzleID='{puzzleid}'")
        self.cur.execute(command)

        result = self.cur.fetchall()
        return result[0][0]




if __name__ == "__main__":
    db = Sql()
    print(db.get_edited_board(4, 7717))