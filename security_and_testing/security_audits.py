```python
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.json_util import dumps
import json
from security import SecurityManager

# Load environment variables
load_dotenv()

# Connect to MongoDB
client = MongoClient(os.getenv('MONGO_URI'))
db = client[os.getenv('DB_NAME')]

# Initialize SecurityManager
security_manager = SecurityManager()

def audit_users():
    users = db.users.find()
    for user in json.loads(dumps(users)):
        if not security_manager.validate_user(user):
            print(f"User {user['_id']} failed security audit.")

def audit_tweets():
    tweets = db.tweets.find()
    for tweet in json.loads(dumps(tweets)):
        if not security_manager.validate_tweet(tweet):
            print(f"Tweet {tweet['_id']} failed security audit.")

def main():
    audit_users()
    audit_tweets()

if __name__ == "__main__":
    main()
```