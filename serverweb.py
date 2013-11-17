#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
import sqlite3
import database_manager

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def x():
    if request.method == 'GET':
        #return 'this is GET\n'
        db = database_manager.DatabaseManager()
        db.connect()
	titles = db.select_title()
	movies_list = db.import_db()
        db.close()
        return render_template('index.html', to_print=movies_list)

    if request.method == 'POST':
        print 'POST keys: ', request.form.keys()
        return 'this is a POST\n'


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')


