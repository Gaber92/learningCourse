from flask import Flask
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def index2():
    return render_template("index2.html")


@app.route("/hair/")
def hairsaloon():
    return render_template("hairsaloon.html")

@app.route("/aboutus/")
def aboutus():
    return render_template("fakebook.html")

@app.route("/count/")
def count():
    out = ''
    for i in range(10):
        out += str(i) + '<br>'
    return out


if __name__ == '__main__':
    app.run()
