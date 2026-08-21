'''
from flask import Flask
app = Flask(__name__)
@app.route('/user/<name>/<int:age>')

def user(name,age):
   return f'my name is {name} iam {age} years old'
if __name__ == '__main__':
   app.run(debug = True)

  

from flask import Flask, app 
app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    return 'this is my app'
if __name__ == '__main__':
    app.run(debug = True) 



from flask import Flask 
app = Flask(__name__)
@app.route('/user/<name>')
def user(name):
    return f'my name is {name}'
if __name__ == '__main__':
    app.run(debug=True,port=4000)
    
from flask import Flask
app = Flask(__name__)
@app.route('/user/<uuid:user_id>')
def user(user_id):
    return str(user_id)
if __name__ == '__main__':
    app.run(debug=True, port=4000)
     '''
from flask import Flask
app = Flask(__name__)
@app.route('/user/<path:filename>')
def user(filename):
    return f'{filename}'
if __name__ == '__main__':
    app.run(debug=True)