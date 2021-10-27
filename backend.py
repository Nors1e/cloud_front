from flask import Flask, redirect, render_template, url_for, request
from markupsafe import escape


# Instance of a flask web application
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

#fixed
# @app.route("/login", methods=["POST", "GET"])
# def login():
#     if request.method == "POST":
#         user = request.form["nm"]
#         return redirect(url_for("user", usr=user))
#     else:
#         return render_template("base.html")


# @app.route("/<usr>")
# def user(usr):
#     return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)


# Adding new line


# # If user tries to access this page they get redirected to another page if they do not have privs
# @app.route("/admin")
# def admin():
#     return redirect(url_for("home"))

# # Registers unique url and feeds it into page
# @app.route("/<name>")
# def user(name):
#     return f"Hello <h1>{name}</h1>!"

# # Routing
# @app.route("/")
# def homepage(name=None):
#     return render_template('index.html', name=name)

# # Route to the home page
# @app.route("/home")
# def spice():
#     return "I'm back"

# @app.route('/home/user/<username>')
#     return f'User {escape(username)}'
