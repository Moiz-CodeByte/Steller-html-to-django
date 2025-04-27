# Steller Portfolio

A Django-based portfolio website built from the Steller HTML template. This web application provides a professional portfolio site with multiple sections including home, about, services, portfolio, testimonials, blog, and contact pages.

## Features

- Responsive design
- Multiple page sections (Home, About, Services, Portfolio, Testimonials, Blog, Contact)
- User authentication (Login functionality)
- Modern UI with Bootstrap

## Prerequisites

- Python 3.x
- Django (see requirements.txt for specific version)

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd Steller
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Apply migrations:
   ```
   python manage.py migrate
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the site at http://127.0.0.1:8000/

## Project Structure

- `StellerProject/` - Django project folder
- `stellerapp/` - Main application folder
- `templates/` - HTML templates
- `static/` - Static files (CSS, JavaScript, images)

## Customization

To customize the site for your personal use:
1. Modify the templates in `stellerapp/templates/`
2. Update static content in `stellerapp/static/`
3. Add your own data through the Django admin interface

## Credits

- Original Design: Steller HTML Template
- Development: Django conversion by Abdul Moiz 
