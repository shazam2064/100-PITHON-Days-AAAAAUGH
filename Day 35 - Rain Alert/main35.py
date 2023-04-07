import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "9dc8b4b779f036a34d25913abf0dac7b"

weather_params = {
    "lat": 33.935101,
    "lon": -84.360924,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def telegram_bot_sendtext(bot_message):
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


test = telegram_bot_sendtext("Testing Telegram bot")
print(test)

# 404 942 8617
