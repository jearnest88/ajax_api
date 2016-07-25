from flask import Flask, render_template, request, redirect, jsonify, flash
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'myownapi')
@app.route('/')
def index():
    quotes = mysql.fetch("SELECT * FROM quotes")
    return render_template('quotes/index.html', quotes=quotes)

@app.route('/quotes/index_json')
def index_json():
    print 'in index_json'
    query = "SELECT * FROM quotes"
    print "after query"
    quotes = mysql.fetch(query)
    print "after fetch"
    return jsonify(quotes)

@app.route('/quotes/index_html')
def index_html():
    query = "SELECT * FROM quotes"
    quotes = mysql.fetch(query)
    return render_template('partials/quotes.html', quotes=quotes)

@app.route('/quotes/create', methods=['POST'])
def create():
	query = "INSERT INTO quotes(author, quote) VALUES('{0}','{1}')".format(request.form['author'], request.form['quote'])
	mysql.run_mysql_query(query)
	rquery = "SELECT * FROM quotes"
	quotes = mysql.fetch(rquery)
	return render_template('partials/quotes.html', quotes=quotes)


app.run(debug=True)
