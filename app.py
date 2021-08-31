import sqlite3
from hashids import Hashids
from flask import Flask, render_tenplate, request, flash, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'futureproof10daystogo'
hashids = Hashids(min_length=5, salt = app.config['SECRET_KEY'])

def get_db_con():
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    return con