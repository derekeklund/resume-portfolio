from flask import Flask, request, render_template
from flask.wrappers import Response
import git

app = Flask(__name__)

# Webhook for continuous deployment
@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('./resume-portfolio')
    origin = repo.remotes.origin
    repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return "Updated PythonAnywhere successfully", 200

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')
    # return "Continuous deployment enabled :) It's working! Yayyyy. Test 1, 2, 3..."

@app.route('/about', methods=["GET", "POST"])
def about():
    return render_template('about.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
    return render_template('contact.html')

@app.route('/resume', methods=["GET", "POST"])
def resume():
    return render_template('resume.html')


if __name__ == '__main__':
    app.run(debug=True) # This should be set to false in a production environment