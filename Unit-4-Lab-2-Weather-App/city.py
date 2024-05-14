class City:
	"""Stores weather information for a city"""
	def __init__(self, name, temp_in_K, desc, feel_K, min_temp_K, max_temp_K, wind):
		"""Initializes the city class"""
		self.name = name
		self.temp = temp_in_K
		self.desc = desc
		self.feel = feel_K
		self.min = min_temp_K
		self.max = max_temp_K
		self.windy = wind
		self.tempC = "None"
		self.tempF = "None"
		self.feelC = "None"
		self.feelF = "None"
		self.maxC = "None"
		self.maxF = "None"
		self.minC = "None"
		self.minF = "None"

	def __str__(self):
		"""String method to display the city"""
		return f"City - {self.name}: \n\t Temperature (C): {self.tempC} \n\t Temperature (F): {self.tempF} \n\t Feels like (C): {self.feelC} \n\t Feels like (F): {self.feelF} \n\t Minimum Temperature (C): {self.minC} \n\t Minimum Temperature (F): {self.minF} \n\t Maximum Temperature (C): {self.maxC} \n\t Maximum Temperature (F): {self.maxF} \n\t Weather: {self.desc} \n\t Wind Speed (MPH): {self.wind}"
	
	def get_name(self):
		"""Gets the name of the city"""
		return self.name
	
	def get_desc(self):
		"""Gets the description of the city"""
		return self.desc
	
	def get_temp_in_K(self):
		"""Gets the temperature in Kelvin of the city"""
		return self.temp

	def get_temp_in_C(self):
		"""Gets the temperature in Celsius of the city"""
		cTemp = self.temp - 273.15
		self.tempC = round(cTemp, 2)
		return self.tempC

	def get_temp_in_F(self):
		"""Gets the temperature in Fahrenhiet of the city"""
		fTemp = ((self.temp - 273.15) * 1.8) + 32
		self.tempF = round(fTemp, 2)
		return self.tempF 
	
	def get_feel_in_C(self):
		"""Gets the feel in Celsius of the city"""
		cFeel = self.feel - 273.15
		self.feelC = round(cFeel, 2)
		return self.feelC

	def get_feel_in_F(self):
		"""Gets the feel in Fahrenhiet of the city"""
		fFeel = ((self.feel - 273.15) * 1.8) + 32
		self.feelF = round(fFeel, 2)
		return self.feelF

	def get_min_in_C(self):
		"""Gets the minimum temperature in Celsius of the city"""
		cMin = self.min - 273.15
		self.minC = round(cMin, 2)
		return self.minC

	def get_min_in_F(self):
		"""Gets the minimum temperature in Fahrenhiet of the city"""
		fMin = ((self.min - 273.15) * 1.8) + 32
		self.minF = round(fMin, 2)
		return self.minF 
	
	def get_max_in_C(self):
		"""Gets the maximum temperature in Celsius of the city"""
		cMax = self.max - 273.15
		self.maxC = round(cMax, 2)
		return self.maxC

	def get_max_in_F(self):
		"""Gets the maximum temperature in Fahrenhiet of the city"""
		fMax = ((self.max - 273.15) * 1.8) + 32
		self.maxF = round(fMax, 2)
		return self.maxF
	
	def get_wind_speed(self):
		"""Gets the wind speed of the city"""
		speedWind = self.windy * 2.237
		self.wind = round(speedWind, 2)
		return self.wind

	
	