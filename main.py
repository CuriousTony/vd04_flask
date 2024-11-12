from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def browse_index():
    return render_template("index.html")


@app.route("/blog/")
def browse_blog():
    return render_template("blog.html")


@app.route("/contacts/")
def browse_contacts():
    return render_template("contacts.html")


if __name__ == "__main__":
    app.run()
