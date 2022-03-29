# requests library is to make requests from the API and time librabry is to count the needed time
import requests
import time


#global variables
btc_api_key = '7c667c1a-b5fa-4a6b-83c1-4024c3aa788e'
bot_key = '1846331338:AAHTIiI4T1x54epo7E4NeQf1OQz3CAnxD1A'
chat_id = '956402152'
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
            send_update(chat_id, f"  يا نجم سعر البيتكوين : {price}")
        time.sleep(request_time)


main()
