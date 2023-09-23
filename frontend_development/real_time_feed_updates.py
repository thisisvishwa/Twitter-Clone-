```python
import json
import requests
from flask_socketio import SocketIO, emit

# Initialize Flask-SocketIO
socketio = SocketIO()

# Shared variables
tweets = []

@socketio.on('connect')
def connect():
    emit('tweets', json.dumps(tweets))

@socketio.on('new_tweet')
def new_tweet(data):
    tweet = json.loads(data)
    tweets.append(tweet)
    emit('tweets', json.dumps(tweets), broadcast=True)

def fetch_tweets():
    global tweets
    response = requests.get('http://localhost:5000/api/tweets')
    tweets = response.json()

if __name__ == '__main__':
    fetch_tweets()
    socketio.run(app)
```