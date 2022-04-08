import tkinter as tk
import requests
import time


#get data from API
def getWeather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&APPID=a6b79f5e1eccc19ed71f19b701e95ddc&units=metric"
    response = requests.get(api)
    if response.status_code == 404 :
        label1.config(text="Wrong City")
        label2.config(text="Try again")
        return
    json_data = response.json()
    condition = json_data['weather'][0]['main']
    temp = json_data['main']['temp']
    min_temp = json_data['main']['temp_min']
    max_temp = json_data['main']['temp_max']
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunrise'] + 10800))
    sunset = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunset'] + 10800))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)


#for canvas
canvas = tk.Tk()
canvas.geometry("500x400")
canvas.title("Weather App")

#for font
f = ("poppins", 12, "bold")
t = ("poppins", 32, "bold")

#text field for city name
textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)

#display data
label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()