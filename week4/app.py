<<<<<<< HEAD
from flask import *
app=Flask(__name__,static_folder="public",static_url_path="/")

app.secret_key="any string but secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signin():
    account=request.form["account"]
    password=request.form["password"]
    if account == "test" and password == "test":
        session["account"]=account
        return redirect("/member")
    elif account == None or password == None:
        return redirect("/error?message=請輸入帳號、密碼")
    else:
        return redirect("/error?message=帳號或密碼輸入錯誤")

@app.route("/member")
def member():
    if "account" in session :
        return render_template("member.html")
    else:
        return redirect("/")


# /error?message=錯誤訊息
@app.route("/error")
def error():
    msg=request.args.get("message", "")
    return render_template("error.html", message=msg)

@app.route("/signout")
def signout():
    del session["account"]
    return redirect("/")

@app.route("/square")
def square():
    number=request.args.get("number", "")
    return redirect(url_for("result", Num=number))

@app.route("/square/<string:Num>")
def result(Num):
    Num=int(Num)
    result=Num*Num
    return render_template("square.html", ans=result)

=======
from flask import *
app=Flask(__name__,static_folder="public",static_url_path="/")

app.secret_key="any string but secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signin():
    account=request.form["account"]
    password=request.form["password"]
    if account == "test" and password == "test":
        session["account"]=account
        return redirect("/member")
    elif account == None or password == None:
        return redirect("/error?message=請輸入帳號、密碼")
    else:
        return redirect("/error?message=帳號或密碼輸入錯誤")

@app.route("/member")
def member():
    if "account" in session :
        return render_template("member.html")
    else:
        return redirect("/")

# /error?message=錯誤訊息
@app.route("/error")
def error():
    msg=request.args.get("message", "")
    return render_template("error.html", message=msg)

@app.route("/signout")
def signout():
    del session["account"]
    return redirect("/")

@app.route("/square")
def square():
    number=request.args.get("number", "")
    return redirect(url_for("result", Num=number))

@app.route("/square/<string:Num>")
def result(Num):
    Num=int(Num)
    result=Num*Num
    return render_template("square.html", ans=result)

>>>>>>> 99530c3b8ce0b5b41fa4d0b27b2b29ae9ec3dc0a
app.run(port=3000)