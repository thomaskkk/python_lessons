from flask import Flask, render_template
from post import Post

app = Flask(__name__)


@app.route("/")
def home():
    post = Post()
    all_posts = post.get_posts()
    return render_template("index.html", all_posts=all_posts)

@app.route("/single_post/<int:num>")
def single_post(num):
    post = Post()
    blog_post = post.get_single_post(num)
    return render_template("post.html", blog_post=blog_post)

@app.route("/about")
def about():
    return render_template("about.html") 

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)