```python
import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/admin')
def admin_panel():
    return render_template('admin.html')

@app.route('/admin/responsive')
def responsive_design():
    if os.environ.get('FLASK_ENV') == 'development':
        return render_template('admin_responsive.html')
    else:
        return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
```
This Python code uses Flask and Flask-Bootstrap to create a simple web server that serves an admin panel. The admin panel has a responsive design, which is served only in the development environment. In the production environment, the regular admin panel is served.