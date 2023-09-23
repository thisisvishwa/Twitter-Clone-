```python
from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from .models import Tweet, User
from . import db

tweet = Blueprint('tweet', __name__)

@tweet.route('/create', methods=['POST'])
@login_required
def create_tweet():
    data = request.get_json()
    new_tweet = Tweet(content=data['content'], author=current_user)
    db.session.add(new_tweet)
    db.session.commit()
    return jsonify({'message': 'Tweet posted!'})

@tweet.route('/edit/<tweet_id>', methods=['PUT'])
@login_required
def edit_tweet(tweet_id):
    data = request.get_json()
    tweet = Tweet.query.get(tweet_id)
    if tweet.author == current_user:
        tweet.content = data['content']
        db.session.commit()
        return jsonify({'message': 'Tweet updated!'})
    return jsonify({'error': 'Not authorized to edit this tweet'})

@tweet.route('/delete/<tweet_id>', methods=['DELETE'])
@login_required
def delete_tweet(tweet_id):
    tweet = Tweet.query.get(tweet_id)
    if tweet.author == current_user:
        db.session.delete(tweet)
        db.session.commit()
        return jsonify({'message': 'Tweet deleted!'})
    return jsonify({'error': 'Not authorized to delete this tweet'})

@tweet.route('/follow/<user_id>', methods=['POST'])
@login_required
def follow_user(user_id):
    user_to_follow = User.query.get(user_id)
    if user_to_follow not in current_user.followed:
        current_user.followed.append(user_to_follow)
        db.session.commit()
        return jsonify({'message': 'User followed!'})
    return jsonify({'error': 'Already following this user'})

@tweet.route('/unfollow/<user_id>', methods=['POST'])
@login_required
def unfollow_user(user_id):
    user_to_unfollow = User.query.get(user_id)
    if user_to_unfollow in current_user.followed:
        current_user.followed.remove(user_to_unfollow)
        db.session.commit()
        return jsonify({'message': 'User unfollowed!'})
    return jsonify({'error': 'Not following this user'})

@tweet.route('/like/<tweet_id>', methods=['POST'])
@login_required
def like_tweet(tweet_id):
    tweet = Tweet.query.get(tweet_id)
    if current_user not in tweet.liked_by:
        tweet.liked_by.append(current_user)
        db.session.commit()
        return jsonify({'message': 'Tweet liked!'})
    return jsonify({'error': 'Already liked this tweet'})

@tweet.route('/retweet/<tweet_id>', methods=['POST'])
@login_required
def retweet(tweet_id):
    original_tweet = Tweet.query.get(tweet_id)
    retweet = Tweet(content=original_tweet.content, author=current_user, retweet_id=original_tweet.id)
    db.session.add(retweet)
    db.session.commit()
    return jsonify({'message': 'Tweet retweeted!'})
```