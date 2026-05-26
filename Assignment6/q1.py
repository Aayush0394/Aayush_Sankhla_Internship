import requests
key="APIKEYHIDDENFORSECURITY"
Geourl="http://api.openweathermap.org/geo/1.0/direct?"
weatherUrl="https://api.openweathermap.org/data/2.5/weather?"
def getCurrentWeather(key,city):
    try:
        finalurl=f"{Geourl}q={city},IN&limit=5&appid={key}"
        res=requests.get(finalurl)
        res.raise_for_status()
        data=res.json()
        lat=data[0]['lat']
        lon=data[0]['lon']
        finalurl=f"{weatherUrl}lat={lat}&lon={lon}&appid={key}&units=metric"
        result=requests.get(finalurl)
        data=result.json()
        weather=data['weather'][0]['main']
        temp=data['main']['temp']
        maxTemp=data['main']['temp_max']
        humidity=data['main']['humidity']
        windSpeed=data['wind']['speed']
        print(f"""
        Current weather : {weather}
        Current temperature : {temp}°C and Max temperature : {maxTemp}°C
        Humidity level : {humidity}%
        Wind speed : {windSpeed}kph
        """)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data:{e}")
city=input("Enter your city name:").capitalize()
getCurrentWeather(key,city)
