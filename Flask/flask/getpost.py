from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome my home page"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/Home")
def Home():
    return render_template('Home.html')

@app.route("/file",methods=['GET','POST'])
def file():
    if request.method=='POST':
        name=request.file['name']
        return f'Hello{name}!'
    return render_template('file.html')






if __name__=='__main__':
    app.run(debug=True)