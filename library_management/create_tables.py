from connection import get_connection


def create_table():
    """Creates table in database 
    Args:
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS KSIT_AIML_LIBRARY")
    cur.execute("USE DATABSE KSIT_AIML_LIBRARY")
    cur.execute("""CREATE TABLE IF NOT EXISTS BOOKS(
                B_NAME  PRIMARY KEY VARCHAR(50), B_AUTHOR VARCHAR(30), 
                B_GENRE VARCHAR(20), IN_STOCK INT"""
                )
    cur.execute("""CREATE TABLE IF NOT EXISTS BORROWED(
                B_NAME VARCHAR(50), BORROWER VARCHAR(50), BORROWED_DATE DATE ,
                FOREIGN KEY(B_ID) REFERENCES BOOKS(B_NAME))"""
                )
    cur.close()
    conn.commit()
    conn.close()
