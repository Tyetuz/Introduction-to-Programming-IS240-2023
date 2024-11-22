import sqlite3
with sqlite3.connect("users.db") as db:
    cursor = db.cursor()

cursor.execute('''Create table if not exists user(userID integer primary key, username Varchar(20) not null, firstname Varchar(20) not null, surname Varchar(20) not null, password Varchar(20) not null);''')

cursor.execute('''Insert into user(username, firstname, surname, password) values("test_user", "Bill","Smith","password")''')
db.commit()

cursor.execute("Select * from user;")
print(cursor.fetchall())

