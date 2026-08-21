from flask import Flask
Likhith = Flask(__name__)
@Likhith.route("/")
def home():
    return 'Welcome to flask'
if __name__ == "__main__":
    Likhith.run(debug=True)
