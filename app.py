import random
import string

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://admin:YilyrXo6PFkO5R6YAxu0@database-1.carye9sb9qqd.us-east-2.rds.amazonaws.com:3306/ShortUrldatabase"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Urls(db.Model):
    id_ = db.Column("id_", db.Integer, primary_key=True)
    long = db.Column("long", db.String(255))
    short = db.Column("short", db.String(3))
    count = db.Column("count", db.Integer)
    def __init__(self, long, short, count):
        self.long = long
        self.short = short
        self.count = count
@app.before_first_request
def create_tables():
    db.create_all()
def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=3)
        rand_letters = "".join(rand_letters)
        short_url = Urls.query.filter_by(short=rand_letters).first()
        if not short_url:
            return rand_letters
@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        url_received = request.form["nm"]
        found_url = Urls.query.filter_by(long=url_received).first()
        if found_url:
           return render_template('base.html', short_url_display=found_url.short, count_display=found_url.count)
        else:
            short_url = shorten_url()
            # return render_template('base.html', short_url_display=short_url, count_display=0)
            new_url = Urls(url_received, short_url, 0)
            db.session.add(new_url)
            db.session.commit()
            return render_template('base.html', short_url_display=short_url, count_display=0)
    else:
        return render_template("base.html")
@app.route('/<short_url>')
def redirection(short_url):
    long_url = Urls.query.filter_by(short=short_url).first()
    if long_url:
        long_url.count = long_url.count + 1
        db.session.commit()
        return redirect(long_url.long)
    else:
        return f'<h1>Url doesnt exist</h1>'
if __name__ == '__main__':
    app.run(host=12.0.0,port=3306, debug=True)
