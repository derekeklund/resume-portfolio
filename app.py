from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Let's try this again!"

if __name__ == '__main__':
    app.run(debug=True) # This should be set to false in a production environment