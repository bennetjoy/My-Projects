import requests, json 
  
api_key = "107902956b603bbda527674bf22ede54"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city = input("Enter city name : ") 
  
complete_url = base_url + "appid=" + api_key + "&q=" + city 

response = requests.get(complete_url) 

x = response.json() 
  
# "404", means city is found otherwise,
if x["cod"] != "404": 
  
    y = x["main"] 
   
    current_temperature = y["temp"] 

    current_pressure = y["pressure"] 
   
    current_humidiy = y["humidity"] 
 
    z = x["weather"] 

    weather_description = z[0]["description"] 

    tempinf =int(current_temperature-278) #convert temp in k to c and to avoid decimal values

    print("Temperature in " + city + ' is ' + str(tempinf)+ " Degree Celcius ")
    print("Atmospheric pressure is " + str(current_pressure) + " hecto Pascal ")
    print("Humidity is " + str(current_humidiy) + " % ")
    print("It will be " + str(weather_description) + " today ") 
  
else: 
    print(" City Not Found ") 