import pyowm
owm = pyowm.OWM('<api_key>') # TODO: Replace <api_key> with your API key
boston = owm.weather_at_place('Boston, US')
weather = boston.get_weather()
print(weather.get_sunrise_time(timeformat='iso')) # Prints time in GMT timezone
print(weather.get_sunset_time(timeformat='iso')) # Prints time in GMT timezone