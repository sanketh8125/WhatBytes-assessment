# User Authentication System

This is a user authentication system built as part of an internship assessment. The application allows users to **Sign Up**, **Login**, **Change Password**, and **Reset Password** through a series of simple and secure forms. It also includes a **Dashboard** where users can manage their profiles.

## Features

- **User Sign Up**: Create a new user account with a username, email, and password.
- **User Login**: Authenticate users with their username/email and password.
- **Forgot Password**: Send a reset link to the user’s email to change their password if they forget it.
- **Change Password**: Change the current password after successful authentication.
- **Profile Page**: View user details like username, email, date joined, and last login.
- **Dashboard**: A welcoming page that greets the user by their username with links to change password and view their profile.

## Technologies Used

- **Backend**: Python (Django)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite, or configure your preferred database in `settings.py`
- **Email Service**: Django’s built-in email system to send password reset links.

## Installation

Follow these steps to run the project locally.

### Prerequisites

- Python 3.x
- Django (can be installed via pip)

### Clone the Repository

```bash
git clone https://github.com/sanketh8125/WhatBytes-assessment.git
