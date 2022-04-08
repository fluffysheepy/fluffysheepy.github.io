from flask import Flask, render_template

app = Flask(__name__)

@app.route("/words/<string:word>")
def words(word):
    f = open('words.txt')
    words = f.read().splitlines()
    l=[]
    for w in words:
        if sorted(w) == sorted(word.upper()):
            l.append(w)

    return render_template('words.html', word=word, words=words, l=l, w=w)