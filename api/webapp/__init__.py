"""
The flask  application package.
"""
__author__ = 'fengbq@live.com'


from flask import Flask

app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

import webapp.views
import webapp.apiroute