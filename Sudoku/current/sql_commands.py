import sqlite3



# All of my SQL code is executed inside this class
class Sql:
    def __init__(self):
        self.con = sqlite3.connect("data.db") # Connect to the DB

        self.cur = self.con.cursor() # Cursor


    def commit(self):
        self.con.commit() # commit function


    # Close the DB
    def close(self):
        self.con.close()


    # Create the "user" table
    def create_user_table(self):
        command1 = ("CREATE TABLE user("
                    "UserID INTEGER PRIMARY KEY,"
                    "username TEXT,"
                    "email TEXT,"
                    "password TEXT)")

        self.cur.execute(command1)



    # Add a new user
    def add_user(self, username, email, password):
        command = ("SELECT * FROM user ORDER BY UserID DESC LIMIT 1") # Fetch the latest item to see the newest user ID
        # So this user inserted into the DB has a userID one more than the most recent user
        
        self.cur.execute(command)  
        results = self.cur.fetchall()
        latest_user_id = results[0][0]


        command2 = (f"INSERT INTO user VALUES ({latest_user_id+1}, '{username}', '{email}', '{password}')")
        self.cur.execute(command2)

        self.commit()

    
    # Return password
    def return_password(self, username):
        command = (f"SELECT password FROM user WHERE username='{username}'")
        self.cur.execute(command)

        result = self.cur.fetchall()
        return result[0][0]
    

    # Check if the inputted email is in the DB
    def check_email(self, inputted_email):
        command = (f"SELECT EXISTS(SELECT 1 FROM user WHERE email='{inputted_email}')")
        self.cur.execute(command)

        result = self.cur.fetchall()
        return result[0][0]
    

    # Check if the inputted username is already taken
    def check_username(self, username): 
        command = (f"SELECT EXISTS(SELECT 1 FROM user WHERE username='{username}')")
        self.cur.execute(command)

        result = self.cur.fetchall()
        return result[0][0]
    

    # Update the password (user has changed their password)
    def update_password(self, email, new_password):
        command = (f"UPDATE user SET password='{new_password}' WHERE email='{email}'")
        self.cur.execute(command)

        self.commit()


    # Get the user ID from the username provided
    def get_user_id(self, username):
        command = (f"SELECT UserID from user WHERE username='{username}'")
        self.cur.execute(command)

        result = self.cur.fetchall()
        try:
            return result[0][0] # Return the ID if it exits. It should always return the UserID as this is only called when the person is signed in 
                                # so they will always have a valid username
        except:
            return False # Else, return False
        

    # Delete values - used for testing
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
                   "lives INTEGER,"
                   "editedBoard TEXT)")
        
        self.cur.execute(command)


    # Check if the inputted save ID exists in the save table
    def check_save_id(self, inputted_saveid):
        command = (f"SELECT EXISTS(SELECT 1 FROM save WHERE SaveID='{inputted_saveid}')")
        self.cur.execute(command)

        result = self.cur.fetchall()
        return result[0][0]
    

    # Insert into the save table
    def insert_into_save(self, saveid, userid, puzzleid, lives, editedBoard):
        command = (f"INSERT INTO save VALUES ({saveid}, {userid}, {puzzleid}, {lives}, '{editedBoard}')")

        self.cur.execute(command)

        self.commit()

    
    # Get the puzzle ID from the save ID
    def get_puzzle_id(self, saveid):
        command = (f"SELECT PuzzleID FROM save WHERE SaveID={saveid}")
        self.cur.execute(command)

        result = self.cur.fetchall()

        return result[0][0]
    

    # Get the edited board from the user ID and the save ID to make sure the correct user is accessing the edited board, as they are locked to the account that saved them
    def get_edited_board(self, userid, saveid):
        command = (f"SELECT editedBoard FROM user, save WHERE user.UserID = save.UserID AND user.UserID={userid} AND save.SaveID={saveid}")
        self.cur.execute(command)

        result = self.cur.fetchall()

        return result[0][0]
    

    # Get the number of lives from the "save" table
    def get_lives(self, userid, saveid):
        command = (f"SELECT lives FROM user, save WHERE user.UserID = save.UserID AND user.UserID={userid} AND save.SaveID={saveid}")
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

    
    # Get the latest puzzleID
    def get_latest_puzzleid(self):
        command = ("SELECT * FROM puzzle ORDER BY PuzzleID DESC LIMIT 1") # Fetch the latest item to see the newest user ID
        
        self.cur.execute(command)
        results = self.cur.fetchall()
        latest_puzzle_id = results[0][0]
        return latest_puzzle_id


    # Insert into the "puzzle" table
    def insert_into_puzzle(self, puzzle_id, starting_board, difficulty):
        command2 = (f"INSERT INTO puzzle VALUES ('{puzzle_id}', '{starting_board}', '{difficulty}')")
        self.cur.execute(command2)

        self.commit()


    # Get the starting board from the save ID
    def get_starting_board_with_saveid(self, saveid):
        command = (f"SELECT startingBoard FROM save, puzzle WHERE save.PuzzleID = puzzle.PuzzleID AND save.SaveID={saveid}")
        self.cur.execute(command)

        result = self.cur.fetchall()
        return result[0][0]


    # Get the starting board from the puzzle ID
    def get_starting_board_with_puzzleid(self, puzzleid):
        command = (f"SELECT startingBoard FROM puzzle WHERE PuzzleID={puzzleid}")
        self.cur.execute(command)

        result = self.cur.fetchall()
        return result[0][0]



if __name__ == "__main__":
    db = Sql()
    print(db.get_starting_board_with_puzzleid(26))