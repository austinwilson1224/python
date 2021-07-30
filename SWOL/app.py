from flask import Flask, render_template, request

app = Flask(__name__)

ENV = "dev"
if ENV == "dev":
    app.debug=True
app.debug=True

@app.route("/")
def home():
    return render_template("signin.html", title="Home")
@app.route("/submit", methods=["POST"])
def submit():
    print(request.form['test'], request.form['test2'])
    return render_template("submit.html", msg1=request.form['test'], msg2=request.form['test2'])


@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/test")
def test():
    return render_template("test.html")




if __name__ == "__main__":
    app.run()