from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
import telebot

config_dict = get_default_config()
config_dict['language']='ru'
owm = OWM('472bca84ff51831e395d4c32f5ee1b4c',config_dict)
mgr = owm.weather_manager()

bot = telebot.TeleBot("1381583188:AAEmbqENIsjUKMtwBY84rg8SHcR0kCkWFZs", parse_mode=None)

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]

    answer = "На улице " + str(temp) + " градусов и " + str(w.detailed_status) + "\n"
    if -10 < temp < 10:
        answer += "Прохладненько..."
    elif temp < -10:
        answer += "Дубак ибаный, сиди дома!"
    elif temp > 25:
        answer += "Асфальт плавится, ну его нахуй!"
    else:
        answer += "Норм, пиздуй"
    
    bot.send_message(message.chat.id, answer)
bot.polling(none_stop = True)
	
