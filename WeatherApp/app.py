from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_KEY = "fe18de3cdfd0e199cb4312206981ff48"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/', methods=['GET', 'POST'])
def weather_app():
    if request.method == 'POST':
        city = request.form['city']
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        return render_template('weather.html', weather=data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False, host = '0.0.0.0')