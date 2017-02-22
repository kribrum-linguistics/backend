#!/usr/bin/python3
# -*- coding: utf-8 -*-
try:
    from os import getuid
except ImportError:
    def getuid():
        return 4000

from flask import Flask, render_template, request, redirect
import json, datetime

app = Flask(__name__, template_folder='templates')

@app.route("/", methods=['GET','POST'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=getuid() + 1000)