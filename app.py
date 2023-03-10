from flask import Flask, request,render_template
from stories import story
from stories2 import story2
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickenzarecool21837"
debug = DebugToolbarExtension(app)


@app.route("/")
def story_form():
    mock_prompts = story.prompts

    return render_template("story-form.html", prompts = mock_prompts)

@app.route("/story")
def show_story():
    if request.args["theme"] == "dark":
        my_story = story.generate((request.args))
        
    elif request.args["theme"] == "light":
        my_story = story2.generate((request.args))
    return render_template("story.html", text = my_story)



