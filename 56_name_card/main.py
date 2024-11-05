from flask import Flask, render_template, request, session
from flask_babel import Babel, _,lazy_gettext as _l, gettext, refresh
from dotenv import load_dotenv
import os


app = Flask(__name__)
babel = Babel(app)
refresh()

load_dotenv()

app.config['BABEL_DEFAULT_LOCALE'] = "en"
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")  

def get_locale():
    return request.accept_languages.best_match(["pt_BR", "en"])

babel = Babel(app, locale_selector=get_locale)

@app.route("/")
def home():
    return render_template ("index.html", current_locale=get_locale())

if __name__ == "__main__":
    app.run(debug=True)