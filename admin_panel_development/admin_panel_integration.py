```python
from flask import Flask, render_template
from flask_admin import Admin

app = Flask(__name__)

# Initialize the Flask-Admin extension
admin = Admin(app, name='Twitter Clone Admin', template_mode='bootstrap3')

@app.route('/')
def index():
    return render_template('index.html')

# Define the main function that will run the application
if __name__ == '__main__':
    app.run(debug=True)
```