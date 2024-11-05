from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)

@app.route('/')
def home():
    post = Post()
    return render_template("index.html", all_posts=post.get_all_posts())

@app.route('/post/<num>')
def get_post(num):
    post = Post()
    return render_template("post.html", all_posts=post.get_all_posts(), post_number=int(num))


if __name__ == "__main__":
    app.run(debug=True)
