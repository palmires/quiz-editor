#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, time
import json

import collections
import operator
import os,subprocess
from subprocess import Popen, PIPE
from operator import itemgetter
from flask import Flask, render_template, request
from flask import send_from_directory

import threading
from threading import Thread
import subprocess
from Queue import Queue
from subprocess import Popen, PIPE

app = Flask(__name__)

@app.route("/")
def general():
    return render_template('main.html')

@app.route("/add_question",methods = ['POST', 'GET'])
def add_question():
    return render_template('add_question.html')

@app.route("/complete_added",methods = ['POST', 'GET'])
def complete_added():
    if request.method == 'POST':
        ower = request.form
        ower=dict(ower)
        q_name = ower['question']
        print(q_name)
        position = ',{"question":"%s","answer":"-"}]}' %(q_name)
        with open ('/home/deliany/test/test.json') as json_data:
            data = json.load(json_data)
            s = json.dumps(data)
            print(data)
            print(s)
            d = s[:-2]+position
            print(d)
            print json.loads(d)
            text = json.loads(d)
            with open ('/home/deliany/test/test.json', 'w') as file:
                json.dump(text, file)
        #print(g_name)
        #ower.pop("name")
        return render_template('main.html')
    else:
        return render_template('main.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)
