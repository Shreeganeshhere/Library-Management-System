from mysql.connector import connect


def get_connection():
    conn = connect(user = "root", password = "abccdefg@1234", host = "localhost")
    return conn
