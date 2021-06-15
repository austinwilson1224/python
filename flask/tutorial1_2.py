from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home</h1>"

@app.route("/<name>")
def name(name):
    return f"<div style='color: red;'>Hello {name}</div>"

@app.route("/admin")
def admin():
    return redirect(url_for("name", name="Admin!"))# name of the function you want to redirect to
if __name__ == "__main__":
    app.run()