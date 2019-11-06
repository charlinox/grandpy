from flask import Flask, render_template
from config import Config
from .parser import Parser
from .api import GoogleMapsDownloader, WikiDownloader
from .forms import QuestionForm

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object(Config)
# To get one variable, tape app.config['MY_VARIABLE']

@app.route("/")
def index():
    return render_template("base.html", title="Grand Py")

@app.route('/question')
def login():
    form = QuestionForm()
    return render_template('question.html', title='Question à Grang Py', form=form)

@app.route("/api", methods=["POST"])
def api():
    form = QuestionForm()
    if form.validate_on_submit():
        data = form.post.question
        parser = Parser(data)
        parsed_question = parser.start()
        data_localisation = GoogleMapsDownloader(parsed_question)
        data_wiki = WikiDownloader(data_localisation)
        data_by_coord = data_wiki.fetch_by_coord(data_localisation)
        data_by_title = data_wiki.fetch_by_title(data_by_coord)
        return

# if __name__ == "__main__":
#     app.run(debug=True)
