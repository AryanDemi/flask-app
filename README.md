Here's a step-by-step guide to creating a Flask app with three routes (`/skill`, `/about`, `/connect`), using Bootstrap for styling, setting up a virtual environment, and creating a Docker image.

---

## 📂 **Project Structure**
```
flask_app/
│── app/
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css  # Custom CSS (if needed)
│   ├── templates/
│   │   ├── base.html      # Base Bootstrap template
│   │   ├── skill.html     # Skill Page
│   │   ├── about.html     # About Page
│   │   ├── connect.html   # Connect Page
│   ├── __init__.py
│   ├── routes.py
│── .env                   # Environment variables
│── requirements.txt       # Dependencies
│── Dockerfile             # Docker image setup
│── docker-compose.yml     # Docker Compose file
│── app.py                 # Main entry file
│── run.sh                 # Run script
│── README.md              # Documentation
```

---

## **Step 1: Set Up a Virtual Environment**
1. Open a terminal and create a project folder:
   ```bash
   mkdir flask_app && cd flask_app
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install Flask and dependencies:
   ```bash
   pip install flask python-dotenv
   pip freeze > requirements.txt
   ```

---

## **Step 2: Create the Flask App**
Inside `flask_app/`, create a folder `app/` and add the following files.

### 📌 `app/__init__.py`
```python
from flask import Flask
from app.routes import main

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app
```

### 📌 `app/routes.py`
```python
from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("base.html", title="Home")

@main.route("/skill")
def skill():
    return render_template("skill.html", title="Skills")

@main.route("/about")
def about():
    return render_template("about.html", title="About")

@main.route("/connect")
def connect():
    return render_template("connect.html", title="Connect")
```

---

## **Step 3: Create HTML Templates**
Inside `app/templates/`, create the following files.

### 📌 `app/templates/base.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="/">My Flask App</a>
            <div class="collapse navbar-collapse">
                <ul class="navbar-nav">
                    <li class="nav-item"><a class="nav-link" href="/skill">Skills</a></li>
                    <li class="nav-item"><a class="nav-link" href="/about">About</a></li>
                    <li class="nav-item"><a class="nav-link" href="/connect">Connect</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <div class="container mt-5">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

### 📌 `app/templates/skill.html`
```html
{% extends "base.html" %}
{% block content %}
<h2>My Skills</h2>
<p>Here are my skills...</p>
{% endblock %}
```

### 📌 `app/templates/about.html`
```html
{% extends "base.html" %}
{% block content %}
<h2>About Me</h2>
<p>Welcome to the about page.</p>
{% endblock %}
```

### 📌 `app/templates/connect.html`
```html
{% extends "base.html" %}
{% block content %}
<h2>Contact Me</h2>
<p>Email me at: contact@example.com</p>
{% endblock %}
```

---

## **Step 4: Create `.env` File**
Create a `.env` file to store environment variables.
```
FLASK_APP=app.py
FLASK_ENV=development
```

---

## **Step 5: Create `app.py` (Main Entry)**
```python
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
```

---

## **Step 6: Create Docker Configuration**
### 📌 `Dockerfile`
```dockerfile
# Use official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
```

### 📌 `docker-compose.yml`
```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/app
    environment:
      - FLASK_ENV=development
```

---

## **Step 7: Create a Shell Script to Run App**
### 📌 `run.sh`
```bash
#!/bin/bash
source venv/bin/activate
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
```
Make it executable:
```bash
chmod +x run.sh
```

---

## **Step 8: Run the Flask App**
1. Run the Flask app locally:
   ```bash
   ./run.sh
   ```
   or manually:
   ```bash
   flask run
   ```

2. To run with Docker:
   ```bash
   docker build -t flask_app .
   docker run -p 5000:5000 flask_app
   ```

3. To use Docker Compose:
   ```bash
   docker-compose up --build
   ```

---

## ✅ **Final Notes**
- Open `http://localhost:5000` in your browser to see the app.
- The three pages (`/skill`, `/about`, `/connect`) are styled using Bootstrap.
- This setup allows for easy containerization using Docker.

Let me know if you need modifications! 🚀