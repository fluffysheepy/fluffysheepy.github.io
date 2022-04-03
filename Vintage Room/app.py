from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "Welcome to the Vintage Room!"
    
    text = """You wake up and open your eyes.. Where are you? You look around and see old floral wallpaper and vintage furniture. It is quite cozy, and it feels like you went back to the times of your great grandparents. The only problem this room has is that the door out doesn't seem to open, and you realize that you are completely locked in.
    Will you be able to get out of here?"""

    choices = [
        ('room',"See what you can find in the room"),
        ('window',"Open the window")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/inside")
def room():
    title = "You look around..."
    
    text = """... and you start noticing everything that surrounds you. There is another door that you haven't noticed before as it is covered in wallapaper."""

    choices = [
        ('closet',"Open the hidden door"),
        ('window',"Open the window")
    ]

    return render_template('inside.html', title=title, text=text, choices=choices)

@app.route("/window")
def window():
    title = "You open the window!"
    
    text = """That is a mistake. White dense smoke enters the room, and you faint..."""

    choices = []

    return render_template('window.html', title=title, text=text, choices=choices)



@app.route("/closet")
def closet():
    title = "Closet it is!"
    
    text = """You open the hidden door and see that you stumbled upon a closet. There is a lot of clothes hanging. You decide to try some of them on since you have a lot of time on your hands, but as soon as you step into the tiny closet, the door slams shut behind you. """

    choices = []

    return render_template('closet.html', title=title, text=text, choices=choices)
