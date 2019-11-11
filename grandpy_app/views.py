from flask import Flask, request, render_template, jsonify
from flask_wtf.csrf import CSRFProtect

from config import Config
from .forms import QuestionForm
from .main import main


app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object(Config)
# To get one variable, tape app.config['MY_VARIABLE']
csrf = CSRFProtect(app)

@app.route('/')
def index():
    form = QuestionForm()
    return render_template(
        'question.html',
        title='Question à Grang Py',
        form=form,
        API_KEY=app.config['API_KEY_FRONT']
    )

# @app.route('/question', methods=['POST'])
# def question():
    # if request.method == "POST":
#     return request.form['question']

@app.route("/api", methods=["POST"])
def api():
    form = QuestionForm()
    if form.validate_on_submit():
        question = form.question.data
        return jsonify(main(question))
        

# if __name__ == "__main__":
#     app.run(debug=True)
