import praw
import heapq
from collections import defaultdict

#careful the time complexity due to reddit api is 5000 years 
reddit = praw.Reddit(
    client_id = "Z_H9V-jhUNeD1W9R4nJyTw",
    client_secret = "ISqWLUsyFJi5o1a9WMUPCUzaTP_yew",
    user_agent = "WsbQuantTrading"
)

wsb = reddit.subreddit("wallstreetbets")
topRedditors = defaultdict(int) #will store any unique reddit user with 75k+ karma
top_k = 100 #limit to top 100 redditors

try:
    for post in wsb.hot(limit=1000):
        try:
            author = post.author
            if(author and author.link_karma >= 75000):
                topRedditors[author.name] = max(topRedditors[author.name], author.link_karma)

        except AttributeError as e:
            continue
    top_k_redditors = heapq.nlargest(top_k, topRedditors.items(), key=lambda x: x[1])
        
    # Print header
    print(f"{'Redditor':<20} | {'Karma':>10}")
    print("-" * 33)  # Separator line
    for username, karma in top_k_redditors:
        print(f"{username:<20} | {karma:>10,}")


except Exception as e:
    print(f"Exception occured in {e}")



