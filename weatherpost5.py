from flask import Flask
from flask import render_template
from flask import request
import os
import json
import time
import urllib.request

app = Flask(__name__)

def get_weather(city):
    url = "http://api.openweathermap.org/data/2.5/forecast?q={}&units=imperial&appid=d1bb542ef3f0d208e77e3d35bd6f6e2a".format(city)
    response = urllib.request.urlopen(url).read()
    return response

@app.route("/")
def index():
    searchcity = request.args.get("searchcity")
    if not searchcity:
        searchcity = "Philadelphia"
    data = json.loads(get_weather(searchcity))
    city = data['city']['name']
    country = data['city']['country']
    location=city
    forecast_list = []
    for d in data.get("list"):
        day = time.strftime('%d %B', time.localtime(d.get('dt')))
        mini = d.get("main").get("temp_min")
        maxi = d.get("main").get("temp_max")
        description = d.get("weather")[0].get("description")
        forecast_list.append((day,mini,maxi,description))
    return render_template("index.html", forecast_list=forecast_list, location=location)
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
