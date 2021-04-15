#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 22:34:55 2021

@author: x0
"""

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config['SECRET_KEY'] = "OIHIIH8Y8HG8TUV3DFCYV3FDVC77F7FVV"

from . import routes