# -*- coding: utf-8 -*-
"""
    My First Pastebin models
    Copyright 2010 Bjørn Tore Håvie
"""
from google.appengine.ext import db

class Paste(db.Model):
    content = db.TextProperty()
    type = db.StringProperty()