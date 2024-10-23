import praw
import re
import yfinance as yf

#This is a prototype, not fully accurate.

reddit = praw.Reddit(
    client_id = "Z_H9V-jhUNeD1W9R4nJyTw",
    client_secret = "ISqWLUsyFJi5o1a9WMUPCUzaTP_yew",
    user_agent = "WsbQuantTrading"
)

wsb = reddit.subreddit("wallstreetbets")
unique_tickers = []

for posts in wsb.new(limit=1000):
    post_flair = posts.link_flair_text
    if(post_flair == "Gain"):
        pattern = r'[0-9]'
        tickers = list(re.findall(r'(?<=\$)\w+|[A-Z]{3,6}', re.sub(pattern, '', posts.title)))
        if(len(tickers) > 0):
            for stocks in tickers:
                if stocks not in unique_tickers: unique_tickers.append(stocks)

for valid_tickers in unique_tickers:
    try:
        ticker = yf.Ticker(valid_tickers)
        print(valid_tickers + " INFO:")
        print(ticker.history(period="5d"))
        print()
    except:
        continue
    
        