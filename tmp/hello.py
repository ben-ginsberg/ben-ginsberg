from flask import Flask, url_for, render_template
from shorturl import getIdFromShortUrl
app = Flask(__name__)

@app.route('/')
def index():
    return "Yuki"

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' %post_id



    #with app.test_request_context():
    #print url_for('index')
    #print url_for('hello')
    #print url_for('hello', next='/')
    #print url_for('show_user_profile',username='John Doe')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

@app.route('/m/<mstr>')
def show_media(mstr):
    mid = getIdFromShortUrl(mstr)
    return mid

if __name__ == '__main__':
    app.run(debug=True)