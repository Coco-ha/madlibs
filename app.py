from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def homepage():
    prompt = silly_story.prompts

    return render_template(
        "questions.html",
        prompt = prompt
    )

@app.get("/results")
def results_here():
    story = silly_story.get_result_text(request.args)
    return render_template(
        "results.html",
        story=story
         )