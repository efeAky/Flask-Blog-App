# Flask Blog Application

A simple blog application built with Flask that allows users to register, 
login, create posts, and delete their own posts.

## Features

- User registration and authentication
- Secure password hashing
- Create and delete blog posts
- View all posts from all users

## Technologies

Flask, Flask-SQLAlchemy, Flask-Login, Flask-WTF, SQLite

## Setup Instructions

1. **Install dependencies**
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Login Flask-WTF
   ```

2. **Run the application**
   ```bash
   python app.py
   ```

3. **Access the app**
   - Open browser: `http://127.0.0.1:5000`

## Testing Guide

### Basic Flow Test
1. **Register**: Create account with username and password
2. **Login**: Use your credentials to login
3. **Create Post**: Click "Create Post" and add title/body
4. **Delete Post**: Click "Delete This Post" on your own posts
5. **Logout**: Click logout in navigation

### Edge Cases to Test
- Register with duplicate username (should fail)
- Login with wrong password (should fail)
- Try accessing `/post` while logged out (redirects to login)
- Try deleting another user's post (should fail)
- Password confirmation mismatch during registration (should fail)

## Security Notes

⚠️ **Before production:**
- Change `SECRET_KEY` in `app.py`
- Set `debug=False`
- Use production database (PostgreSQL/MySQL)
- Enable HTTPS

## Troubleshooting

- **Import errors**: Ensure virtual environment is activated and packages installed
- **Port in use**: Change port with `app.run(debug=True, port=5001)`
- **Database issues**: Delete `instance` folder and restart