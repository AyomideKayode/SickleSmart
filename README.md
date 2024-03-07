# SickleSmart Web App

My Portfolio Project to complete the Foundations Phase of ALX.

This repository contains a Flask-based web application called SickleSmart, which provides functionality for user authentication, user health status tracking, and associated views. Below is an overview of the key components, Architecture, Features, Technologies Used and API endpoints available in the application.😁

![SickleSmart](./sicklesmart_web/static/images/web_logo1.png)

## Overview

SickleSmart is a web platform designed to empower individuals managing sickle cell anemia by providing tools for health tracking, access to educational resources, and a supportive community forum.

## Architecture

SickleSmart follows a traditional three-tier architecture:

- **Frontend Client:** Handles user interaction and interface using HTML, CSS, and JavaScript (potentially with frameworks like React or Vue.js).

- **Web Server:** Manages HTTP requests, serves web pages, and interacts with backend services using Python language with Flask.

- **Database:** Stores and manages data using SQL-based database management system - SQLite.

## Features

- **User Authentication:** Users can log in securely without providing personal details.

- **User Interface:** Clean and intuitive user interface designed with HTML, CSS and JavaScript.

- **Health Tracking:** In this current MVP version, Users can track their health status and update symptoms. Working on how they can delete health statuses or symptoms they have previously updated which is currently being implemented and eventually implement how Users can receive reminders for hydration and medication.

- **Educational Resources:** Access to educational resources on managing sickle cell anemia. \*_(Needs a bit more materials to be fully done with)_

- **Personalized Recommendations:** Users receive personalized recommendations for diet and lifestyle modifications. _(Not implemented yet.)_

- **Community Forums:** Connect with others affected by sickle cell anemia through community forums. _(Also not implemented yet, bear with me🥴☹)_

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript

- **Backend:** Python with Flask

- **Database:** SQL-based database management system => SQLite

- **Additional Tools:** Werkzeug for password hashing, Flask-Login for user session management.

## Components

- **[Auth Module](./sicklesmart_web/auth.py):** Responsible for user authentication, registration, and login/logout functionality.

- **[Views Module](./sicklesmart_web/views.py):** Handles user navigation and interactions within the application.

- **[Models](./sicklesmart_web/models.py):** Contains database models for users and their health status.

- **[Main Application Module](./sicklesmart_web/__init__.py):** Initializes the Flask app, registers blueprints, sets up database, and configures login management.

- **[Static Assets](./sicklesmart_web/static/):** Directory containing images, scripts, and stylesheets used in the application's frontend.

## API Endpoints

- ### Auth Module

  - **POST /login:** Authenticates users based on provided email and password.
  - **GET /logout:** Logs out the currently authenticated user.
  - **POST /register:** Registers a new user with the provided details.

- ### Views Module

  - **GET /:** Renders the homepage of the application.
  - **POST /user-logged_in:** Handles user health status updates.
  - **POST /delete-entry:** Deletes a user's health status entry.

## Data Model

The data model includes entities such as users and health status along with their attributes and relationships for now. Resources, Diet Modifications etc. would be added in future deployments.

## How to Run

To run the SickleSmart web application locally, follow these steps:

1. Clone this repository to your local machine.

```bash
git clone https://github.com/AyomideKayode/SickleSmart.git
cd SickleSmart
```

2. Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

3. Set up the Flask application environment by executing

```bash
export FLASK_APP=sicklesmart_web
```

4. Initialize the database by running:

```bash
flask init-db
```

5. Start the Flask development server with:

```bash
flask run
```

6. Access the application in your web browser at

```bash
http://localhost:5000
```

## Dependencies

- **Flask**

- **Flask-SQLAlchemy**

- **Flask-Login**

---

### Environment

- Language: Python 3.4.3
  - OS: Ubuntu 20.04 LTS
  - Compiler: python3
  - Style guidelines:
    - [PEP 8 (version 1.7)](https://www.python.org/dev/peps/pep-0008/)

---

## Author

- _Website_ - [Ayomide Kayode](https://github.com/AyomideKayode)
- _ALX Software Engineering Program_ - [ALX_AFRICA](https://www.alxafrica.com/programmes/)
- _Twitter_ - [@kazzy_wiz](https://www.twitter.com/kazzy_wiz)
