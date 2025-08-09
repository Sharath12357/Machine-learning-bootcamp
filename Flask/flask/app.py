from flask import Flask

app=Flask(__name__)
@app.route('/')
def welcome():
    return "Welcome to my house i am here if i am not there in my home i am in my friend  home near by my home  "
@app.route('/index')
def index():
    return "Welcome to my index page it was beautiful"

@app.route('/main')
def main():
    return "Welcome to my Main Page"


if __name__=="__main__":
    app.run(debug=True)
