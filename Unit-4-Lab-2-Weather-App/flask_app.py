"""
Name:
Title: Weather App
Description: Make a weather web app using Flask and Openweathermap API
"""
# imports for Flask, API calls, City class
from datetime import datetime
from flask import Flask, request, render_template, redirect, url_for  
import requests
from city import City

# list of City objects
cities = []
citynames = []
API_KEY = "dcb9deb505067260a9d290e0f4030b13"
LowTemp = [1000, "Name"]
HighTemp = [-1000, "Name"]

def get_data(city):
	"""
	Returns API data from a given city string.

	Parameters:
	city (str): The name of the city to fetch data for.

	Returns:
	list: A list of data fetched from the API, with the city name as the first element.
	"""

	# list of data fetched from API
	data = [city.title()]
	# insert code to get API data (Step 3)

	# initialize your API key here
	API_KEY = 'dcb9deb505067260a9d290e0f4030b13'
	lat = 41.748489
	lon = 88.186111
	layer = 'precipitation_new'
	z = 8
	y = 200
	x = 200

	# Future

	urlExp = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}"
	responseExp = requests.get(urlExp)
	responseExp = responseExp.json()
	print(responseExp)

	# Weather Map
	#urlExp2 = f"https://tile.openweathermap.org/map/{layer}/{z}/{x}/{y}.png?appid={API_KEY}"
	#responseExp2 = requests.get(urlExp2)
	#responseExp2 = responseExp2.json()
	#print(responseExp2)

	# Pollution
	print(""".
	   .
	   .
	   .
	   .
	   .""")
	urlExp3 = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
	responseExp3 = requests.get(urlExp3)
	responseExp3 = responseExp3.json()
	print(responseExp3)
	print(""".
	   .
	   .
	   .
	   .
	   .""")

	# request data from API and retrieve json data response
	url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}'
	response = requests.get(url)

	# convert json response into python dictionary
	response = response.json()
	print(response)

	dict = response.get('main')
	current_temp = dict.get('temp')
	data.append(current_temp)

	# get current description from dictionary and add it to the data list
	current_desc = response.get('weather')[0].get('description')
	data.append(current_desc.title())

	temp_feel = response.get("main").get("feels_like")
	data.append(temp_feel)

	min_temp = response.get("main").get("temp_min")
	data.append(min_temp)

	max_temp = response.get("main").get("temp_max")
	data.append(max_temp)

	windSpeed = response.get("wind").get("speed")
	data.append(windSpeed)

	return data

