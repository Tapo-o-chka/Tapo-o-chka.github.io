from flask import *
import re
import database

app = Flask(__name__)
app.secret_key = 'secret_key'
db = database.Database('base.db')
@app.route('/home')#r
def home():
    return render_template("home.html")
@app.route('/app') #r
def web_app():
    if 'warehouse' in session and 'login' in session:
        return render_template("app.html")
    else:
        return redirect('/home')

@app.route('/login',methods=['POST']) #r
def login(): 
    if request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]
        if re.match(r"[A-Za-z0-9]{3,}", login) and re.fullmatch(r"[A-Za-z0-9]{7,}", password):
            data = db.login(login,password)
            if data != None:
                session['role'],session['warehouse'],session['login'] = data[1],data[2],login
            return redirect('/home')
@app.route('/logout',methods=['POST']) #r
def logout():
    if request.method == "POST":
        if 'warehouse' in session and 'login' in session:
            del session['warehouse']
            del session['login']
            del session['role']
            return redirect('/home')
@app.route('/register',methods=['POST']) #r
def register():    
    if request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]
        email = request.form['email']
        if re.match(r"[A-Za-z0-9]{3,}", login) and re.fullmatch(r"[A-Za-z0-9]{7,}", password):
            db.register_warehouse(login,password,email)
            data = db.login(login,password)
            session['login'],session['warehouse'],session["role"] = login,data[2], 0
            return redirect('/app')
@app.route('/orders/<type>',methods=['GET']) #r
def orders(type):
    if request.method == "GET":
        if 'warehouse' in session or 'login' in session:
            orderz = db.get_orders(type,0,session['warehouse'])
            return orderz

@app.route('/makeorder',methods=['POST']) #r
def makeorder():    
    if request.method == 'POST':
        if 'warehouse' in session and 'login' in session:
            client = request.form["client"]
            type = request.form["type"]
            date = request.form["date"]
            place = request.form["place"]
            if re.fullmatch(r'^[0-9]+$',client) and (type == "outcoming" or type == "incoming"):
                db.add_order(0,client,type,date,place,session['warehouse'])
                return redirect('/app')
@app.route('/toapprove/<id>',methods=['POST']) #r
def toapprove(id):
    if request.method == "POST":
        if 'warehouse' in session and 'login' in session:
            db.approve_order(id)
            return redirect('/app')
@app.route('/approve/<id>/<type>', methods=['POST']) #r
def approve(id, type):
    if request.method == "POST":
        if 'warehouse' in session and 'login' in session:
            if type == 'reject':
                print(db.get_orders('all',0,2))
                print(db.get_orders('all',1,2))
                print(db.get_orders('all',2,2))
                db.decline_order(id)
                return redirect('/app')  
            elif type == 'approve':
                print('approve')
                db.approve_order(id)
                return redirect('/app')
        else:
            return redirect('/home')
@app.route('/approvement/<type>',methods=['GET']) #r
def approvement(type):
    if request.method == "GET":
        if 'warehouse' in session or 'login' in session:
            orderz = db.get_orders(type,1,session['warehouse'])
            print(orderz)
            return orderz

@app.route('/hystory/<type>',methods=['GET']) #r
def hystory(type):
    if request.method == "GET":
        if 'warehouse' in session and 'login' in session:
            orderz = db.get_orders(type,2,session['warehouse'])
            print(orderz)
            return orderz

app.run(debug=True)