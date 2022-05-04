from flask import Flask, render_template
import database

app = Flask(__name__)

@app.route("/")
def suppliers():
    suppliers = database.get_suppliers()
    return render_template('index.html', suppliers=suppliers)


@app.route("/suppliers/<int:supplier_id>")
def products(supplier_id):
    products = database.get_supplier_products(supplier_id)
    suppliers = database.get_suppliers()
    companynames = database.get_companyname(supplier_id)
    return render_template("products.html", products=products, suppliers=suppliers, companynames=companynames)


@app.route("/categories")
def categories():
    categories=database.get_categories()
    return render_template('categories.html', categories=categories, category=category)

@app.route("/categories/<int:category_id>")
def category(category_id):
    category=database.get_category(category_id)
    categorynames = database.get_categoryname(category_id)
    return render_template('category.html', category=category, categorynames=categorynames, products=products)
    