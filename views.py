#！/usr/bin/env python3
#-*-coding -utf8 -*-
'router register'
from flask import Flask,render_template,session,request
import os
#变量初始化
app=Flask(__name__)
app.secret_key=os.urandom(24)

@app.route('/')
def index():
	return render_template('index.html')
@app.route('/echarts')
def echarts():
	return render_template('图表绘制.html')
@app.route('/floatbox')
def floatbox():
	return render_template('浮动登录框.html')

if __name__=='__main__':
	app.debug=True
	app.run(host='0.0.0.0',port=10000,threaded=True)
