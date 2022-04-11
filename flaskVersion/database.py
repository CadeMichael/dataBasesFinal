import sqlite3

sea = sqlite3.connect('sea.db')
cur = sea.cursor()

# create a table 
cur.execute("""CREATE TABLE stocks
                (date text, trans text, symbol text, qty real, price real)""")

# Insert a row of data
cur.execute("INSERT INTO stocks VALUES ('2006', 'buy', 'rhat', 100, 35.14)")

sea.commit()

sea.close()
