from flask import Flask, redirect, url_for
from flask import render_template
app = Flask(__name__)
from flask import request,session,jsonify
from datetime import timedelta
import mysql.connector
from flask import blueprints
app.secret_key='123'
app.config['session parament']=True
app.config['parament_session_lifetime'] = timedelta(minutes=200)


@app.route('/')
@app.route('/hw1')
def Homepage():
    return render_template('hw1.html')

@app.route('/CreateContact')
def CreateContact():
    return render_template('CreateContact.html')

@app.route('/assignement3_1')
def assignement3_1():
    curr_user={'firstname':"Ron", 'lastname':"Hazan"}
    return render_template('assignement3_1.html', name='Ron Hazan',
                           curr_user=curr_user,
                           hobbies=['Football','Real Madrid','Hangout with friends','Listen to music','Vactions'])

@app.route('/assignement3_2',methods=['GET','POST'])
def assignement3_2fc():
    users_dict={'Omer':{'lastname2':"Azulay",'email':"omerazulay@Gmail.com"},
                'Maor':{'lastname2': "Minay", 'email': "Maorminay@Gmail.com"},
           'Cristiano':{'lastname2':"Ronaldo",'email':"CrisRon@Gmail.com"},
                'Luka':{'lastname2':"Modrich",'email':"lokamodrich@Gmail.com"},
               'Vini': {'lastname2': "jr", 'email': "vinijr@Gmail.com"}}
    users_reg_dic = {'Omer':'1234',
                   'Maor':'2234',
                   'Cristiano':'1223',
                   'Luka':'3343',
                   'Vini':'5432',
                     'Noam':'1234'}
    if request.method=='GET':
     if 'username' in request.args:
         username=request.args['username']
         lastname2=request.args['lastname']
         email=request.args['email']
         if username in users_dict:
                 return render_template('assignement3_2.html', username=username, lastname=lastname2, email=email)
         else:
               return render_template('assignement3_2.html', messeage='Please try again!', users_dict=users_dict)

    if request.method=='POST':
        print('hello')
        username1 = request.form['username1']
        password = request.form['password']
        if username1 in users_reg_dic:
            return render_template('assignement3_2.html', messeage2='UserName already taken,choose another one!')
        else:

            users_reg_dic[username1] = password
            print(users_reg_dic.keys())
            session['username1'] = username1
            print(password)
            return render_template('assignement3_2.html', username1=username1, messeage2='')





    return render_template('assignement3_2.html')


@app.route('/log_in', methods=['GET','POST'])
def log_infc():
    return render_template('log_in.html')


@app.route('/log_out')
def log_outfc():
    session.clear()
    return redirect(url_for('assignement3_2fc'))
@app.route('/About')
def About():
    return render_template('About.html')


from assignement_4.assignement4 import assignement_4
app.register_blueprint(assignement_4)

if __name__ == '__main__':
    app.run(debug=True)



