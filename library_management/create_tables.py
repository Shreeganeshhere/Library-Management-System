from connection import get_connection


def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS BOOKS(B_ID PRIMARY KEY INT,
                B_NAME VARCHAR(30), B_AUTHOR VARCHAR(30), 
                B_GENRE VARCHAR(20), STOCK INT""")
    cur.execute("""CREATE TABLE IF NOT EXISTS BORROWED(B_ID INT,
                BORROWER VARCHAR(50), BORROWED_DATE DATE )""")
    cur.close()
    conn.commit()
    conn.close()
