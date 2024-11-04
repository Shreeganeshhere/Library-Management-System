from mysql.connector import connect, cursor

def get_connection():
    conn = connect(user = "root", password = "abccdefg@1234", host = "localhost", database = "trial" )
    return conn
