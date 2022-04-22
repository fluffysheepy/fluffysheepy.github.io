from flask import Flask, render_template
import re

app = Flask(__name__)

@app.route("/dictionary/")
def dictionary():
    title = "Dictionary"
    f = open('words.txt')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    return render_template('dictionary.html', title=title, letters=letters)

@app.route("/dictionary/<string:letter>")
def letters(letter):
    title = "Dictionary"
    f = open('words.txt')
    words = f.read().splitlines()
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if letter.upper() in words:
        is_word = True
    else:
        is_word = False

    linklist = []
    for item in letters:
        linklist.append(letter + item)
    count = 0
    for n in words:
        if n.lower().startswith(letter):
            count +=1
        

    return render_template('dictionary.html', title=title, letters=letters, count=count, letter=letter, is_word=is_word, linklist=linklist, n=n)

