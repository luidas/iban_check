"""Flask web application for user interface"""
from flask import Flask, redirect, url_for, request, render_template
import checker

app = Flask(__name__)


@app.route("/")
def index():
    """Returns the index template"""
    return render_template("index.html")


@app.route("/output")
def output():
    """
    Calls checker to check user input.
    Returns output template.
    """
    checked_ibans = checker.check_input_file("ibans_input.txt")
    return render_template("output.html", title="Output", ibans=checked_ibans)


@app.route("/upload", methods=["POST"])
def upload():
    """
    Gets user input from form.
    Writes to a file.
    Redirects to output URL.
    """
    user_input = request.form["input"]
    with open("ibans_input.txt", mode="w", encoding="utf8") as file:
        file.write(user_input)
        file.close()
    return redirect(url_for("output"))


if __name__ == "__main__":
    app.run(debug=True)
