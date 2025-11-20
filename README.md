# Clean_Agent_App_Django_Project

## Overview

Clean Agent App is a platform for managing cleaning services between
**Admins**, **Clients**, and **Service Providers**.\
Built with Django, it offers booking management, service control, and a
full workflow system.

## Features

-   User Authentication (Register, Login, Logout, Password Reset)
-   Role-Based Dashboards (Admin, Client, Service Provider)
-   Booking System for Clients
-   Service Creation & Management for Providers
-   Admin controls users, bookings, and services
-   Notification workflow (approved / pending / completed)
-   Ready for Payment Integration
-   API-ready structure for mobile apps

## System Architecture

### Admin

-   Manage users
-   Review and manage bookings
-   Manage services
-   View system reports

### Client/User

-   Register an account
-   View available services
-   Book services
-   Track service progress

### Service Provider

-   Create and manage services
-   Receive bookings
-   Update job status until completion

## Badges

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg" />
  <img src="https://img.shields.io/badge/Django-Framework-success.svg" />
  <img src="https://img.shields.io/badge/Status-Active-green.svg" />
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" />
</p>


## Installation

Getting Started

1.  Clone repository

    ``` bash
    git clone <repo-url>
    ```

2.  Navigate to project folder

    ``` bash
    cd Clean_Agent_App_Django_Project
    ```

3.  Create virtual environment

    ``` bash
    python -m venv venv
    ```

4.  Activate environment

    -   Windows:

        ``` bash
        venv\Scripts\activate
        ```

    -   Linux/Mac:

        ``` bash
        source venv/bin/activate
        ```

5.  Install dependencies

    ``` bash
    pip install -r requirements.txt
    ```

6.  Run migrations

    ``` bash
    python manage.py migrate
    ```

7.  Start server

    ``` bash
    python manage.py runserver
    ```

## Usage

-   Create account as Client or Service Provider
-   Login to your dashboard
-   Clients book services
-   Providers manage services and bookings
-   Admin oversees the entire system

## Contributing

1.  Fork the repository.

2.  Create a new branch

    ``` bash
    git checkout -b feature/your-feature
    ```

3.  Commit your changes

   ``` bash
   git commit -am `Add new feature
   ```

4.  Push the branch

    ``` bash
    git push origin feature/your-feature
    ```
5.  Open a Pull Request.

## Screenshots

Add your screenshots here: - Login page
- Admin dashboard
- Client booking page
- Provider service panel

## Contact

**Developer:** zebida123
**Email:** solomondaudi05@gmail.com
**Project:** Clean_Agent_App_Django_Project

## License

    This project is licenced under the MIT License see the LICENCE file for details
    
    THE SOFTWARE.
