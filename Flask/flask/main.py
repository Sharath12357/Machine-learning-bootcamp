from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome my home page"

@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/Home")
def Home():
    return render_template('Home.html')



if __name__=='__main__':
    app.run(debug=True)