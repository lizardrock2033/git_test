from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language']='ru'
owm = OWM('472bca84ff51831e395d4c32f5ee1b4c',config_dict)
mgr = owm.weather_manager()

place = input("В каком городе?: ")

observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')["temp"]

print ("На улице " + str(temp) + " градусов и " + str(w.detailed_status))

if -10 < temp < 10:
    print ("Прохладненько...")
elif temp < -10:
    print ("Дубак, сиди дома!")
elif temp > 25:
    print ("Асфальт плавится!")
else:
    print ("Норм.")
