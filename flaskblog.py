#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 22:34:55 2021

@author: x0
"""

from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
        {
            'author': 'Petec 0x0',
            'title': 'First blog',
            'content': 'This is the content of the first blog post on the flask blog',
            'date_posted': 'March 29 2021'
         },
        {
            'author': 'Onyedikachi',
            'title': 'Techinical blog',
            'content': 'THere you can get help of any object by pressing Ctrl+I in front of it, either on the Editor or the Console.',
            'date_posted': 'March 30 2021'
         }
    ]

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')