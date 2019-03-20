from flask import Flask, url_for, request, render_template, Markup

app = Flask(__name__)


# simple Hello World
# @app.route('/')
# def hello():
#     return "Hello World!"


# # routing
# @app.route('/')
# def index():
#     return "Index page"
#
#
# @app.route('/hello')
# def hello():
#     return "Hello World!"
#
#
# # variable rules
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username
#
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id
#
#
# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath %s' % subpath
#
#
# # unique URLs /redirection behavior
# @app.route('/projects/')
# def projects():
#     return 'The project page'
#
#
# @app.route('/about')
# def about():
#     return 'The about page'
#
# # URL building
# @app.route('/')
# def index():
#     return 'index'
#
#
# # @app.route('/login')
# # def login():
# #     return 'login'
#
#
# @app.route('/user/<username>')
# def profile(username):
#     return '{}\'s profile'.format(username)


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))


# testing in browser
# /
# /login
# /login?next=/
# /user/John%20Doe

# # HTTP methods
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return "login"
#     else:
#         return 'loginform'


# # Static files
# url_for('static', filename="style.css")

# Rendering templates
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


# Accessing request data
# The request object
@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
