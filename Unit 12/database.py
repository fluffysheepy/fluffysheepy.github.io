import sqlite3

def query(query_text, *param):
    conn = sqlite3.connect('Northwind_large.sqlite')
    cur = conn.cursor()
    cur.execute(query_text, param)
    
    column_names=[]
    for column in cur.description:
        column_names.append(column[0])

    rows = cur.fetchall()
    dicts=[]

    for row in rows:
        d=dict(zip(column_names, row))
        dicts.append(d)

    conn.close()
    return dicts

def get_suppliers():
    return query("""SELECT * FROM Supplier""")

def get_supplier_products(supplier_id):
    return query("""
    SELECT ProductName, QuantityPerUnit, UnitPrice FROM Product
    WHERE SupplierId = ?""", supplier_id)

def get_companyname(supplier_id):
    return query("""
    SELECT CompanyName FROM Supplier WHERE Id=?""", supplier_id)

def get_categories():
    return query("""
    SELECT COUNT(Product.CategoryId) AS ProductCount, Category.Id AS FoodCategory, CategoryName, Description FROM Category
    INNER JOIN Product
	ON Product.CategoryId = Category.Id
    GROUP BY CategoryName""")

def get_category(category_id):
    return query("""
    SELECT ProductName, Supplier.CompanyName, Supplier.Id AS Supplier, Category.CategoryName, Category.Id FROM Product
    INNER JOIN Supplier
    ON SupplierId = Supplier.Id
    INNER JOIN Category
    ON CategoryId = Category.Id WHERE CategoryId=?""", category_id)

def get_categoryname(category_id):
    return query("""
    SELECT CategoryName FROM Category WHERE Id=?""", category_id)