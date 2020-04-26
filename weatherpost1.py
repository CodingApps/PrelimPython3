from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Wazzup All 'Round the World";

@app.route("/goodbye")
def goodbye():
    return "Wazzup LaterOn";

@app.route("/hello/<name>/<int:age>")
def hello_name(name, age):
    return "Wazzup, {} you're {}".format(name, age)

if __name__ == '__main__' :
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port, debug=True)