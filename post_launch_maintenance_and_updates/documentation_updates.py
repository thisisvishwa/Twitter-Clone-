```python
import os
import json

# Shared dependencies
user = {}
tweets = []
users = []

# Data Schemas
UserSchema = {}
TweetSchema = {}

# Function to update documentation
def update_documentation():
    # Load existing documentation
    with open('documentation.json', 'r') as file:
        documentation = json.load(file)

    # Update documentation for UserSchema
    documentation['UserSchema'] = UserSchema

    # Update documentation for TweetSchema
    documentation['TweetSchema'] = TweetSchema

    # Update documentation for user
    documentation['user'] = user

    # Update documentation for tweets
    documentation['tweets'] = tweets

    # Update documentation for users
    documentation['users'] = users

    # Save updated documentation
    with open('documentation.json', 'w') as file:
        json.dump(documentation, file, indent=4)

# Call the function to update documentation
update_documentation()
```