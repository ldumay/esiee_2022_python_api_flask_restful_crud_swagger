# app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

from app import routes, model