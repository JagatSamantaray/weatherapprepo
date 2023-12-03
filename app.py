from flask import Flask, request, render_template 
import requests


app = Flask(__name__)

app.route('/')
def home_page():
    return render_template('index.html')

app.route('/weatherapp', methods = ['GET', 'POST'])
def get_weather_data():
    url = "http:api.openweathermap.org/weather"
    param = {
        'q': requests.form.get('city'),
        'appid':request.form.get('appid'),
        "units": request.form.get('units')
    }
    data = requests.get(url, params=param)
    return sf"data: {data}, city: {data.json()['name']} "
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
    