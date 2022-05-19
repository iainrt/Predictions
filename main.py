from flask import Flask, render_template, flash, redirect, url_for, request
from replit import db, web
from db_init import db_init

app = Flask(__name__)

# Secret key
app.config['SECRET_KEY'] = "ZZENE67UP8QHA82Q05B2"

# Database setup
db_init()
users = web.UserStore()

ADMINS = ["iainrt"]

# Routes
@app.route("/")
@web.authenticated
def index():
    return f"Hello {web.auth.name}"

web.run(app)