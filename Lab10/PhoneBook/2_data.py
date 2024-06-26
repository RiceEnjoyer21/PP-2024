import psycopg2

def insert_data_from_console():
    conn = psycopg2.connect(
        host='localhost',
        database='phone',
        user='user',
        password='12345',
        port='54321'
    )
    conn.autocommit = True

    cursor = conn.cursor()

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_num = input("Enter phone number: ")

    cursor.execute(
        "INSERT INTO PhoneBook (first_name, last_name, phone_num) VALUES (%s, %s, %s)",
        (first_name, last_name, phone_num)
    )

    conn.close()

insert_data_from_console()
