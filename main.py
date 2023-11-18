# connection = sqlite3.connect('shop.db')
# cursor = connection.cursor()
# cursor.execute("""CREATE TABLE IF NOT EXISTS film (id INTEGER PRIMARY KEY,
#                                      title VARCHAR(100) UNIQUE NOT NULL,
#                                      genre VARCHAR(100) NOT NULL,
#                                      year DATE NOT NULL,
#                                      director VARCHAR(100));""")
# cursor.execute("""CREATE TABLE IF NOT EXISTS directors (id INTEGER PRIMARY KEY,
#                                      name VARCHAR(100) UNIQUE NOT NULL,
#                                      birth DATE NOT NULL);""")
# cursor.execute("""INSERT INTO film (title, genre, year, director) VALUES ('Titanic', 'drama', '1998-11-23', 'Bob Smith'),
#                                                                          ('Romeo and Juliette', 'drama', '1999-06-24', 'Jack Jackson')""")
#
# connection.commit()
# connection.close()

# connection = sqlite3.connect('shop.db')
# cursor = connection.cursor()
# cursor.execute("""SELECT * FROM film WHERE id = 1; """)
# data = cursor.fetchall()
# print(data)
# connection.close()