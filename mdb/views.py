from mdb import app
import database_manager
from flask import Flask, render_template, flash, redirect, make_response, Response
from forms import AnaelleRateForm

@app.route('/')
@app.route('/index')
def index():
    db = database_manager.DatabaseManager()
    db.connect()
    movies_list = db.import_db()
    db.close
    return render_template('index.html', to_print=movies_list)


@app.route('/movie/<id_>')
def movie(id_):
    db = database_manager.DatabaseManager()
    db.connect()
    m = db.find_movie(id_)
    return render_template('movie.html', i=m)

@app.route('/update_s/<id_>')
def update_s(id_):
    db = database_manager.DatabaseManager()
    db.connect()
    m = db.find_movie(id_)
    if(m.seen == 0):
        m.seen = 1
    else:
        m.seen = 0
    db.update_seen(id_,m.seen)
    db.close
    return render_template('movie.html', i=m)

@app.route('/my_rating/<id_>',methods = ['GET', 'POST'])
def my_rating(id_):
    form = AnaelleRateForm()
    db = database_manager.DatabaseManager()
    db.connect()
    m = db.find_movie(id_)
    if form.validate_on_submit():
        flash('thanks')
        db.update_rating(id_,form.rate.data)
        return redirect('/index')
    return render_template('rate_form.html', title = 'rating', form = form,i=m)

@app.route('/images/<id_>.jpg')
def getImage(id_):
    db = database_manager.DatabaseManager()
    db.connect()
    m = db.find_movie(id_)
    print m.cover[0:20]
    open('/tmp/x.jpg', 'w').write(m.cover)
    #response = make_response(m.cover)
    #response.headers['Content-Type'] = 'image/jpeg'
    #return response
    return Response(m.cover, content_type='image/jpeg')

