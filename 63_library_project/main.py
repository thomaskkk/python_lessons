from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

with app.app_context():
    db.create_all()

all_books = []


@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all()

    return render_template("index.html", all_books=all_books, book_qnty=len(all_books))


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        with app.app_context():
            new_book = Book(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
            db.session.add(new_book)
            db.session.commit()
        
        return redirect(url_for("home"))
    
    else:
        return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

