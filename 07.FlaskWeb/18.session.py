from flask import Flask, render_template, request, redirect, session, flash
from weather_util import get_weather, get_weather_by_coord
import crawl_util as cu
import map_util as mu
import image_util as iu
import os, random, json
import 식신_unity as su
import gene_unity as gu
from user import user_bp

app = Flask(__name__)
app.secret_key = '123456789'
app.config['SESSION_COOKIE_PATH'] = '/'

app.register_blueprint(user_bp, url_prefix='/user')


# # flask 2.3 에서는 이 코드만 사용 가능
# with app.app_context():
#     global quote, quotes            # quote, quotes 변수를 전역 변수로 만들어 줌
#     global addr
#     filename = os.path.join(app.static_folder, 'data/todayQuote.txt')
#     with open(filename, encoding='utf-8') as f:
#         quotes = f.readlines()
#     quote = random.sample(quotes, 1)[0]
#     session['quote'] = quote
#     addr = '수원시 장안구'

@app.before_first_request
def before_first_request():
    global quote, quotes            # quote, quotes 변수를 전역 변수로 만들어 줌
    global addr
    filename = os.path.join(app.static_folder, 'data/todayQuote.txt')
    with open(filename, encoding='utf-8') as f:
        quotes = f.readlines()
    quote = random.sample(quotes, 1)[0]
    session['quote'] = quote
    addr = '수원시 장안구'
    session['addr'] = addr

# for AJAX  #############################
@app.route('/change_quote')
def change_quote():
    global quote
    quote = random.sample(quotes, 1)[0]
    session['quote'] = quote
    return quote

@app.route('/change_addr')
def change_addr():
    global addr
    addr = request.args.get('addr')
    session['addr'] = addr
    return addr

@ app.route('/weather')
def weather():
    addr = request.values['addr']
    lat, lng = mu.get_coord(addr + '청')
    html = get_weather_by_coord(app, lat, lng)
    return html

@app.route('/change_profile', methods=['POST'])
def change_profile():
    file_image = request.files['image']
    filename = os.path.join(app.static_folder, f'upload/{file_image.filename}')
    file_image.save(filename)
    mtime = iu.change_profile(app, filename)
    return str(mtime)
#########################################

@app.route('/user')
def user():
    menu = {'ho':0, 'us':1, 'cr':0, 'sc':0}
    return redirect('/schedule')

@app.route('/')
def home():
    menu = {'ho':1, 'us':0, 'cr':0, 'sc':0}
    return render_template('prototype/home.html', menu=menu, weather = get_weather(app))

@app.route('/schedule')
def schedule():
    try:
        _ = session['uid']
    except:
        flash('스케쥴을 확인하려면 로그인 하세요')
        return redirect('/user/login')
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

@app.route('/genie_jquery')
def genie_jquery():
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    song_list = gu.gene()
    return render_template('prototype/genie_jquery.html', song_list=song_list,menu=menu, weather = get_weather(app))

@app.route('/eating')
def eating():
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    eat_list = su.eat()
    return render_template('prototype/식신.html',eat_list=eat_list,menu=menu, weather = get_weather(app))




if __name__ == '__main__':
    app.run(debug=True)
