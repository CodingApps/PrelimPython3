from flask import Flask
from flask import render_template
import os
import json
import time
import urllib.request

app = Flask(__name__)

def get_weather():
    url = "http://api.openweathermap.org/data/2.5/forecast?id=5454711&units=imperial&appid=d1bb542ef3f0d208e77e3d35bd6f6e2a"
    response = urllib.request.urlopen(url).read()
    return response

@app.route("/")
@app.route("/<searchcity>")
def index():
    data = json.loads(get_weather())
    forecast_list = []
    for d in data.get("list"):
        day = time.strftime('%d %B', time.localtime(d.get('dt')))
        mini = d.get("main").get("temp_min")
        maxi = d.get("main").get("temp_max")
        print(day)
        print(mini)
        print(max)
        description = d.get("weather")[0].get("description")
        forecast_list.append((day,mini,maxi,description))
    return render_template("index.html", forecast_list=forecast_list)
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
