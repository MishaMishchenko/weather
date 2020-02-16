# import pyowm
# import telebot

# owm = pyowm.OWM('9a894fbcb3198fd3612e6c6def4af9bd', language = "ru")
# bot = telebot.TeleBot("990620537:AAGQHDbqu3cN2v0ftRIC9MGZo9ZkX6_04bM")

# @bot.message_handler(content_types=['text'])
# def send_echo(message):
# 	observation = owm.weather_at_place( message.text )
# 	w = observation.get_weather()
# 	temp = w.get_temperature('celsius')["temp"]


# 	answer = " В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
# 	answer += " Температура сейчас " + str(temp) + "\n\n"


# 	if temp < 5:
# 	    answer +=" На улице холодно, одевайся теплее"

# 	elif temp < 15:
# 	    answer += " На улице прохладно"

# 	elif temp > 16:
# 	    answer += " На улице жарко"

# bot.send_message(message.chat.id, answer)

# bot.polling( none_stop = True )

import pyowm
import telebot

owm = pyowm.OWM('9a894fbcb3198fd3612e6c6def4af9bd', language = "ru")
bot = telebot.TeleBot("990620537:AAGQHDbqu3cN2v0ftRIC9MGZo9ZkX6_04bM")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]
	
	answer = " В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
	answer += " Температура сейчас " + str(temp) + "\n\n"
	if temp < 5:
	    answer +=" На улице холодно, одевайся теплее"

	elif temp < 15:
	    answer += " На улице прохладно"

	elif temp > 15:
	    answer += " На улице жарко"
	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )



# import pyowm
# import telebot
# owm = pyowm.OWM('9a894fbcb3198fd3612e6c6def4af9bd', language = "ru")
# bot = telebot.TeleBot("990620537:AAGQHDbqu3cN2v0ftRIC9MGZo9ZkX6_04bM")

# @bot.message_handler(content_types=['text'])
# def send_echo(message):
# 	observation = owm.weather_at_place( message.text )
# 	w = observation.get_weather()
# 	temp = w.get_temperature('celsius')["temp"]
#     answer = " В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
#     answer +=  "Температура сейчас " + str(temp) + "\n\n"
#     if temp < 5:
# 	    answer +=" На улице холодно, одевайся теплее"
# 	elif temp < 15:
# 	    answer += " На улице прохладно"
# 	elif temp > 15:
# 	    answer += " На улице жарко"
# 	bot.send_message(message.chat.id, message.text)

# bot.polling( none_stop = True)









