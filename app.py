from flask import Flask,render_template,request
import pymysql
app=Flask(__name__)
db_config = {
    "host" : "localhost",
    "user" : "root",
    "password" : "Root",
    "database" : "atm"
}
@app.route("/")
def landing():
    return render_template("index.html")

@app.route("/withdraw1")
def withdraw1():
    return render_template("withdraw1.html")
@app.route("/index")
def home():
    return render_template("index.html")
@app.route("/withdraw2",methods=["POST","GET"])
def withdraw2():
    accno = request.form["accno"]
    pin = request.form["pin"]
    print(accno)
    print(pin)

    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    query = "select * from accounts where user_accno = %s"
    cursor.execute(query,(accno))
    data = cursor.fetchone()
    conn.close()
    print(data)
    if data is None:
        return render_template("withdraw1.html",msg="noaccount")
    elif data[-2] is None:
        return render_template("withdraw1.html",msg="nopin")
    elif data[-2] != int(pin):
        return render_template("withdraw1.html",msg="wrongpin")
    else:
        return render_template("withdraw2.html",user_name=data[1],accno=accno)
    
@app.route("/withdraw3",methods=["POST","GET"])
def withdraw3():
    accno = request.form["accno"]
    amount = request.form["amount"]
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    query = "select user_balance,user_name from accounts where user_accno = %s"
    cursor.execute(query,(accno))
    data = cursor.fetchone()
    conn.close()
    print(data)
    if int(amount) <= int(data[0]):
        balance = int(data[0]) - int(amount)
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()
        query = "update accounts set user_balance = %s where user_accno = %s"
        cursor.execute(query,(balance,accno))
        conn.commit()
        conn.close()
        return render_template("withdraw2.html",msg="balance",accno=accno,user_name=data[1])
    else:
        return render_template("withdraw2.html",msg="nobalance",accno=accno,user_name=data[1])

    
@app.route("/deposit")
def deposit():
    return render_template("deposit.html")

@app.route("/deposit2",methods=["POST","GET"])
def deposit2():
    accno = request.form["accno"]
    amount = int(request.form["amount"])
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    query = "select * from accounts where user_accno = %s"
    cursor.execute(query,(accno))
    data = cursor.fetchone()
    conn.close()
    print(data)
    if data is None:
        return render_template("deposit.html",msg="noaccount")
    else:
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()
        query = "update accounts set user_balance = user_balance + %s where user_accno = %s"
        cursor.execute(query,(amount,accno))
        conn.commit()
        conn.close()
        return render_template("deposit.html",msg="account")
    
@app.route("/ministatement1")
def ministatement1():
    return render_template("ministatement1.html")
@app.route("/ministatement2",methods=["POST","GET"])
def ministatement2():
    accno = request.form["accno"]
    pin = request.form["pin"]
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    query = "select * from accounts where user_accno = %s"
    cursor.execute(query,(accno))
    data = cursor.fetchone()
    conn.close()
    print(data)
    if data is None:
        return render_template("ministatement1.html",msg="noaccount")
    elif data[-2] is None:
        return render_template("ministatement1.html",msg="nopin")
    elif int(pin) != int(data[-2]):
        return render_template("ministatement1.html",msg="wrongpin")
    else:
        name = data[1]
        email = data[2]
        balance = data[-1]
        return render_template("ministatement2.html",accno=accno,name=name,email=email,balance=balance)
    
@app.route("/pingeneration1")
def pingeneration1():
    return render_template("pingeneration1.html")
@app.route("/pingeneration2",methods=["POST","GET"])
def pingeneration2():
    accno = request.form["accno"]
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    query = "select * from accounts where user_accno = %s"
    cursor.execute(query,(accno))
    data = cursor.fetchone()
    conn.close()
    print(data)
    if data is None:
        return render_template("pingeneration1.html",msg="noaccount")
    elif data[-2] != None:
        return render_template("pingeneration1.html",msg="account")
    else:
        return render_template("pingeneration2.html",accno=accno)
    
@app.route("/pingeneration3",methods=["POST","GET"])
def pingeneration3():
    accno = request.form["accno"]
    pin = request.form["pin"]
    cpin = request.form["cpin"]
    if pin != cpin:
        return render_template("pingeneration2.html",accno=accno,msg="wrongpin")
    else:
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()
        query = "update accounts set user_pin = %s where user_accno = %s"
        cursor.execute(query,(pin,accno))
        conn.commit()
        conn.close()
        return render_template("pingeneration2.html",msg="ok")
app.run(port=5014)