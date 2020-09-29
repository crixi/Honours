from flask import Flask
app = Flask(__name__)

@app.route("/")
def root() :
    return "The default, 'root' route"

@app.route("/hello/")
def hello():
    return "Hello Napier!!!"

@app.route("/goodbye/")
def goodbye():
    return "Goodbye crual world"

if __name__== "__main":
    app.run(host='0.0.0.0',debug=True)



