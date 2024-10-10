import praw

reddit = praw.Reddit(
    client_id = "Z_H9V-jhUNeD1W9R4nJyTw",
    client_secret = "ISqWLUsyFJi5o1a9WMUPCUzaTP_yew",
    user_agent = "WsbQuantTrading"
)

for submission in reddit.subreddit("wallstreetbets").hot(limit=10):
    print(submission.title)