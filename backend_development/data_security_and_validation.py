```python
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_mongoengine import MongoEngine
from mongoengine.errors import ValidationError
from schemas import UserSchema, TweetSchema

app = Flask(__name__)
bcrypt = Bcrypt(app)
db = MongoEngine(app)

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    user_schema = UserSchema()
    try:
        user = user_schema.load(data)
        user['password'] = bcrypt.generate_password_hash(user['password']).decode('utf-8')
        db.users.insert_one(user)
        return jsonify({"message": "User created successfully"}), 201
    except ValidationError as e:
        return jsonify({"message": "Invalid data", "errors": e.messages}), 400

@app.route('/tweet', methods=['POST'])
def create_tweet():
    data = request.get_json()
    tweet_schema = TweetSchema()
    try:
        tweet = tweet_schema.load(data)
        db.tweets.insert_one(tweet)
        return jsonify({"message": "Tweet posted successfully"}), 201
    except ValidationError as e:
        return jsonify({"message": "Invalid data", "errors": e.messages}), 400

if __name__ == '__main__':
    app.run(debug=True)
```