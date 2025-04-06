# Course Management System

A modern web-based Course Management System built with Django that allows students to enroll in courses and faculty members to manage course offerings.

## Features

### For Students
- User registration and authentication
- Browse available courses
- Enroll in up to 2 courses
- View enrolled courses
- Drop courses when needed

### For Faculty
- User registration and authentication
- Create new courses
- Manage existing courses
- View enrolled students count
- Update course information

### General Features
- Clean and modern user interface
- Secure authentication system
- Role-based access control
- Responsive design for all devices
- Traditional form submissions (no JavaScript required)

## Technical Details

### Built With
- Django 5.0.2 (Backend Framework)
- HTML5 & CSS3 (Frontend)
- PostgreSQL (Database)

### Security Features
- CSRF protection
- Password hashing
- Session management
- Form validation

## Pages and Functionality

### 1. Home Page
- Welcome message
- Login and Register buttons
- Feature highlights for students and faculty

### 2. Login Page
- Username and password fields
- Error message display
- Link to registration page
- Back to home navigation

### 3. Registration Page
- User information fields (username, email, password)
- Role selection (student/faculty)
- Form validation
- Error message display

### 4. Student Dashboard
- View enrolled courses
- Course enrollment functionality
- Maximum 2 courses limit
- Course dropping capability
- Display of course details

### 5. Faculty Dashboard
- Course creation form
- List of created courses
- Student enrollment count
- Course management options (update/delete)


### Database Setup

1. Install PostgreSQL if you haven't already:
   - [PostgreSQL Downloads](https://www.postgresql.org/download/)

2. Create a PostgreSQL database:
   ```sql
   CREATE DATABASE Task1db;
   ```

3. Configure Environment Variables:
   - Create a `.env` file in the project root directory
   - Add your database credentials to the `.env` file:
   ```
   DATABASE_NAME=Task1db
   DATABASE_USER=postgres
   DATABASE_PASSWORD=your_password
   DATABASE_HOST=127.0.0.1
   DATABASE_PORT=5432
   SECRET_KEY=your_secret_key
   DEBUG=True
   ```

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/course-management-system.git
   cd course-management-system
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

6. Access the application at http://127.0.0.1:8000/



