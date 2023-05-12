from flask import Flask, render_template
import youtube_util as yu

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/youtube_ranking')
def youtube():
    rank_list = yu.youtube()
    return render_template('/youtube.html',rank_list=rank_list)

if __name__ == '__main__':
    app.run(debug=True)
