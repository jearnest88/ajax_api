from flask import Flask, render_template, request, redirect, jsonify, flash
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)

mysql = MySQLConnector(app, 'postsdb')
@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)
