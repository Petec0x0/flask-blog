#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 13:29:25 2021

@author: x0
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from blog.models import User, Post


class RegisterForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(label="Email Address", validators=[Email(), DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
    password_confirm = PasswordField(label="Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label="Register")

    # custom validation to check if username already exist
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exist.')
            
    # custom validation to check if email address already exist
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email Address already exist.')

class LoginForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Login")
