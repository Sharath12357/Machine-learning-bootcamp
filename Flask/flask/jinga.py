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

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello{name}!'
    return render_template('form.html')

@app.route('/sucess/<int:score>')
def sucess(score):
    res=''
    if score>=50:
       res='PASS'
    else:
        res='FAIL'
    return render_template('result.html',results=res)
       




if __name__=='__main__':
    app.run(debug=True)