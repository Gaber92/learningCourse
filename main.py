from flask import Flask
from flask import Flask, render_template
from flask import request


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


@app.route("/aboutus/", methods=["GET"])
def aboutus():
    return render_template("fakebook.html")


@app.route("/contact", methods=["POST"])
def contact():
    contact_name = request.form.get("contact-name")
    contact_email = request.form.get("contact-email")
    contact_message = request.form.get("contact-message")
    return render_template("savemsg.html", contact_name=contact_name, contact_email=contact_email, contact_message=contact_message)


@app.route("/count/")
def count():
    out = ''
    for i in range(10):
        out += str(i) + '<br>'
    return out


if __name__ == '__main__':
    app.run()
