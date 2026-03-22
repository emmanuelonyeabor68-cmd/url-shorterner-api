# 🔗 URL Shortener API

A robust and scalable URL Shortener built with Django and Django REST Framework. It converts long URLs into short, shareable links and handles redirection efficiently while tracking usage.

## Overview

This project demonstrates core backend engineering concepts such as RESTful API design, database modeling, URL routing & redirection, unique shortcode generation, and request validation using serializers.

## Features

- Shorten long URLs into unique short codes  
- Automatic redirection to original links  
- Click tracking (basic analytics)  
- Clean and structured API endpoints  
- Error handling and validation  

## Tech Stack

- Python  
- Django  
- Django REST Framework  
- SQLite (default database)  

## Installation & Setup

# Clone the repository
git clone https://github.com/your-username/url-shortener.git
cd url-shortener

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver

# Server will run at http://127.0.0.1:8000/

## API Endpoints

### Create Short URL
POST /shorten/

Request:
{
  "original_url": "https://google.com"
}

Response:
{
  "original_url": "https://google.com",
  "short_url": "http://127.0.0.1:8000/abc123"
}

### Redirect to Original URL
GET /{short_code}/

Example:
http://127.0.0.1:8000/abc123
➡️ Redirects to the original URL

### URL Statistics
GET /stats/{short_code}/

Response:
{
  "original_url": "https://google.com",
  "short_code": "abc123",
  "clicks": 3,
  "created_at": "2026-01-01T12:00:00Z"
}

## Testing

- API endpoints tested using Postman  
- Redirect functionality verified in browser  

## Future Improvements

- Custom alias support  
- Link expiration  
- Advanced analytics (IP tracking, timestamps)  
- Deployment to cloud platforms (Render)  

## Author

Emmanuel Onyeabor  
Backend Developer (Python/Django)

## Support

If you found this project useful, consider giving it a ⭐ on GitHub.  
