from flask import Flask, request, render_template, session, flash, jsonify, redirect
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "lol123"
mysql = MySQLConnector(app,"notesdb")

@app.route('/')
def index():
	query = "SELECT * FROM notes"
	notes = mysql.fetch(query)
	return render_template('index.html', notes=notes)

@app.route('/index_json')
def index_json():
	query = "SELECT * FROM notes"
	notes = mysql.fetch(query)
	return jsonify(notes)

@app.route('/index')
def index_html():
	query = "SELECT * FROM notes"
	notes = mysql.fetch(query)
	return render_template('partials/_note_partial.html', notes=notes)

@app.route('/posts/create',methods=['POST'])
def create():
	session['note'] = request.form['get_note']
	insQuery = "INSERT INTO notes (note, created_at, updated_at) VALUES ('{0}', NOW(), NOW())".format(session['note'])
	print "in first query"
	mysql.run_mysql_query(insQuery)
	query = "SELECT * FROM notes"
	print "in rquery"
	notes = mysql.fetch(query)
	print "redirect"
	return render_template('partials/_note_partial.html', notes=notes)

app.run(debug=True) # run the server
