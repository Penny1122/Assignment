from flask import *
import mysql.connector
from mysql.connector import pooling
from flask_restful import Api, Resource

connection_pool = mysql.connector.pooling.MySQLConnectionPool(
    host="localhost",
    user="root",
    password="free4321",
    database="website",
    pool_name = "mypool",
    pool_size = 5,
    pool_reset_session = True,

)

app=Flask(__name__,static_folder="public",static_url_path="/")
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
api = Api(app)
app.secret_key="any string but secret"

class ResearchUser(Resource):
    def get(self):
        if "id" and "name" in session :
            try:
                connection = connection_pool.get_connection()
                cursor =  connection.cursor()
                username = request.args.get("username")
                cursor.execute("SELECT id, name , username FROM member where username=%s",[username])                
                result = cursor.fetchone()
                if result !=None:
                    return {
                        "data":{
                            "id":result[0],
                            "name":result[1],
                            "username":result[2],
                    }}
                return {"data":None}
            except:
                print("Unexpected Error")
            finally:
                cursor.close()
                connection.close()
        return {"data":None}
    def patch(self):
        if "id" and "name" in session :
            id=session["id"]
            try:
                connection = connection_pool.get_connection()
                cursor =  connection.cursor()
                newName=request.json["name"]
                print(request.json)
                cursor.execute("UPDATE member SET name=%s WHERE `id`=%s",[newName,id])
                connection.commit()
                return {"ok":True}
            except:
                print("Unexpected Error")
                return{"error":True}
            finally:
                cursor.close()
                connection.close()
        return{"error":True}

api.add_resource(ResearchUser,"/api/member")

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
    try:
        connection = connection_pool.get_connection()
        cursor =  connection.cursor()
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
    except:
            print("Unexpected Error")
    finally:
        cursor.close()
        connection.close()

    

@app.route("/signin", methods=["POST"])
def sign_in():
    account=request.form["account"]
    password=request.form["password"]
    try:
        connection = connection_pool.get_connection()
        cursor =  connection.cursor()
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
    except:
            print("Unexpected Error")
    finally:
        cursor.close()
        connection.close()

@app.route("/member")
def member():
    if "id" and "name" in session :
        name=session["name"]
        try:
            connection = connection_pool.get_connection()
            cursor =  connection.cursor()
            cursor.execute("SELECT member.name, message.content FROM member INNER JOIN message WHERE member.id=message.member_id ORDER BY message.time DESC")
            content=cursor.fetchall()
            return render_template("member.html", name=name, content=content)
        except:
            print("Unexpected Error")
        finally:
            cursor.close()
            connection.close()
    else:
        return redirect("/")

@app.route("/message",  methods=["POST"])
def message():
    content=request.form["content"]
    id=session["id"]
    try:
        connection = connection_pool.get_connection()
        cursor =  connection.cursor()
        sql="INSERT INTO message (member_id,content) VALUES (%s, %s)"
        values=(id, content)
        cursor.execute(sql, values)
        connection.commit()
    except:
        print("Unexpected Error")
    finally:
        cursor.close()
        connection.close()
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



app.run(port=3000, debug=True)