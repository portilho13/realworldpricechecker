import requests
import telebot
import sys
import bs4
import validators
from time import sleep

"""
This code is specificly to get the chat_id, if you want to run it create a different .py file, install telegram and search for the name of the bot (@CS50Price_bot), on the chat type "/start"
and then run the problem on new .py file and the bot should print your chat_id.

BOT_KEY = "6449929924:AAGg3e0DUKE220kNChBo8SxbCIp-qBSc-5s"
bot = telebot.TeleBot(BOT_KEY)
@bot.message_handler(commands=["start"])
def handle_start(message):
    chat_id = message.chat.id
    bot.reply_to(message, f"{chat_id}")
bot.polling()

"""

#Declare Headers and API Keys

apiKey = "6449929924:AAGg3e0DUKE220kNChBo8SxbCIp-qBSc-5s"

url = ""


headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0'
}

interval = 0

def main():
    global initial_price
    initial_price = None
    interval = input("Interval: ")
    if check_interval(interval):
        url = input("URL: ")
        if validate_url(url):
            print("[STATUS] Launching Bot")
            while True:
                price = get_price(url)
                result, initial_price = compare_price(price, initial_price)
                if result != None:
                    print(send_message(result, apiKey, url))
                sleep(30 * int(interval)) #Change Interval
        else:
            sys.exit("[Error] Invalid Values.")
    else:
        sys.exit("[Error] Invalid Values.")



def check_interval(interval):
    for n in interval:
        if n.isalpha() or int(interval) < 0:
            return False
    return True

def validate_url(url):
    if validators.url(url):
        return True
    return False


def get_price(url):
    st = []
    r = requests.get(url, headers=headers)
    html = bs4.BeautifulSoup(r.content, 'html.parser')
    price_element = html.find(class_="userPrice")
    price_text = price_element.text
    for i in price_text.strip():
        if i.isdigit():
            st.append(i)
    price = float("".join(st))
    return price

def compare_price(price, initial_price):
    if initial_price and price < initial_price:
        initial_price = float(price)
        return "The price has decreased", initial_price
    elif initial_price and price > initial_price:
        initial_price = float(price)
        return "The price has incrised", initial_price
    elif initial_price and price == initial_price:
        initial_price = float(price)
        return "The price still the same", initial_price
    else:
        initial_price = float(price)
        return None, initial_price

def send_message(result, apiKey, url):
    url_bot = f"https://api.telegram.org/bot{apiKey}/sendMessage"
    data = {
        "chat_id": 5951495480,
        "text": f"{result}, here is the URL: {url}"
    }
    try:
        requests.post(url_bot, data=data)
    except requests.exceptions.ConnectionError:
        return "[ERROR] Connection error"
    except requests.exceptions.HTTPError:
        return "[ERROR] HTTP error occurred"
    except requests.exceptions.RequestException:
        return "[ERROR] An error occurred"
    else:
        return "[STATUS] Message sent sucessfully"



if __name__ == "__main__":
    main()
