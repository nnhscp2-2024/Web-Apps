if __name__ == "__main__":
	import flask_app
	from city import City

	dataCity = list(flask_app.get_data("Naperville"))
	print(dataCity)

	for i in range(0,7):
		print(dataCity[i])

	cityWeather = City(dataCity[0], dataCity[1], dataCity[2], dataCity[3], dataCity[4], dataCity[5], dataCity[6])
	cityWeather.get_feel_in_C()
	cityWeather.get_feel_in_F()
	cityWeather.get_max_in_C()
	cityWeather.get_max_in_F()
	cityWeather.get_min_in_C()
	cityWeather.get_min_in_F()
	cityWeather.get_temp_in_C()
	cityWeather.get_temp_in_F()
	cityWeather.get_wind_speed()

	print(cityWeather)