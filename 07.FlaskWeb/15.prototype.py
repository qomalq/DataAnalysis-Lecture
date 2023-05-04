from flask import Flask, render_template, request
import os
import crawl_util as cu
from weather_util  import get_weather
import gene_unity as gu
import 식신_unity as su
app = Flask(__name__)

@app.route('/')
def home():
    menu = {'ho':1, 'us':0, 'cr':0, 'sc':0}
    return render_template('prototype/home.html', menu=menu, weather = get_weather(app))

@app.route('/user')
def user():
    menu = {'ho':0, 'us':1, 'cr':0, 'sc':0}
    return render_template('prototype/소개글.html', menu=menu, weather = get_weather(app))

@app.route('/schedule')
def schedule():
    menu = {'ho':0, 'us':0, 'cr':0, 'sc':1}
    return render_template('prototype/schedule.html', menu=menu, weather = get_weather(app))

@app.route('/crw')
def crw():
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    return render_template('prototype/schedule.html', menu=menu, weather = get_weather(app))

@app.route('/interpark')
def interpark():
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    book_list = cu.interpark()
    return render_template('prototype/인터파크.html',book_list=book_list,menu=menu, weather = get_weather(app))

@app.route('/gene')
def gene():
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    gene_list = gu.gene()
    return render_template('prototype/지니차트.html',gene_list=gene_list,menu=menu, weather = get_weather(app))

@app.route('/eating')
def eating():
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    eat_list = su.eat()
    return render_template('prototype/식신.html',eat_list=eat_list,menu=menu, weather = get_weather(app))




if __name__ == '__main__':
    app.run(debug=True)
