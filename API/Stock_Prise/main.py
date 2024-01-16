import os
import requests
import newsapi

STOCK = "TSLA"

COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_api_key = os.environ["STOCK_API_KEY"]
news_api_key = os.environ["NEWS_API_KEY"]

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outsize": "compact",
    "apikey": stock_api_key,
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)

stock_prices_data = stock_response.json()["Time Series (Daily)"]

yesterday_closing_price = float(list(stock_prices_data.items())[0]["4. close"])
day_after_yesterday_closing_price = float(list(stock_prices_data.items())[1]["4. close"])
diff = abs(yesterday_closing_price - day_after_yesterday_closing_price)

if diff * 100 / yesterday_closing_price >= 5:
    print("Send news")
    newsapi = newsapi.NewsApiClient(api_key=news_api_key)
    article = newsapi.get_everything(q=COMPANY_NAME, sources='bbc-news, the-verge', domains="bbc.co.uk, techcrunch.com",
                                     from_param=list(stock_prices_data.items())[1]["day"],
                                     to=list(stock_prices_data.items())[0]["day"], sort_by="relevancy", page=3)

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
# HINT 1: Consider using a List Comprehension.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
