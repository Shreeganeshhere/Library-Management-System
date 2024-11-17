from connection import get_connection
from mysql.connector import errorcode
import mysql.connector


def addbooks(bname : str, bauthor : str, genre : str, nob=1):
    """function to add books to the database.
    if the book exists in database the nob is added to the existing stock
    Args:
    bname: name of the boook
    bauthor: author of the book
    genre: genre of book
    nob: no. of books"""
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO BOOKS VALUES(%s,%s,%s,%s)",(bname,bauthor,genre,nob))
        conn.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DUP_ENTRY:
            cur.execute("SELECT IN_STOCK FROM BOOKS WHERE B_NAME = %s",(bname,))
            current_stock = cur.fetchone()
            new_stock = int(current_stock[0]) + nob
            cur.execute("UPDATE BOOKS SET IN_STOCK = %s WHERE B_NAME = %s",(new_stock, bname))
            conn.commit()
        else:
            print(f"Integrity error: {err}")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        conn.close()
        cur.close()
