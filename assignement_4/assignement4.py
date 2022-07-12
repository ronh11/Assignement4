from flask import Blueprint, render_template, request, redirect
import mysql.connector
from flask import jsonify
import requests
assignement_4 = Blueprint('assignement4', __name__,
                          static_folder='static',
                          template_folder='templates')


@assignement_4.route('/assignement4')
def assi4_func():
    query = 'select * from users'
    users_list = intreact_db(query, query_type='fetch')
    return render_template('assignement4.html', users=users_list)


@assignement_4.route('/insert_user', methods=['POST'])
def insert_user():
    name = request.form['name']
    lastname = request.form['lastname']
    email = request.form['email']
    query = 'select * from users'
    users_list = intreact_db(query, query_type='fetch')
    for user in users_list:
        if name == user.name:
           return redirect('/assignement4')
    else:
     print(name, lastname, email)
     query = "INSERT INTO users(name,lastname,email) VALUES ('%s','%s','%s')" % (name, lastname, email)
     intreact_db(query=query, query_type='commit')
     query2 = 'select * from users'
     users_new_list = intreact_db(query2, query_type='fetch')
     return render_template('/assignement4.html', messeage34='User Inserted Successfully!', users=users_new_list)

@assignement_4.route('/delete_user', methods=['POST'])
def delete_user_func():
    user_id = request.form['user_id']
    query = "DELETE FROM users WHERE name='%s';" % user_id
    intreact_db(query, query_type='commit')
    query2='select * from users'
    users_new_list=intreact_db(query2, query_type='fetch')
    return render_template('/assignement4.html',messeage35='User Deleted Successfully!',users=users_new_list)


@assignement_4.route('/update_user', methods=['POST'])
def update_user():
    new_messeage=""
    name = request.form['user_name_update']
    lastname = request.form['user_lastname_update']
    email = request.form['user_email_update']
    if lastname != "" and email != "":
        query = "UPDATE users SET lastname='%s',email='%s'WHERE name='%s'" % (lastname, email, name)
        new_messeage = "last name and email is updated!"
    elif (lastname != "" and email == ""):
        query = "UPDATE users SET lastname='%s' WHERE name='%s'" % (lastname, name)
        new_messeage = "last name  is updated!"
    elif (lastname == "" and email != ""):
        query = "UPDATE users SET email='%s'WHERE name='%s'" % (email, name)
        new_messeage = "email is updated!"
    else:
        query2 = 'select * from users'
        users_new_list = intreact_db(query2, query_type='fetch')
        return render_template('/assignement4.html', messeage36='Nothing has Inserted', users=users_new_list)

    intreact_db(query=query, query_type='commit')
    query2 = 'select * from users'
    users_new_list = intreact_db(query2, query_type='fetch')
    return render_template('/assignement4.html', messeage36='User Updated Successfully!', users=users_new_list)

@assignement_4.route('/assignement4/users')
def users_listjs():
    query = 'select * from users'
    query_list = intreact_db(query, query_type='fetch')
    return jsonify(query_list)
@assignement_4.route('/assignement4/outer_source')
def outer_source_funct():
    return render_template('outer_source.html')

@assignement_4.route('/assignement4/restapi_users',defaults={'user_name':1})
@assignement_4.route('/assignement4/restapi_users/<string:user_name>')
def restapi_func(user_name):
    query = "select * from users WHERE name='%s';" % user_name
    print(query)
    query_result = intreact_db(query=query, query_type='fetch')
    print(query_result)
    response = {}
    if len(query_result) != 0:
        messeage=''
        response = {'user_name': user_name}
        UserDetails=query_result
    else:
        messeage={'User ID is not exist'}
        response = {'user_name': "Omer"}
        UserDetails=query_result


    return response
#backend
@assignement_4.route('/assignement4/outer_source/fetch_from_backend')
def outer_source_fetch_data():
    user_id = request.args['user_id_back']
    resulst = requests.get(f"https://reqres.in/api/users/{user_id}")
    return render_template('outer_source.html', request_data=resulst.json()['data'])






def intreact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='assi4schema')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    if query_type == 'commit':
        connection.commit()
        return_value = True;
    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result
    connection.close()
    cursor.close()
    return return_value
