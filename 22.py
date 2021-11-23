import sqlite3

connection = sqlite3.connect("films.sqlite")
cursor = connection.cursor()
result = cursor.execute(""" 
SELECT DISTINCT genre FROM films
WHERE year = 2011 OR year = 2010
""").fetchall()

for i in result:
    result2 = cursor.execute(f""" 
    SELECT title FROM genres
    WHERE id = {i[0]} """).fetchall()
    print(result2[0][0])