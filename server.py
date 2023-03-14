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
        session['functions'] = db.lazy_get_functionality(session['login'])
        return render_template("app.html")
    else:
        return redirect('/home')

@app.route('/login',methods=['POST']) #r
def login(): 
    if request.method == "POST":
        user_login = request.form["login"]
        password = request.form["password"]
        if re.match(r"[A-Za-z0-9]{3,}", user_login) and re.fullmatch(r"[A-Za-z0-9]{7,}", password):
            data = db.login(user_login,password)
            if data != None:
                session['functions'],session['warehouse'],session['login'] = db.lazy_get_functionality(user_login),data[1],user_login
            return redirect('/home')
@app.route('/logout',methods=['POST']) #r
def logout():
    if request.method == "POST":
        if 'warehouse' in session and 'login' in session:
            del session['warehouse']
            del session['login']
            del session['functions']
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
            session['login'],session['warehouse'],session["functions"] = login,data[2], 0
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

@app.route('/get_jsx_function/<func_id>')
def get_jsx_function(func_id):
  with open(f'C:\\Users\\ander\\OneDrive\\Документы\\GitHub\\tapkasklad.github.io\\plugins\\function{func_id}.html', encoding='utf-8') as f:
    html_template = f.read()
  return html_template


@app.route('/api/warehouse/edit_tags/', methods=['POST'])
def get_edit_tags():
    if 'warehouse' in session and 'login' in session:
        tags = request.json['tags']
        tags = [tag.replace('\n','',1).replace('×','',1)for tag in tags]
        for i in range(len(tags)):
            while tags[i].count(' ') > 0:
                tags[i] = tags[i].replace(' ','',1)
        session['functions'] = db.edit_functionality(tags,session['login'])

        return jsonify(success=True), 200
    else:
        return jsonify(success=False), 401
@app.route('/api/warehouse/get_users/',methods=['GET'])
def get_warehouse_users():
    if 'warehouse' in session and 'login' in session:
        warehouse_id = session['warehouse']
        users = db.get_warehouse_acounts(warehouse_id)
        if users:
            results = []
            for user in users:
                results.append({
                    'login': user[0],
                    'password' : user[1],
                    'functionality': user[2]
                })
            return jsonify(results)
        else:
            return jsonify([])

app.run(debug=True)