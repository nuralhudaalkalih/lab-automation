class UserDAO:
    def __init__(self, db):
        self.db=db
    def add_user(self, username, password, role):
        self.db.cursor.execute("INSERT INTO Users (username, password, role) VALUES (?,?,?)", (username, password, role))
        self.db.connection.commit()
    def get_userByUsername(self, username):
        self.db.cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
        return self.db.cursor.fetchone() # return a single user or None if not found
    def get_all_users(self):
        self.db.cursor.execute("SELECT * FROM Users")
        return self.db.cursor.fetchall() # return a list of all users
    def delete_user(self,username):
        self.db.cursor.execute("DELETE FROM Users WHERE username=?",(username,))
        self.db.connection.commit()