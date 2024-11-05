# Name card

This is a simple website to teach concepts of Flask templates.


This challenge teaches the concepts of:

 - Flask templates
 - Flask static
 - Flask babel for localization

## Setup

This program uses the Python flask, Flask-Babel, python-dotenv modules

```
pip install -r requirements.txt
```
or

```
pip install flask Flask-Babel python-dotenv
```
## How to run

```
python main.py
```

## How to make translations

Add your language in get_locale() at main.py

Generate .pot file to find strings that are avaliable for translation
```
pybabel extract -F babel.cfg -o messages.pot .
```

Create a translation file and dir for the specific languague in this example "pt_BR"
```
pybabel init -i messages.pot -d translations -l pt_BR
```

Compile translations
```
pybabel compile -d translations
```