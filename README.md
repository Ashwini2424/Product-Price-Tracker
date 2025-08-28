# Product-Price-Tracker
# scrape-Amazon-EmailPriceDropAlertSystem
First install beautifulsoup4 and requests
I have added the scraper for amazon , the email_alert.py deals with emails notification
# 🛒 Amazon Price Tracker – Python (All-in-One Script)

A simple yet powerful Python script that monitors the price of a product on Amazon and sends you an **email alert** when the price drops below your desired threshold. It also logs the product data (title, price, timestamp) in a JSON file for tracking.

---

## 🚀 Features

- ✅ Scrapes product title and price using `requests` + `BeautifulSoup`
- ✅ Sends **email alert** if price goes below a specified threshold
- ✅ Logs each price check to a `product_data.json` file with timestamps
- ✅ Automatically checks again every 60 seconds if the price is still high

---

## 📁 Project Structure

📁 amazon-price-tracker/
├── amazon_price_tracker.py # ✅ All logic in one file
├── product_data.json # 📝 Automatically generated (price logs)
└── README.md # 📘 Project documentation

yaml
Copy
Edit

---

## 🧰 Tech Stack

- `requests` for fetching HTML
- `BeautifulSoup` for parsing the webpage
- `smtplib` & `email` for Gmail alerts
- `json` for data logging
- `threading.Timer` for repeat checks

---

## 🔧 Setup Instructions

### 1. ✅ Install Required Libraries

```bash
pip install requests beautifulsoup4
2. ✏️ Update These in the Python Script
Set your Gmail credentials:
python
Copy
Edit
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"  # Generate from Gmail settings
RECEIVER_EMAIL = "your_email@gmail.com"
🔐 Use a Gmail App Password, not your main password:
Create one here →

Set product URL and price threshold:
python
Copy
Edit
URL = "https://www.amazon.in/your-product-url"

if final_price <= 20000:  # ← Set your desired alert price
▶️ How to Run
Run the script in the terminal or VS Code:

bash
Copy
Edit
python amazon_price_tracker.py
The script will:

Fetch the title and current price from Amazon

Save a log entry in product_data.json

Send an email if the price is lower than your threshold

Retry every 60 seconds if not

📧 Email Example
makefile
Copy
Edit
Subject: Price Drop Alert: Bose QuietComfort Headphones

📉 Price Drop Alert!

Product: Bose QuietComfort Headphones
Price: ₹19999.0
Link: https://www.amazon.in/Bose-QuietComfort...

-- Sent by your Python Price Tracker
📝 product_data.json Sample
json
Copy
Edit
[
    {
        "title": "Bose QuietComfort Wireless Headphones",
        "price": 19999.0,
        "url": "https://www.amazon.in/Bose-QuietComfort...",
        "timestamp": "2025-07-27 13:20:45"
    }
]
⚠️ Disclaimers
For educational purposes only.

Amazon may block scraping if overused. Be respectful in request frequency.

Layout changes on Amazon may require updates to the scraping logic.

💡 Optional Improvements
Track multiple products from different URLs

Export data to .csv or Google Sheets

Deploy as a web app or run on Raspberry Pi

Add logging, retries, or notification via Telegram or Discord


