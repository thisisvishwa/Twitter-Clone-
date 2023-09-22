```python
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from schemas import UserSchema, TweetSchema

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/twitterClone"
mongo = PyMongo(app)

@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    return jsonify([UserSchema().dump(user) for user in users])

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.users.find_one({"_id": ObjectId(id)})
    return UserSchema().dump(user)

@app.route('/tweets', methods=['GET'])
def get_tweets():
    tweets = mongo.db.tweets.find()
    return jsonify([TweetSchema().dump(tweet) for tweet in tweets])

@app.route('/tweets/<id>', methods=['GET'])
def get_tweet(id):
    tweet = mongo.db.tweets.find_one({"_id": ObjectId(id)})
    return TweetSchema().dump(tweet)

@app.route('/users', methods=['POST'])
def create_user():
    user = UserSchema().load(request.json)
    result = mongo.db.users.insert_one(user)
    return {'_id': str(result.inserted_id)}

@app.route('/tweets', methods=['POST'])
def create_tweet():
    tweet = TweetSchema().load(request.json)
    result = mongo.db.tweets.insert_one(tweet)
    return {'_id': str(result.inserted_id)}

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    user = UserSchema().load(request.json)
    mongo.db.users.update_one({"_id": ObjectId(id)}, {"$set": user})
    return {'message': 'userUpdated'}

@app.route('/tweets/<id>', methods=['PUT'])
def update_tweet(id):
    tweet = TweetSchema().load(request.json)
    mongo.db.tweets.update_one({"_id": ObjectId(id)}, {"$set": tweet})
    return {'message': 'tweetPosted'}

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({"_id": ObjectId(id)})
    return {'message': 'userUpdated'}

@app.route('/tweets/<id>', methods=['DELETE'])
def delete_tweet(id):
    mongo.db.tweets.delete_one({"_id": ObjectId(id)})
    return {'message': 'tweetPosted'}

if __name__ == '__main__':
    app.run(debug=True)
```