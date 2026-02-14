import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API = "STOCK API"
NEWS_API_KEY = "NEWS API"

TWILIO_SID = "TWI ID "
TWILIO_AUTH_TOKEN = "TWI AUD"

# --- STOCK DATA ---
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API
}

# ... (Previous code)

response = requests.get(STOCK_ENDPOINT , params=stock_params)
data = response.json()  # Get the JSON first

# DEBUG PRINT: Check what the API actually sent back
print(data)

# Only try to get the data if the key exists
if "Time Series (Daily)" in data:
    data = data["Time Series (Daily)"]
    data_list = [value for (key , value) in data.items()]

    #
else:
    print("Error: 'Time Series (Daily)' not found. You might have hit the API limit.")

# Get Closing Prices
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

# --- LOGIC FIX: CALCULATE RAW DIFFERENCE FIRST ---
# We need the raw number (positive or negative) to decide the Emoji
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Now we use abs() for the percentage calculation
diff_percent = round((abs(difference) / float(yesterday_closing_price)) * 100)

# --- NEWS & SMS ---
if abs(diff_percent) > 0.00001:  # Low threshold for testing

    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    # --- SYNTAX FIX BELOW ---
    # Added the closing quote (") after {article['description']}
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
        for article in three_articles
    ]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+16315025904",
            to="+94784160422"
        )
        print(f"Message sent: {message.status}")