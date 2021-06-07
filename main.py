# import required modules
from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebox

# extract key from the
# configuration file
config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['gfg']['api']
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


# explicit function to get
# weather details
def getweather(city):
    result = requests.get(url.format(city, api_key))

    if result:
        json = result.json()
        city = json['name']
        country = json['sys']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin-273.15.__round__()
        weather1 = json['weather'][0]['main']
        final = city, country, temp_kelvin, temp_celsius.__round__(), weather1
        return final
    else:
        print("No Content Found")


# explicit function to
# search city
def search():
    city = city_text.get()
    weather = getweather(city)
    if weather:
        location_lbl['text'] = '{} ,{}'.format(weather[0], weather[1])
        temperature_label['text'] = str(weather[3])+" Degree Celsius"
        weather_l['text'] = weather[4]
    else:
        messagebox.showerror('Error', "Cannot find {}".format(city))


# exit function
def exit_program():
    return root.destroy()

# clear function
def clear_input():
    city_entry.delete(0, END)
    location_lbl.delete(0, END)
    temperature_label.delete(0, END)



# Driver Code
# create object
root = Tk()
# add title
root.title("Weather App")
# adjust window size
root.geometry("800x300")
# background
root.config(bg="skyblue")

# add labels, buttons and text
city_text = StringVar()

city_entry = Entry(root, textvariable=city_text)

city_entry.place(x=350, y=5)

Search_btn = Button(root, text="Search Weather", borderwidth=12, font="Consolas 12 bold", command=search, bg="yellow")

Search_btn.place(x=200, y=50)

location_lbl = Label(root, text="Location", font={'bold', 20}, bg="skyblue")

location_lbl.place(x=20, y=120)

temperature_label = Label(root, text="", bg="skyblue")

temperature_label.place(x=350, y=220)

weather_l = Label(root, text="", bg="skyblue")

weather_l.place(x=150, y=350)

clear = Button(root, text="Clear", command=clear_input, bg="yellow", font="Consolas 12 bold", borderwidth=12)

clear.place (x=400, y=50)

exit = Button(root, text="Exit", command=exit_program, bg="yellow", font="Consolas 12 bold", borderwidth=12)

exit.place(x=510, y=50)


# to run the program
root.mainloop()
