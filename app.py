import checker
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success")
def success():
    checked_ibans = checker.check_input_file("ibans_input.txt")
    return render_template('output.html', title='Output', ibans=checked_ibans)


@app.route("/upload", methods=["POST"])
def upload():
    user_input = request.form["ibans"]
    file = open("ibans_input.txt", "w")
    file.write(user_input)
    file.close()
    return redirect(url_for("success"))


if __name__ == "__main__":
    app.run(debug=True)
