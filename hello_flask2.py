from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask_script import Manager
app = Flask(__name__)
manager = Manager(app)

# app = Flask(__name__)

# @app.route('/')
# def index():
#     user_agent = request.headers.get('User-Agent')
#     return '<h1>Hello, Flask! Your browser is %s.</h1>' %user_agent

# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, %s!</h1>' %name

# @app.route('/ashes/')
# def ashes():
#     return '<h1>Ashes!</h1>', 400

# @app.route('/response/')
# def response_test():
#     response = make_response('<h1>This document carries a cookie!</h1>')
#     response.set_cookie('answer', '42')
#     return response

# @app.route('/redirect/')
# def redirect_test():
#     return redirect('http://www.baidu.com')

# @app.route('/abort/user/<id>')
# def abort_test(id):
#     user = load_user(id)
#     if not user:
#         abort(404)
#     return '<h1>Hello, %s</h1>' % user.name

if __name__ == '__main__':
    manager.run()