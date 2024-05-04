class City:
	"""Stores weather information for a city"""
	def __init__(self, name, temp_in_K, desc, feel_K, min_temp_K, max_temp_K, wind):
		self.name = name
		self.temp = temp_in_K
		self.desc = desc
		self.feel = feel_K
		self.min = min_temp_K
		self.max = max_temp_K
		self.wind = wind
		self.tempC = "None"
		self.tempF = "None"
		self.feelC = "None"
		self.feelF = "None"
		self.maxC = "None"
		self.maxF = "None"
		self.minC = "None"
		self.minF = "None"

	def __str__(self):
		return f"City - {self.name}: \n\t Temperature (C): {self.tempC} \n\t Temperature (F): {self.tempF} \n\t Feels like (C): {self.feelC} \n\t Feels like (F): {self.feelF} \n\t Minimum Temperature (C): {self.minC} \n\t Minimum Temperature (F): {self.minF} \n\t Maximum Temperature (C): {self.maxC} \n\t Maximum Temperature (F): {self.maxF} \n\t Weather: {self.desc} \n\t Wind Speed (MPH): {self.wind}"
	
	def get_name(self):
		return self.name
	
	def get_desc(self):
		return self.desc
	
	def get_temp_in_K(self):
		return self.temp

	def get_temp_in_C(self):
		cTemp = self.temp - 273.15
		self.tempC = round(cTemp, 2)
		return self.tempC

	def get_temp_in_F(self):
		fTemp = ((self.temp - 273.15) * 1.8) + 32
		self.tempF = round(fTemp, 2)
		return self.tempF 
	
	def get_feel_in_C(self):
		cFeel = self.feel - 273.15
		self.feelC = round(cFeel, 2)
		return self.feelC

	def get_feel_in_F(self):
		fFeel = ((self.feel - 273.15) * 1.8) + 32
		self.feelF = round(fFeel, 2)
		return self.feelF

	def get_min_in_C(self):
		cMin = self.min - 273.15
		self.minC = round(cMin, 2)
		return self.minC

	def get_min_in_F(self):
		fMin = ((self.min - 273.15) * 1.8) + 32
		self.minF = round(fMin, 2)
		return self.minF 
	
	def get_max_in_C(self):
		cMax = self.max - 273.15
		self.maxC = round(cMax, 2)
		return self.maxC

	def get_max_in_F(self):
		fMax = ((self.max - 273.15) * 1.8) + 32
		self.maxF = round(fMax, 2)
		return self.maxF
	
	def get_wind_speed(self):
		speedWind = self.wind * 2.237
		self.wind = round(speedWind, 2)
		return self.wind
	
	