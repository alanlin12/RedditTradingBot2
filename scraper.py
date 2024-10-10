import praw

reddit = praw.Reddit(
    client_id = "Z_H9V-jhUNeD1W9R4nJyTw",
    client_secret = "ISqWLUsyFJi5o1a9WMUPCUzaTP_yew",
    user_agent = "WsbQuantTrading"
)

wsb = reddit.subreddit("wallstreetbets")

for submissions in wsb.new(limit=30):
    print("author:", submissions.author, "karma:", (submissions.author).link_karma)

