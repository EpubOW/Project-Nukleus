from datetime import datetime
from flask import request, json, jsonify, make_response, Response, render_template,redirect
from config import *
from model.data.Box import *

@app.route('/', methods=['GET'])
def main():
    return render_template('main.html', boxes=Box.getAll())

@app.route('/another', methods=['GET'])
def another():
    return render_template('main1.html')