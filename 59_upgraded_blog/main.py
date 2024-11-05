from flask import Flask, render_template
from post import Post

app = Flask(__name__)


@app.route("/")
def home():
    post = Post()
    all_posts = post.get_posts()
    print(all_posts)
    return render_template("index.html", all_posts=all_posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)