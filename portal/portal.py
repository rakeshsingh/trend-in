# all the imports
import sqlite3
import time
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
# for db initiation
from contextlib import closing


# configuration
DATABASE = '/tmp/portal.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    """
    connect to database and get db connection
    """
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    """
    initiate the database for the app
    """
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


# run this functions before and after a request
# g is a special object in flask
@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

# request handler functions


@app.route('/')
def show_entries():
    cur = g.db.execute(
        'select url, title, description, type from entries order by date desc')
    entries = [dict(url=row[0], title=row[1], description=row[2], type=row[3])
               for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

# add a new entry


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (url,title,description,type,date) values (?, ?,?,?,?)',
                 [request.form['url'], request.form['title'], request.form['description'], request.form['type'], time.strftime("%Y-%m-%d")])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

# login request handler


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

# logout request handler


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

# app starting point
if __name__ == '__main__':
    app.run()
