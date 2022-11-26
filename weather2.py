import requests

api_address='http://api.openweathermap.org/data/2.5/weather?appid=ff483293a2e02eeca90ec2bcfa8f2c28kq='
city = input('City Name :')
url = api_address + city
json_data = requests.get(url).json()
format_add = json_data['base']
print(format_add)