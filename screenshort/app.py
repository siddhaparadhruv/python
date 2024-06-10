from flask import Flask, render_template, redirect
import subprocess

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/take_screenshot")
def take_screenshot():
    try:
        subprocess.run(["python", "screenshot_capture.py"])
        return redirect("/")
    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    app.run(debug=True)
