from flask import Flask, render_template
import melon_unity as mu

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/melon')
def melon():
    song_list = mu.melon()
    return render_template('/melon.html', song_list=song_list)

if __name__ == '__main__':
    app.run(debug=True)
