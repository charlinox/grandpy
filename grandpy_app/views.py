from flask import Flask, request, render_template

from config import Config
from .forms import QuestionForm
from .main import main

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object(Config)
# To get one variable, tape app.config['MY_VARIABLE']

@app.route("/")
def index():
    return render_template("base.html", title="Grand Py")

@app.route('/question')
def question():
    form = QuestionForm()
    return render_template('question.html', title='Question à Grang Py', form=form)

# @app.route('/question', methods=['POST'])
# def question():
    # if request.method == "POST":
#     return request.form['question']

@app.route("/api", methods=["POST"])
def api():
    form = QuestionForm()
    if form.validate_on_submit():
        question = form.post.question
        api_data = main(question)

# if __name__ == "__main__":
#     app.run(debug=True)
