import pymysql

# Create database and table if not exists
def initialize_database():
    connection = pymysql.connect(host="localhost", user="root", password="")
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS HotelManagement")
    connection.commit()

    connection = pymysql.connect(host="localhost", user="root", password="", database="HotelManagement")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS checkin_guest (
        Name VARCHAR(50),
        Address VARCHAR(50),
        Number BIGINT UNIQUE KEY,
        RoomNumber INT,
        Days INT,
        room_type VARCHAR(50),
        payment_method VARCHAR(50)
    )
    """)
    connection.commit()
    connection.close()

# 1.Check-in guest
def insert_guest(name, address, number, days,room_number, room_type, payment_method):
    connection = pymysql.connect(host="localhost", user="root", password="", database="HotelManagement")
    cursor = connection.cursor()
    query = """
    INSERT INTO checkin_guest (Name, Address, Number ,Days, RoomNumber, room_type, payment_method)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (name, address, number, days, room_number, room_type, payment_method)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

# 2.Show guest list
def fetch_all_guests():
    connection = pymysql.connect(host="localhost", user="root", password="", database="HotelManagement")
    cursor = connection.cursor()
    query = """
          SELECT * FROM checkin_guest;
          """
    cursor.execute(query)
    return cursor.fetchall()

# Check if the room number is valid - 3.Chek out
def is_valid_room(room_number): 
    connection = pymysql.connect(host="localhost", user="root", password="", database="HotelManagement") 
    cursor = connection.cursor() 
    query = "SELECT * FROM checkin_guest WHERE RoomNumber=%s" 
    cursor.execute(query, (room_number,)) 
    result = cursor.fetchone() 
    cursor.close() 
    connection.close() 
    return result


# Initialize the database when the script runs
initialize_database()
