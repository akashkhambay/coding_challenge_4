import sqlite3
from hashids import Hashids
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'futureproof10daystogo'
hashids = Hashids(min_length=5, salt = app.config['SECRET_KEY'])

def get_db_con():
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    return con


@app.route('/', methods=('GET', 'POST'))
def home():
    con = get_db_con()

    #add conditional statements to handle requests
    if request.method == 'POST':
        url = request.form['url'] #This gets url form the request and assigns to the variable

        if url is None:
            flash('PLease provide the URL')
            return redirect(url_for('home'))

        old_url = con.execute('INSERT INTO urls (old_url) VALUES (?)',
                                (url,))

        con.commit()
        con.close()

        url_id = old_url.lastrowid #lastrowid attribute allows for the id of the most recent entry into the table
        hashid = hashids.encode(url_id)
        shorterned_url = request.host_url + hashid

        return render_template('home.html', shorterned_url=shorterned_url)

    return render_template('home.html')

@app.route('/<id>')
def page_redirect(id):
    con = get_db_con()
    old_id = hashids.decode(id)
    if old_id:
        old_id = f'{old_id[0]}' #Needed to add a formatted string since sqlite was complaining about an integer...
        data = con.execute('SELECT old_url FROM urls WHERE id = ?', (old_id)).fetchone()
        old_url = data['old_url']

        con.commit()
        con.close()
        return redirect (old_url)
    else:
        flash('This URL is sad, it is not valid.')
        return redirect (url_for('home'))                 

if __name__ == "__main__":
    app.run(debug=True)