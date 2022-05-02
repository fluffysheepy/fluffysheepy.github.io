import sqlite3

def get_suppliers():
    conn = sqlite3.connect('Northwind_large.sqlite')
    cur = conn.cursor()
    cur.execute("""SELECT CompanyName, City, Country FROM Supplier""")
    rows = cur.fetchall()
    conn.close()
    return rows