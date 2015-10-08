__author__ = 'fengbq@live.com'

from flask import render_template
from webapp import app

# web page
@app.route('/')
@app.route('/help')
def hello_world():
    return render_template(
        "index.jade",
        title="API DOC",
    )
    return 'Hello World!'

