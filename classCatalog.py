import sqlite3

# Connect to the database
connection = sqlite3.connect('dataBase.db')
cursor = connection.cursor()

# Create Classes TABLE (if it does not already exist)
cursor.execute("CREATE TABLE IF NOT EXISTS classes (class_id integer PRIMARY KEY AUTOINCREMENT, Name TEXT NOT NULL, Code CHAR(5) NOT NULL)")

# Create Professors TABLE (if it does not already exist)
cursor.execute("CREATE TABLE IF NOT EXISTS professors (professor_id integer PRIMARY KEY AUTOINCREMENT, Name TEXT NOT NULL, Rating CHAR(5) NOT NULL)")

# Create Rating TABLE (if it does not already exist)
cursor.execute("CREATE TABLE IF NOT EXISTS rates (rating_id integer PRIMARY KEY AUTOINCREMENT, Rating CHAR(5) NOT NULL)")

# get course code for dispaly
def get_class(cursor):
    cursor.execute("SELECT Name FROM classes")
    records = cursor.fetchall()
    for index, Name in enumerate(records):
      print(f"{index+1} - {Name[0]}")
    choice = int(input("Delect"))
    return records[choice-1][0]

# get Professor's name for dispaly
def get_professors(cursor):
    cursor.execute("SELECT Name FROM professors")
    records = cursor.fetchall()
    for index, name in enumerate(records):
      print(f"{index+1} - {name[0]}")
    choice = int(input("Fire"))
    return records[choice-1][0]

# get Rates for dispaly
def get_rating(cursor):
    cursor.execute("SELECT rating FROM rates")
    records = cursor.fetchall()
    for index, name in enumerate(records):
      print(f"{index+1} - {name[0]}")
    choice = int(input("Fire"))
    return records[choice-1][0]

choice = None
if choice != "4":
    print("1) Display Classes")
    print("2) Display Professor")
    print("3) Display Rating")
    print("4) Quit")
    choice = input("> ")
    print()
    if choice == "1":
        # Display Classes
        cursor.execute("SELECT * FROM classes")
        print("{:>10}  {:>10}  {:>10}".format("class_id", "Name", "Code"))
        for record in cursor.fetchall():
            print("{:>10}  {:>10}  {:>10}".format(record[0], record[1], record[2]))
        c_choice = None
        while c_choice != 4:
            print("1) Add Class")
            print("2) Update Class")
            print("3) Delete Class")
            print("4) Quit")
            c_choice = input("> ")
            print()
            if c_choice == "1":
                # Add New Class
                name = input("Class Name: ")
                code = input("Class Code: ")
                Values = (name, code)
                cursor.execute("INSERT INTO classes (Name, Code) VALUES (?,?)", Values)
                connection.commit()

            elif c_choice == "2":
                # Update Class
                name = input("Class Name: ")
                code = input("Class Code: ")
                Values = (name,code,code)
                cursor.execute("UPDATE classes SET  Name = ?, code = ? WHERE classes.Name = ?", Values)
                connection.commit()
                
            elif choice == "3":
                # Delete Class
                name = get_class(cursor)
                print(name)
                Values = (name,)
                cursor.execute("DELETE FROM classes WHERE class = ?", Values)
                connection.commit()

    if choice == "2":
        # Display 
        cursor.execute("SELECT * FROM professors")
        print("{:>10}  {:>10}".format("Name", "Code"))
        for record in cursor.fetchall():
            print("{:>10}  {:>10}".format(record[1], record[2]))
        c_choice = None
        while c_choice != 4:
            print("1) Add Professor")
            print("2) Update Professor")
            print("3) Delete Professor")
            print("4) Quit")
            c_choice = input("> ")
            print()
            if c_choice == "1":
                # Add New Class
                ident = 1
                name = input("Class Name: ")
                code = input("Class Code: ")
                Values = (ident, name, code)
                cursor.execute("INSERT INTO classes VALUES (?,?,?)", Values)
                connection.commit()

            elif c_choice == "2":
                # Update Class
                name = input("Class Name: ")
                code = input("Class Code: ")
                Values = (name,code,code)
                cursor.execute("UPDATE classes SET  Name = ?, code = ? WHERE classes.Name = ?", Values)
                connection.commit()
                
            elif choice == "3":
                # Delete Class
                name = get_class(cursor)
                print(name)
                Values = (name,)
                cursor.execute("DELETE FROM classes WHERE class = ?", Values)
                connection.commit()

    if choice == "3":
        # Display Classes
        cursor.execute("SELECT * FROM rates")
        print("{:>10}  {:>10}".format("rate_id", "Rating"))
        for record in cursor.fetchall():
            print("{:>10}  {:>10}".format(record[0], record[1],))
        r_choice = None
        while r_choice != 3:
            print("1) Add Rating")
            print("2) Delete Class")
            print("3) Quit")
            r_choice = input("> ")
            print()
            if r_choice == "1":
                # Add New Rating
                rating = input("Add new Rating(This must be in sequence to the last one): ")
                Values = (rating,)
                cursor.execute("INSERT INTO rates (rating) VALUES (?)", Values)
                connection.commit()
            elif r_choice == "2":
                # Delete Class
                name = get_rating(cursor)
                print(name)
                Values = (name,)
                cursor.execute("DELETE FROM rates WHERE rating_id = ?", Values)
                connection.commit()




# cursor.execute("SELECT name from sqlite_master WHERE type='table';")
# tables = cursor.fetchall()
# print(tables)