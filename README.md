# Clean_Agent_App_Full (Skeleton with core features)

This is a scaffold of Clean Agent App including:
- Accounts (custom user)
- Services, Providers, Clients
- Bookings
- Payments (M-Pesa helper)
- Wallets
- Notifications (Channels consumers)
- Reviews
- Chat (Channels)
- Reports

Instructions:
1. Create a virtualenv and install requirements: pip install -r requirements.txt
2. Update clean_agent/settings.py secrets or set environment variables.
3. Run migrations and start server:
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
4. For production use Redis channel layer and Daphne/uvicorn for ASGI.
