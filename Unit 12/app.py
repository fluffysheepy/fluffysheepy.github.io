from flask import Flask, render_template
import database

app = Flask(__name__)

@app.route("/")
def suppliers():
    suppliers = database.get_suppliers()
    return render_template('index.html', suppliers=suppliers)