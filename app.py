# I'd love to the further study on this,
# I feel like I'm falling behind here.


from flask import Flask, request, render_template
from stories import story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "okay-then"
debug = DebugToolbarExtension(app)

@app.route('/madlibs')
def get_prompts():
    prompts = story.prompts
    return render_template('madlibs.html', prompts=prompts)

@app.route('/story')
def generate_story():
    text = story.generate(request.args)
    return render_template('story.html', text=text)