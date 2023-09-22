```python
import os
from git import Repo

def deployApp():
    # Define the local and remote repositories
    local_repo = os.path.join(os.getcwd(), 'twitter_clone')
    remote_repo = 'git@github.com:username/twitter_clone.git'

    # Initialize the local repository
    repo = Repo.init(local_repo)

    # Add all changes to the staging area
    repo.git.add(A=True)

    # Commit the changes
    repo.git.commit(m='Production deployment')

    # Define the remote repository
    remote = repo.create_remote('origin', remote_repo)

    # Push the changes to the remote repository
    remote.push(refspec='master:master')

    print("Application has been successfully deployed to production.")

deployApp()
```