def get_pollution():
	API_KEY = 'dcb9deb505067260a9d290e0f4030b13'
	lat = 41.748489
	lon = 88.186111
	dataPol = []
	indexCalc = 0
	coIndex = 0
	no2Index = 0
	o3Index = 0
	so2Index = 0
	pm2_5Index = 0
	pm10Index = 0

	urlExp3 = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
	responseExp3 = requests.get(urlExp3)
	responseExp3 = responseExp3.json()
	print(responseExp3)

	coinit = responseExp3.get("list")
	co = coinit[0].get("components").get("co")
	no2init = responseExp3.get("list")
	no2 = no2init[0].get("components").get("no2")
	o3init = responseExp3.get("list")
	o3 = o3init[0].get("components").get("o3")
	so2init = responseExp3.get("list")
	so2 = so2init[0].get("components").get("so2")
	pm2_5init = responseExp3.get("list")
	pm2_5 = pm2_5init[0].get("components").get("pm2_5")
	pm10init = responseExp3.get("list")
	pm10 = pm10init[0].get("components").get("pm10")

	if co <= 4400:
		indexCalc += 1
		coIndex = 1
	elif co >= 4400 and co <= 9400:
		indexCalc += 2
		coIndex = 2
	elif co >= 9400 and co <= 12400:
		indexCalc += 3
		coIndex = 3
	elif co >= 12400 and co <= 15400:
		indexCalc += 4
		coIndex = 4
	elif co > 15400:
		indexCalc += 5
		coIndex = 5

	if no2 <= 40:
		indexCalc += 1
		no2Index = 1
	elif no2 >= 40 and no2 <= 70:
		indexCalc += 2
		no2Index = 2
	elif no2 >= 70 and no2 <= 150:
		indexCalc += 3
		no2Index = 3
	elif no2 >= 150 and no2 <= 200:
		indexCalc += 4
		no2Index = 4
	elif no2 > 200:
		indexCalc += 5
		no2Index = 5

	if o3 <= 40:
		indexCalc += 1
		o3Index = 1
	elif o3 >= 40 and o3 <= 70:
		indexCalc += 2
		o3Index = 2
	elif o3 >= 70 and o3 <= 150:
		indexCalc += 3
		o3Index = 3
	elif o3 >= 150 and o3 <= 200:
		indexCalc += 4
		o3Index = 4
	elif o3 > 200:
		indexCalc += 5
		o3Index = 5

	if so2 <= 20:
		indexCalc += 1
		so2Index = 1
	elif so2 >= 20 and so2 <= 80:
		indexCalc += 2
		so2Index = 2
	elif so2 >= 80 and so2 <= 250:
		indexCalc += 3
		so2Index = 3
	elif so2 >= 250 and so2 <= 350:
		indexCalc += 4
		so2Index = 4
	elif so2 > 350:
		indexCalc += 5
		so2Index = 5

	if pm2_5 <= 10:
		indexCalc += 1
		pm2_5Index = 1
	elif pm2_5 >= 10 and pm2_5 <= 25:
		indexCalc += 2
		pm2_5Index = 2
	elif pm2_5 >= 25 and pm2_5 <= 50:
		indexCalc += 3
		pm2_5Index = 3
	elif pm2_5 >= 50 and pm2_5 <= 75:
		indexCalc += 4
		pm2_5Index = 4
	elif pm2_5 > 75:
		indexCalc += 5
		pm2_5Index = 5

	if pm10 <= 20:
		indexCalc += 1
		pm10Index = 1
	elif pm10 >= 20 and pm10 <= 50:
		indexCalc += 2
		pm10Index = 2
	elif pm10 >= 50 and pm10 <= 100:
		indexCalc += 3
		pm10Index = 3
	elif pm10 >= 100 and pm10 <= 200:
		indexCalc += 4
		pm10Index = 4
	elif pm10 > 200:
		indexCalc += 5
		pm10Index = 5

	indexCalc = round(indexCalc / 6, 2)
	percentage = round(indexCalc / 5, 2)

	return [indexCalc, coIndex, no2Index, o3Index, so2Index, pm2_5Index, pm10Index, percentage]



app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
	return render_template('index.html') 

@app.route('/', methods = ['POST'])
def index2():
	"""Page one of the webapp"""
	# get the city name from the form's search box
	city_str = request.form["search_box"]
	dataOfCity = get_data(city_str)
	print(dataOfCity)

	cityWeather = City(dataOfCity[0], dataOfCity[1], dataOfCity[2], dataOfCity[3], dataOfCity[4], dataOfCity[5], dataOfCity[6])
	cityWeather.get_feel_in_C()
	cityWeather.get_feel_in_F()
	cityWeather.get_max_in_C()
	cityWeather.get_max_in_F()
	cityWeather.get_min_in_C()
	cityWeather.get_min_in_F()
	cityWeather.get_temp_in_C()
	cityWeather.get_temp_in_F()
	cityWeather.get_wind_speed()

	if cityWeather.name not in citynames:
		cities.append(cityWeather)

	citynames.append(cityWeather.name)
	
	print(cities)
	print(citynames)

	if LowTemp[0] > cityWeather.tempC:
		LowTemp[0] = cityWeather.tempC
		LowTemp[1] = cityWeather.name

	if HighTemp[0] < cityWeather.tempC:
		HighTemp[0] = cityWeather.tempC
		HighTemp[1] = cityWeather.name
	
	print(LowTemp)
	print(HighTemp)

	return render_template('index.html', city = city_str, tempC = cityWeather.tempC, tempF = cityWeather.tempF, minC = cityWeather.minC, minF = cityWeather.minF, maxC = cityWeather.maxC, maxF = cityWeather.maxF, feelC = cityWeather.feelC, feelF = cityWeather.feelF, windSpeed = cityWeather.wind, desc = cityWeather.desc)

@app.route('/cities.html', methods = ['GET'])
def page2():
	"""Page to off the webapp"""
	# insert page 2 code here
	return render_template("cities.html", listofcities = cities, lowtemp = LowTemp[1], hightemp = HighTemp[1])

@app.route('/pollution.html', methods = ['GET'])
def page3():
	"""Page to off the webapp"""
	cityPol = get_pollution()

	return render_template("pollution.html", polIndex = cityPol[0], coInd = cityPol[1], no2Ind = cityPol[2], o3Ind = cityPol[3], so2Ind = cityPol[4], pm2_5Ind = cityPol[5], pm10Ind = cityPol[6], percent = cityPol[7])

app.run(host='0.0.0.0', port=8080) # any code below 'app.run' line won't run