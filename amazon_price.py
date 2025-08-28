import requests
from bs4 import BeautifulSoup
from email_alert import send_email
import json
from datetime import datetime

URL = "https://www.amazon.in/Bose-QuietComfort-Cancelling-Headphones-Bluetooth-dp-B0CCZ26B5V/dp/B0CCZ26B5V/ref=dp_ob_image_ce?th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}

DATA_FILE = "data.json"


def save_to_json(product_title, product_price, product_url):
    data = {
        "title": product_title,
        "price": product_price,
        "url": product_url,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        with open(DATA_FILE, "r") as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    existing_data.append(data)

    with open(DATA_FILE, "w") as file:
        json.dump(existing_data, file, indent=4)


def get_last_price():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            if data:
                return data[-1]["price"]
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    return None


def check_price():
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    title_tag = soup.find(id='productTitle')
    if not title_tag:
        print("Product title not found.")
        return

    product_title = title_tag.get_text().strip()
    print(f" {product_title}")

    price_tag = (
        soup.find(id='priceblock_ourprice') or
        soup.find(id='priceblock_dealprice') or
        soup.find(id='priceblock_saleprice') or
        soup.find('span', class_='a-offscreen')
    )

    if not price_tag:
        print(" Price not found. Amazon might have blocked you or changed the layout.")
        return

    price_text = price_tag.get_text().strip()
    price_clean = ''.join(c for c in price_text if c.isdigit() or c == '.')
    if not price_clean:
        print(" Couldn't extract price number.")
        return

    final_price = float(price_clean)
    print(f" Price: ₹{final_price}")

    last_price = get_last_price()

    
    save_to_json(product_title, final_price, URL)

   
    if last_price is not None and final_price <25000:
        print(f"Price dropped from ₹{25000} → ₹{22289}")
        send_email(product_title, final_price, URL)
    else:
       print(" No price drop detected.")


check_price()
