# Flask Blog App

A simple blog application built with Flask, featuring user authentication, post creation, and SQLite database integration.

## Setup Instructions

Follow these steps to run the Flask Blog App locally:

### Prerequisites

- Python 3.x installed
- Git (to clone the repository)
- (Optional) Virtual environment tool (venv)

### Installation Steps

#### 1. Clone the repository

```bash
git clone https://github.com/efeAky/Flask-Blog-App.git
cd Flask-Blog-App
```

#### 2. Create and activate a virtual environment (recommended)

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows (cmd):**
```bash
python -m venv venv
venv\Scripts\activate
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not present, manually install:
```bash
pip install Flask Flask-SQLAlchemy Flask-Login Flask-WTF
```

#### 4. Run the application

```bash
python app.py
```

The app will start on **http://127.0.0.1:5000**.

#### 5. Open in your browser

Navigate to **http://127.0.0.1:5000** to access the blog.

## Important Notes

⚠️ **Security & Production Considerations:**

- Change `SECRET_KEY` in `app.py` before deploying to production
- For production, consider using a proper database (e.g., PostgreSQL) instead of SQLite
- Do not run with `debug=True` in a production environment

## Features

- User authentication (registration and login)
- Create, read, update, and delete blog posts
- SQLite database for data persistence
- Flask-WTF forms with validation

## License

This project is open source and available for educational purposes.
