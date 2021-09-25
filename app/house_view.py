from app import app
from flask import render_template,jsonify
from flask import request
from flaskext.mysql import MySQL

#to search for a house
@app.route("/search/<page_id>")
def house_list(page_id):
    mysql = MySQL()
    mysql.init_app(app)
    mycursor = mysql.connect().cursor()
    page_id = int(page_id)
    num_rows = int(page_id*10-10)
    try:
        sql = """SELECT * FROM house"""
        mycursor.execute(sql)
        rv = mycursor.fetchall()
    finally:
        mycursor.close()
    return jsonify(rv)

#to display the house
@app.route("/house/<house_id>")
def house_details(house_id):
    mysql = MySQL()
    mysql.init_app(app)
    mycursor = mysql.connect().cursor()
    try:
        sql = "SELECT * FROM house WHERE id =%s"
        house_id=(house_id)
        mycursor.execute(sql,house_id)
        rv = mycursor.fetchall()
    finally:
        mycursor.close()
    return jsonify(rv)

#to display the edit house details form
@app.route("/house/<house_id>/edit/<user_name>")
def house_edit(house_id,user_name):
    mysql = MySQL()
    mysql.init_app(app)
    cur = mysql.connect().cursor()
    try:
        sql = "SELECT * FROM house WHERE id =%s"
        house_id=(house_id)
        mycursor.execute(sql,house_id)
        rv = mycursor.fetchall()
    finally:
        curs.close()
    return jsonify(rv)

#edit the house
@app.route("/house/edit")
def house_edit_details():
    mysql = MySQL()
    mysql.init_app(app)
    cur = mysql.connect().cursor()
    try:
        if request.form['house_name']!="":
            sql = """ UPDATE house SET house_name=%s WHERE house_id =%s"""
            house_details=(request.form['house_name'],request.form['house_id'])
            mycursor.execute(sql,house_id)
        if request.form['house_address']!="":
            sql = """ UPDATE house SET house_name=%s WHERE house_id =%s"""
            house_details=(request.form['house_name'],request.form['house_id'])
            mycursor.execute(sql,house_id)
        if request.form['house_type']:
            pass
        if request.form['house_state']:
            pass
        if request.form['house_city']:
            pass
        if request.form['house_address']:
            pass
        if request.form['house_pin_code']:
            pass
        rv = mycursor.fetchall()
    finally:
        curs.close()
    return jsonify(rv)
    
# rent the house
@app.route("/house/<house_id>/rent")
def rent_house(house_id):
    mysql = MySQL()
    mysql.init_app(app)
    cur = mysql.connect().cursor()
    try:
        sql = """INSERT INTO rented_house(house_id,start_dates,end_date,users_id) 
        VALUES(%s,%s,%s,%s)"""
        start_dates = request.form['start_date']
        end_date = request.form['end_date']
        users_id = request.form['users_id']
        house_data=(house_id,start_dates,end_date,users_id)
        mycursor.execute(sql,house_data)
        rv = mycursor.fetchall()
    finally:
        curs.close()
    return jsonify(rv)