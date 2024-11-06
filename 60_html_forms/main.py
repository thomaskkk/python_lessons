from flask import Flask, render_template, request
import requests
from mail import Mail

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/19178aee7e641ba9e7fc").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        body = f"{request.form['message']}\n{request.form['name']}\n{request.form['phone']}"

        mail_service = Mail()
        mail_service.send_email("Message from you blog", body, request.form["email"])
        info = {}
        info["name"] = request.form["name"]
        info["email"] = request.form["email"]
        info["phone"] = request.form["phone"]
        info["message"] = request.form["message"]
        return render_template("sent.html", info=info)
    elif request.method == 'GET':
        return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
