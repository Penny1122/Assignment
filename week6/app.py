from sqlite3 import connect
from flask import *
import mysql.connector

connection = mysql.connector.connect(
host="localhost",
user="root",
password="free4321",
database="website"
)
cursor = connection.cursor()

app=Flask(__name__,static_folder="public",static_url_path="/")

app.secret_key="any string but secret"

@app.route("/")
def index():
    message=request.args.get("message", "")
    message2=request.args.get("message2", "")
    return render_template("index.html", message=message, message2=message2)

@app.route("/signup", methods=["POST"])
def register():
    name=request.form["name"]
    account=request.form["account"]
    password=request.form["password"]
    sql= "SELECT * FROM member WHERE username = %s"
    cursor.execute(sql, (account,))
    records=cursor.fetchone()
    if name!="" and account!="" and password!="":
        if records != None:
            return redirect("/error?message=帳號已經被註冊")
        else:
            insert = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
            value = (name, account, password)
            cursor.execute(insert, value)
            connection.commit()
            return redirect("/")
    else:
        return redirect("/?message=資料不可空白")

    

@app.route("/signin", methods=["POST"])
def sign_in():
    account=request.form["account"]
    password=request.form["password"]
    sql= "SELECT id, name, username FROM member WHERE username = %s AND password = %s"
    cursor.execute(sql, (account,password))
    records=cursor.fetchone()
    if account!="" and password!="":
        if records != None:
            session["id"]=records[0]
            session["name"]=records[1]
            return redirect("/member")
        else:
           return redirect("/error?message=帳號或密碼輸入錯誤") 
    else:
        return redirect("/?message2=請輸入帳號、密碼")

@app.route("/member")
def member():
    if "id" and "name" in session :
        name=session["name"]
        cursor.execute("SELECT member.name, message.content FROM member INNER JOIN message WHERE member.id=message.member_id ORDER BY message.time DESC")
        content=cursor.fetchall()
        return render_template("member.html", name=name, content=content)
    else:
        return redirect("/")

@app.route("/message",  methods=["POST"])
def message():
    content=request.form["content"]
    id=session["id"]
    sql="INSERT INTO message (member_id,content) VALUES (%s, %s)"
    values=(id, content)
    cursor.execute(sql, values)
    connection.commit()
    return redirect("/member")

# /error?message=錯誤訊息
@app.route("/error")
def error():
    msg=request.args.get("message", "")
    return render_template("error.html", message=msg)

@app.route("/signout")
def sign_out():
    del session["id"]
    del session["name"]
    return redirect("/")

@app.route("/square/<getNumber>")
def result(getNumber):
    Num=int(getNumber)
    result=Num*Num
    return render_template("square.html", ans=result)



app.run(port=3000)