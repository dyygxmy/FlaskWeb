
from flask import Flask,render_template,url_for,request,redirect

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return redirect(url_for('add'))

@app.route('/add',methods=['GET','POST'])
def add():
    message="这是一个计算器"
    if request.method == 'POST':
        a=request.form['adder1']
        b=request.form['adder2']
        a=int(a)
        b=int(b)
        c=a+b
        return render_template("index.html", message=str(c))
    return render_template("index.html",message=message) #返回渲染后的结果()

if __name__=="__main__":
    app.run(port=8080)