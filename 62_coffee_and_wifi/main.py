from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location on Google Maps (URL)', validators=[DataRequired(), URL(require_tld=True)])
    open = StringField('Opening time e.g.: 8:00AM', validators=[DataRequired()])
    close = StringField('Closing time e.g.: 8:00PM', validators=[DataRequired()])
    coffe_choice = ["☕️",  "☕️☕️",  "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"]
    coffee = SelectField('Coffee rating', choices=coffe_choice, validators=[DataRequired()])
    wifi_choice = [ "💪", "💪💪",  "💪💪💪", "💪💪💪💪", "💪💪💪💪💪", "✘"]
    wifi = SelectField('Wifi strenght', choices=wifi_choice, validators=[DataRequired()])
    power_choice = ["🔌", "🔌🔌",  "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌", "✘"]
    power = SelectField('Power socket availiability', choices=power_choice, validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        with open('cafe-data.csv', "a", encoding='utf-8') as csv_file:
            csv_data = csv.writer(csv_file, delimiter=',')
            csv_data.writerow([
                form.cafe.data,
                form.location.data,
                form.open.data,
                form.close.data,
                form.coffee.data,
                form.wifi.data,
                form.power.data
            ])
            return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
