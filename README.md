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

#### 4. Navigate to the application folder

```bash
cd blog_app
```

#### 5. Run the application

```bash
python app.py
```

The app will start on **http://127.0.0.1:5000**.

#### 6. Open in your browser

Navigate to **http://127.0.0.1:5000** to access the blog.

## Important Notes

⚠️ **Security & Production Considerations:**

- Change `SECRET_KEY` in `app.py` before deploying to production
- For production, consider using a proper database (e.g., PostgreSQL) instead of SQLite
- Do not run with `debug=True` in a production environment

## Project Structure

```
Flask-Blog-App/
├── blog_app/              # Main application folder
│   ├── app.py            # Flask application entry point
│   ├── templates/        # HTML templates
│   ├── static/           # CSS, JavaScript, images
│   └── instance/         # SQLite database (auto-generated)
├── venv/                 # Virtual environment
├── requirements.txt      # Python dependencies
├── LICENSE              # MIT License
└── README.md            # This file
```

## Features

- **User authentication** - Secure registration and login system
- **Create, read, update, and delete blog posts** - Full CRUD functionality
- **SQLite database** - Lightweight data persistence
- **Flask-WTF forms** - Form validation and CSRF protection
- **User-specific content** - Users can only edit/delete their own posts

## Technologies Used

- **Flask** - Web framework
- **Flask-SQLAlchemy** - Database ORM
- **Flask-Login** - User session management
- **Flask-WTF** - Form handling and validation
- **SQLite** - Database

## Troubleshooting

### Common Issues

**"Module not found" errors:**
```bash
# Make sure virtual environment is activated
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

**"Template not found" errors:**
- Ensure you're running the app from inside the `blog_app` folder
- Check that the `templates/` folder exists

**Database errors:**
- Delete the `instance/` folder and restart the app to recreate the database

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created by [efeAky](https://github.com/efeAky)

## Acknowledgments

Built with Flask and designed for educational purposes to demonstrate web application development with Python.
