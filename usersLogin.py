from flask import Flask,request,render_template,redirect
from wtforms import Form,TextAreaField,PasswordField,validators,IntegerField,DateField,StringField
# from db import *
from model import *
user = User()
# app=Flask(__name__) # model里面有定义了，这里再定义就会出错


class LoginForm(Form):
    username = StringField("username",[validators.DataRequired()])
    password = PasswordField("password",[validators.DataRequired()])

class PublishForm(Form):
    content = StringField("content",[validators.DataRequired()])
    sender = StringField("sender",[validators.DataRequired()])

@app.route("/user",methods=['GET','POST'])
def login():
    myForm = LoginForm(request.form)
    if request.method == "POST":
        # username=request.form['username']
        # password=request.form['password']
        # if username == "jikexueyuan" and password == "123456":
        # myForm.validate()是为了判断表单是否有效
        # if myForm.username.data=="jikexueyuan" and myForm.password.data=="123456" and myForm.validate():
        user.username,user.password = (myForm.username.data,myForm.password.data)
        if user.isExisted():
            return redirect("http://www.jikexueyuan.com")
        else:
            message="Login Failed"
            return render_template("usersLogin.html",message=message,form=myForm)
    return render_template("usersLogin.html",form=myForm)

@app.route("/register",methods=["GET","POST"])
def register():
    myForm = LoginForm(request.form)
    if request.method == "POST":
        user.username, user.password = (myForm.username.data, myForm.password.data)
        user.add()
        return "Register Successfully!"
    return render_template("usersLogin.html",form=myForm)

@app.route("/show",methods=["GET","POST"])
def show():
    myEntryForm = PublishForm(request.form)
    list = getAllEntry()
    e = Entry()
    if request.method == "POST":
        e.content,e.sender=(myEntryForm.content.data,myEntryForm.sender.data)
        e.add()
        return render_template("messageBoard.html",entries=list,form=myEntryForm)
    return render_template("messageBoard.html",entries=list, form=myEntryForm)


@app.route("/search",methods=["GET","POST"])
def search():
    if request.method == "POST":
        username=request.form["username"]
        u=User.query.filter_by(username=username).first()
        l=[]
        l=Item.query.filter_by(sender_id=u.id).all()
        return render_template("search.html",context=l)
    return render_template("search.html")



if __name__=="__main__":
    app.run(port=8080)