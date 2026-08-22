'''
from flask import Flask, url_for
app_react = Flask(__name__)
@app_react.route('/')
def home():
    return 'This is my flask app'

@app_react.route('/login')
def login():
    return f'{url_for("login")}'
if __name__ == "__main__":
    app_react.run(debug=True,port=3456)
    '''


'''
from flask import Flask,url_for
app_react = Flask(__name__)
@app_react.route('/login')
def login():
    return f'{url_for("user")}'

@app_react.route('/user')
def user():
    return 'This is my flask app'
if __name__ == "__main__":
    app_react.run(debug=True)
    '''

'''
from flask import Flask, redirect, url_for
app_react = Flask(__name__)
@app_react.route('/login')
def login():
    return redirect(url_for("dashboard"))

@app_react.route('/dashboard')
def dashboard():
    return 'This is my dashboard'
if __name__ == "__main__":
    app_react.run(debug=True)
    '''

'''
from flask import Flask
app_react = Flask(__name__)
@app_react.route('/',methods=['GET','POST'])

def home():
    return 'Send data to the server'
if __name__ == "__main__":
    app_react.run(debug=True)
'''

'''
from flask import Flask, request
app_react = Flask(__name__)
@app_react.route('/', methods = ['GET','PUT'])

def user():
    return 'Update data to the server'
if __name__ == "__main__":
    app_react.run(debug=True)
'''


'''
from flask import Flask, request
app_react = Flask(__name__)
@app_react.route('/', methods = ['GET','DELETE'])

def home():
    return 'Delete data to the server'
if __name__ == "__main__":
    app_react.run(debug=True)
'''

'''
from flask import Flask, request
app_react = Flask(__name__)
@app_react.route('/')

def home():
    return f"Method {request.method}"
if __name__ == "__main__":
    app_react.run(debug=True)
'''


'''
from flask import Flask, request
app_react = Flask(__name__)
@app_react.route('/student')

def home():
    name = request.args.get("name")
    age = request.args.get("age")
    batch = request.args.get("batch")

    return f"Name: {name}, Age:{age}, batch:{batch}"
if __name__ == "__main__":
    app_react.run(debug=True)
'''


'''
from flask import Flask, request
app_react = Flask(__name__)
@app_react.route('/login', methods = ['GET', 'POST'])

def login():
    if request.method == "POST":
       email = request.form.get("email")
       password = request.form.get("password")
       return f"email: {email}, password: {password}"
   
    return """
    <form method = "POST">
        <input type = "email" name = "email">
        <input type = "password" name = "password">
        <button type = "submit">Login</button>
    </form>
    """
if __name__ == "__main__":
    app_react.run(debug=True)
'''


'''
from flask import Flask, request
app_react = Flask(__name__)
@app_react.route('/student', methods = ['GET', 'POST'])

def student():
    if request.method == "GET":
        return "Please send student data using POST"
    data = request.get_json()
    name = request.get_json("name")
    age = request.get_json("age")
    return f"Name: {name}, Age:{age}"

if __name__ == "__main__":
    app_react.run(debug=True)
'''






