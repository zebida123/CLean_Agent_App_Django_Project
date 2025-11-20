# Clean_Agent_App_Django_Project

## Badges

```{=html}
<p align="left">
```
`<img src="https://img.shields.io/badge/Python-3.10+-blue.svg" />`{=html}
`<img src="https://img.shields.io/badge/Django-4.x-success.svg" />`{=html}
`<img src="https://img.shields.io/badge/Build-Passing-brightgreen.svg" />`{=html}
`<img src="https://img.shields.io/badge/Status-Active-informational.svg" />`{=html}
`<img src="https://img.shields.io/badge/License-MIT-green.svg" />`{=html}
```{=html}
</p>
```
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

### Client

-   Register an account
-   View available services
-   Book services
-   Track service progress

### Service Provider

-   Create and manage services
-   Receive bookings
-   Update job status until completion

## Installation

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

1.  Fork the repository\

2.  Create a new branch

    ``` bash
    git checkout -b feature/your-feature
    ```

3.  Make changes\

4.  Submit a Pull Request

## Screenshots

Add your screenshots here: - Login page\
- Admin dashboard\
- Client booking page\
- Provider service panel

## Contact

**Developer:** zebida123\
**Email:** solomondaudi05@gmail.com\
**Project:** Clean_Agent_App_Django_Project

## License (MIT License)

    MIT License

    Copyright (c) 2025 Clean_Agent_App_Django_Project

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights  
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
    copies of the Software, and to permit persons to whom the Software is  
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in  
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN  
    THE SOFTWARE.
