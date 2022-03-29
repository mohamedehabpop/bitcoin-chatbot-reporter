# requests library is to make requests from the API and time librabry is to count the needed time
import requests
import time


#global variables
btc_api_key = 'place your key here'
bot_key = 'place your key here'
chat_id = 'place your chatbot id here'
limit = 40000
request_time = 60


# function that makes the request form the API and gets the needed data
def get_price():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': btc_api_key,
    }

    response = requests.get(url, headers=headers).json()
    btc_price = response['data'][0]['quote']['USD']['price']
    return btc_price


# function that sends the data rhrough the telegram bot
def send_update(chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)


def main():
    while True:
        price = get_price()
        print(price)
        if price < limit:
            send_update(chat_id, f"   سعر البيتكوين : {price}")
        time.sleep(request_time)


main()
