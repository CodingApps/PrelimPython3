from flask import Flask
from flask import render_template
import os
import json
import time
import urllib.request

app = Flask(__name__)

def get_weather():
    url = "http://api.openweathermap.org/data/2.5/forecast?id=5454711&units=imperial&appid=[API Key]"
    response = urllib.request.urlopen(url).read()
    return response

@app.route("/")
def index():
    data = json.loads(get_weather())
    print(data)
    page = "<html><head><title>My Weather</title></head><body>"
  #  page += "<h1>Weather for {}, {}</h1>".format(data.get('city').get('name'), data.get('city').get('country'))
  #  for day in data.get("list"):
  #      page += "<b>date:</b> {} <b>min:</b> {} <b>max:</b> {} <b>description:</b> {} <br/> ".format(time.strftime('%d %B', time.localtime(day.get('dt'))), (day.get("temp").get("min")), day.get("temp").get("max"), day.get("weather")[0].get("description"))
        
    page+= "</body></html>"
    return page


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
