# QuotesApp

## Overview
QuotesApp is a Django web application for browsing and managing a collection of quotes and their respective authors. The application allows users to view quotes, search for quotes by tags, and view detailed information about authors. Registered users can add new authors and quotes to the database.

## Features
- **User Authentication**: Users can register and log in to the application. Only authenticated users can add new authors and quotes.
- **Author Management**: Users can view a list of authors and detailed information about each author.
- **Quote Management**: Users can view a list of quotes, and these can be filtered by tags.
- **Add Quotes and Authors**: Registered users can add new quotes and authors to the database.
- **Tag-Based Search**: Users can search for quotes based on specific tags.
- **Data Import**: Admin users can import authors and quotes data from JSON files.
- **Pagination**: The quotes list is paginated to enhance user experience and performance.
- **Scraping**: Read the Readme.md in the `scrappyquotes`

## Technologies
- **Backend**: Python, Django
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS 

## Setup and Installation
1. **Clone the Repository**
   ```
   git clone https://github.com/your-repository/QuotesApp.git
   cd QuotesApp
   ```

2. **Set Up a Virtual Environment (Optional)**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Initialize the Database**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create an Admin User**
   ```
   python manage.py createsuperuser
   ```

6. **Run the Server**
   ```
   python manage.py runserver
   ```

## Usage
- Visit `http://localhost:8000` in your browser to access the application.
- Log in as an admin to import data from JSON files and manage the application.
- Register a new user account to add new authors and quotes.

