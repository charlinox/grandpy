from flask import Flask, render_template

app = Flask(__name__)

@app.route("/charles/casassus")
def index():
    return render_template("base.html", title="Mon super site")


if __name__ == "__main__":
    app.run()