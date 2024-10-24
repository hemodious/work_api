from flask import Flask,request,jsonify
import sqlite3

app = Flask(__name__)

def connection():
    conn=None
    try:
        conn = sqlite3.connect('user.sqlite')

    except sqlite3.error as e:
        print(e)
    return conn

