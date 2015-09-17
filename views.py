from little_web_dev import app
from flask import Flask, url_for, render_template
from shorturl import getIdFromShortUrl
import urllib
import json


@app.route('/')
def index():
    return "Yuki"

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/home.html')
def home():
    return render_template("home.html")

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/privacy.html')
def privacy():
    return render_template("privacy.html")

@app.route('/terms.html')
def terms():
    return render_template("terms.html")

@app.route('/under.html')
def under():
    return render_template("under.html")

@app.route('/m/<mstr>')
def show_media(mstr):
    mid = getIdFromShortUrl(mstr)
    fd = urllib.urlopen("http://dev1.getlittleapp.com/medias/"+mid)
    data = fd.read()
    dict = json.loads(data)
    return render_template("mediaTemplate.html",
                           mediaInfo = dict)

#@app.route('/hello')
    #def hello():
#return 'Hello World!'

#@app.route('/user/<username>')
#def show_user_profile(username):
#    return 'User %s' % username

#@app.route('/post/<int:post_id>')
#def show_post(post_id):
#    return 'Post %d' %post_id
#


    #with app.test_request_context():
    #print url_for('index')
    #print url_for('hello')
    #print url_for('hello', next='/')
    #print url_for('show_user_profile',username='John Doe')
#@app.route('/hello/<name>')
    #def hello(name=None):
#return render_template('hello.html',name=name)



