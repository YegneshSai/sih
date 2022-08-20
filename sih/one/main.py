from flask import Flask,render_template,request,redirect,url_for
from forms import details
import database as db


from playsound import playsound
#creating an app instance for the website
app=Flask(__name__)

#adding secret key
app.config['SECRET_KEY']='sih'

global user_name
global location
@app.route("/",methods=['GET',"POST"])
def open():
    data = details()
    if data.validate_on_submit():
        print(request.form)
        if 'user' in request.form:
            return redirect(url_for('user_login'))
        elif 'mechanic' in request.form:
            return redirect(url_for('mechanic_login'))
    return render_template('open.html', data=data)

@app.route("/user_login",methods=['GET',"POST"])
def user_login():
    data = details()
    if data.validate_on_submit():
        print(request.form)
        if 'register' in request.form:
            return redirect(url_for('user_register'))
        if 'login' in request.form:
            if db.check_user(request.form['username'],request.form['password']):
                global user_name
                user_name = request.form['username']
                return redirect(url_for('home'))
            else:
                print("no user found")
    return render_template('login.html', data=data)


@app.route("/mechanic_login",methods=['GET',"POST"])
def mechanic_login():
    data = details()
    if data.validate_on_submit():
        print(request.form)
        if 'register' in request.form:
            return redirect(url_for('mechanic_register'))
        if 'login' in request.form:
            if db.check_mechanic(request.form['username'],request.form['password']):
                global user_name
                user_name = request.form['username']
                return redirect(url_for('home'))
            else:
                print("no user found")
    return render_template('mlogin.html', data=data)

@app.route("/user_register",methods=['GET',"POST"])
def user_register():
    data = details()
    if data.validate_on_submit():
        print(request.form)
        if 'register' in request.form:
            v=("hi",request.form['username'],request.form['car_model'],request.form['name'],request.form['password1'],"vijayawada")
            db.add_user(v)

    return render_template('register.html', data=data)


@app.route("/mechanic_register",methods=['GET',"POST"])
def mechanic_register():
    data = details()
    if data.validate_on_submit():
        print(request.form)
        if 'register' in request.form:
            v=("hi",request.form['username'],request.form['name'],request.form['password1'],request.form['expertise'],request.form['location'],request.form['center'])
            db.add_mechanic(v)

    return render_template('mregister.html', data=data)


@app.route("/home",methods=["GET","POST"])
def home():
    data=details()
    if data.validate_on_submit():
        print(request.form)
        print(request.form['audio'])
        print(type(request.form['audio']))
    return render_template('home.html',data=data)


@app.route("/report",methods=['GET',"POST"])
def report():
    data = details()
    if data.validate_on_submit():
        print(request.form)
        if 'find' in request.form:
            return redirect(url_for('mechanic'))
    return render_template('report.html', data=data)


@app.route("/mechanic",methods=['GET',"POST"])
def mechanic():
    print(user_name)
    data = details()
    list=db.get_mechanic(user_name,"vijayawada")
    print(list)
    if data.validate_on_submit():

        print(request.form)
    return render_template('mechanic.html',data=data,list=list)

@app.route("/track",methods=['GET',"POST"])
def track():
    data = details()
    if data.validate_on_submit():
        print(request.form)
    return render_template('track.html',data=data)


#make the app run continusly with debugging
if __name__=='__main__':
    app.run(debug=True)