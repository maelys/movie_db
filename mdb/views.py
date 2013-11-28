from mdb import app
import database_manager
from flask import Flask, render_template

@app.route('/')
@app.route('/index')
def index():
    db = database_manager.DatabaseManager()
    db.connect()
    movies_list = db.import_db()
    db.close
    return render_template('index.html', to_print=movies_list)


@app.route('/movie/<title>')
def movie(title):
    db = database_manager.DatabaseManager()
    db.connect()
    m = db.find_movie(title)
    print m.imdb_link
    return render_template('movie.html', i=m)

    
