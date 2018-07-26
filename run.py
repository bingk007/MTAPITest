#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  @author: WuBingBing


from flask import Flask, render_template, request, send_file
import os


app = Flask(__name__)
imagepath = os.path.join(os.getcwd(),"static/images")
# dirpath = os.path.join(app.root_path, 'upload')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test', methods=['GET'])
def test():
    os.system("python StartTest.py")
    return render_template('index.html')


@app.route('/report.html', methods=['GET'])
def report():
    # return render_template('TestReport.html')
    # return send_from_directory(dirpath, 'TestReport.html', as_attachment=True)
    return send_file('./upload/TestReport.html')


@app.route('/new_add', methods=['GET'])
def login_index():
    return render_template('new_add.html')


@app.route('/add', methods=['POST'])
def add():
    username = request.form.get('username','default value')
    password = request.form.get('password','default value')
    print(username)
    print(password)
    return render_template('new_add.html')


@app.route('/list', methods=['GET'])
def get_list():
    return render_template('list.html')


if __name__ == '__main__':
    # app.run(host='192.168.0.189', port=5000, debug=True)
    # from werkzeug.contrib.fixers import ProxyFix
    # app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(debug=True)
