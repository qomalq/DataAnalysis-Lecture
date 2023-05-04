import requests, os

def get_weather(app):
    file = os.path.join(app.static_folder, 'key/openweather.txt')
    with open('static/key/openweather.txt') as f:
        weather_key = f.read()
        lat, lon = 37.295, 127.045
        lat, lon = 37.295, 127.045
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_key}&units=metric&lang=kr'
        result =requests.get(url).json()
        desc = result['weather'][0]['description']
        icon_code = result['weather'][0]['icon']
        icon_url =f'http://api.openweathermap.org/img/w/{icon_code}'
        temp_ = result['main']['temp']
        temp =round(float(temp_)+0.01, 1)
        html = f'''<img src="{icon_url}" height="32"><strong>{desc}</strong>
             온도: <strong>{temp}</strong>&#8451'''
        return html