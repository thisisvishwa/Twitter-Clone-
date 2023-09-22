```python
import pymongo
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['twitter_clone']

# Shared Variables
users = db['users']
tweets = db['tweets']

# Function to generate user analytics
def generate_user_analytics():
    user_count = users.count_documents({})
    active_users = users.count_documents({"status": "active"})
    inactive_users = users.count_documents({"status": "inactive"})
    
    print(f"Total Users: {user_count}")
    print(f"Active Users: {active_users}")
    print(f"Inactive Users: {inactive_users}")

# Function to generate tweet statistics
def generate_tweet_stats():
    tweet_count = tweets.count_documents({})
    retweets = tweets.count_documents({"type": "retweet"})
    likes = sum(tweet['likes'] for tweet in tweets.find({}))
    
    print(f"Total Tweets: {tweet_count}")
    print(f"Retweets: {retweets}")
    print(f"Total Likes: {likes}")

# Function to generate overall analytics
def generate_stats():
    print("User Analytics:")
    generate_user_analytics()
    print("\nTweet Statistics:")
    generate_tweet_stats()

# Call the function to generate statistics
generate_stats()
```