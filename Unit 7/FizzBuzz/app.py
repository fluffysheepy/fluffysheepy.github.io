from flask import Flask, render_template

app = Flask(__name__)


@app.route("/fizzbuzz/<int:count_to>")
def fizzbuzz(count_to):
    f = open('fizzbuzz.py')
    title = "FizzBuzz"
    text = """Challenge"""
    l=[]
    for n in range(1,count_to + 1):
        if n%3==0 and n%5==0:
            l.append("FizzBuzz")
        elif n%5==0:
            l.append("Buzz")
        elif n%3==0:
            l.append("Fizz")
        else:
            l.append(n)

    return render_template('fizzbuzz.html', fizzbuzz=fizzbuzz, title=title, text=text, count_to=count_to, n=n, numbers=l)


