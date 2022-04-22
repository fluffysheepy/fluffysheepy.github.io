from flask import Flask, render_template
from data import test_posts, profiles

app = Flask(__name__)

@app.route("/")
def feed():

    return render_template('feed.html', posts=test_posts, title="My Feed")


@app.route("/comments/<int:post_id>")
def comments(post_id):
    post = test_posts[post_id]
    return render_template('comments.html', title="Comments", post=post)

    
@app.route("/profiles/<string:profile_id>")
def profile(profile_id):
    profile = profiles[profile_id]
    return render_template('profile.html', title="Profile", profile=profile)