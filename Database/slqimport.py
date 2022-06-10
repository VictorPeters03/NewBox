import mysql.connector

host_args = {
    "host": "localhost",
    "user": "newboxsql",
    "password": "newbox"
}

con = mysql.connector.connect(**host_args)

cur = con.cursor(dictionary=True)


with open('Song.sql', 'r') as sql_file:
    result_iterator = cur.execute(sql_file.read(), multi=True)
    for res in result_iterator:
        print("Running query: ", res)  # Will print out a short representation of the query
        print(f"Affected {res.rowcount} rows" )

    con.commit()  # Remember to commit all your changes!