from flask import Flask, redirect, render_template, url_for
from markupsafe import escape


# Instance of a flask web application
app = Flask(__name__)


@app.route("/<name>")
def home(name):
    return render_template("index.html", content=name)


if __name__ == "__main__":
    app.run()





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