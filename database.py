from sqlite3 import connect
 
class Database():
    def __init__(self) -> None:
        self.db = connect('rta.db')
        self.cursor = self.db.cursor()
        self.tableCreate = ""

    def createTable(self):
        self.cursor.execute()
        print()

if __name__ == "__main__":
    pass 